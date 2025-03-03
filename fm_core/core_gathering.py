# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/uo-razor-enhanced
#   2024-03-26
# Use at your own risk. 

from System.Collections.Generic import List
import sys
from System import Byte, Int32
from Scripts.omgarturo.fm_core.core_player import find_first_in_container_by_ids
from Scripts.omgarturo.fm_core.core_player import find_first_in_hands_by_ids
from Scripts.omgarturo.fm_core.core_player import move_all_items_from_container
from Scripts.omgarturo.fm_core.core_player import move_item_to_container_by_id
from Scripts.omgarturo.fm_core.core_player import move_item_to_container
from Scripts.omgarturo.fm_core.core_player import find_in_container_by_id
from Scripts.omgarturo.fm_core.core_player import find_first_in_container_by_name
from Scripts.omgarturo.fm_core.core_player import find_all_in_container_by_id
from Scripts.omgarturo.fm_core.core_player import find_all_in_container_by_ids
from Scripts.omgarturo.fm_core.core_player import equip_weapon
from Scripts.omgarturo.fm_core.core_rails import move
from Scripts.omgarturo.fm_core.core_rails import go_to_tile
from Scripts.omgarturo.fm_core.core_rails import get_tile_in_front
from Scripts.omgarturo.fm_core.core_rails import get_tile_behind
from Scripts.omgarturo.fm_core.core_items import get_corpses
from Scripts.omgarturo.fm_core.core_items import AXE_STATIC_IDS
from Scripts.omgarturo.fm_core.core_items import LOG_STATIC_IDS
from Scripts.omgarturo.fm_core.core_items import TREE_STATIC_IDS
from Scripts.omgarturo.fm_core.core_items import DAGGER_STATIC_IDS
from Scripts.omgarturo.fm_core.core_items import DAGGER_STATIC_ID
from Scripts.omgarturo.fm_core.core_items import BOARD_STATIC_IDS
from Scripts.omgarturo.fm_core.core_items import MINER_TOOLS_STATIC_IDS
from Scripts.omgarturo.fm_core.core_items import ORE_STATIC_IDS
from Scripts.omgarturo.fm_core.core_items import INGOT_STATIC_IDS
from Scripts.omgarturo.fm_core.core_items import STONE_STATIC_IDS
from Scripts.omgarturo.fm_core.core_items import SAND_STATIC_IDS
from Scripts.omgarturo.fm_core.core_items import FISH_STATIC_IDS
from Scripts.omgarturo.fm_core.core_items import LOBSTER_TRAP_STATIC_IDS
from Scripts.omgarturo.fm_core.core_items import DEPLOYED_LOBSTER_TRAP_STATIC_ID
from Scripts.omgarturo.fm_core.core_items import FISHING_POLE_STATIC_IDS
from Scripts.omgarturo.fm_core.core_items import RESOURCE_HUE_DEFAULT
from Scripts.omgarturo.fm_core.core_items import RESOURCE_HUE_OAK
from Scripts.omgarturo.fm_core.core_items import RESOURCE_HUE_ASH
from Scripts.omgarturo.fm_core.core_items import RESOURCE_HUE_YEW
from Scripts.omgarturo.fm_core.core_items import RESOURCE_HUE_HEARTWOOD
from Scripts.omgarturo.fm_core.core_items import RESOURCE_HUE_BLOODWOOD
from Scripts.omgarturo.fm_core.core_items import RESOURCE_HUE_FROSTWOOD
from Scripts.omgarturo.fm_core.core_items import RESOURCE_HUE_DULL_COPPER
from Scripts.omgarturo.fm_core.core_items import RESOURCE_HUE_SHADOW_IRON
from Scripts.omgarturo.fm_core.core_items import RESOURCE_HUE_COPPER
from Scripts.omgarturo.fm_core.core_items import RESOURCE_HUE_BRONZE
from Scripts.omgarturo.fm_core.core_items import RESOURCE_HUE_GOLD
from Scripts.omgarturo.fm_core.core_items import RESOURCE_HUE_AGAPITE
from Scripts.omgarturo.fm_core.core_items import RESOURCE_HUE_VERITE
from Scripts.omgarturo.fm_core.core_items import RESOURCE_HUE_VALORITE
from Scripts.omgarturo.fm_core.core_mobiles import FIRE_BEETLE_MOBILE_ID
from Scripts.omgarturo.fm_core.core_mobiles import BLUE_BEETLE_MOBILE_ID
from Scripts.omgarturo.fm_core.core_mobiles import get_friends_by_names
from Scripts.omgarturo.fm_core.core_mobiles import get_pets

