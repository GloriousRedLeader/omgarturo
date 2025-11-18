# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-11-18
# Use at your own risk.

# ##########################################################
# #                                                        #
# #              INLINED DEPENDENCIES                      #
# #                                                        #
# #  DO NOT EDIT THIS SECTION - AUTO-GENERATED CODE        #
# #                                                        #
# #  These are dependencies from fm_core that have been    #
# #  automatically inlined. For user-editable code,        #
# #  scroll down to the bottom of this file.               #
# #                                                        #
# ##########################################################

from System import Byte, Int32
from System.Collections.Generic import List
from ctypes import wintypes
import ctypes
import sys
import time

LOG_STATIC_IDS = [0x1BDD]

TREE_STATIC_IDS = [ 0x0C95, 0x0C96, 0x0C99, 0x0C9B, 0x0C9C, 0x0C9D, 0x0C8A, 0x0CA6,
    0x0CA8, 0x0CAA, 0x0CAB, 0x0CC3, 0x0CC4, 0x0CC8, 0x0CC9, 0x0CCB,
    0x0CCC, 0x0CCD, 0x0CD0, 0x0CD3, 0x0CD6, 0x0CD8, 0x0CDA, 0x0CDD, 0x0CE0,
    0x0CE3, 0x0CE6, 0x0CF8, 0x0CFB, 0x0CFE, 0x0D01, 0x0D25, 0x0D27, 0x0D35,
    0x0D37, 0x0D38, 0x0D42, 0x0D43, 0x0D59, 0x0D70, 0x0D85, 0x0D94, 0x0D96,
    0x0D98, 0x0D9A, 0x0D9C, 0x0D9E, 0x0DA0, 0x0DA2, 0x0DA4, 0x0DA8 ]

def find_in_container_by_id(itemID, containerSerial = Player.Backpack.Serial, color = -1, ignoreContainer = [], recursive = False):
    ignoreColor = False
    if color == -1:
        ignoreColor = True
        
    container = Items.FindBySerial(containerSerial)

    if isinstance( itemID, int ):
        foundItem = next( ( item for item in container.Contains if ( item.ItemID == itemID and ( ignoreColor or item.Hue == color ) ) ), None )
    elif isinstance( itemID, list ):
        foundItem = next( ( item for item in container.Contains if ( item.ItemID in itemID and ( ignoreColor or item.Hue == color ) ) ), None )
    else:
        raise ValueError( 'Unknown argument type for itemID passed to FindItem().', itemID, container )

    if foundItem != None:
        return foundItem        
    elif recursive == True:
        for item in container.Contains:
            if item.IsContainer:
                foundItem = find_in_container_by_id(itemID, containerSerial = item.Serial, color = color, ignoreContainer = ignoreContainer, recursive = recursive)
                if foundItem != None:
                    return foundItem

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

def move_all_items_from_container(sourceSerial, destinationSerial):
    for item in Items.FindBySerial(sourceSerial).Contains:
        Player.HeadMessage(455, "Moving item {}".format(item.Name))
        Items.Move(item, destinationSerial, item.Amount)
        Misc.Pause(800)

# ##########################################################
# #                                                        #
# #                 USER EDITABLE CODE                      #
# #                                                        #
# #  This is the original script code that you can         #
# #  modify and customize. Edit the parameters, logic,     #
# #  and function calls below as needed for your setup.    #
# #                                                        #
# #  The dependencies above have been automatically        #
# #  inlined and should not be modified.                   #
# ##########################################################

# Used this for the spellweaving quest to get fish steaks I believe. Worthless otherwise.

Player.HeadMessage(455, "start")

AMOUNT_TO_MAKE = 100

for i in range(0, AMOUNT_TO_MAKE):
    Spells.CastMagery("Create Food")    
    Misc.Pause(3000)
