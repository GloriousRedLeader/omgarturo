from System import Byte, Int32
from System.Collections.Generic import List
from ctypes import wintypes
import ctypes
import sys
import time

# Inlined dependencies (topologically sorted)
AXE_STATIC_IDS = [3913, 3911]
BLUE_BEETLE_MOBILE_ID = 791
BOARD_STATIC_IDS = [7127]
FIRE_BEETLE_MOBILE_ID = 169
LOG_STATIC_IDS = [7133]
RESOURCE_HUE_ASH = 1191
RESOURCE_HUE_BLOODWOOD = 1194
RESOURCE_HUE_DEFAULT = 0
RESOURCE_HUE_FROSTWOOD = 1151
RESOURCE_HUE_HEARTWOOD = 1193
RESOURCE_HUE_OAK = 2010
RESOURCE_HUE_YEW = 1192
TREE_STATIC_IDS = [3221, 3222, 3225, 3227, 3228, 3229, 3210, 3238, 3240, 3242, 3243, 3267, 3268, 3272, 3273, 3275, 3276, 3277, 3280, 3283, 3286, 3288, 3290, 3293, 3296, 3299, 3302, 3320, 3323, 3326, 3329, 3365, 3367, 3381, 3383, 3384, 3394, 3395, 3417, 3440, 3461, 3476, 3478, 3480, 3482, 3484, 3486, 3488, 3490, 3492, 3496]
class Tree:

    def __init__(self, x, y, z, staticId):
        self.x = x
        self.y = y
        self.z = z
        self.staticId = staticId
        self.tooFarAwayAttempts = 0

    def __str__(self):
        return f"Tree(x='{self.x}', y='{self.y}', z='{self.z}', staticId={self.staticId})"
def cut_tree(tree, tool, cutDelayMs):
    Target.Cancel()
    Misc.Pause(int(cutDelayMs / 2))
    if Player.MaxWeight - Player.Weight < 50:
        print('You are too heavy!')
        sys.exit()
    Journal.Clear()
    Items.UseItem(tool)
    Target.WaitForTarget(4000)
    print('Cutting tree {}'.format(tree), 66)
    Target.TargetExecute(tree.x, tree.y, tree.z, tree.staticId)
    Misc.Pause(cutDelayMs)
    if Journal.Search("There's not enough wood here to harvest."):
        print('(no more wood) Moving on')
    elif Journal.Search('That is too far away'):
        tree.tooFarAwayAttempts = tree.tooFarAwayAttempts + 1
        Journal.Clear()
        if tree.tooFarAwayAttempts < 5:
            return True
        else:
            print('(cant reach tree) Moving on')
            return False
    else:
        return True
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
def find_all_in_container_by_id(itemID, containerSerial=Player.Backpack.Serial):
    return Items.FindAllByID(itemID, -1, containerSerial, 1)
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
def cut_logs_to_boards(axe, itemMoveDelayMs):
    for logStaticID in LOG_STATIC_IDS:
        logs = find_all_in_container_by_id(logStaticID, containerSerial=Player.Backpack.Serial)
        for log in logs:
            Items.UseItem(axe)
            Target.WaitForTarget(10000, False)
            Target.TargetExecute(log.Serial)
            Misc.Pause(itemMoveDelayMs)
