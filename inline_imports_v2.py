#!/usr/bin/env python3
"""
Simple inline imports tool that recursively resolves dependencies.
"""

import ast
import pathlib
from typing import Dict, Set, List, Optional, Tuple
import os

def collect_names_used(node: ast.AST) -> Set[str]:
    """Collect all names that are referenced (loaded) in this AST node."""
    names = set()
    for child in ast.walk(node):
        if isinstance(child, ast.Name) and isinstance(child.ctx, ast.Load):
            names.add(child.id)
    return names

def collect_names_defined(tree: ast.AST) -> Dict[str, ast.AST]:
    """Collect all names defined at module level in this module."""
    defined = {}
    
    # Only look at top-level statements, not inside functions/classes
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            defined[node.name] = node
        elif isinstance(node, ast.ClassDef):
            defined[node.name] = node
        elif isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    defined[target.id] = node
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            defined[node.target.id] = node
    
    return defined

def collect_imports(tree: ast.AST) -> Dict[str, str]:
    """Collect import mappings: symbol_name -> module_name"""
    imports = {}
    
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom):
            if node.module and not node.module.startswith('Scripts.'):
                continue  # Only process local imports
            if node.names[0].name == '*':
                continue  # Skip star imports
            
            for alias in node.names:
                symbol_name = alias.asname if alias.asname else alias.name
                module_name = node.module
                imports[symbol_name] = module_name
        elif isinstance(node, ast.Import):
            for alias in node.names:
                if not alias.name.startswith('Scripts.'):
                    continue  # Only process local imports
                symbol_name = alias.asname if alias.asname else alias.name.split('.')[-1]
                imports[symbol_name] = alias.name
    
    return imports

