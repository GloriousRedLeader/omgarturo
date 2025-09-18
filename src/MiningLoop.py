# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-02-12
# Use at your own risk. 

from Scripts.omgarturo.src.fm_core.core_gathering import run_mining_loop
from Scripts.omgarturo.src.fm_core.core_mobiles import FIRE_BEETLE_MOBILE_ID
from Scripts.omgarturo.src.fm_core.core_mobiles import BLUE_BEETLE_MOBILE_ID
from Scripts.omgarturo.src.fm_core.core_items import RESOURCE_HUE_DEFAULT
from Scripts.omgarturo.src.fm_core.core_items import RESOURCE_HUE_DULL_COPPER
from Scripts.omgarturo.src.fm_core.core_items import RESOURCE_HUE_SHADOW_IRON
from Scripts.omgarturo.src.fm_core.core_items import RESOURCE_HUE_COPPER
from Scripts.omgarturo.src.fm_core.core_items import RESOURCE_HUE_BRONZE
from Scripts.omgarturo.src.fm_core.core_items import RESOURCE_HUE_GOLD
from Scripts.omgarturo.src.fm_core.core_items import RESOURCE_HUE_AGAPITE
from Scripts.omgarturo.src.fm_core.core_items import RESOURCE_HUE_VERITE
from Scripts.omgarturo.src.fm_core.core_items import RESOURCE_HUE_VALORITE

# Mines in a straight line. Perfect for cave floors. Your character will mine
# a vein until it runs out and then step forward numTilesToMove tiles.
# You can provide a mobile ID for a pack animal and a forge animal
# so you can smelt and store smelted ore in your pack animal. Note: This is the
# mobile ID (NOT the Serial of your pack / forge animals). I have constants for these
# for commone ones like fire beetle and blue beetle.
run_mining_loop(

    # (Optional) After a vein runs out, how many tiles forward to move.
    numTilesToMove = 1,
    
    # (Optional) Only keep ingots that match these hues. By default that is all hues. Remove the ones
    # you wish to discard. It will drop them at your feet. It is a common case where you may not care
    # about the basic iron ingots (RESOURCE_HUE_DEFAULT), so remove that from the list if you only
    # want special ingots.
    keepItemHues = [RESOURCE_HUE_DULL_COPPER, RESOURCE_HUE_SHADOW_IRON, RESOURCE_HUE_COPPER, RESOURCE_HUE_BRONZE, RESOURCE_HUE_GOLD, RESOURCE_HUE_AGAPITE, RESOURCE_HUE_VERITE, RESOURCE_HUE_VALORITE],

    # (Optional) The mobile ID of your pack animal. NOT the Serial. Defaults to blue beetle.
    packAnimalMobileId = BLUE_BEETLE_MOBILE_ID,       
    
    # (Optional) The mobile ID of your forge animal. NOT the serial. Defaults to fire beetle.
    forgeAnimalMobileId = FIRE_BEETLE_MOBILE_ID,
    
    # (Optional) Number of miliseconds between item moves typically from one pack to another.
    itemMoveDelayMs = 1000
)