# This contains three main gathering loops:
# 1. run_lumberjacking_loop
# 2. run_mining_loop
# 3. run_fishing_loop
#
# Use with caution. Dont be rude.
#
# Lumberjacking original author: https://github.com/hampgoodwin/razorenhancedscripts/blob/master/LumberjackingScanTile.py
# Mining original author: https://github.com/getoldgaming/razor-enhanced-/blob/master/autoMiner.py
# Note I did modify these and make them much worse. Use the one linked above.


################## ################## ################## ##################
#
#   Lumberjacking
#
################## ################## ################## ##################

# Represents a tree to cut
class Tree:
    def __init__(self, x, y, z, staticId):
        self.x = x
        self.y = y
        self.z = z
        self.staticId = staticId
        self.tooFarAwayAttempts = 0
        
    def __str__(self):
        return f"Tree(x='{self.x}', y='{self.y}', z='{self.z}', staticId={self.staticId})"                        

# Internal helper to generate a list of Tree        
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
    
# Internal helper method that cuts a tree with either axe (logs) or dagger (kindling)
# Returns True if there is more wood to harvest, False if it is time to move on
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
    
# Internal helper  method to discard logs or cut logs into boards
def cut_logs_to_boards(axe, itemMoveDelayMs):    
    for logStaticID in LOG_STATIC_IDS:
        logs = find_all_in_container_by_id(logStaticID, containerSerial = Player.Backpack.Serial)
        for log in logs:
            Items.UseItem(axe)
            Target.WaitForTarget(10000, False)
            Target.TargetExecute(log.Serial)
            Misc.Pause(itemMoveDelayMs)    
            
# Makes a box around where player is standing and chops trees inside. The
# size of the box is determined by tileRange.
# You will need an axe equipped I believe.
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
            
# Variation of above that will get kindling usinga knife
def run_kindling_loop(

    # Makes a square tileRange * tileRange and will search for trees inside of it. So,
    # all you have to do is place yourself near a bunch of trees and hit the hotkey that
    # runs this function.
    tileRange = 10, 
    
    # Ids of static tile graphics that we consider trees. May vary.
    # Default is all the trees I know about.
    treeStaticIds = TREE_STATIC_IDS,
    
    # (Optional) Number of miliseconds between chopping attempts. Reducing will make
    # script go faster.
    cutDelayMs = 2000
):
    
    Misc.SendMessage("Getting Kindling", 123)
    dagger = find_first_in_container_by_ids(DAGGER_STATIC_IDS, Player.Backpack)
    
    if not dagger:
        print("No dagger found!")
        sys.exit()
        
    trees = scan_trees(tileRange, treeStaticIds)
    Misc.SendMessage("Total tree number {}".format(treenumber))
    
    for tree in trees:
        Misc.SendMessage("Moving to a tree")
        go_to_tile(tree.x - 1, tree.y - 1, 10.0)
        cut_tree(tree, dagger, cutDelayMs)
        Misc.Pause(500)    

    Misc.SendMessage("All done", 123) 
    
# Internal helper to move resource items from backpack to a pack animal
# Used for both mining and lumberjacking   
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
                    
# Internal helper  method to discard logs/ingots not in our list
def drop_unwanted_resources(itemStaticIds, keepItemHues, itemMoveDelayMs):    
    for itemStaticId in itemStaticIds:
        resources = find_all_in_container_by_id(itemStaticId, containerSerial = Player.Backpack.Serial)
        for resource in resources:
            if resource.Color not in keepItemHues:
                print("Dropping {} on ground".format(resource.Name))
                tileX, tileY, tileZ = get_tile_behind(2)
                Items.MoveOnGround(resource, resource.Amount, tileX, tileY, tileZ)
                Misc.Pause(itemMoveDelayMs)

