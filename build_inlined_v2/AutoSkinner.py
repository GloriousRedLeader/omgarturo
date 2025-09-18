from System import Byte, Int32
from System.Collections.Generic import List
from ctypes import wintypes
import ctypes
import sys
import time

# Inlined dependencies (topologically sorted)
AXE_STATIC_IDS = [3913, 3911]
BOARD_STATIC_IDS = [7127]
DAGGER_STATIC_IDS = [3922]
INGOT_STATIC_IDS = [7154]
LOG_STATIC_IDS = [7133]
MINER_TOOLS_STATIC_IDS = [3897, 3718]
ORE_STATIC_IDS = [6583, 6586, 6584, 6585, 0, 1045, 1119, 1752, 1109, 1719, 2430, 2002, 1348, 2413]
SAND_STATIC_IDS = [16954]
STONE_STATIC_IDS = [6009]
TREE_STATIC_IDS = [3221, 3222, 3225, 3227, 3228, 3229, 3210, 3238, 3240, 3242, 3243, 3267, 3268, 3272, 3273, 3275, 3276, 3277, 3280, 3283, 3286, 3288, 3290, 3293, 3296, 3299, 3302, 3320, 3323, 3326, 3329, 3365, 3367, 3381, 3383, 3384, 3394, 3395, 3417, 3440, 3461, 3476, 3478, 3480, 3482, 3484, 3486, 3488, 3490, 3492, 3496]
def find_all_in_container_by_id(itemID, containerSerial=Player.Backpack.Serial):
    return Items.FindAllByID(itemID, -1, containerSerial, 1)
def find_first_in_container_by_name(itemName, containerSerial=Player.Backpack.Serial):
    return Items.FindByName(itemName, -1, containerSerial, 1)
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
def move(x):
    for _ in range(x):
        Player.Run(Player.Direction)
        Misc.Pause(200)
def move_all_items_from_container(sourceSerial, destinationSerial):
    for item in Items.FindBySerial(sourceSerial).Contains:
        Player.HeadMessage(455, 'Moving item {}'.format(item.Name))
        Items.Move(item, destinationSerial, item.Amount)
        Misc.Pause(800)
def move_item_to_container(item, destinationSerial):
    Items.Move(item, destinationSerial, item.Amount)
    Misc.Pause(800)
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

# Main code
self_pack = Player.Backpack.Serial
corpse = 8198
uncutleather = 4217
scalesType = 9908
scissorsType = 3999
bladeList = [11552, 3922, 3780, 5110, 3779]
leathersList = List[Int32](4225)
ignore = []
def scan():
    skin = Items.Filter()
    skin.Enabled = True
    skin.RangeMin = 0
    skin.RangeMax = 2
    skin.IsCorpse = True
    skins = Items.ApplyFilter(skin)
    for toskin in skins:
        if toskin:
            if not toskin.Serial in ignore:
                Misc.SendMessage('Corpse found', 20)
                skinLoot(toskin)
                ignore.append(toskin.Serial)
                Misc.Pause(1100)
    else:
        Misc.SendMessage('No corpse', 20)
def getByItemID(itemid, source):
    for item in Items.FindBySerial(source).Contains:
        if item.ItemID == itemid:
            return item
        else:
            Misc.NoOperation()
def getBlade():
    for item in bladeList:
        blade = getByItemID(item, self_pack)
        if blade is not None:
            return blade
def getLeatherFromGround():
    leatherFilter = Items.Filter()
    leatherFilter.Enabled = True
    leatherFilter.OnGround = True
    leatherFilter.Movable = True
    leatherFilter.Graphics = leathersList
    leatherFilter.RangeMax = 2
    leathers = Items.ApplyFilter(leatherFilter)
    Misc.SendMessage
    for leather in leathers:
        Items.Move(leather.Serial, self_pack, 100)
        Misc.Pause(700)
def skinLoot(x):
    corpse = x
    if corpse:
        Items.UseItem(corpse)
        Misc.Pause(550)
        for item in bladeList:
            blade = getBlade()
        if blade is not None:
            Items.UseItem(blade)
            Target.WaitForTarget(3000, True)
            Target.TargetExecute(corpse)
            Misc.Pause(1000)
        else:
            Misc.SendMessage('No Blades Found')
    else:
        Misc.SendMessage('cantfind corpse')
    leather = getByItemID(uncutleather, corpse.Serial)
    scales = getByItemID(scalesType, corpse.Serial)
    if scales is not None:
        Items.Move(scales, self_pack, 0)
        Misc.Pause(550)
    if leather is not None:
        Misc.Pause(150)
        Items.MoveOnGround(leather, 0, Player.Position.X + 1, Player.Position.Y + 1, Player.Position.Z)
        Misc.Pause(550)
        scissors = getByItemID(scissorsType, self_pack)
        if scissors is not None:
            Items.UseItem(scissors)
            Target.WaitForTarget(3000, True)
            Target.TargetExecute(leather)
            Misc.Pause(700)
        else:
            Misc.SendMessage('No Scissors Found')
        getLeatherFromGround()
while True:
    scan()
    Misc.Pause(3000)
