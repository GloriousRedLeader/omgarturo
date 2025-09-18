# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-02-12
# Use at your own risk. 

from Scripts.omgarturo.src.fm_core.core_items import RESOURCE_HUE_DEFAULT
from Scripts.omgarturo.src.fm_core.core_items import RESOURCE_HUE_OAK
from Scripts.omgarturo.src.fm_core.core_items import RESOURCE_HUE_ASH
from Scripts.omgarturo.src.fm_core.core_items import RESOURCE_HUE_YEW
from Scripts.omgarturo.src.fm_core.core_items import RESOURCE_HUE_HEARTWOOD
from Scripts.omgarturo.src.fm_core.core_items import RESOURCE_HUE_BLOODWOOD
from Scripts.omgarturo.src.fm_core.core_items import RESOURCE_HUE_FROSTWOOD
from Scripts.omgarturo.src.fm_core.core_items import TREE_STATIC_IDS
from Scripts.omgarturo.src.fm_core.core_gathering import run_lumberjacking_loop
from Scripts.omgarturo.src.fm_core.core_mobiles import FIRE_BEETLE_MOBILE_ID
from Scripts.omgarturo.src.fm_core.core_mobiles import BLUE_BEETLE_MOBILE_ID

#run_lumberjacking_loop(tileRange = 12, weightLimit = 425, cutLogsToBoards = True, dropOnGround = False, packAnimalNames = ["one"])

# Makes a box around where player is standing and chops trees inside. The
# size of the box is determined by tileRange.
# You will need an axe equipped I believe.
run_lumberjacking_loop(

    # (Optional) Makes a square tileRange * tileRange and will search for trees inside of it. So,
    # all you have to do is place yourself near a bunch of trees and hit the hotkey that
    # runs this function.
    tileRange = 30, 
    
    # (Optional) Flag that will convert the logs into boards. I think you need an axe.
    cutLogsToBoards = True, 

    # (Optional) Only keep logs and boards that match these hues. By default that is all hues. Remove the ones
    # you wish to discard. It will drop them at your feet. It is a common case where you may not care
    # about the basic wood board (RESOURCE_HUE_DEFAULT), so remove that from the list if you only
    # want special woods.
    keepItemHues = [RESOURCE_HUE_OAK, RESOURCE_HUE_ASH, RESOURCE_HUE_YEW, RESOURCE_HUE_HEARTWOOD, RESOURCE_HUE_BLOODWOOD, RESOURCE_HUE_FROSTWOOD    ],
    
    # (Optional) The mobile ID of your pack animal. Defaults to blue beetle.
    packAnimalMobileId = BLUE_BEETLE_MOBILE_ID,
    
    # Ids of static tile graphics that we consider trees. May vary.
    # Default is all the trees I know about.
    treeStaticIds = TREE_STATIC_IDS,
    
    # (Optional) Number of miliseconds between item moves typically from one pack to another.
    itemMoveDelayMs = 1000,
    
    # (Optional) Number of miliseconds between chopping attempts. Reducing will make
    # script go faster.
    cutDelayMs = 2000
)