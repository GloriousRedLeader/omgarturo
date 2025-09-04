# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-03-23
# Use at your own risk. 

from Scripts.omgarturo.fm_core.core_items import RUNEBOOK
from Scripts.omgarturo.fm_core.core_spells import cast_recall_or_sacred_journey

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