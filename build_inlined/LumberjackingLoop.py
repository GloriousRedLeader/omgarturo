# ===============================================
# Imports
# ===============================================
from System import Byte, Int32
from System.Collections.Generic import List
import sys

# ===============================================
# Auto-generated inlined code. Do not edit
# ===============================================

# ===== Inlined block from core_gathering.py =====
# ===== Inlined block from core_rails.py =====
# ---- get_tile_behind (from core_rails.py)
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

# ---- move_items_to_pack_animal (from core_gathering.py)
def move_items_to_pack_animal(itemIds, packAnimalMobileId, itemMoveDelayMs):
    for itemId in itemIds:
        for item in Items.FindAllByID(itemId, -1, Player.Backpack.Serial, 0):
            packAnimals = get_pets(range = 2, checkLineOfSight = True, mobileId = packAnimalMobileId)
            
            if len(packAnimals) == 0:
                return
        
            for packAnimal in packAnimals:
                if packAnimal.Backpack.Weight < 1350:
                    print("Moving {} to {} (Weight: {})".format(item.Name, packAnimal.Name, packAnimal.Backpack.Weight))
                    Items.Move(item, packAnimal.Backpack.Serial, item.Amount)
                    Misc.Pause(itemMoveDelayMs)

# ---- cut_logs_to_boards (from core_gathering.py)
def cut_logs_to_boards(axe, itemMoveDelayMs):    
    for logStaticID in LOG_STATIC_IDS:
        logs = find_all_in_container_by_id(logStaticID, containerSerial = Player.Backpack.Serial)
        for log in logs:
            Items.UseItem(axe)
            Target.WaitForTarget(10000, False)
            Target.TargetExecute(log.Serial)
            Misc.Pause(itemMoveDelayMs)

# ---- Tree (from core_gathering.py)
class Tree:
    def __init__(self, x, y, z, staticId):
        self.x = x
        self.y = y
        self.z = z
        self.staticId = staticId
        self.tooFarAwayAttempts = 0
        
    def __str__(self):
        return f"Tree(x='{self.x}', y='{self.y}', z='{self.z}', staticId={self.staticId})"

# ---- cut_tree (from core_gathering.py)
def cut_tree(tree, tool, cutDelayMs):
    Target.Cancel()
    Misc.Pause(int(cutDelayMs / 2))
        
    if Player.MaxWeight - Player.Weight < 50:
        print("You are too heavy!")
        sys.exit()
    
    Journal.Clear()
    Items.UseItem(tool)
    Target.WaitForTarget(4000)
    print("Cutting tree {}".format(tree), 66)
    Target.TargetExecute(tree.x, tree.y, tree.z, tree.staticId)
    Misc.Pause(cutDelayMs)
    
    if Journal.Search("There's not enough wood here to harvest."):# '
        print("(no more wood) Moving on")
    elif Journal.Search("That is too far away"):
        tree.tooFarAwayAttempts = tree.tooFarAwayAttempts + 1
        Journal.Clear()
        if (tree.tooFarAwayAttempts < 5):
            #cut_tree(tree, tool, cutDelayMs)
            return True
        else:
            print("(cant reach tree) Moving on")
            return False
    else:
        #cut_tree(tree, tool, cutDelayMs)
        return True

# ---- drop_unwanted_resources (from core_gathering.py)
def drop_unwanted_resources(itemStaticIds, keepItemHues, itemMoveDelayMs):    
    for itemStaticId in itemStaticIds:
        resources = find_all_in_container_by_id(itemStaticId, containerSerial = Player.Backpack.Serial)
        for resource in resources:
            if resource.Color not in keepItemHues:
                print("Dropping {} on ground".format(resource.Name))
                tileX, tileY, tileZ = get_tile_behind(2)
                Items.MoveOnGround(resource, resource.Amount, tileX, tileY, tileZ)
                Misc.Pause(itemMoveDelayMs)

# ---- scan_trees (from core_gathering.py)
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
                            print("Tree Registered: {}".format(tree))

            minx = minx + 1
        minx = Player.Position.X - tileRange            
        miny = miny + 1

    Misc.SendMessage('Total Trees: %i' % (len(trees)), 66) 
    return trees

