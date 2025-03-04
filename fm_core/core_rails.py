# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2024-03-26
# Use at your own risk. 

from Scripts.omgarturo.fm_core.core_player import move_all_items_from_container
from Scripts.omgarturo.fm_core.core_mobiles import get_enemies
from Scripts.omgarturo.fm_core.core_spells import cast_until_works
from System.Collections.Generic import List 
from System import Byte, Int32
import sys
import time

# This stuff is used to detect keypresses like mouse for movement
import ctypes
from ctypes import wintypes
user32 = ctypes.WinDLL('user32', use_last_error=True)
user32.GetAsyncKeyState.restype = wintypes.SHORT
user32.GetAsyncKeyState.argtypes = [wintypes.INT]

# Globals. Put in a class one day.
CORE_LOOP_DELAY_MS = 650
railsStartingTime = 0
railsEarnedGold = 0
railsLastGold = 0

# Is right mouse button down (player moving)? Does NOT detect if player is moving
# via rails.
def is_player_moving():
    return user32.GetAsyncKeyState(0x02) & 0x8000

# Lifted this from the mining script. Returns the same thing as relative
# to player +1 based on direction. The relative function doesnt always
# work for some reason though Target.TargetExecuteRelative(Player.Serial, 1)
def get_tile_in_front(distance = 1):
    direction = Player.Direction
    playerX = Player.Position.X
    playerY = Player.Position.Y
    playerZ = Player.Position.Z
    
    if direction == 'Up':
        tileX = playerX - distance
        tileY = playerY - distance
        tileZ = playerZ
    elif direction == 'North':
        tileX = playerX
        tileY = playerY - distance
        tileZ = playerZ
    elif direction == 'Right':
        tileX = playerX + distance
        tileY = playerY - distance
        tileZ = playerZ
    elif direction == 'East':
        tileX = playerX + distance
        tileY = playerY
        tileZ = playerZ
    elif direction == 'Down':
        tileX = playerX + distance
        tileY = playerY + distance
        tileZ = playerZ
    elif direction == 'South':
        tileX = playerX
        tileY = playerY + distance
        tileZ = playerZ
    elif direction == 'Left':
        tileX = playerX - distance
        tileY = playerY + distance
        tileZ = playerZ
    elif direction == 'West':
        tileX = playerX - distance
        tileY = playerY
        tileZ = playerZ
    return tileX, tileY, tileZ

# Get tile behind player
def get_tile_behind(distance = 1):
    direction = Player.Direction
    tileX = Player.Position.X
    tileY = Player.Position.Y
    
    if Player.Direction == 'Up':
        tileX = Player.Position.X + distance
        tileY = Player.Position.Y + distance
    elif Player.Direction == 'North':
        tileY = Player.Position.Y + distance
    elif Player.Direction == 'Right':
        tileX = Player.Position.X - distance
        tileY = Player.Position.Y + distance
    elif Player.Direction == 'East':
        tileX = Player.Position.X - distance
    elif Player.Direction == 'Down':
        tileX = Player.Position.X - distance
        tileY = Player.Position.Y - distance
    elif Player.Direction == 'South':
        tileY = Player.Position.Y - distance
    elif Player.Direction == 'Left':
        tileX = Player.Position.X + distance
        tileY = Player.Position.Y - distance
    elif Player.Direction == 'West':
        tileX = Player.Position.X + distance

    return tileX, tileY, Player.Position.Z
    
# Runs this many tiles forward according to player direction
# Not super useful, but helps with mining script or if you just
# want to go in a straight line.
def move(x):
    for _ in range(x):
        Player.Run(Player.Direction)
        Misc.Pause(200)

