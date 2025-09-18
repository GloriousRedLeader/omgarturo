from System import Byte, Int32
from System.Collections.Generic import List
from ctypes import wintypes
import ctypes
import sys
import time

# Inlined dependencies (topologically sorted)
BUTCHERS_WAR_CLEAVER_STATIC_ID = 11567
DAGGER_STATIC_ID = 3922
FISHING_POLE_STATIC_IDS = [3520]
FISH_STATIC_IDS = [17154, 17155, 17158, 17159, 2508, 2509, 2510, 2511, 17603, 17604, 17605, 17606, 17617, 17618, 17619, 17620]
HARVESTERS_BLADE_STATIC_ID = 11552
TRUE_NORTH_DIRECTION_MAP = ['Forward One', 'Right One', 'Back One', 'Left One']
corpseScannerCache = []
def equip_weapon(newItem):
    leftHand = Player.GetItemOnLayer('LeftHand')
    if leftHand != None:
        Player.UnEquipItemByLayer('LeftHand', True)
        Misc.Pause(1000)
    rightHand = Player.GetItemOnLayer('RightHand')
    if rightHand != None:
        Player.UnEquipItemByLayer('RightHand', True)
        Misc.Pause(1000)
    Player.EquipItem(newItem)
    Misc.Pause(1000)
    return [leftHand, rightHand]
def find_all_in_container_by_ids(itemIDs, containerSerial=Player.Backpack.Serial):
    items = []
    for itemID in itemIDs:
        items = items + Items.FindAllByID(itemID, -1, containerSerial, 1)
    return items
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
def find_in_hands_by_id(itemID):
    leftHand = Player.GetItemOnLayer('LeftHand')
    if leftHand != None and leftHand.ItemID == itemID:
        return leftHand
    rightHand = Player.GetItemOnLayer('RightHand')
    if rightHand != None and rightHand.ItemID == itemID:
        return rightHand
    return None
def get_boat_direction():
    boatDirection = None
    playerX = Player.Position.X
    playerY = Player.Position.Y
    Player.ChatSay('forward one')
    Misc.Pause(1000)
    if Player.Position.X < playerX:
        boatDirection = 'West'
        boatDirection = 1
    elif Player.Position.X > playerX:
        boatDirection = 'East'
        boatDirection = 3
    elif Player.Position.Y < playerY:
        boatDirection = 'North'
        boatDirection = 0
    elif Player.Position.Y > playerY:
        boatDirection = 'South'
        boatDirection = 2
    Player.ChatSay('back one')
    Misc.Pause(1000)
    return boatDirection
def get_corpses(range=2):
    filter = Items.Filter()
    filter.OnGround = True
    filter.RangeMax = range
    filter.IsCorpse = True
    return Items.ApplyFilter(filter)
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
def move_item_to_container(item, destinationSerial):
    Items.Move(item, destinationSerial, item.Amount)
    Misc.Pause(800)
def find_first_in_container_by_ids(itemIDs, containerSerial=Player.Backpack.Serial):
    for itemID in itemIDs:
        item = find_in_container_by_id(itemID, containerSerial)
        if item != None:
            return item
    return None
def find_first_in_hands_by_ids(itemIDs):
    for itemID in itemIDs:
        item = find_in_hands_by_id(itemID)
        if item != None:
            return item
    return None
def sail_to_tile(x, y, boatDirection, moveCmdLatencyMs=650):
    directionMap = TRUE_NORTH_DIRECTION_MAP[boatDirection:] + TRUE_NORTH_DIRECTION_MAP[:boatDirection]
    while True:
        if Player.Position.X == x and Player.Position.Y == y:
            break
        if Player.Position.X > x:
            Player.ChatSay(directionMap[3])
        elif Player.Position.X < x:
            Player.ChatSay(directionMap[1])
        elif Player.Position.Y < y:
            Player.ChatSay(directionMap[2])
        elif Player.Position.Y > y:
            Player.ChatSay(directionMap[0])
        Misc.Pause(1000)