# ---- run_lumberjacking_loop (from core_gathering.py)
def run_lumberjacking_loop(

    # (Optional) Makes a square tileRange * tileRange and will search for trees inside of it. So,
    # all you have to do is place yourself near a bunch of trees and hit the hotkey that
    # runs this function.
    tileRange = 10, 
    
    # (Optional) If this limit is reached, the script just stops apparently.
    #weightLimit = 500, 
    
    # (Optional) Flag that will convert the logs into boards. I think you need an axe.
    cutLogsToBoards = True, 

    # (Optional) Only keep logs and boards that match these hues. By default that is all hues. Remove the ones
    # you wish to discard. It will drop them at your feet. It is a common case where you may not care
    # about the basic wood board (RESOURCE_HUE_DEFAULT), so remove that from the list if you only
    # want special woods.
    keepItemHues = [RESOURCE_HUE_DEFAULT, RESOURCE_HUE_OAK, RESOURCE_HUE_ASH, RESOURCE_HUE_YEW, RESOURCE_HUE_HEARTWOOD, RESOURCE_HUE_BLOODWOOD, RESOURCE_HUE_FROSTWOOD    ],
    
    # (Optional) The mobile ID of your pack animal. Defaults to blue beetle.
    packAnimalMobileId = BLUE_BEETLE_MOBILE_ID,
    
    # Ids of static tile graphics that we consider trees. May vary.
    # Default is all the trees I know about.
    treeStaticIds = TREE_STATIC_IDS,
    
    # (Optional) Number of miliseconds between item moves typically from one pack to another.
    itemMoveDelayMs = 1000,
    
    # (Optional) Number of miliseconds between chopping attempts. Reducing will make
    # script go faster.
    cutDelayMs = 2000
):

    axe = find_first_in_hands_by_ids(AXE_STATIC_IDS)
    if axe is None:
        print("Equipping axe")
        axe = find_first_in_container_by_ids(AXE_STATIC_IDS)
        equip_weapon(axe)
        
    axe = find_first_in_hands_by_ids(AXE_STATIC_IDS)
    if axe is None:
        print("Could not find axe!")
        return
        
    trees = scan_trees(tileRange, treeStaticIds)
    print("Total tree number {}".format(len(trees)))
    
    for tree in trees:
        print("Moving to a tree")

        drop_unwanted_resources(BOARD_STATIC_IDS + LOG_STATIC_IDS, keepItemHues, itemMoveDelayMs) 

        if cutLogsToBoards:
            cut_logs_to_boards(axe, itemMoveDelayMs)
        
        move_items_to_pack_animal(BOARD_STATIC_IDS, packAnimalMobileId, itemMoveDelayMs)
        
        go_to_tile(tree.x - 1, tree.y - 1, 10.0)
        
        #cut_tree(tree, axe, cutDelayMs)
        while cut_tree(tree, axe, cutDelayMs) == True:
            drop_unwanted_resources(BOARD_STATIC_IDS + LOG_STATIC_IDS, keepItemHues, itemMoveDelayMs) 

            if cutLogsToBoards:
                cut_logs_to_boards(axe, itemMoveDelayMs)
        
            move_items_to_pack_animal(BOARD_STATIC_IDS, packAnimalMobileId, itemMoveDelayMs)
            
        
        Misc.Pause(int(itemMoveDelayMs / 3))

    #cut_or_drop_logs(axe, keepItemHues, cutLogsToBoards, itemMoveDelayMs)
    #move_items_to_pack_animal(BOARD_STATIC_IDS, packAnimalMobileId, itemMoveDelayMs)        
    drop_unwanted_resources(BOARD_STATIC_IDS + LOG_STATIC_IDS, keepItemHues, itemMoveDelayMs) 

    if cutLogsToBoards:
        cut_logs_to_boards(axe, itemMoveDelayMs)
    
    move_items_to_pack_animal(BOARD_STATIC_IDS, packAnimalMobileId, itemMoveDelayMs)    
    
    print("All done")

# ===== Inlined block from core_mobiles.py =====
# ---- FIRE_BEETLE_MOBILE_ID (binding from core_mobiles.py)
FIRE_BEETLE_MOBILE_ID = 0x00A9

# ===== Inlined block from core_mobiles.py =====
# ---- BLUE_BEETLE_MOBILE_ID (binding from core_mobiles.py)
BLUE_BEETLE_MOBILE_ID = 0x0317

# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-02-12
# Use at your own risk. 


#run_lumberjacking_loop(tileRange = 12, weightLimit = 425, cutLogsToBoards = True, dropOnGround = False, packAnimalNames = ["one"])

# Makes a box around where player is standing and chops trees inside. The
# size of the box is determined by tileRange.
# You will need an axe equipped I believe.
run_lumberjacking_loop(

    # (Optional) Makes a square tileRange * tileRange and will search for trees inside of it. So,
    # all you have to do is place yourself near a bunch of trees and hit the hotkey that
    # runs this function.
    tileRange = 30, 
    
    # (Optional) Flag that will convert the logs into boards. I think you need an axe.
    cutLogsToBoards = True, 

    # (Optional) Only keep logs and boards that match these hues. By default that is all hues. Remove the ones
    # you wish to discard. It will drop them at your feet. It is a common case where you may not care
    # about the basic wood board (RESOURCE_HUE_DEFAULT), so remove that from the list if you only
    # want special woods.
    keepItemHues = [RESOURCE_HUE_OAK, RESOURCE_HUE_ASH, RESOURCE_HUE_YEW, RESOURCE_HUE_HEARTWOOD, RESOURCE_HUE_BLOODWOOD, RESOURCE_HUE_FROSTWOOD    ],
    
    # (Optional) The mobile ID of your pack animal. Defaults to blue beetle.
    packAnimalMobileId = BLUE_BEETLE_MOBILE_ID,
    
    # Ids of static tile graphics that we consider trees. May vary.
    # Default is all the trees I know about.
    treeStaticIds = TREE_STATIC_IDS,
    
    # (Optional) Number of miliseconds between item moves typically from one pack to another.
    itemMoveDelayMs = 1000,
    
    # (Optional) Number of miliseconds between chopping attempts. Reducing will make
    # script go faster.
    cutDelayMs = 2000
)