################## ################## ################## ##################
#
#   Mining
#
################## ################## ################## ##################    
    
def getMinerTool():
    for minerToolStaticID in MINER_TOOLS_STATIC_IDS:
        miningTool = find_in_container_by_id(minerToolStaticID, Player.Backpack.Serial)
        if miningTool is not None:
            return miningTool    

def smelt_ore(forgeAnimalMobileId, itemMoveDelayMs):
    forgeAnimals = get_pets(range = 2, checkLineOfSight = True, mobileId = forgeAnimalMobileId)
    if len(forgeAnimals) > 0:
        for oreId in ORE_STATIC_IDS:
            ores = find_all_in_container_by_id(oreId, Player.Backpack.Serial)
            for ore in ores:
                Journal.Clear()
                Items.UseItem(ore)
                Target.WaitForTarget(5000, True)
                Target.TargetExecute(forgeAnimals[0])
                Misc.Pause(itemMoveDelayMs)
                if Journal.Search("There is not enough metal-bearing ore in this pile to make an ingot."):
                    print(ore)
                    print(ore.Serial)
                    #tileX, tileY, tileZ = get_tile_in_front()
                    tileX, tileY, tileZ = get_tile_behind(2)
                    Items.MoveOnGround(ore, 0, tileX, tileY , 0)
                    Misc.Pause(itemMoveDelayMs)
        Misc.Pause(itemMoveDelayMs)     
    else:
        print("No forge animal found")
                    
# Internal helper whether we should move        
def should_move():
    if Journal.Search('no metal') or Journal.Search('t mine that') or Journal.Search('no sand'):
        Journal.Clear()
        return True
    else:
        Journal.Clear()
        return False    
        
# Gets the tile serial. This isnt a trivial task.
# Searching by cave floor tile id. Then doing an item search.
# The cave floor tile is apparently an item with a serial. That is
# how we get the serial.
# The tile serial is provided to Target execute. We cant just use
# the x,y coords because it doesnt work. It just says you cant mine there.
# Also cant use target relative.
def get_tile_in_front_serial():
    tileX, tileY, tileZ = get_tile_in_front()
    #tileinfo = Statics.GetStaticsLandInfo(tileX, tileY, Player.Map)

    filter = Items.Filter()
    # 0x053B is Cave floor
    # 0x0018 is Sand
    filter.Graphics = List[Int32]((0x053B)) 
    filter.OnGround = True
    filter.RangeMax = 1
    items = Items.ApplyFilter(filter)
    for item in items:
        if item.Position.X == tileX and item.Position.Y == tileY:
            return item.Serial, tileX, tileY, tileZ 
    return None, tileX, tileY, tileZ 

# Mines in a straight line. Perfect for cave floors. Your character will mine
# a vein until it runs out and then step forward numTilesToMove tiles.
# You can provide a mobile ID for a pack animal and a forge animal
# so you can smelt and store smelted ore in your pack animal. Note: This is the
# mobile ID (NOT the Serial of your pack / forge animals). I have constants for these
# for commone ones like fire beetle and blue beetle.
def run_mining_loop(

    # (Optional) After a vein runs out, how many tiles forward to move.
    numTilesToMove = 1,
    
    # (Optional) Only keep ingots that match these hues. By default that is all hues. Remove the ones
    # you wish to discard. It will drop them at your feet. It is a common case where you may not care
    # about the basic iron ingots (RESOURCE_HUE_DEFAULT), so remove that from the list if you only
    # want special ingots.
    keepItemHues = [RESOURCE_HUE_DULL_COPPER, RESOURCE_HUE_SHADOW_IRON, RESOURCE_HUE_COPPER, RESOURCE_HUE_BRONZE, RESOURCE_HUE_GOLD, RESOURCE_HUE_AGAPITE, RESOURCE_HUE_VERITE, RESOURCE_HUE_VALORITE],

    # (Optional) The mobile ID of your pack animal. NOT the Serial. Defaults to blue beetle.
    packAnimalMobileId = BLUE_BEETLE_MOBILE_ID,       
    
    # (Optional) The mobile ID of your forge animal. NOT the serial. Defaults to fire beetle.
    forgeAnimalMobileId = FIRE_BEETLE_MOBILE_ID,
    
    # (Optional) Number of miliseconds between item moves typically from one pack to another.
    itemMoveDelayMs = 1000
):
                
    while True:
        drop_unwanted_resources(INGOT_STATIC_IDS + STONE_STATIC_IDS + ORE_STATIC_IDS, keepItemHues, itemMoveDelayMs) 
        smelt_ore(forgeAnimalMobileId, itemMoveDelayMs)
        move_items_to_pack_animal(INGOT_STATIC_IDS + STONE_STATIC_IDS + SAND_STATIC_IDS, packAnimalMobileId, itemMoveDelayMs)
        miningTool = getMinerTool()
        
        Journal.Clear()
        Items.UseItem(miningTool)
        Target.WaitForTarget(5000, True)
        
        tileSerial, tileX, tileY, tileZ  = get_tile_in_front_serial()
        if tileSerial is not None:
            Target.TargetExecute(tileSerial)
        else:
            Target.TargetExecute(tileX, tileY, tileZ)
        
        Misc.Pause(itemMoveDelayMs)
        
        if should_move():
            move(numTilesToMove)

        Misc.Pause(int(itemMoveDelayMs / 2))
        