# Can potentially swap implementation to use this pathfinder:
# https://github.com/YulesRules/Ultima-Online-Razor-Enhanced-Pathfinding/blob/main/README.md
# The timeout value is in seconds. It is a float. 
# tileOffset of 0 means land right on x, y. Positive value means stop short of the 
# provided x, y. This is useful for casters or anyone who doesnt wish to be directly
# on top of a mobile.
def go_to_tile(
    # Desired X coordinate to travel to. Typically a mobile X.
    x, 
    
    # Desired Y coordinate to travel to. Typically a mobile Y.
    y, 
    
    # Number of seconds to attempt travel. Blocks until we arrive or this many seconds elapses.
    timeoutSeconds = -1, 
    
    # Value of 0 means land right on x, y. This is the default behavior. Positive value means stop 
    # short of the provided x, y by that many tiles. This is useful for casters or anyone who 
    # doesnt wish to be directly on top of a mobile.
    tileOffset = 0
):
    if Player.Position.X == x and Player.Position.Y == y:
        return True
        
    start_time = time.time()
    
    if tileOffset > 0:
        tiles = PathFinding.GetPath(x, y, True)
        numTiles = len(tiles) if tiles is not None else 0
        
        if numTiles - tileOffset > 1:
            # There is a duplicate of last tile entry. Its in there twice.
            tileIndex = numTiles - tileOffset - 2
            x = tiles[tileIndex].X
            y = tiles[tileIndex].Y
        else:
            return True
        
    route = PathFinding.Route() 
    route.X = x
    route.Y = y
    route.MaxRetry = 3
    route.IgnoreMobile = True
    route.Timeout = timeoutSeconds
    res = PathFinding.Go(route)
    
    #total = "{:.2f}".format(time.time() - start_time)
    return res  

# This method moves our character next to the x, y provided (not on top of it)
# the go_to_tile method is exact. This one takes a little bit more processing,
# and it is wonkie processing by the way, to find a tile adjacent to the target
# that is also closest along our path.
def go_to_adjacent_tile(x, y, timeoutSeconds = -1):

    start_time = time.time()
    path = PathFinding.GetPath(x, y, True)

    Misc.SendMessage("Timeout is {} and coords found {}".format(timeoutSeconds, len(path)))    
    if len(path) <= 2:
        Misc.SendMessage("Did not have to do any work we were already there", 48)
        return True

    # this is the secret to not standing on the monster and losing stamina
    # we are doing this because there is no way to directly interact with
    # a Tile object as it isnt exposed to python
    # In any case whats happening here is we are removing the last two entries
    # in the path which are the exact x, y (duplicated for some reason) so we stop
    # right in front of the tile
    path.RemoveAt(len(path) - 1)
    path.RemoveAt(len(path) - 1)

    res = PathFinding.RunPath(path, timeoutSeconds, useResync = False)
    
    total = "{:.2f}".format(time.time() - start_time)
    #Misc.SendMessage("It took {} seconds to generate a route result of {}".format(total, res), 48)
    return res

# range is the number of tiles to search for monsters in each "sector"
# autoLootBufferMs is the time in MS to stand around like an idiot before moving
# on after a monster dies. Gives the auto looter a little bit of extra time to grab
# gold. 0 means its disabled and no wait.
# pathFindingTimeoutSeconds is a float that represents number of seconds before quitting
# on a path. It is a value passed to the pathfinding method. The Pathfinding algorithm 
# could go on for days. Instead of derping, just give up after this many seconds and 
# move on with your life.
def do_route(
    # List of x,y coordinates. Will cycle through sequentially.
    path, 
    
    # If an enemy is found within this many tiles, go to that enemy. Stay there
    # until it is dead. If we cant reach it after x number of tries, quit and go back
    # to normal route.
    range = 6, 
    
    # Pause for this many MS after a mobile we are after dies.
    autoLootBufferMs = 0, 
    
    # Number of seconds to attempt travel. Blocks until we arrive or this many seconds elapses. 
    pathFindingTimeoutSeconds = 3.0,
    
    # Value of 0 means land right on x, y. This is the default behavior. Positive value means stop 
    # short of the provided x, y by that many tiles. This is useful for casters or anyone who 
    # doesnt wish to be directly on top of a mobile.
    tileOffset = 0
):
    sectorId = 0
    for coord in path:
        sectorId = sectorId + 1
        serialsToExclude = []

        while not Player.IsGhost:
            rails_stats("report_head")
            
            if not go_to_tile(coord[0],coord[1], pathFindingTimeoutSeconds):
                Misc.SendMessage("Cant make it to target, aborting this coord", 38)
                break
            
            Misc.Pause(1000)
            eligible = get_enemies(range, serialsToExclude) 

            if len(eligible) > 0:  
                nearest = Mobiles.Select(eligible, 'Nearest')
                goToNearestAttempts = 3
                while Mobiles.FindBySerial(nearest.Serial) is not None and Player.DistanceTo(nearest)<=range:            
                    res = go_to_tile(nearest.Position.X, nearest.Position.Y, pathFindingTimeoutSeconds, tileOffset)
                    Misc.Pause(50)
                    
                    if res == False or (Player.DistanceTo(nearest) > 1 and goToNearestAttempts <= 0):
                        serialsToExclude.append(nearest.Serial)
                        break
                    elif Player.DistanceTo(nearest) > 1:
                        goToNearestAttempts = goToNearestAttempts - 1
                    
                    Misc.Pause(250)
                        
                # Always pause for some amount because the world will end
                rails_stats("report_head")
                Misc.Pause(1000)
                
                # Pause a little longer if we are prioritizing gold so the auto looter can have a moment
                # dont do this in shitty places like deceipt.
                # The check for goToNearestAttempts is a general rule that tells us whether the monster
                # got away or not. It is more likely that there is loot and the monster is dead if attempts 
                # is greater than zero.
                if autoLootBufferMs > 0 and goToNearestAttempts > 0:
                    Misc.Pause(autoLootBufferMs)
            else:
                break
    
