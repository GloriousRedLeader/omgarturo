from System import Byte, Int32
from System.Collections.Generic import List
from ctypes import wintypes
import ctypes
import sys
import time

# Constants
RESOURCE_HUE_COPPER = 2413
INGOT_STATIC_IDS = [7154]
ORE_STATIC_IDS = [6583, 6586, 6584, 6585, 0, 1045, 1119, 1752, 1109, 1719, 2430, 2002, 1348, 2413]
RESOURCE_HUE_AGAPITE = 2425
RESOURCE_HUE_GOLD = 2213
MINER_TOOLS_STATIC_IDS = [3897, 3718]
RESOURCE_HUE_BRONZE = 2418
SAND_STATIC_IDS = [16954]
STONE_STATIC_IDS = [6009]
RESOURCE_HUE_VERITE = 2207
FIRE_BEETLE_MOBILE_ID = 169
BLUE_BEETLE_MOBILE_ID = 791
RESOURCE_HUE_SHADOW_IRON = 2406
RESOURCE_HUE_VALORITE = 2219
RESOURCE_HUE_DULL_COPPER = 2419
RESOURCE_HUE_DEFAULT = 0

# Functions
def move(x):
    for _ in range(x):
        Player.Run(Player.Direction)
        Misc.Pause(200)
def smelt_ore(forgeAnimalMobileId, itemMoveDelayMs):
    forgeAnimals = get_pets(range=2, checkLineOfSight=True, mobileId=forgeAnimalMobileId)
    if len(forgeAnimals) > 0:
        for oreId in ORE_STATIC_IDS:
            ores = find_all_in_container_by_id(oreId, Player.Backpack.Serial)
            for ore in ores:
                Journal.Clear()
                Items.UseItem(ore)
                Target.WaitForTarget(5000, True)
                Target.TargetExecute(forgeAnimals[0])
                Misc.Pause(itemMoveDelayMs)
                if Journal.Search('There is not enough metal-bearing ore in this pile to make an ingot.'):
                    print(ore)
                    print(ore.Serial)
                    tileX, tileY, tileZ = get_tile_behind(2)
                    Items.MoveOnGround(ore, 0, tileX, tileY, 0)
                    Misc.Pause(itemMoveDelayMs)
        Misc.Pause(itemMoveDelayMs)
    else:
        print('No forge animal found')
def run_mining_loop(numTilesToMove=1, keepItemHues=[RESOURCE_HUE_DULL_COPPER, RESOURCE_HUE_SHADOW_IRON, RESOURCE_HUE_COPPER, RESOURCE_HUE_BRONZE, RESOURCE_HUE_GOLD, RESOURCE_HUE_AGAPITE, RESOURCE_HUE_VERITE, RESOURCE_HUE_VALORITE], packAnimalMobileId=BLUE_BEETLE_MOBILE_ID, forgeAnimalMobileId=FIRE_BEETLE_MOBILE_ID, itemMoveDelayMs=1000):
    while True:
        drop_unwanted_resources(INGOT_STATIC_IDS + STONE_STATIC_IDS + ORE_STATIC_IDS, keepItemHues, itemMoveDelayMs)
        smelt_ore(forgeAnimalMobileId, itemMoveDelayMs)
        move_items_to_pack_animal(INGOT_STATIC_IDS + STONE_STATIC_IDS + SAND_STATIC_IDS, packAnimalMobileId, itemMoveDelayMs)
        miningTool = getMinerTool()
        Journal.Clear()
        Items.UseItem(miningTool)
        Target.WaitForTarget(5000, True)
        tileSerial, tileX, tileY, tileZ = get_tile_in_front_serial()
        if tileSerial is not None:
            Target.TargetExecute(tileSerial)
        else:
            Target.TargetExecute(tileX, tileY, tileZ)
        Misc.Pause(itemMoveDelayMs)
        if should_move():
            move(numTilesToMove)
        Misc.Pause(int(itemMoveDelayMs / 2))
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
def get_tile_in_front_serial():
    tileX, tileY, tileZ = get_tile_in_front()
    filter = Items.Filter()
    filter.Graphics = List[Int32](1339)
    filter.OnGround = True
    filter.RangeMax = 1
    items = Items.ApplyFilter(filter)
    for item in items:
        if item.Position.X == tileX and item.Position.Y == tileY:
            return (item.Serial, tileX, tileY, tileZ)
    return (None, tileX, tileY, tileZ)
def find_all_in_container_by_id(itemID, containerSerial=Player.Backpack.Serial):
    return Items.FindAllByID(itemID, -1, containerSerial, 1)
def drop_unwanted_resources(itemStaticIds, keepItemHues, itemMoveDelayMs):
    for itemStaticId in itemStaticIds:
        resources = find_all_in_container_by_id(itemStaticId, containerSerial=Player.Backpack.Serial)
        for resource in resources:
            if resource.Color not in keepItemHues:
                print('Dropping {} on ground'.format(resource.Name))
                tileX, tileY, tileZ = get_tile_behind(2)
                Items.MoveOnGround(resource, resource.Amount, tileX, tileY, tileZ)
                Misc.Pause(itemMoveDelayMs)
def should_move():
    if Journal.Search('no metal') or Journal.Search('t mine that') or Journal.Search('no sand'):
        Journal.Clear()
        return True
    else:
        Journal.Clear()
        return False
def getMinerTool():
    for minerToolStaticID in MINER_TOOLS_STATIC_IDS:
        miningTool = find_in_container_by_id(minerToolStaticID, Player.Backpack.Serial)
        if miningTool is not None:
            return miningTool
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
def move_items_to_pack_animal(itemIds, packAnimalMobileId, itemMoveDelayMs):
    for itemId in itemIds:
        for item in Items.FindAllByID(itemId, -1, Player.Backpack.Serial, 0):
            packAnimals = get_pets(range=2, checkLineOfSight=True, mobileId=packAnimalMobileId)
            if len(packAnimals) == 0:
                return
            for packAnimal in packAnimals:
                if packAnimal.Backpack.Weight < 1350:
                    print('Moving {} to {} (Weight: {})'.format(item.Name, packAnimal.Name, packAnimal.Backpack.Weight))
                    Items.Move(item, packAnimal.Backpack.Serial, item.Amount)
                    Misc.Pause(itemMoveDelayMs)
def get_tile_behind(distance=1):
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
    return (tileX, tileY, Player.Position.Z)
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

# Main code
run_mining_loop(numTilesToMove=1, keepItemHues=[RESOURCE_HUE_DULL_COPPER, RESOURCE_HUE_SHADOW_IRON, RESOURCE_HUE_COPPER, RESOURCE_HUE_BRONZE, RESOURCE_HUE_GOLD, RESOURCE_HUE_AGAPITE, RESOURCE_HUE_VERITE, RESOURCE_HUE_VALORITE], packAnimalMobileId=BLUE_BEETLE_MOBILE_ID, forgeAnimalMobileId=FIRE_BEETLE_MOBILE_ID, itemMoveDelayMs=1000)