def drop_unwanted_resources(itemStaticIds, keepItemHues, itemMoveDelayMs):
    for itemStaticId in itemStaticIds:
        resources = find_all_in_container_by_id(itemStaticId, containerSerial=Player.Backpack.Serial)
        for resource in resources:
            if resource.Color not in keepItemHues:
                print('Dropping {} on ground'.format(resource.Name))
                tileX, tileY, tileZ = get_tile_behind(2)
                Items.MoveOnGround(resource, resource.Amount, tileX, tileY, tileZ)
                Misc.Pause(itemMoveDelayMs)
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
def scan_trees(tileRange, treeStaticIds):
    minx = Player.Position.X - tileRange
    maxx = Player.Position.X + tileRange
    miny = Player.Position.Y - tileRange
    maxy = Player.Position.Y + tileRange
    trees = []
    while miny <= maxy:
        while minx <= maxx:
            tileinfo = Statics.GetStaticsTileInfo(minx, miny, Player.Map)
            if tileinfo.Count > 0:
                for tile in tileinfo:
                    for staticid in treeStaticIds:
                        if staticid == tile.StaticID:
                            tree = Tree(minx, miny, tile.StaticZ, tile.StaticID)
                            trees.append(tree)
                            print('Tree Registered: {}'.format(tree))
            minx = minx + 1
        minx = Player.Position.X - tileRange
        miny = miny + 1
    Misc.SendMessage('Total Trees: %i' % len(trees), 66)
    return trees
def run_lumberjacking_loop(tileRange=10, cutLogsToBoards=True, keepItemHues=[RESOURCE_HUE_DEFAULT, RESOURCE_HUE_OAK, RESOURCE_HUE_ASH, RESOURCE_HUE_YEW, RESOURCE_HUE_HEARTWOOD, RESOURCE_HUE_BLOODWOOD, RESOURCE_HUE_FROSTWOOD], packAnimalMobileId=BLUE_BEETLE_MOBILE_ID, treeStaticIds=TREE_STATIC_IDS, itemMoveDelayMs=1000, cutDelayMs=2000):
    axe = find_first_in_hands_by_ids(AXE_STATIC_IDS)
    if axe is None:
        print('Equipping axe')
        axe = find_first_in_container_by_ids(AXE_STATIC_IDS)
        equip_weapon(axe)
    axe = find_first_in_hands_by_ids(AXE_STATIC_IDS)
    if axe is None:
        print('Could not find axe!')
        return
    trees = scan_trees(tileRange, treeStaticIds)
    print('Total tree number {}'.format(len(trees)))
    for tree in trees:
        print('Moving to a tree')
        drop_unwanted_resources(BOARD_STATIC_IDS + LOG_STATIC_IDS, keepItemHues, itemMoveDelayMs)
        if cutLogsToBoards:
            cut_logs_to_boards(axe, itemMoveDelayMs)
        move_items_to_pack_animal(BOARD_STATIC_IDS, packAnimalMobileId, itemMoveDelayMs)
        go_to_tile(tree.x - 1, tree.y - 1, 10.0)
        while cut_tree(tree, axe, cutDelayMs) == True:
            drop_unwanted_resources(BOARD_STATIC_IDS + LOG_STATIC_IDS, keepItemHues, itemMoveDelayMs)
            if cutLogsToBoards:
                cut_logs_to_boards(axe, itemMoveDelayMs)
            move_items_to_pack_animal(BOARD_STATIC_IDS, packAnimalMobileId, itemMoveDelayMs)
        Misc.Pause(int(itemMoveDelayMs / 3))
    drop_unwanted_resources(BOARD_STATIC_IDS + LOG_STATIC_IDS, keepItemHues, itemMoveDelayMs)
    if cutLogsToBoards:
        cut_logs_to_boards(axe, itemMoveDelayMs)
    move_items_to_pack_animal(BOARD_STATIC_IDS, packAnimalMobileId, itemMoveDelayMs)
    print('All done')

# Main code
run_lumberjacking_loop(tileRange=30, cutLogsToBoards=True, keepItemHues=[RESOURCE_HUE_OAK, RESOURCE_HUE_ASH, RESOURCE_HUE_YEW, RESOURCE_HUE_HEARTWOOD, RESOURCE_HUE_BLOODWOOD, RESOURCE_HUE_FROSTWOOD], packAnimalMobileId=BLUE_BEETLE_MOBILE_ID, treeStaticIds=TREE_STATIC_IDS, itemMoveDelayMs=1000, cutDelayMs=2000)
