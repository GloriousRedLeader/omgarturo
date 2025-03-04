# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-01-11
# Use at your own risk. 

from Scripts.omgarturo.fm_core.core_gathering import run_crab_fishing_loop

# Deploys traps. Collects traps after trapDelayMs. Loots the traps. Moves crabs to hold.
# You need lobster traps in your bag. You need to stand near the cargo hold on your ship.
run_crab_fishing_loop(

    # Number of times to run the crab loop. Default is 1 then it stops.
    numLoops = 2,
    
    # If on a boat, tells the tiller to move forward this many times.
    moveTiles = 4, 
    
    # Number of traps to use. If you dont have this many, will use only what you have.
    maxTraps = 5,
    
    # How long to pause between casts
    trapDelayMs = 5000,
    
    # Will not do any fishHandling operations on this fish. Leaves it in backpack. Useful for fishing quests.
    fishToKeep = "blue crab"
)