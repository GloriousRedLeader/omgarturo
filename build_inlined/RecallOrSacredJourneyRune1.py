# ===============================================
# Imports
# ===============================================
from pathlib import Path
import __main__
import inspect
import os
import re

# ===============================================
# Auto-generated inlined code. Do not edit
# ===============================================

# ===== Inlined block from core_items.py =====
# ---- RUNEBOOK (binding from core_items.py)
RUNEBOOK = 0x22C5

# ===== Inlined block from core_spells.py =====
# ---- cast_recall_or_sacred_journey (from core_spells.py)
def cast_recall_or_sacred_journey(

    # Time in milliseconds to wait IF we need to morph into
    # wraith form form for necro.
    shapeshiftDelayMs = 3000
):
    RUNEBOOK_GUMP_ID = 0x59
    #script_name = os.path.basename(__file__)
    script_name = getattr(__main__, "__file__", None) or sys.argv[0]
    rune = int(re.search(r"RecallOrSacredJourneyRune(\d+)\.py", script_name).group(1))
    magerySkill = Player.GetSkillValue("Magery")
    chivalrySkill = Player.GetSkillValue("Chivalry")
    necroSkill = Player.GetSkillValue("Necromancy")
    hasWraith = Player.BuffsExist("Wraith Form")
    hasVampire = Player.BuffsExist("Vampiric Embrace")

    # Magery Rune 1 = 50
    # Magery Rune 2 = 51
    # Chivalry Rune 1 = 75
    # Chivalry Rune 2 = 76
    # Defaults to magery if both magery and chivalry are 0 (pure necro)
    buttonId = 74 + rune if chivalrySkill > magerySkill else 49 + rune

    if magerySkill < 50 and chivalrySkill < 50 and necroSkill > 80:
        while not Player.BuffsExist("Wraith Form"):
            cast_spell("Wraith Form", None, 650)

    runebook = Items.FindByID(RUNEBOOK, -1, Player.Backpack.Serial, 0)
    if runebook is None:
        Misc.SendMessage("No runebook found. Must be in backpack.", 38)
        sys.exit()

    print(runebook)
    print(script_name)
    print(f"Magery Skill {magerySkill}")
    print(f"Chivalry Skill {chivalrySkill}")
    print(f"Necromancy Skill {necroSkill}")
    print(f"Rune {rune}")
    print(f"Button ID {buttonId}")

    Items.UseItem(runebook)
    Gumps.WaitForGump(RUNEBOOK_GUMP_ID, 10000)
    Gumps.SendAction(RUNEBOOK_GUMP_ID, buttonId) 

    Misc.Pause(3000)

    if hasVampire and Player.BuffsExist("Wraith Form"):
        Spells.CastNecro("Vampiric Embrace")
    if not hasVampire and not hasWraith and Player.BuffsExist("Wraith Form"):
        Spells.CastNecro("Wraith Form")

# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-03-23
# Use at your own risk. 


# Finds first runebook in inventory and attempts to recall / sacred journey to 
# the rune indicated in the file name. File name must match this pattern for it to work:
# RecallOrSacredJourneyRune<NUMBER>.py where NUMBER is an integer starting at 1 (first rune in book)
# Will use sacred journey if chiv skill is present and higher than magery, otherwise uses recall.
# Only works with runebooks (not atlas). Picks the first runebook in backpack. If  you have multiple
# runebooks, good luck. Runebook must be in first layer of backpack.
# Also will cast wraith form if you are a necor without magery or chivalry.
# If player needs to cast wraith form, will automatically retun to whatever form they
# were in before enering wraith form (vampiric embrace /no form)
cast_recall_or_sacred_journey()