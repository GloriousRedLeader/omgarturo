# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-02-13
# Use at your own risk. 

from Scripts.omgarturo.fm_core.core_rails import run_defend_loop

Player.HeadMessage(48, "Starting Rail Loop Defend!")

# Stays put until an enemy comes into range, then moves to it.
# Useful if you are at a champ for example. No need for a specific
# set of route coordinates, just stand still and wait until a mob
# happens by.
run_defend_loop(

    # range is the number of tiles to search for monsters in each "sector"
    range = 5, 
    
    # autoLootBufferMs is the time in MS to stand around like an idiot before moving
    autoLootBufferMs = 0, 
    
    # pathFindingTimeoutSeconds is a float that represents number of seconds before quitting
    # on a path. It is a value passed to the pathfinding method. The Pathfinding algorithm 
    # could go on for days. Instead of derping, just give up after this many seconds and 
    # move on with your life.
    pathFindingTimeoutSeconds = 3.0,
    
    # Value of 0 means land right on x, y. This is the default behavior. Positive value means stop 
    # short of the provided x, y by that many tiles. This is useful for casters or anyone who 
    # doesnt wish to be directly on top of a mobile.
    tileOffset = 0    
)