class SimpleInliner:
    def __init__(self):
        self.module_cache = {}  # path -> (tree, defined_names, imports)
        self.collected_code = {}  # (module_path, symbol_name) -> ast_node
        self.processed = set()  # (module_path, symbol_name)
        
    def resolve_module_path(self, module_name: str) -> Optional[pathlib.Path]:
        """Convert module name to file path."""
        if not module_name.startswith('Scripts.omgarturo.'):
            return None
            
        # Scripts.omgarturo.fm_core.core_gathering -> fm_core/core_gathering.py
        parts = module_name.split('.')
        if len(parts) < 3:
            return None
            
        rel_path = '/'.join(parts[2:]) + '.py'
        full_path = pathlib.Path(rel_path)
        
        if full_path.exists():
            return full_path
        return None
    
    def load_module(self, module_path: pathlib.Path) -> Tuple[ast.AST, Dict[str, ast.AST], Dict[str, str]]:
        """Load and parse a module, with caching."""
        if module_path in self.module_cache:
            return self.module_cache[module_path]
            
        try:
            with open(module_path, 'r') as f:
                source = f.read()
            tree = ast.parse(source)
            defined_names = collect_names_defined(tree)
            imports = collect_imports(tree)
            
            result = (tree, defined_names, imports)
            self.module_cache[module_path] = result
            return result
        except Exception as e:
            print(f"Error loading module {module_path}: {e}")
            return ast.Module(body=[], type_ignores=[]), {}, {}
    
    def collect_symbol_dependencies(self, symbol_name: str, module_path: pathlib.Path, needed_deps: Set[Tuple[pathlib.Path, str]]):
        """Recursively collect all dependencies for a symbol."""
        key = (module_path, symbol_name)
        if key in self.processed:
            return
        self.processed.add(key)
        
        tree, defined_names, imports = self.load_module(module_path)
        
        # Find the symbol definition
        if symbol_name not in defined_names:
            print(f"Warning: {symbol_name} not found in {module_path}")
            return
            
        symbol_node = defined_names[symbol_name]
        self.collected_code[key] = symbol_node
        
        # Find what names this symbol uses
        used_names = collect_names_used(symbol_node)
        
        # UO API built-ins and Python built-ins
        builtins = {
            'True', 'False', 'None', 'len', 'range', 'str', 'int', 'float', 'bool', 
            'list', 'dict', 'set', 'tuple', 'print', 'isinstance', 'hasattr', 'getattr', 
            'enumerate', 'zip', 'min', 'max', 'sum', 'abs', 'open', 'Exception', 
            'ValueError', 'TypeError', 'AttributeError', 'KeyError', 'IndexError',
            'Items', 'Player', 'Gumps', 'Misc', 'Target', 'Timer', 'Journal', 
            'Mobiles', 'Spells', 'PathFinding', 'Statics'
        }
        
        # For each used name, check if it's defined locally or imported
        for used_name in used_names:
            # Skip built-ins
            if used_name in builtins:
                continue
                
            if used_name in defined_names:
                # It's defined in the same module
                needed_deps.add((module_path, used_name))
                self.collect_symbol_dependencies(used_name, module_path, needed_deps)
            elif used_name in imports:
                # It's imported from another module
                import_module = imports[used_name]
                import_path = self.resolve_module_path(import_module)
                if import_path:
                    needed_deps.add((import_path, used_name))
                    self.collect_symbol_dependencies(used_name, import_path, needed_deps)
            else:
                # It's not defined locally and not imported - might be a missing dependency
                # or a parameter/local variable, so we don't error here
                pass
    
    def inline_file(self, input_file: pathlib.Path, output_file: pathlib.Path):
        """Process a single file and create inlined version."""
        print(f"Processing {input_file.name}...")
        
        # Clear dependency tracking for this file (but keep module cache)
        self.collected_code = {}
        self.processed = set()
        
        # Load the original file
        with open(input_file, 'r') as f:
            source = f.read()
        
        tree = ast.parse(source)
        imports = collect_imports(tree)
        
        # Collect all dependencies
        needed_deps = set()
        for symbol_name, module_name in imports.items():
            module_path = self.resolve_module_path(module_name)
            if module_path:
                needed_deps.add((module_path, symbol_name))
                self.collect_symbol_dependencies(symbol_name, module_path, needed_deps)
        
        print(f"  Found {len(needed_deps)} total dependencies for {input_file.name}")
        
        # Build the inlined code
        inlined_parts = []
        
        # Collect all imports - both from original file and from inlined modules
        all_imports = set()
        
        # Add original imports (non-local ones)
        for node in tree.body:
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                if isinstance(node, ast.ImportFrom):
                    if node.module and node.module.startswith('Scripts.'):
                        continue  # Skip local imports - these will be inlined
                elif isinstance(node, ast.Import):
                    if any(alias.name.startswith('Scripts.') for alias in node.names):
                        continue  # Skip local imports - these will be inlined
                # Keep all other imports (System imports, etc.)
                import_str = ast.unparse(node)
                all_imports.add(import_str)
        
        # Add imports from inlined modules
        processed_modules = set()
        for (module_path, symbol_name) in needed_deps:
            if module_path in processed_modules:
                continue
            processed_modules.add(module_path)
            
            _, _, module_imports = self.load_module(module_path)
            # Add System and other non-local imports from this module
            module_tree, _, _ = self.load_module(module_path)
            for node in module_tree.body:
                if isinstance(node, (ast.Import, ast.ImportFrom)):
                    if isinstance(node, ast.ImportFrom):
                        if node.module and node.module.startswith('Scripts.'):
                            continue  # Skip local imports
                    elif isinstance(node, ast.Import):
                        if any(alias.name.startswith('Scripts.') for alias in node.names):
                            continue  # Skip local imports
                    # Keep System imports, standard library imports, etc.
                    import_str = ast.unparse(node)
                    all_imports.add(import_str)
        
        # Add all collected imports
        inlined_parts.extend(sorted(all_imports))
        
        # Organize collected symbols by type
        constants = []
        functions = []
        classes = []
        
        for (module_path, symbol_name) in needed_deps:
            if (module_path, symbol_name) in self.collected_code:
                symbol_node = self.collected_code[(module_path, symbol_name)]
                symbol_code = ast.unparse(symbol_node)
                
                if isinstance(symbol_node, ast.FunctionDef):
                    functions.append(symbol_code)
                elif isinstance(symbol_node, ast.ClassDef):
                    classes.append(symbol_code)
                elif isinstance(symbol_node, ast.Assign):
                    constants.append(symbol_code)
                else:
                    # Other types (like complex expressions)
                    constants.append(symbol_code)
        
        # Build organized code sections
        code_sections = []
        
        # Add imports first
        code_sections.extend(sorted(all_imports))
        
        if code_sections:
            code_sections.append('')  # Blank line after imports
        
        # Add constants
        if constants:
            code_sections.append('# Constants')
            code_sections.extend(constants)
            code_sections.append('')  # Blank line after constants
        
        # Add classes
        if classes:
            code_sections.append('# Classes')
            code_sections.extend(classes)
            code_sections.append('')  # Blank line after classes
        
        # Add functions
        if functions:
            code_sections.append('# Functions')
            code_sections.extend(functions)
            code_sections.append('')  # Blank line after functions
        
        # Add original code (excluding import statements)
        original_code = []
        for node in tree.body:
            if not isinstance(node, (ast.Import, ast.ImportFrom)):
                original_code.append(ast.unparse(node))
        
        if original_code:
            code_sections.append('# Main code')
            code_sections.extend(original_code)
        
        # Combine everything
        final_code = '\n'.join(code_sections)
        
        # Write output
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, 'w') as f:
            f.write(final_code + '\n')
        
        print(f"Wrote {output_file}")

