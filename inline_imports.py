#!/usr/bin/env python3
"""
Inline selected imports from a local package prefix into one or more scripts.

Fixed version that handles import paths that don't directly map to file system paths.

Features:
- Inlines top-level defs (functions/classes) that your script imports via:
    from <prefix>.<mod> import name[, ...]
- Also inlines module-level bindings those defs reference (e.g. FOO = 123).
- Recursively chases intra-prefix symbols imported via "from <prefix>.* import X".
- Never inlines anything outside your prefix (stdlib/third-party remain imports).
- Builds one script, a glob of scripts, or auto-discovers top-level scripts.
- Writes to an output dir by default or overwrites in place if you insist.

Limitations:
- Does not follow "import core.mod as m" and then "m.foo". Use "from ... import foo".
- Ignores star imports. Use explicit symbols like an adult.
- Only captures simple module-scope bindings: "NAME = ..." or "NAME: T = ...".
"""

import argparse
import ast
import fnmatch
import pathlib
from typing import Dict, Iterable, List, Optional, Set, Tuple

# -------------------- I/O helpers

def read_text(p: pathlib.Path) -> str:
    return p.read_text(encoding="utf-8", errors="ignore")

def module_path_to_file(project_root: pathlib.Path, module: str, prefix_mapping: Dict[str, str] = None) -> Optional[pathlib.Path]:
    """
    Convert a module path to a file path, with support for custom prefix mappings.
    
    Args:
        project_root: The root directory of the project
        module: The module name (e.g., "Scripts.omgarturo.fm_core.core_gathering")
        prefix_mapping: Dict mapping prefixes to actual directory paths
    """
    if prefix_mapping:
        for prefix, actual_path in prefix_mapping.items():
            if module.startswith(prefix + "."):
                # Replace the prefix with the actual path
                remainder = module[len(prefix) + 1:]  # +1 for the dot
                parts = remainder.split(".")
                candidate = project_root / actual_path
                for part in parts:
                    candidate = candidate / part
                file_py = candidate.with_suffix(".py")
                if file_py.is_file():
                    return file_py
                pkg_init = candidate / "__init__.py"
                if pkg_init.is_file():
                    return pkg_init
                return None
    
    # Fall back to standard resolution
    parts = module.split(".")
    candidate = project_root.joinpath(*parts)
    file_py = candidate.with_suffix(".py")
    if file_py.is_file():
        return file_py
    pkg_init = candidate / "__init__.py"
    if pkg_init.is_file():
        return pkg_init
    return None

def slice_source(text: str, node: ast.AST) -> str:
    lines = text.splitlines()
    start = getattr(node, "lineno", 1) - 1
    end = getattr(node, "end_lineno", start + 1)
    return "\n".join(lines[start:end])

# -------------------- AST analysis

def top_level_defs(module_ast: ast.Module) -> Dict[str, ast.AST]:
    out: Dict[str, ast.AST] = {}
    for stmt in module_ast.body:
        if isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            out[stmt.name] = stmt
    return out

def module_level_bindings(module_ast: ast.Module) -> Dict[str, ast.AST]:
    """
    Collect simple module-scope assignments/annotated assignments to a bare Name.
    Examples:
        FOO = 1
        BAR: int = 2
    """
    out: Dict[str, ast.AST] = {}
    for stmt in module_ast.body:
        if isinstance(stmt, ast.Assign):
            # Only single-name targets like X = ...
            names = [t.id for t in stmt.targets if isinstance(t, ast.Name)]
            if len(names) == 1:
                out[names[0]] = stmt
        elif isinstance(stmt, ast.AnnAssign) and isinstance(stmt.target, ast.Name):
            out[stmt.target.id] = stmt
    return out

def params_for(fn: ast.AST) -> Set[str]:
    if not isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)):
        return set()
    a = fn.args
    names = {x.arg for x in a.args}
    if a.vararg: names.add(a.vararg.arg)
    names.update(x.arg for x in a.kwonlyargs)
    if a.kwarg: names.add(a.kwarg.arg)
    return names

