# ===============================================
# Imports
# ===============================================
from System import Byte, Int32
from System.Collections.Generic import List
from ctypes import wintypes
import ctypes
import sys
import time

# ===============================================
# Auto-generated inlined code. Do not edit
# ===============================================

# ===== Inlined block from core_rails.py =====
# ---- run_defend_loop (from core_rails.py)
def run_defend_loop(

    # range is the number of tiles to search for monsters in each "sector"
    range = 6, 
    
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
):
    rails_stats("start")   
    
    while not Player.IsGhost:
        rails_stats("report_head")
        Misc.Pause(2000)
        
        eligible = get_enemies(range) 
        if len(eligible) > 0:  
            Player.HeadMessage(48, "Found {} things to attack".format(len(eligible)))    
            nearest = Mobiles.Select(eligible, 'Nearest')
            
            while Mobiles.FindBySerial(nearest.Serial) is not None and Player.DistanceTo(nearest)<=range:            
                Mobiles.Message(nearest,68,"^ {} tiles ^".format(Player.DistanceTo(nearest)),False)
                
                res = go_to_tile(nearest.Position.X, nearest.Position.Y, pathFindingTimeoutSeconds, tileOffset)
                
                Misc.Pause(250)
            
            # Pause a little longer if we are prioritizing gold so the auto looter can have a moment
            # dont do this in shitty places like deceipt.
            # The check for goToNearestAttempts is a general rule that tells us whether the monster
            # got away or not. It is more likely that there is loot and the monster is dead if attempts 
            # is greater than zero.
            if autoLootBufferMs > 0 and goToNearestAttempts > 0:
                Player.HeadMessage(48, "Pausing a little extra for more loot")
                Misc.Pause(autoLootBufferMs)
        else:
            Player.HeadMessage(48, "Nothing left in sector")
            Misc.Pause(1000)

# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-02-13
# Use at your own risk. 


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