# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2024-03-26
# Use at your own risk. 

from Scripts.omgarturo.src.fm_core.core_player import open_bank_and_resupply
from Scripts.omgarturo.src.fm_core.core_player import move_all_items_from_container
from Scripts.omgarturo.src.fm_core.core_rails import go_to_tile
from Scripts.omgarturo.src.fm_core.core_items import LOG_STATIC_IDS, TREE_STATIC_IDS
from Scripts.omgarturo.src.fm_core.core_player import find_in_container_by_id
from Scripts.omgarturo.src.fm_core.core_player import open_bank_and_deposit_items
from System.Collections.Generic import List
import sys
import time

# Used this for the spellweaving quest to get fish steaks I believe. Worthless otherwise.

Player.HeadMessage(455, "start")

AMOUNT_TO_MAKE = 100

for i in range(0, AMOUNT_TO_MAKE):
    Spells.CastMagery("Create Food")    
    Misc.Pause(3000)