def collect_free_names(node: ast.AST) -> Set[str]:
    """
    Conservative pass: collect Name loads that are not local variables/params.
    Used to find sibling defs and module-level bindings a def depends on.
    """
    refs: Set[str] = set()
    locals_stack: List[Set[str]] = [set()]

    def add_targets(t: ast.AST):
        if isinstance(t, ast.Name):
            locals_stack[-1].add(t.id)
        elif isinstance(t, (ast.Tuple, ast.List)):
            for e in t.elts:
                add_targets(e)

    class V(ast.NodeVisitor):
        def visit_FunctionDef(self, n: ast.FunctionDef):
            locals_stack.append(params_for(n))
            for s in n.body:
                self.visit(s)
            locals_stack.pop()
        visit_AsyncFunctionDef = visit_FunctionDef

        def visit_ClassDef(self, n: ast.ClassDef):
            locals_stack.append(set())
            for s in n.body:
                self.visit(s)
            locals_stack.pop()

        def visit_Assign(self, n: ast.Assign):
            for t in n.targets:
                add_targets(t)
            self.visit(n.value)

        def visit_AnnAssign(self, n: ast.AnnAssign):
            add_targets(n.target)
            if n.value: self.visit(n.value)

        def visit_For(self, n: ast.For):
            add_targets(n.target)
            self.generic_visit(n)

        def visit_With(self, n: ast.With):
            for it in n.items:
                if it.optional_vars:
                    add_targets(it.optional_vars)
            self.generic_visit(n)

        def visit_Name(self, n: ast.Name):
            if isinstance(n.ctx, ast.Load):
                if not any(n.id in s for s in locals_stack):
                    refs.add(n.id)

    V().visit(node)
    return refs

# -------------------- Cache

class ModuleCache:
    def __init__(self, project_root: pathlib.Path, prefix_mapping: Dict[str, str] = None):
        self.root = project_root.resolve()
        self.prefix_mapping = prefix_mapping or {}
        self.text: Dict[pathlib.Path, str] = {}
        self.ast: Dict[pathlib.Path, ast.Module] = {}
        self.defs: Dict[pathlib.Path, Dict[str, ast.AST]] = {}
        self.bindings: Dict[pathlib.Path, Dict[str, ast.AST]] = {}
        self.importfrom: Dict[pathlib.Path, Dict[str, str]] = {}  # localname -> module path

    def load(self, p: pathlib.Path):
        p = p.resolve()
        if p in self.ast:
            return
        t = read_text(p)
        m = ast.parse(t, filename=str(p))
        self.text[p] = t
        self.ast[p] = m
        self.defs[p] = top_level_defs(m)
        self.bindings[p] = module_level_bindings(m)
        mapping: Dict[str, str] = {}
        for n in m.body:
            if isinstance(n, ast.ImportFrom) and n.module:
                for alias in n.names:
                    if alias.name != "*":
                        mapping[alias.asname or alias.name] = n.module
        self.importfrom[p] = mapping

# -------------------- Inliner

