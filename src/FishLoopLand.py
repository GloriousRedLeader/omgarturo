# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2024-03-26
# Use at your own risk. 

from Scripts.omgarturo.src.fm_core.core_gathering import run_fishing_loop
from Scripts.omgarturo.src.fm_core.core_items import DAGGER_STATIC_ID
from Scripts.omgarturo.src.fm_core.core_items import HARVESTERS_BLADE_STATIC_ID
from Scripts.omgarturo.src.fm_core.core_items import BUTCHERS_WAR_CLEAVER_STATIC_ID

# Auto fishes. Works on a boat. Works on a dock. Works if youre on a rock. 
# Take advantage of the moveTiles param to move boat after 
# each fishing attempt. It will say forward one X number of times.
# Can automatically cut fish. Can automatically store fish in hold.
# Can automatically move to nearby corpses so you can loot (this script does not
# loot though).
#
# Setup:
# 1) Read the parameters below and configure as needed.
# 2) If you want to automatically cut fish, you will need a basic dagger in your pack (or provide your own tool).
# 3) If you want to put fish directly in your hold, you will need to stand right on top of it.
# 4) You will need a fishing pole of course.
# 5) The useCorpseScanner feature will sail to nearby corpses so  you dont miss MiBs.
run_fishing_loop(

    # (Optional) How many tiles in front of character to cast. Defaults to 4 tiles
    # in front of character.
    fishRange = 4, 
    
    # (Optional) After each cast move the boat forward this many tiles. Useful if on a boat.
    # Just tells the tiller forward one this many times. Default is 0 (stay in same spot). 
    moveTiles = 0, 
    
    # (Optional) How long to pause between casts in ms. Default is 9000ms.
    fishDelayMs = 9000,
    
    # 0 = Do nothing, leave in backpack
    # 1 = cut fish with a tool of your choice to reduce weight, makes lots of fish steaks (see cutToolItemId)
    # 2 = place fish in cargo hold of ship, have to be standing near cargo hold
    fishHandling = 0,
    
    # (Optional) String name of fish you want to keep safe. Will not do any fishHandling operations on this fish. 
    # Leaves it in backpack. Useful if you are doing fish monger quests. Just type the fish name
    # you want to keep in your backpack (lower case). Default is none, but you could enter
    # something like "gray snapper"
    fishToKeep = None,
    
    # (Optional) The item id (not serial) of the tool you want to use to cut fish. Default is dagger but other
    # shards may have more optimized tools with bonuses.
    cutToolItemId = DAGGER_STATIC_ID,
    
    # (Optional) Enable this and you will sail to nearby corpses that match those in corpseNames below. This
    # is useful if you want to look sea serpents for MiBs and such. At present there is no support for auto loot.
    # You need to enable what you want in your auto looter (tazuo or doranas lootmaster).
    # This is very crude. It just sails one tile at a time until it finds a corpse. Then, it pauses for a bit
    # while your autolooter does what it needs to do. It will do this for all nearby corpses before returning to
    # where you started and resume fishing. There are several more options below to customize this behavior.
    useCorpseScanner = False,
    
    # (Optional) Time delay in miliseconds between issuing commands to move boat. Adjust based on your servers latency.
    corpseScannerMoveCommandDelayMs = 650,
    
    # (Optional) Set the number of miliseconds to wait at a corpse once reaching it so your auto looter can do the business.
    corpseScannerPauseDelayMs = 2000,
    
    # (Optional) Array of corpse names. Only sail to loot these. Useful for message in a bottle enemies.
    corpseNames = ["a deep sea serpents corpse", "a sea serpents corpse"],
)