################## ################## ################## ##################
#
#   Fishing
#
################## ################## ################## ##################
        
TRUE_NORTH_DIRECTION_MAP = ["Forward One", "Right One", "Back One", "Left One"]

# Global cache for the useCorpseScanner function so we dont sail to the same corpses repeatadly.
corpseScannerCache = []

# Auto fishes. Works on a boat. Works on a dock. Works if youre on a rock. 
# Take advantage of the moveTiles param to move boat after 
# each fishing attempt. It will say forward one X number of times.
# Can automatically cut fish. Can automatically store fish in hold.
# Can automatically move to nearby corpses so you can loot (this script does not
# loot though).
#
# Setup:
# 1) Read the parameters below and configure as needed.
# 2) If you want to automatically cut fish, you will need a basic dagger in your pack (or provide your own tool).
# 3) If you want to put fish directly in your hold, you will need to stand right on top of it.
# 4) You will need a fishing pole of course.
# 5) The useCorpseScanner feature will sail to nearby corpses so  you dont miss MiBs.
def run_fishing_loop(

    # (Optional) How many tiles in front of character to cast. Defaults to 4 tiles
    # in front of character.
    fishRange = 4, 
    
    # (Optional) After each cast move the boat forward this many tiles. Useful if on a boat.
    # Just tells the tiller forward one this many times. Default is 0 (stay in same spot). 
    moveTiles = 0, 
    
    # (Optional) How long to pause between casts in ms. Default is 9000ms.
    fishDelayMs = 9000,
    
    # 0 = Do nothing, leave in backpack (default)
    # 1 = cut fish with a tool of your choice to reduce weight, makes lots of fish steaks (see cutToolItemId)
    # 2 = place fish in cargo hold of ship, have to be standing near cargo hold
    fishHandling = 0,
    
    # (Optional) String name of fish you want to keep safe. Will not do any fishHandling operations on this fish. 
    # Leaves it in backpack. Useful if you are doing fish monger quests. Just type the fish name
    # you want to keep in your backpack (lower case). Default is none.
    fishToKeep = None,
    
    # (Optional) The item id (not serial) of the tool you want to use to cut fish. Default is dagger but other
    # shards may have more optimized tools with bonuses. This tool can be in your backpack OR in a container in your
    # backpack, but it wont search any more nested containers after that.
    cutToolItemId = DAGGER_STATIC_ID,
    
    # (Optional) Enable this and you will sail to nearby corpses that match those in corpseNames below. This
    # is useful if you want to look sea serpents for MiBs and such. At present there is no support for auto loot.
    # You need to enable what you want in your auto looter (tazuo or doranas lootmaster).
    # This is very crude. It just sails one tile at a time until it finds a corpse. Then, it pauses for a bit
    # while your autolooter does what it needs to do. It will do this for all nearby corpses before returning to
    # where you started and resume fishing. There are several more options below to customize this behavior.
    useCorpseScanner = False,
    
    # (Optional) Time delay in miliseconds between issuing commands to move boat. Adjust based on your servers latency.
    corpseScannerMoveCommandDelayMs = 650,
    
    # (Optional) Set the number of miliseconds to wait at a corpse once reaching it so your auto looter can do the business.
    corpseScannerPauseDelayMs = 2000,
    
    # (Optional) Array of corpse names. Only sail to loot these. Useful for message in a bottle enemies.
    corpseNames = ["a deep sea serpents corpse", "a sea serpents corpse"],
):
    global corpseScannerCache
    
    fishingPole = find_first_in_hands_by_ids(FISHING_POLE_STATIC_IDS)
    if fishingPole == None:
        fishingPole = find_first_in_container_by_ids(FISHING_POLE_STATIC_IDS)
        if fishingPole == None:
            print("Need a fishing pole")
            return False
        else:
            equip_weapon(fishingPole)
        
    while Player.Weight < Player.MaxWeight - 40:
        # Cut fish they are heavy
        if fishHandling == 1:
            cutTool = Items.FindByID(cutToolItemId, -1, Player.Backpack.Serial, 1)
            #dagger = find_first_in_container_by_ids(DAGGER_STATIC_IDS)
            if cutTool is not None:
                fishies = find_all_in_container_by_ids(FISH_STATIC_IDS)
                for fish in fishies:
                    if fishToKeep is not None and fish.Name.lower().find(fishToKeep.lower()) > -1:
                        Player.HeadMessage(28, "Keeping fish {} item id {}".format(fish.Name, fish.ItemID))
                        continue
                    print("Cutting fish {} item id {}".format(fish.Name, fish.ItemID))
                    Items.UseItem(cutTool)
                    Target.WaitForTarget(1000, False)
                    Target.TargetExecute(fish)
            else:
                print("You have elected to cut fish however no dagger was found in backpack.")
                return
        elif fishHandling == 2:
            fishies = find_all_in_container_by_ids(FISH_STATIC_IDS)
            fil = Items.Filter()
            fil.Name = "cargo hold"
            fil.RangeMax = 3
            hatches = Items.ApplyFilter(fil)
            if len(hatches) > 0:
                for fish in fishies:
                    if fishToKeep is not None and fish.Name.lower().find(fishToKeep.lower()) > -1:
                        Player.HeadMessage(28, "Keeping fish {} item id {}".format(fish.Name, fish.ItemID))
                        continue
                    print("Moving fish {} item id {}".format(fish.Name, fish.ItemID))                        
                    move_item_to_container(fish, hatches[0].Serial)
                    
        Target.Cancel()
        Items.UseItem(fishingPole)
        Target.WaitForTarget(2000, False)
        x, y, z = get_tile_in_front(fishRange)
        
        # The people who made this game made some questionable decisions.
        # If we are in britain, the water tile is the land tile.
        # If we are in tokumo, the water tile is a static tile on top of land tile.
        # So, we will look for something with the "Wet" flag and go from there.
        fished = False
        
        tileInfoList = Statics.GetStaticsTileInfo(x, y, Player.Map)
        if len(tileInfoList) > 0:
            for tileInfo in tileInfoList:
                val = Statics.GetTileFlag(tileInfo.StaticID,"Wet")
                if Statics.GetTileFlag(tileInfo.StaticID,"Wet") == True:
                    print("TargetExecute(x = {}, y = {}, staticZ = {}, staticId = {})".format(x, y, tileInfo.StaticZ, tileInfo.StaticID))
                    Target.TargetExecute(x, y, tileInfo.StaticZ, tileInfo.StaticID)
                    fished = True
                    Misc.Pause(fishDelayMs)
                    break

        if not fished:
            landInfo = Statics.GetStaticsLandInfo(x,y,Player.Map)
            if landInfo is not None:
                val = Statics.GetLandFlag(landInfo.StaticID,"Wet")
                if Statics.GetLandFlag(landInfo.StaticID,"Wet"):
                    Target.TargetExecute(x, y, landInfo.StaticZ)
                    Misc.Pause(fishDelayMs)
                    fished = True
                else:
                    print("This tile is not wet")

        if useCorpseScanner:
            items = get_corpses(range = 10)
            
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
                        print("cacheLooted size = {}".format(len(corpseScannerCache)))
                        if len(corpseScannerCache) >= 30:
                            corpseScannerCache.pop(0)
                            print("cacheLooted popping one off {}".format(len(corpseScannerCache)))
                        corpseScannerCache.append(corpse.Serial)
                    sail_to_tile(playerX, playerY, boatDirection, corpseScannerMoveCommandDelayMs)               

        for i in range(0, moveTiles):
            Player.ChatSay("forward one")
            Misc.Pause(750)