def check_undefined_variables(output_dir: pathlib.Path):
    """Check all generated files for undefined variables."""
    print("\n" + "="*50)
    print("QUALITY CHECK: Scanning for undefined variables...")
    print("="*50)
    
    undefined_vars = {}
    
    # UO API objects that are automatically available (built-ins)
    uo_builtins = {
        'Items', 'Player', 'Gumps', 'Misc', 'Target', 'Timer', 'Journal', 
        'Mobiles', 'Spells', 'PathFinding', 'Statics'
    }
    
    # Standard Python built-ins
    python_builtins = {
        'True', 'False', 'None', 'len', 'range', 'str', 'int', 'float', 'bool', 
        'list', 'dict', 'set', 'tuple', 'print', 'input', 'type', 'isinstance', 
        'hasattr', 'getattr', 'setattr', 'enumerate', 'zip', 'sorted', 'reversed', 
        'all', 'any', 'min', 'max', 'sum', 'abs', 'round', 'open', 'Exception', 
        'ValueError', 'TypeError', 'AttributeError', 'KeyError', 'IndexError', 
        'ImportError', 'RuntimeError', 'NotImplementedError', 'StopIteration', 
        'GeneratorExit', 'KeyboardInterrupt', 'SystemExit', 'object', 'super', 
        'property', 'staticmethod', 'classmethod', 'iter', 'next', 'map', 
        'filter', 'format', 'repr', 'ord', 'chr', 'bin', 'hex', 'oct', 'divmod', 'pow'
    }
    
    all_builtins = python_builtins | uo_builtins
    
    for py_file in output_dir.glob('*.py'):
        try:
            with open(py_file, 'r') as f:
                source = f.read()
            
            tree = ast.parse(source)
            
            # Collect defined names (only at module level)
            defined = set()
            for node in tree.body:
                if isinstance(node, ast.FunctionDef):
                    defined.add(node.name)
                elif isinstance(node, ast.ClassDef):
                    defined.add(node.name)
                elif isinstance(node, ast.Assign):
                    for target in node.targets:
                        if isinstance(target, ast.Name):
                            defined.add(target.id)
                elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
                    defined.add(node.target.id)
                elif isinstance(node, ast.Import):
                    for alias in node.names:
                        defined.add(alias.asname or alias.name.split('.')[0])
                elif isinstance(node, ast.ImportFrom):
                    if node.names[0].name == '*':
                        continue  # Skip star imports
                    for alias in node.names:
                        defined.add(alias.asname or alias.name)
            
            # Collect referenced names
            referenced = set()
            for node in ast.walk(tree):
                if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
                    referenced.add(node.id)
            
            undefined = referenced - defined - all_builtins
            
            if undefined:
                undefined_vars[py_file.name] = sorted(undefined)
        
        except Exception as e:
            print(f'Error processing {py_file.name}: {e}')
    
    if undefined_vars:
        print(f"\n❌ Found undefined variables in {len(undefined_vars)} files:")
        for filename, vars in sorted(undefined_vars.items()):
            print(f"  {filename}: {vars[:10]}" + (" ..." if len(vars) > 10 else ""))
        print(f"\nTotal files with issues: {len(undefined_vars)}")
    else:
        print(f"\n✅ All {len(list(output_dir.glob('*.py')))} files passed validation!")
    
    print("="*50)

def main():
    """Process all Python files in the current directory."""
    inliner = SimpleInliner()
    
    # Create output directory
    output_dir = pathlib.Path('build_inlined_v2')
    output_dir.mkdir(exist_ok=True)
    
    # Process all Python files (excluding the inliner itself)
    processed_count = 0
    for py_file in pathlib.Path('.').glob('*.py'):
        if py_file.name.startswith('inline_imports'):
            continue
        if py_file.name.startswith('__'):
            continue
        
        output_file = output_dir / py_file.name
        inliner.inline_file(py_file, output_file)
        processed_count += 1
    
    print(f"\nProcessed {processed_count} files.")
    
    # Run quality check
    check_undefined_variables(output_dir)

if __name__ == '__main__':
    main()
