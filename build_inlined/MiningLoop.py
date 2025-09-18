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
# ---- smelt_ore (from core_gathering.py)
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

# ---- getMinerTool (from core_gathering.py)
def getMinerTool():
    for minerToolStaticID in MINER_TOOLS_STATIC_IDS:
        miningTool = find_in_container_by_id(minerToolStaticID, Player.Backpack.Serial)
        if miningTool is not None:
            return miningTool

# ---- should_move (from core_gathering.py)
def should_move():
    if Journal.Search('no metal') or Journal.Search('t mine that') or Journal.Search('no sand'):
        Journal.Clear()
        return True
    else:
        Journal.Clear()
        return False

# ---- get_tile_in_front_serial (from core_gathering.py)
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

# ---- run_mining_loop (from core_gathering.py)
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

# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-02-12
# Use at your own risk. 


# Mines in a straight line. Perfect for cave floors. Your character will mine
# a vein until it runs out and then step forward numTilesToMove tiles.
# You can provide a mobile ID for a pack animal and a forge animal
# so you can smelt and store smelted ore in your pack animal. Note: This is the
# mobile ID (NOT the Serial of your pack / forge animals). I have constants for these
# for commone ones like fire beetle and blue beetle.
run_mining_loop(

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
)