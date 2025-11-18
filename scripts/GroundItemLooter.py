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

BLUE_BEETLE_ITEM_ID = 0x260F

BOARD_STATIC_IDS = [0x1BD7]

DAGGER_STATIC_IDS = [0x0F52]

INGOT_STATIC_IDS = [0x1BF2]

LOG_STATIC_IDS = [0x1BDD]

MINER_TOOLS_STATIC_IDS = [0x0F39, 0x0E86]

ORE_STATIC_IDS = [
    0x19B7, 
    0x19BA, 
    0x19B8, 
    0x19B9, 
    0x0000, 
    0x0415, 
    0x045F, 
    0x06D8, 
    0x0455, 
    0x06B7, 
    0x097E, 
    0x07D2, 
    0x0544 ,
    
    0x096D,
    #0x19B7
]

SAND_STATIC_IDS = [0x423A]

STONE_STATIC_IDS = [0x1779]

TREE_STATIC_IDS = [ 0x0C95, 0x0C96, 0x0C99, 0x0C9B, 0x0C9C, 0x0C9D, 0x0C8A, 0x0CA6,
    0x0CA8, 0x0CAA, 0x0CAB, 0x0CC3, 0x0CC4, 0x0CC8, 0x0CC9, 0x0CCB,
    0x0CCC, 0x0CCD, 0x0CD0, 0x0CD3, 0x0CD6, 0x0CD8, 0x0CDA, 0x0CDD, 0x0CE0,
    0x0CE3, 0x0CE6, 0x0CF8, 0x0CFB, 0x0CFE, 0x0D01, 0x0D25, 0x0D27, 0x0D35,
    0x0D37, 0x0D38, 0x0D42, 0x0D43, 0x0D59, 0x0D70, 0x0D85, 0x0D94, 0x0D96,
    0x0D98, 0x0D9A, 0x0D9C, 0x0D9E, 0x0DA0, 0x0DA2, 0x0DA4, 0x0DA8 ]

def find_all_in_container_by_id(itemID, containerSerial = Player.Backpack.Serial):
    return Items.FindAllByID(itemID, -1, containerSerial, 1)

def find_first_in_container_by_name(itemName, containerSerial = Player.Backpack.Serial):
    return Items.FindByName(itemName, -1, containerSerial, 1)

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

def get_friends_by_names (friendNames = [], range = 8):
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = range
    fil.Notorieties = List[Byte](bytes([1, 2]))
    fil.IsGhost = False
    fil.Friend = False
    fil.CheckLineOfSight = True
    mobs = Mobiles.ApplyFilter(fil)

    #listValid = [m.Serial for m in mobs if m.Name in friendNames]

    if len(mobs) > 0:
        mobsList = List[type(mobs[0])]([mob for mob in mobs if mob.Name in friendNames])
        return mobsList    
    
    
    #if len(listValid) == 0:
    #    return []

    #fil = Mobiles.Filter()
    #fil.Enabled = True
    #for l in listValid:
    #    fil.Serials.Add(l)
    #fil.RangeMax = range
    #fil.Notorieties = List[Byte](bytes([1, 2]))
    #fil.IsGhost = False
    #fil.Friend = False
    #fil.CheckLineOfSight = True

    mobs = Mobiles.ApplyFilter(fil)

    return mobs

def get_pets(range = 10, checkLineOfSight = True, mobileId = None):
    pets = []
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = range
    fil.Notorieties = List[Byte](bytes([1, 2]))
    fil.IsGhost = False
    fil.Friend = False
    fil.CheckLineOfSight = checkLineOfSight
    
    if mobileId is not None:
        fil.Bodies = List[Int32]([mobileId])
    
    blues = Mobiles.ApplyFilter(fil)    
    for blue in blues:
        if blue.CanRename:
            pets.append(blue)
    return pets

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

def move(x):
    for _ in range(x):
        Player.Run(Player.Direction)
        Misc.Pause(200)

def move_all_items_from_container(sourceSerial, destinationSerial):
    for item in Items.FindBySerial(sourceSerial).Contains:
        Player.HeadMessage(455, "Moving item {}".format(item.Name))
        Items.Move(item, destinationSerial, item.Amount)
        Misc.Pause(800)

def move_item_to_container(item, destinationSerial):
    Items.Move(item, destinationSerial, item.Amount)
    Misc.Pause(800)

def find_first_in_container_by_ids(itemIDs, containerSerial = Player.Backpack.Serial):
    for itemID in itemIDs:
        item = find_in_container_by_id(itemID, containerSerial)
        if item != None:
            return item
    return None

def move_item_to_container_by_id(itemID, sourceSerial, destinationSerial, color = -1):
    while True:
        item = find_in_container_by_id(itemID, sourceSerial, color = color, ignoreContainer = [])
        if item is not None:
            move_item_to_container(item, destinationSerial)
        else:
            break

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

# Will pick up items on the ground and stash them in inventory or giant beetles
# Will attempt to deploy giant beetles that are in inventory.
# You can use this for idocs. It isnt great though. Needs work.
# Basically it launches a bunch of beetles, looks for things on the ground
# and tries to stash as much crap as it finds in the beetles and your inventory.

deployGiantBeetle = True

Timer.Create( 'pingTimer', 1 )

numDeployedPets = len(Player.Pets)
if numDeployedPets < 5 and deployGiantBeetle:
    for blueBeetle in Items.FindAllByID(BLUE_BEETLE_ITEM_ID, -1, Player.Backpack.Serial, -1):
        Items.UseItem(blueBeetle)
        Misc.Pause(650)
        numDeployedPets = numDeployedPets + 1
        if numDeployedPets == 5:
            break

Player.ChatSay("All Follow Me")

while True:
    if Timer.Check( 'pingTimer' ) == False:
        Player.HeadMessage( 118, "Ground Looter Running...")
        Timer.Create( 'pingTimer', 3000)
        
    filter = Items.Filter()
    filter.Movable = 1
    filter.OnGround = True
    filter.RangeMax = 2
    items = Items.ApplyFilter(filter)

    packAnimals = get_pets()
    for packAnimal in packAnimals:
        Items.UseItem(packAnimal.Backpack.Serial)
        Misc.Pause(650)
        
    for item in items:
      
        if Player.Weight + item.Weight < Player.MaxWeight and ((not item.IsContainer and Player.Backpack.Contains.Count < 125) or (item.IsContainer and Player.Backpack.Contains.Count + item.Contains.Count < 125)):
            print("Moving item {}".format(item.Name))
            move_item_to_container(item, Player.Backpack.Serial)
        elif len(packAnimals) > 0:
            for packAnimal in packAnimals:
                Items.UseItem(packAnimal.Backpack.Serial)
                Misc.Pause(650)
                print("Animal: {}, Weight: {}, Items: {}".format(packAnimal.Name, packAnimal.Backpack.Weight, packAnimal.Backpack.Contains.Count))
                if packAnimal.Backpack.Weight + item.Weight < 1350:
                    if item.IsContainer:
                        if item.Contains.Count + packAnimal.Backpack.Contains.Count < 125:
                            print("Moving container {}".format(item.Name))
                            move_item_to_container(item, packAnimal.Backpack.Serial)
                            break
                        else:
                            print("Not moving container because there are too many items in the container")
                    else:
                        print("Moving container {}".format(item.Name))
                        move_item_to_container(item, packAnimal.Backpack.Serial)
                        break
                else:
                    print("Not moving item {} because it is too heavy".format(item.Name))
    Misc.Pause(650)                    