class Inliner:
    def __init__(self, project_root: pathlib.Path, allowed_prefix: str, prefix_mapping: Dict[str, str] = None):
        self.root = project_root.resolve()
        self.prefix = allowed_prefix
        self.prefix_mapping = prefix_mapping or {}
        self.cache = ModuleCache(self.root, prefix_mapping)
        # Track what we already emitted to avoid duplicates
        self.emitted_defs: Set[Tuple[pathlib.Path, str]] = set()
        self.emitted_bindings: Set[Tuple[pathlib.Path, str]] = set()

    def resolve_module(self, module: str) -> Optional[pathlib.Path]:
        return module_path_to_file(self.root, module, self.prefix_mapping)

    def parse_file(self, p: pathlib.Path) -> Tuple[str, ast.Module]:
        t = read_text(p)
        return t, ast.parse(t, filename=str(p))

    def find_script_targets(self, script_ast: ast.Module) -> List[Tuple[ast.ImportFrom, str, List[str]]]:
        out = []
        for node in script_ast.body:
            if isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
                if node.module == self.prefix or node.module.startswith(self.prefix + "."):
                    names = [a.name for a in node.names if a.name != "*"]
                    if names:
                        out.append((node, node.module, names))
        return out

    def _inline_symbol_block(self, module_file: pathlib.Path, symbol_names: Iterable[str]) -> str:
        """
        Inline requested defs/bindings from a module file, recursively pulling
        sibling defs, module-level bindings, and cross-module symbols imported via
        "from <prefix>.* import name".
        """
        self.cache.load(module_file)
        txt = self.cache.text[module_file]
        defs = self.cache.defs[module_file]
        binds = self.cache.bindings[module_file]
        importmap = self.cache.importfrom[module_file]

        ordered_chunks: List[str] = []
        
        # Track imported symbols that need to be inlined from other modules
        imported_symbols: Set[Tuple[pathlib.Path, str]] = set()

        # First pass: collect all dependencies recursively
        def collect_deps(name: str, deps: Set[str], visited: Set[str]):
            if name in visited:
                return
            visited.add(name)
            
            if name in defs:
                node = defs[name]
                for ref in collect_free_names(node):
                    if ref in binds and ref not in deps:
                        deps.add(ref)
                        collect_deps(ref, deps, visited)
                    elif ref in defs and ref not in deps:
                        deps.add(ref)
                        collect_deps(ref, deps, visited)
                    elif ref in importmap and ref not in deps:
                        # This is an imported symbol - we need to inline it
                        import_module = importmap[ref]
                        imported_dep_path = self.resolve_module(import_module)
                        if imported_dep_path and imported_dep_path.exists():
                            imported_symbols.add((imported_dep_path, ref))
                            deps.add(ref)
            elif name in binds:
                bnode = binds[name]
                val = getattr(bnode, "value", None)
                if val is not None:
                    for ref in collect_free_names(val):
                        if ref in binds and ref not in deps:
                            deps.add(ref)
                            collect_deps(ref, deps, visited)
                        elif ref in defs and ref not in deps:
                            deps.add(ref)
                            collect_deps(ref, deps, visited)
                        elif ref in importmap and ref not in deps:
                            # This is an imported symbol - we need to inline it
                            import_module = importmap[ref]
                            imported_dep_path = self.resolve_module(import_module)
                            if imported_dep_path and imported_dep_path.exists():
                                imported_symbols.add((imported_dep_path, ref))
                                deps.add(ref)
        
        # Collect all dependencies for all requested symbols
        all_deps: Set[str] = set()
        for name in symbol_names:
            collect_deps(name, all_deps, set())
            all_deps.add(name)
        
        # Process imported symbols - recursively inline them from their source modules
        # Keep doing this until no new symbols are discovered
        iteration = 0
        max_iterations = 10  # Prevent infinite loops
        
        while imported_symbols and iteration < max_iterations:
            current_imports = imported_symbols.copy()
            imported_symbols.clear()
            iteration += 1
            
            for import_path, import_name in current_imports:
                # Recursively inline the imported symbol
                import_block = self._inline_symbol_block(import_path, [import_name])
                if import_block:
                    ordered_chunks.append(import_block)
        
        # Separate bindings and defs
        binding_deps = [name for name in all_deps if name in binds]
        def_deps = [name for name in all_deps if name in defs]
        
        # Topological sort that handles dependencies between bindings AND defs
        def topo_sort_all_deps(binding_names: List[str], def_names: List[str]) -> Tuple[List[str], List[str]]:
            all_names = set(binding_names + def_names)
            remaining = all_names.copy()
            sorted_bindings = []
            sorted_defs = []
            
            while remaining:
                ready = []
                
                # Check each remaining item for readiness
                for name in remaining:
                    deps_in_remaining = False
                    
                    if name in binds:
                        # For bindings, check what they reference
                        bnode = binds[name]
                        val = getattr(bnode, "value", None)
                        if val is not None:
                            for ref in collect_free_names(val):
                                if ref in remaining and (ref in binds or ref in defs):
                                    deps_in_remaining = True
                                    break
                    elif name in defs:
                        # For defs, check what they reference
                        node = defs[name]
                        for ref in collect_free_names(node):
                            if ref in remaining and (ref in binds or ref in defs):
                                deps_in_remaining = True
                                break
                    
                    if not deps_in_remaining:
                        ready.append(name)
                
                if not ready:
                    # Circular dependency or issue, just take the first one
                    ready = [next(iter(remaining))]
                
                # Add ready items to appropriate lists
                for name in ready:
                    if name in binds:
                        sorted_bindings.append(name)
                    elif name in defs:
                        sorted_defs.append(name)
                    remaining.remove(name)
            
            return sorted_bindings, sorted_defs
        
        # Get properly sorted bindings and defs
        sorted_bindings, sorted_defs = topo_sort_all_deps(binding_deps, def_deps)
        
        # Process everything in proper dependency order
        # First emit class/function definitions that are needed by bindings
        defs_needed_by_bindings = []
        bindings_ready = []
        
        for name in sorted_bindings:
            # Check if this binding needs any defs
            if name in binds:
                bnode = binds[name]
                val = getattr(bnode, "value", None)
                if val is not None:
                    for ref in collect_free_names(val):
                        if ref in defs and ref not in defs_needed_by_bindings:
                            defs_needed_by_bindings.append(ref)
        
        # Emit class/function definitions needed by bindings first
        for name in defs_needed_by_bindings:
            if (module_file, name) not in self.emitted_defs:
                node = defs[name]
                chunk = f"# ---- {name} (from {module_file.name})\n" + slice_source(txt, node).rstrip() + "\n"
                ordered_chunks.append(chunk)
                self.emitted_defs.add((module_file, name))
        
        # Then emit bindings in dependency order
        for name in sorted_bindings:
            if (module_file, name) not in self.emitted_bindings:
                bnode = binds[name]
                chunk = f"# ---- {name} (binding from {module_file.name})\n" + slice_source(txt, bnode).rstrip() + "\n"
                ordered_chunks.append(chunk)
                self.emitted_bindings.add((module_file, name))
        
        # Finally emit remaining function/class definitions
        for name in sorted_defs:
            if (module_file, name) not in self.emitted_defs:
                node = defs[name]
                chunk = f"# ---- {name} (from {module_file.name})\n" + slice_source(txt, node).rstrip() + "\n"
                ordered_chunks.append(chunk)
                self.emitted_defs.add((module_file, name))

        if not ordered_chunks:
            return ""

        header = f"# ===== Inlined block from {module_file.name} =====\n"
        return header + "\n".join(ordered_chunks)

    def collect_module_imports(self, module_file: pathlib.Path) -> List[str]:
        """Collect all non-local imports from a module file."""
        self.cache.load(module_file)
        module_ast = self.cache.ast[module_file]
        imports = []
        
        for node in module_ast.body:
            if isinstance(node, ast.Import):
                for alias in node.names:
                    import_line = f"import {alias.name}"
                    if alias.asname:
                        import_line += f" as {alias.asname}"
                    imports.append(import_line)
            elif isinstance(node, ast.ImportFrom):
                if node.module and not (node.module == self.prefix or node.module.startswith(self.prefix + ".")):
                    # Only include non-local imports
                    names = []
                    for alias in node.names:
                        if alias.name == "*":
                            names.append("*")
                        else:
                            name = alias.name
                            if alias.asname:
                                name += f" as {alias.asname}"
                            names.append(name)
                    
                    if names:
                        import_line = f"from {node.module} import {', '.join(names)}"
                        imports.append(import_line)
        
        return imports

    def rewrite_script(self, script_path: pathlib.Path) -> str:
        script_text, script_ast = self.parse_file(script_path)
        targets = self.find_script_targets(script_ast)
        
        # Collect all imports from script and inlined modules
        all_imports = set()
        
        # Get imports from the original script (non-local ones)
        for node in script_ast.body:
            if isinstance(node, ast.Import):
                for alias in node.names:
                    import_line = f"import {alias.name}"
                    if alias.asname:
                        import_line += f" as {alias.asname}"
                    all_imports.add(import_line)
            elif isinstance(node, ast.ImportFrom):
                if node.module and not (node.module == self.prefix or node.module.startswith(self.prefix + ".")):
                    # Only include non-local imports
                    names = []
                    for alias in node.names:
                        if alias.name == "*":
                            names.append("*")
                        else:
                            name = alias.name
                            if alias.asname:
                                name += f" as {alias.asname}"
                            names.append(name)
                    
                    if names:
                        import_line = f"from {node.module} import {', '.join(names)}"
                        all_imports.add(import_line)
        
        # Process inline targets
        insertion_blocks: List[str] = []
        imports_to_remove: Set[ast.AST] = set()
        inlined_modules: Set[pathlib.Path] = set()

        for node, module, names in targets:
            mod_file = self.resolve_module(module)
            if not mod_file:
                print(f"Warning: Could not resolve module {module}")
                continue
            block = self._inline_symbol_block(mod_file, names)
            if block:
                insertion_blocks.append(block)
                imports_to_remove.add(node)
                inlined_modules.add(mod_file)
        
        # Collect imports from all inlined modules
        for mod_file in inlined_modules:
            module_imports = self.collect_module_imports(mod_file)
            all_imports.update(module_imports)

        # Remove ALL import statements (both local and non-local) from the original script
        lines = script_text.splitlines()
        to_remove = set()
        for i, node in enumerate(script_ast.body):
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                s = node.lineno - 1
                e = getattr(node, "end_lineno", node.lineno) - 1
                for j in range(s, e + 1):
                    to_remove.add(j)
        
        kept = [ln for i, ln in enumerate(lines) if i not in to_remove]

        # Find insertion point after shebang/encoding/__future__
        idx = 0
        if kept and kept[0].startswith("#!"):
            idx = 1
        if idx < len(kept) and "coding" in kept[idx][:40]:
            idx += 1
        while idx < len(kept) and kept[idx].strip().startswith("from __future__ import"):
            idx += 1

        # Build the new file structure
        new_parts = []
        
        # Add shebang/encoding/__future__ if any
        if idx > 0:
            new_parts.extend(kept[:idx])
        
        # Add imports section
        if all_imports:
            new_parts.append("# ===============================================")
            new_parts.append("# Imports")
            new_parts.append("# ===============================================")
            # Sort imports for consistency
            sorted_imports = sorted(all_imports)
            new_parts.extend(sorted_imports)
            new_parts.append("")
        
        # Add inlined code section
        if insertion_blocks:
            new_parts.append("# ===============================================")
            new_parts.append("# Auto-generated inlined code. Do not edit")
            new_parts.append("# ===============================================")
            new_parts.append("")
            new_parts.extend(insertion_blocks)
        
        # Add the rest of the original script
        new_parts.extend(kept[idx:])
        
        return "\n".join(new_parts)

