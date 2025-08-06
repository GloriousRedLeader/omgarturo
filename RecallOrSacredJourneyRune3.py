# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-03-23
# Use at your own risk. 

from Scripts.omgarturo.fm_core.core_items import RUNEBOOK
import re
import os
import sys

# Finds first runebook in inventory and attempts to recall / sacred journey to 
# the rune indicated in the file name. File name must match this pattern for it to work:
# RecallOrSacredJourneyRune<NUMBER>.py where NUMBER is an integer starting at 1 (first rune in book)
# Will use sacred journey if chiv skill is present and higher than magery, otherwise uses recall.
# Only works with runebooks (not atlas). Picks the first runebook in backpack. If  you have multiple
# runebooks, good luck. Runebook must be in first layer of backpack.
RUNEBOOK_GUMP_ID = 0x59
script_name = os.path.basename(__file__)
rune = int(re.search(r"RecallOrSacredJourneyRune(\d+)\.py", script_name).group(1))
magerySkill = Player.GetSkillValue("Magery")
chivalrySkill = Player.GetSkillValue("Chivalry")

# Magery Rune 1 = 50
# Magery Rune 2 = 51
# Chivalry Rune 1 = 75
# Chivalry Rune 2 = 76
buttonId = 74 + rune if chivalrySkill > magerySkill else 49 + rune

runebook = Items.FindByID(RUNEBOOK, -1, Player.Backpack.Serial, 0)
if runebook is None:
    Misc.SendMessage("No runebook found. Must be in backpack.", 38)
    sys.exit()

print(runebook)
print(script_name)
print(f"Magery Skill {magerySkill}")
print(f"Chivalry Skill {chivalrySkill}")
print(f"Rune {rune}")
print(f"Button ID {buttonId}")

Items.UseItem(runebook)
Gumps.WaitForGump(RUNEBOOK_GUMP_ID, 10000)
Gumps.SendAction(RUNEBOOK_GUMP_ID, buttonId) 