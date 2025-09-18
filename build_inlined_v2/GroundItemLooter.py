from System import Byte, Int32
from System.Collections.Generic import List
from ctypes import wintypes
import ctypes
import sys
import time

# Constants
LOG_STATIC_IDS = [7133]
BOARD_STATIC_IDS = [7127]
AXE_STATIC_IDS = [3913, 3911]
DAGGER_STATIC_IDS = [3922]
INGOT_STATIC_IDS = [7154]
SAND_STATIC_IDS = [16954]
MINER_TOOLS_STATIC_IDS = [3897, 3718]
ORE_STATIC_IDS = [6583, 6586, 6584, 6585, 0, 1045, 1119, 1752, 1109, 1719, 2430, 2002, 1348, 2413]
STONE_STATIC_IDS = [6009]
BLUE_BEETLE_ITEM_ID = 9743
TREE_STATIC_IDS = [3221, 3222, 3225, 3227, 3228, 3229, 3210, 3238, 3240, 3242, 3243, 3267, 3268, 3272, 3273, 3275, 3276, 3277, 3280, 3283, 3286, 3288, 3290, 3293, 3296, 3299, 3302, 3320, 3323, 3326, 3329, 3365, 3367, 3381, 3383, 3384, 3394, 3395, 3417, 3440, 3461, 3476, 3478, 3480, 3482, 3484, 3486, 3488, 3490, 3492, 3496]

# Functions
def get_pets(range=10, checkLineOfSight=True, mobileId=None):
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
def move_item_to_container(item, destinationSerial):
    Items.Move(item, destinationSerial, item.Amount)
    Misc.Pause(800)
def get_friends_by_names(friendNames=[], range=8):
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = range
    fil.Notorieties = List[Byte](bytes([1, 2]))
    fil.IsGhost = False
    fil.Friend = False
    fil.CheckLineOfSight = True
    mobs = Mobiles.ApplyFilter(fil)
    if len(mobs) > 0:
        mobsList = List[type(mobs[0])]([mob for mob in mobs if mob.Name in friendNames])
        return mobsList
    mobs = Mobiles.ApplyFilter(fil)
    return mobs
def find_first_in_container_by_name(itemName, containerSerial=Player.Backpack.Serial):
    return Items.FindByName(itemName, -1, containerSerial, 1)
def go_to_tile(x, y, timeoutSeconds=-1, tileOffset=0):
    if Player.Position.X == x and Player.Position.Y == y:
        return True
    start_time = time.time()
    if tileOffset > 0:
        tiles = PathFinding.GetPath(x, y, True)
        numTiles = len(tiles) if tiles is not None else 0
        if numTiles - tileOffset > 1:
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
    return res
def find_all_in_container_by_id(itemID, containerSerial=Player.Backpack.Serial):
    return Items.FindAllByID(itemID, -1, containerSerial, 1)
def get_tile_in_front(distance=1):
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
    return (tileX, tileY, tileZ)
def move(x):
    for _ in range(x):
        Player.Run(Player.Direction)
        Misc.Pause(200)
def find_in_container_by_id(itemID, containerSerial=Player.Backpack.Serial, color=-1, ignoreContainer=[], recursive=False):
    ignoreColor = False
    if color == -1:
        ignoreColor = True
    container = Items.FindBySerial(containerSerial)
    if isinstance(itemID, int):
        foundItem = next((item for item in container.Contains if item.ItemID == itemID and (ignoreColor or item.Hue == color)), None)
    elif isinstance(itemID, list):
        foundItem = next((item for item in container.Contains if item.ItemID in itemID and (ignoreColor or item.Hue == color)), None)
    else:
        raise ValueError('Unknown argument type for itemID passed to FindItem().', itemID, container)
    if foundItem != None:
        return foundItem
    elif recursive == True:
        for item in container.Contains:
            if item.IsContainer:
                foundItem = find_in_container_by_id(itemID, containerSerial=item.Serial, color=color, ignoreContainer=ignoreContainer, recursive=recursive)
                if foundItem != None:
                    return foundItem
def find_first_in_container_by_ids(itemIDs, containerSerial=Player.Backpack.Serial):
    for itemID in itemIDs:
        item = find_in_container_by_id(itemID, containerSerial)
        if item != None:
            return item
    return None
def move_item_to_container_by_id(itemID, sourceSerial, destinationSerial, color=-1):
    while True:
        item = find_in_container_by_id(itemID, sourceSerial, color=color, ignoreContainer=[])
        if item is not None:
            move_item_to_container(item, destinationSerial)
        else:
            break
def move_all_items_from_container(sourceSerial, destinationSerial):
    for item in Items.FindBySerial(sourceSerial).Contains:
        Player.HeadMessage(455, 'Moving item {}'.format(item.Name))
        Items.Move(item, destinationSerial, item.Amount)
        Misc.Pause(800)

# Main code
deployGiantBeetle = True
Timer.Create('pingTimer', 1)
numDeployedPets = len(Player.Pets)
if numDeployedPets < 5 and deployGiantBeetle:
    for blueBeetle in Items.FindAllByID(BLUE_BEETLE_ITEM_ID, -1, Player.Backpack.Serial, -1):
        Items.UseItem(blueBeetle)
        Misc.Pause(650)
        numDeployedPets = numDeployedPets + 1
        if numDeployedPets == 5:
            break
Player.ChatSay('All Follow Me')
while True:
    if Timer.Check('pingTimer') == False:
        Player.HeadMessage(118, 'Ground Looter Running...')
        Timer.Create('pingTimer', 3000)
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
        if Player.Weight + item.Weight < Player.MaxWeight and (not item.IsContainer and Player.Backpack.Contains.Count < 125 or (item.IsContainer and Player.Backpack.Contains.Count + item.Contains.Count < 125)):
            print('Moving item {}'.format(item.Name))
            move_item_to_container(item, Player.Backpack.Serial)
        elif len(packAnimals) > 0:
            for packAnimal in packAnimals:
                Items.UseItem(packAnimal.Backpack.Serial)
                Misc.Pause(650)
                print('Animal: {}, Weight: {}, Items: {}'.format(packAnimal.Name, packAnimal.Backpack.Weight, packAnimal.Backpack.Contains.Count))
                if packAnimal.Backpack.Weight + item.Weight < 1350:
                    if item.IsContainer:
                        if item.Contains.Count + packAnimal.Backpack.Contains.Count < 125:
                            print('Moving container {}'.format(item.Name))
                            move_item_to_container(item, packAnimal.Backpack.Serial)
                            break
                        else:
                            print('Not moving container because there are too many items in the container')
                    else:
                        print('Moving container {}'.format(item.Name))
                        move_item_to_container(item, packAnimal.Backpack.Serial)
                        break
                else:
                    print('Not moving item {} because it is too heavy'.format(item.Name))
    Misc.Pause(650)