# -------------------- Discovery & CLI

def discover_scripts(root: pathlib.Path, glob_patterns: List[str], exclude_dirs: List[str]) -> List[pathlib.Path]:
    root = root.resolve()
    # Hardcoded files to exclude
    excluded_files = {"__init__.py", "inline_imports.py", "inline_imports_fixed.py"}
    
    candidates: Set[pathlib.Path] = set()
    if glob_patterns:
        for p in root.rglob("*.py"):
            rel = p.relative_to(root).as_posix()
            if any(fnmatch.fnmatch(rel, pat) for pat in glob_patterns):
                candidates.add(p)
    else:
        # Default: plain *.py files directly under root (not in excluded dirs)
        for p in root.iterdir():
            if p.is_file() and p.suffix == ".py":
                candidates.add(p)

    out: List[pathlib.Path] = []
    for p in sorted(candidates):
        # Skip hardcoded excluded files
        if p.name in excluded_files:
            continue
            
        rel_parts = p.relative_to(root).parts
        if any(part in exclude_dirs for part in rel_parts[:-1]):
            continue
        out.append(p)
    return out

def main():
    ap = argparse.ArgumentParser(description="Inline local imports from a given prefix into script(s).")
    ap.add_argument("--project-root", type=pathlib.Path, default=pathlib.Path("."), help="Project root (default: .)")
    ap.add_argument("--prefix", default="Scripts.omgarturo.fm_core", help="Module prefix to inline (default: Scripts.omgarturo.fm_core)")
    ap.add_argument("--prefix-dir", default="fm_core", help="Actual directory name for the prefix (default: fm_core)")
    group = ap.add_mutually_exclusive_group()
    group.add_argument("--script", type=pathlib.Path, help="Build a single script")
    group.add_argument("--scripts-glob", nargs="*", help="Glob(s) for scripts relative to project root, e.g. 'scripts/*.py' 'bin/*.py'")
    ap.add_argument("--out-dir", type=pathlib.Path, default=pathlib.Path("build_inlined"), help="Output directory (default: build_inlined)")
    ap.add_argument("--overwrite", action="store_true", help="Overwrite source scripts instead of writing to out-dir")
    ap.add_argument("--exclude-dir", action="append", default=["fm_core", "__pycache__", "build_inlined", ".venv", "venv", ".git"], help="Directories to ignore when auto-discovering")
    args = ap.parse_args()

    root = args.project_root.resolve()
    if args.script:
        scripts = [args.script.resolve()]
    else:
        scripts = discover_scripts(root, args.scripts_glob or [], args.exclude_dir)

    if not scripts:
        print("No scripts found. Try --script or --scripts-glob.")
        return

    # Create prefix mapping
    prefix_mapping = {args.prefix: args.prefix_dir}
    
    inliner = Inliner(root, args.prefix, prefix_mapping)

    if not args.overwrite:
        out_dir = args.out_dir.resolve()
        out_dir.mkdir(parents=True, exist_ok=True)

    for sp in scripts:
        print(f"Processing {sp.name}...")
        new_text = inliner.rewrite_script(sp)
        if args.overwrite:
            sp.write_text(new_text, encoding="utf-8")
            print(f"Wrote {sp}")
        else:
            target = args.out_dir.resolve() / sp.name
            target.write_text(new_text, encoding="utf-8")
            print(f"Wrote {target}")

if __name__ == "__main__":
    main()