def run_fishing_loop(fishRange=4, moveTiles=0, fishDelayMs=9000, fishHandling=0, fishToKeep=None, cutToolItemId=DAGGER_STATIC_ID, useCorpseScanner=False, corpseScannerMoveCommandDelayMs=650, corpseScannerPauseDelayMs=2000, corpseNames=['a deep sea serpents corpse', 'a sea serpents corpse']):
    global corpseScannerCache
    fishingPole = find_first_in_hands_by_ids(FISHING_POLE_STATIC_IDS)
    if fishingPole == None:
        fishingPole = find_first_in_container_by_ids(FISHING_POLE_STATIC_IDS)
        if fishingPole == None:
            print('Need a fishing pole')
            return False
        else:
            equip_weapon(fishingPole)
    while Player.Weight < Player.MaxWeight - 40:
        if fishHandling == 1:
            cutTool = Items.FindByID(cutToolItemId, -1, Player.Backpack.Serial, 1)
            if cutTool is not None:
                fishies = find_all_in_container_by_ids(FISH_STATIC_IDS)
                for fish in fishies:
                    if fishToKeep is not None and fish.Name.lower().find(fishToKeep.lower()) > -1:
                        Player.HeadMessage(28, 'Keeping fish {} item id {}'.format(fish.Name, fish.ItemID))
                        continue
                    print('Cutting fish {} item id {}'.format(fish.Name, fish.ItemID))
                    Items.UseItem(cutTool)
                    Target.WaitForTarget(1000, False)
                    Target.TargetExecute(fish)
            else:
                print('You have elected to cut fish however no dagger was found in backpack.')
                return
        elif fishHandling == 2:
            fishies = find_all_in_container_by_ids(FISH_STATIC_IDS)
            fil = Items.Filter()
            fil.Name = 'cargo hold'
            fil.RangeMax = 3
            hatches = Items.ApplyFilter(fil)
            if len(hatches) > 0:
                for fish in fishies:
                    if fishToKeep is not None and fish.Name.lower().find(fishToKeep.lower()) > -1:
                        Player.HeadMessage(28, 'Keeping fish {} item id {}'.format(fish.Name, fish.ItemID))
                        continue
                    print('Moving fish {} item id {}'.format(fish.Name, fish.ItemID))
                    move_item_to_container(fish, hatches[0].Serial)
        Target.Cancel()
        Items.UseItem(fishingPole)
        Target.WaitForTarget(2000, False)
        x, y, z = get_tile_in_front(fishRange)
        fished = False
        tileInfoList = Statics.GetStaticsTileInfo(x, y, Player.Map)
        if len(tileInfoList) > 0:
            for tileInfo in tileInfoList:
                val = Statics.GetTileFlag(tileInfo.StaticID, 'Wet')
                if Statics.GetTileFlag(tileInfo.StaticID, 'Wet') == True:
                    print('TargetExecute(x = {}, y = {}, staticZ = {}, staticId = {})'.format(x, y, tileInfo.StaticZ, tileInfo.StaticID))
                    Target.TargetExecute(x, y, tileInfo.StaticZ, tileInfo.StaticID)
                    fished = True
                    Misc.Pause(fishDelayMs)
                    break
        if not fished:
            landInfo = Statics.GetStaticsLandInfo(x, y, Player.Map)
            if landInfo is not None:
                val = Statics.GetLandFlag(landInfo.StaticID, 'Wet')
                if Statics.GetLandFlag(landInfo.StaticID, 'Wet'):
                    Target.TargetExecute(x, y, landInfo.StaticZ)
                    Misc.Pause(fishDelayMs)
                    fished = True
                else:
                    print('This tile is not wet')
        if useCorpseScanner:
            items = get_corpses(range=10)
            if len(items) > 0:
                playerX = Player.Position.X
                playerY = Player.Position.Y
                corpses = List[type(items[0])]([item for item in items if item.Name in corpseNames and item.Serial not in corpseScannerCache])
                if len(corpses) > 0:
                    boatDirection = get_boat_direction()
                    for corpse in corpses:
                        print(corpse.Name, corpse.Position.X, corpse.Position.Y)
                        sail_to_tile(corpse.Position.X, corpse.Position.Y, boatDirection, corpseScannerMoveCommandDelayMs)
                        Misc.Pause(corpseScannerPauseDelayMs)
                        print('cacheLooted size = {}'.format(len(corpseScannerCache)))
                        if len(corpseScannerCache) >= 30:
                            corpseScannerCache.pop(0)
                            print('cacheLooted popping one off {}'.format(len(corpseScannerCache)))
                        corpseScannerCache.append(corpse.Serial)
                    sail_to_tile(playerX, playerY, boatDirection, corpseScannerMoveCommandDelayMs)
        for i in range(0, moveTiles):
            Player.ChatSay('forward one')
            Misc.Pause(750)

# Main code
run_fishing_loop(fishRange=4, moveTiles=0, fishDelayMs=9000, fishHandling=0, fishToKeep=None, cutToolItemId=DAGGER_STATIC_ID, useCorpseScanner=False, corpseScannerMoveCommandDelayMs=650, corpseScannerPauseDelayMs=2000, corpseNames=['a deep sea serpents corpse', 'a sea serpents corpse'])