# Deploys traps. Collects traps after trapDelayMs. Loots the traps. Moves crabs to hold.
# You need lobster traps in your bag. You need to stand near the cargo hold on your ship.
def run_crab_fishing_loop(

    # Number of times to run the crab loop. Default is 1 then it stops.
    numLoops = 1,
    
    # If on a boat, tells the tiller to move forward this many times.
    moveTiles = 0, 
    
    # Number of traps to use. If you dont have this many, will use only what you have.
    maxTraps = 19,
    
    # How long to pause between casts
    trapDelayMs = 65000,
    
    # Will not do any fishHandling operations on this fish. Leaves it in backpack. Useful for fishing quests.
    fishToKeep = None
):

    for i in range(1, numLoops + 1):
        Player.HeadMessage(28, "Running crab fishing loop {} / {}".format(i, numLoops))
        traps = []
        trapItems = find_all_in_container_by_ids(LOBSTER_TRAP_STATIC_IDS)
        for trapItem in trapItems:
            if trapItem.Name == "empty lobster trap":
                traps.append(trapItem)
        actualTraps = len(traps)

        Player.HeadMessage(28, "Stand in middle of cargo hold")
        Misc.Pause(500)
        Player.HeadMessage(28, "You have {}/{} lobster traps". format(actualTraps, maxTraps))

        trapNum = 1
        for trap in traps:
            Target.Cancel()
            if trap.Name != "empty lobster trap":
                continue

            Items.UseItem(trap)
            Target.WaitForTarget(2000)
            if trapNum == 1:
                x = Player.Position.X + 6
                y = Player.Position.Y - 6
                z = Player.Position.Z
            elif trapNum == 2:
                x = Player.Position.X + 6
                y = Player.Position.Y - 4
                z = Player.Position.Z
            elif trapNum == 3:
                x = Player.Position.X + 6
                y = Player.Position.Y - 2
                z = Player.Position.Z        
            elif trapNum == 4:
                x = Player.Position.X + 6
                y = Player.Position.Y
                z = Player.Position.Z
            elif trapNum == 5:
                x = Player.Position.X + 6
                y = Player.Position.Y + 2
                z = Player.Position.Z    
            elif trapNum == 6:
                x = Player.Position.X + 6
                y = Player.Position.Y + 4
                z = Player.Position.Z        
            elif trapNum == 7:
                x = Player.Position.X + 6
                y = Player.Position.Y + 6
                z = Player.Position.Z                
            elif trapNum == 8:
                x = Player.Position.X + 4
                y = Player.Position.Y + 6
                z = Player.Position.Z   
            elif trapNum == 9:
                x = Player.Position.X + 2
                y = Player.Position.Y + 6
                z = Player.Position.Z    
            elif trapNum == 10:
                x = Player.Position.X + 0
                y = Player.Position.Y + 6
                z = Player.Position.Z    
            elif trapNum == 11:
                x = Player.Position.X - 2
                y = Player.Position.Y + 6
                z = Player.Position.Z    
            elif trapNum == 12:
                x = Player.Position.X - 4
                y = Player.Position.Y + 6
                z = Player.Position.Z    
            elif trapNum == 13:
                x = Player.Position.X - 6
                y = Player.Position.Y + 6
                z = Player.Position.Z    
            elif trapNum == 14:
                x = Player.Position.X - 6
                y = Player.Position.Y + 4
                z = Player.Position.Z          
            elif trapNum == 15:
                x = Player.Position.X - 6
                y = Player.Position.Y + 2
                z = Player.Position.Z    
            elif trapNum == 16:
                x = Player.Position.X - 6
                y = Player.Position.Y
                z = Player.Position.Z
            elif trapNum == 17:
                x = Player.Position.X - 6
                y = Player.Position.Y - 2
                z = Player.Position.Z  
            elif trapNum == 18:
                x = Player.Position.X - 6
                y = Player.Position.Y - 4
                z = Player.Position.Z   
            elif trapNum == 19:
                x = Player.Position.X - 6
                y = Player.Position.Y - 6
                z = Player.Position.Z            
            else:
                break

            Target.TargetExecute(x,y,z)
            Misc.Pause(650)
            
            trapNum = trapNum + 1
            if trapNum > maxTraps or trapNum > actualTraps:
                Player.HeadMessage(28, "all traps out")
                break

        Player.HeadMessage(28, "All traps deployed, now we wait")
        Misc.Pause(trapDelayMs)

        Player.HeadMessage(28, "Time to collect traps")
        filter = Items.Filter()
        filter.Graphics = List[Int32]((DEPLOYED_LOBSTER_TRAP_STATIC_ID)) # This filter doesnt work
        filter.Movable = 0
        filter.OnGround = True
        filter.RangeMax = 7
        items = Items.ApplyFilter(filter)

        for item in items:
            if item.ItemID == DEPLOYED_LOBSTER_TRAP_STATIC_ID:
                Items.UseItem(item)
                print("Clicking item {}".format(item.Name))
                Misc.Pause(650)

        Player.HeadMessage(28, "Time to let the crabs out of the traps")
        Misc.Pause(2000)

        trapItems = find_all_in_container_by_ids(LOBSTER_TRAP_STATIC_IDS)
        for trapItem in trapItems:
            if trapItem.Name != "empty lobster trap":
                Items.UseItem(trapItem)
                Misc.Pause(650)
                Target.Cancel()
                
        Player.HeadMessage(28, "Move crabs to hold")
        Misc.Pause(2000)

        fishies = find_all_in_container_by_ids(FISH_STATIC_IDS)
        fil = Items.Filter()
        fil.Name = "cargo hold"
        fil.RangeMax = 3
        hatches = Items.ApplyFilter(fil)
        if len(hatches) > 0:
            for fish in fishies:
                if fishToKeep is not None and fish.Name.lower().find(fishToKeep.lower()) > -1:
                    Player.HeadMessage(28, "Keeping fish {} item id {}".format(fish.Name, fish.ItemID))
                    continue
                print("Moving fish {} item id {}".format(fish.Name, fish.ItemID))                        
                move_item_to_container(fish, hatches[0].Serial)
            
        if i == numLoops:
            return
            
        for i in range(0, moveTiles):
            Player.ChatSay("forward one")
            Misc.Pause(750)    

