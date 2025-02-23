# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/uo-razor-enhanced
#   2025-02-13
# Use at your own risk. 

from Scripts.omgarturo.fm_core.core_rails import run_rail_loop
from Scripts.omgarturo.fm_core.core_routes import new_haven_noob_dungeon
from Scripts.omgarturo.fm_core.core_routes import new_haven_skeleton_town
from Scripts.omgarturo.fm_core.core_routes import deceipt_1_full
from Scripts.omgarturo.fm_core.core_routes import deceipt_2_full
from Scripts.omgarturo.fm_core.core_routes import tortuga_champ_spawn
from Scripts.omgarturo.fm_core.core_routes import vermin_horde_champ_middle
from Scripts.omgarturo.fm_core.core_routes import vermin_horde_champ_top
from Scripts.omgarturo.fm_core.core_routes import hythloth_2
from Scripts.omgarturo.fm_core.core_routes import hythloth_3
from Scripts.omgarturo.fm_core.core_routes import hythloth_4

Player.HeadMessage(48, "Starting Rail Loop")

# Runs a route based on a list of [x, y] coordinates. Will run it repeatadly.
# It is recommended to make those routes a loop that start and end at or
# around the same coordinate since it loops indefinitely.
# You can find a list of coordinates predefined in fm_core/core_routes.py
run_rail_loop(

    # (Required) This is a list of coordinates to travel. See core_routes for a list of available, pre-defined routes.
    # You can generate your own using the rails tool. It's easy. Just load up the script in fm_tools/RailRecorder.py
    # and start adding points. Walk to a location, click add point. When you're done hit save. Open the file. It 
    # will contain a list of coordinates you can paste here. Your character will walk around like an idiot.
    path = new_haven_noob_dungeon,

    # (Optional) Number of tiles to scan for nearby monsters. If you set this too high it will
    # try to find monsters through walls and in other maps and waste time.
    attackRange = 5,    
    
    # (Optional) Number of seconds to allow before giving up when going from one coord to another.
    # Default is 3 seconds.
    pathFindingTimeoutSeconds = 5.0,
    
    # (Optional) Give a little extra time to loot when a monster dies. This is useful. A nice value
    # is about 2000ms.
    autoLootBufferMs = 1000,
    
    # (Optional) Value of 0 means land right on x, y. This is the default behavior. Positive value means stop 
    # short of the provided x, y by that many tiles. This is useful for casters or anyone who 
    # doesnt wish to be directly on top of a mobile.
    tileOffset = 3
)