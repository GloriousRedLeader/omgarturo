# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/uo-razor-enhanced
#   2024-03-26
# Use at your own risk. 

from Scripts.omgarturo.fm_core.core_gathering import run_fishing_loop

# Auto fishes in all the lands. Works on a boat. Works on a dock.
# Works if youre on a rock. Take advantage of the moveTiles param to move boat after 
# each fishing attempt. It will say forward one X number of times.
# Can automatically cut fish. Can automatically store fish in hold.
run_fishing_loop(

    # (Optional) How many tiles in front of character to cast. Defaults to 4 tiles
    # in front of character.
    fishRange = 4, 
    
    # (Optional) After each cast move the boat forward this many tiles. Useful if on a boat.
    # Just tells the tiller forward one this many times. Default is 0 (stay in same spot). 
    moveTiles = 0, 
    
    # (Optional) How long to pause between casts in ms. Default is 9000ms.
    fishDelayMs = 9000,
    
    # 0 = Do nothing, leave in backpack (default)
    # 1 = cut fish with dagger to reduce weight, makes lots of fish steaks
    # 2 = place fish in cargo hold of ship, have to be standing near cargo hold
    fishHandling = 1,
    
    # (Optional) String name of fish you want to keep safe. Will not do any fishHandling operations on this fish. 
    # Leaves it in backpack. Useful for fishing quests. Useful if you are doing fish monger quests. 
    # Default is none.
    fishToKeep = None,
    
    # (Optional) function to call after each fishing attempt, e.g. auto looter (see below)
    # You can call some misc. logic to do whatever you want after each cast
    callback = None
)