# Internal helper
# Essentially returns an array offset for TRUE_NORTH_DIRECTION_MAP
# Depending on boat direction, shift that array so that forward always
# means forward. Otherwise youll end up in Peru.
def get_boat_direction():
    boatDirection = None
    playerX = Player.Position.X
    playerY = Player.Position.Y
    Player.ChatSay("forward one")
    Misc.Pause(1000)
    if Player.Position.X < playerX:
        boatDirection = "West"
        boatDirection = 1
    elif Player.Position.X > playerX:
        boatDirection = "East"        
        boatDirection = 3
    elif Player.Position.Y < playerY:
        boatDirection = "North"                
        boatDirection = 0
    elif Player.Position.Y > playerY:
        boatDirection = "South"  
        boatDirection = 2
    Player.ChatSay("back one")
    Misc.Pause(1000)        

    return boatDirection

# Go to this tile on the ocean. This is slow. Not meant for long trips.
# Instead, use this for precision corpse looting.
def sail_to_tile(

    # Go to this X coord
    x, 
    
    # Go to this Y coord
    y, 

    # Result of get_boat_direction. Dont call it in here because it is wasteful.
    # We would have to do it after each corpse is looted.
    boatDirection,
    
    # Optional Time to delay between issuing commands to move boat. This is slow.
    moveCmdLatencyMs = 650
):
    directionMap = TRUE_NORTH_DIRECTION_MAP[boatDirection:] + TRUE_NORTH_DIRECTION_MAP[: boatDirection]
    while True:
        #print("Player ", Player.Position.X, Player.Position.Y)
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
        