# Stays put until an enemy comes into range, then moves to it.
# Useful if you are at a champ for example. No need for a specific
# set of route coordinates, just stand still and wait until a mob
# happens by.
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

#Timer.Create("railsStatsTimer", 1)

# Crappy way of reporting gold per hour. The optiona parameter has the following values:
#   clear | start | reset = setse initial values and times to 0
#   report_head = flashes data above player head
#   report = Prints message in journal
def rails_stats(option):
    global railsStartingTime
    global railsEarnedGold
    global railsLastGold
    
    if option == "clear" or option == "start" or option == "reset":
        railsStartingTime = time.time()       
        railsEarnedGold = 0
        railsLastGold = Player.Gold
    elif option == "report_head" or option == "report":
        hours = (time.time() - railsStartingTime) / 60 / 60
        if  Player.Gold < railsLastGold:
            railsEarnedGold = railsEarnedGold + Player.Gold
            railsLastGold = Player.Gold
        elif railsLastGold != Player.Gold:
            railsEarnedGold = railsEarnedGold + Player.Gold - railsLastGold
            railsLastGold = Player.Gold
        timeMinutes =round((time.time() - railsStartingTime) / 60)
        
        if hours == 0:
            goldPerHour = 0
        else:
            goldPerHour = "{:,.0f}".format(railsEarnedGold / hours)

        if Timer.Check("railsStatsTimer") == False:
            message = "Gold Earned: {} Minutes: {} GPH: {}".format( "{:,.0f}".format(railsEarnedGold), timeMinutes, goldPerHour)
            Misc.SendMessage(message, 253)    
            Timer.Create("railsStatsTimer", 15000)

# Runs a route based on a list of [x, y] coordinates. Will run it repeatadly.
# It is recommended to make those routes a loop that start and end at or
# around the same coordinate since it loops indefinitely.
# You can find a list of coordinates predefined in fm_core/core_routes.py
# If an enemy is found within attackRange (configued below), your character will move
# to that enemy. It will follow it until it is dead or becomes unreachable.
# Use this script in conjunction with AttackLoop or CasterLoop which will do your offense.
def run_rail_loop(

    # (Required) This is a list of coordinates to travel. See core_routes for a list of available, pre-defined routes.
    # You can generate your own using the rails tool. Its easy. Just load up the script RailRecorder.py
    # and start adding points. Walk to a location, click add point. When youre done hit save. Open the file. It 
    # will contain a list of coordinates you can paste here. Your character will walk around like an idiot.
    path,

    # (Optional) Number of tiles to scan for nearby monsters. If you set this too high it will
    # try to find monsters through walls and in other maps and waste time.
    attackRange = 5,    
    
    # (Optional) Number of seconds to allow before giving up when going from one coord to another.
    # Default is 5 seconds.
    pathFindingTimeoutSeconds = 5.0,
    
    # (Optional) Give a little extra time to loot when a monster dies. This is useful. A nice value
    # is about 2 seconds.
    autoLootBufferMs = 2000,
    
    # (Optional) When a mob is found, your character will move right on top of it. This value governs
    # whether you should stop tileOffset tiles before it. This is useful for casters or anyone who 
    # doesnt wish to be directly on top of a mobile.
    # A value of 0 (default) means land right on the target x, y. Positive value means stop 
    # short of the provided x, y by that many tiles. 
    tileOffset = 0 
):
    rails_stats("start")        

    while not Player.IsGhost:
        if Player.Weight < Player.MaxWeight - 40:
            do_route(path, range = attackRange, autoLootBufferMs = autoLootBufferMs, pathFindingTimeoutSeconds = pathFindingTimeoutSeconds, tileOffset= tileOffset)
            rails_stats("report")
        else:
            Player.HeadMessage(48, "Stopping because max weight reached")
            break
