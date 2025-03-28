# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-02-04
# Use at your own risk. 

from Scripts.omgarturo.fm_core.core_crafting import *

# WARNING: THIS IS IN DEVELOPMENT AND DOESNT WORK YET

# Crafts an item in a loop. Useful for crafters who are looking for
# very specific pieces of gear like armor with 2 or fewer physical resist.
# Can be used to automate any recipe found in omgarturo.fm_core.core_crafting.RECIPES.
#
# WARNING: IF  YOU SET craftContainer AS YOUR BACKPACK IT YOU RISK LOSING ITEMS.
#
# Requirements:
#   - You need a container to do work in (put a bag in your backpack)
#   - You need a container of resources (ingots, etc.)
#   - You need a container of tools
#   - You may need a forge and anvil nearby
#   - You need a container for items to keep
#   - You need a container for items to discard
#
def run_craft_loop(

    # A string for the item name you want to craft like "leather sleeves". You can
    # find the complete list of implemented recipes in the omgarturo.fm_core.core_crafting.RECIPES
    # array. Just grab the item name from that and plug it in here. If the recipe youre looking
    # for doesnt exist, then youre boned.
    recipeName = "leather leggings",

    # Serial of container to do work in. This container must be placed in your backpack. 
    # Get its serial and fill it in here. You *could* use your backpack, but your risk losing
    # things when combining items into large bods (your spellbook for example when crafting spellbooks). 
    # The script will move all tools, bods, and materials to this container. Crafted items will appear here.
    craftContainer = 0x406766F0,
    
    # Stash a bunch of tools in here and let it rip. Serial of container.
    toolContainer = 0x4042E100,
    
    # Serial of regular container / commodity deed box (not a special resource box like insaneuo).
    # Fill this with ingots, reagents, etc. Use the run_restocker() function to help fill it up.
    resourceContainer = 0x408CC21E,
    
    # An array of serials for containers where the items you want to keep will be stored.
    # Plop a container down, secure it, grab the serial, and plug it into this array.
    keepContainers = [0x406FD576],
    
    # (Optional) Serial of a container to dump trash in. This is where we put all
    # crafted items that are to be discarded (perhaps not enough resists, see filters) that cant be salvaged. 
    # I think you can use a trash bin. Maybe place on next to you.
    # "I wish to place a trash barrel"
    trashContainer = 0x406766F3,
    
    # (Optional) Specific a material to use like Shadow Iron or Barbed Leather.
    # Default is to use the basic materials like leather or iron. Possible values are:
    # RESOURCE_HUE_DEFAULT, RESOURCE_HUE_COPPER, RESOURCE_HUE_SHADOW_IRON, RESOURCE_HUE_DULL_COPPER, RESOURCE_HUE_BRONZE, RESOURCE_HUE_GOLD, RESOURCE_HUE_AGAPITE, RESOURCE_HUE_VERITE, RESOURCE_HUE_VALORITE, RESOURCE_HUE_BARBED, RESOURCE_HUE_SPINED, RESOURCE_HUE_HORNED, RESOURCE_HUE_OAK, RESOURCE_HUE_ASH, RESOURCE_HUE_YEW, RESOURCE_HUE_HEARTWOOD, RESOURCE_HUE_BLOODWOOD, RESOURCE_HUE_FROSTWOOD 
    # NOTE: NOT IMPLEMENTED. ONLY WORKS WITH DEFAULT MATERIALS LIKE IRON AND LEATHER
    specialMaterialHue = None,
    
    # (Optional)Time to wait between item moves. Adjust with caution. Reducing this will increase speed
    # of the script, but you risk disconnects and other issues maintaining state. Defaults to 1000ms
    itemMoveDelayMs = 750,
    
    # (Optional) Reducing this will increase speed of script, but Id advise against it. Gump interactions are 
    # catastrophic. God save the queen.
    gumpDelayMs = 750,
    
    # Use these filters to only keep very specific items.Items. This is the main
    # point of this script. Will keep things that match these filters. If not set,
    # will default to None which means that filter isnt considered.
    minPhysicalResist = None,
    maxPhysicalResist = 3,
    
    minFireResist = 11,
    maxFireResist = None,
    
    minColdResist = 11,
    maxColdResist = None,
    
    minPoisonResist = None,
    maxPoisonResist = None,
    
    minEnergyResist = 6,
    maxEnergyResist = None
):
    print("Opening containers, this may take a moment...")
    # Open containers because we may not have that item data yet. Sorry for the spam,
    # but these containers will show 0 items unless theyre loaded.
    for keepContainer in keepContainers:
        Items.UseItem(keepContainer)
        Misc.Pause(itemMoveDelayMs)
    Items.UseItem(toolContainer)
    Misc.Pause(itemMoveDelayMs)
    Items.UseItem(resourceContainer)
    Misc.Pause(itemMoveDelayMs)    
    Items.UseItem(craftContainer)
    Misc.Pause(itemMoveDelayMs)

    recipe = element = next((r for r in RECIPES if r.recipeName == recipeName), None)
    print(f"Found Recipe {recipe}")
    craftGumpSet = False
    while True:
        tool = get_tool(craftContainer, recipe.toolId, toolContainer, itemMoveDelayMs)
        if tool is None:
            print("Error: Cannot find tool")
            sys.exit()

        if not check_resources(craftContainer, recipe.resources, resourceContainer, itemMoveDelayMs, specialMaterialHue):            
            print("Error: Out of resources")
            sys.exit()
            
        Items.UseItem(tool)
        Gumps.WaitForGump(CRAFTING_GUMP_ID, 5000)
        Misc.Pause(int(gumpDelayMs / 2)) #always gump delay (250)
        if not Gumps.HasGump(CRAFTING_GUMP_ID):
            Misc.Pause(gumpDelayMs * 2)
            continue            
        
        if not craftGumpSet:
            # WARNING: Special materials not implemented
            #if smallBod.specialMaterialButton > 0:
            #    # The menu button to select material
            #    Gumps.SendAction(CRAFTING_GUMP_ID, 7)
            #    Gumps.WaitForGump(CRAFTING_GUMP_ID, 5000)
            #    Misc.Pause(gumpDelayMs)#1000 before
            #    if not Gumps.HasGump(CRAFTING_GUMP_ID):
            #        continue                    
                # The actual special material button
            #    Gumps.SendAction(CRAFTING_GUMP_ID, smallBod.specialMaterialButton)
            #    Gumps.WaitForGump(CRAFTING_GUMP_ID, 5000)
            #    Misc.Pause(gumpDelayMs)#1000 before
            #    if not Gumps.HasGump(CRAFTING_GUMP_ID):
            #        continue 
                  
            # Sets category
            Gumps.SendAction(CRAFTING_GUMP_ID, recipe.gumpCategory)
            Gumps.WaitForGump(CRAFTING_GUMP_ID, 10000)
            Misc.Pause(gumpDelayMs)
            if not Gumps.HasGump(CRAFTING_GUMP_ID):
                continue                                        
                
            craftGumpSet = True 
 
        Gumps.SendAction(CRAFTING_GUMP_ID, recipe.gumpSelection)                    
        Gumps.WaitForGump(CRAFTING_GUMP_ID, 10000)
        Misc.Pause(gumpDelayMs) #1000 before           
            
        for item in Items.FindBySerial(craftContainer).Contains:
            if recipeName.lower() in item.Name.lower():
                for prop in item.Properties:
                    print(prop, prop.ToString().lower(), prop.Args, prop.Number)
                    
                keepItem = True
                if minPhysicalResist is not None and Items.GetPropValue(item, "physical resist") < minPhysicalResist:
                    keepItem = False
                if maxPhysicalResist is not None and Items.GetPropValue(item, "physical resist") > maxPhysicalResist:
                    keepItem = False 
 
                if minFireResist is not None and Items.GetPropValue(item, "fire resist") < minFireResist:
                    keepItem = False
                if maxFireResist is not None and Items.GetPropValue(item, "fire resist") > maxFireResist:
                    keepItem = False
                    
                if minColdResist is not None and Items.GetPropValue(item, "cold resist") < minColdResist:
                    keepItem = False
                if maxColdResist is not None and Items.GetPropValue(item, "cold resist") > maxColdResist:
                    keepItem = False                    
                    
                if minPoisonResist is not None and Items.GetPropValue(item, "poison resist") < minPoisonResist:
                    keepItem = False
                if maxPoisonResist is not None and Items.GetPropValue(item, "poison resist") > maxPoisonResist:
                    keepItem = False                                        
                    
                if minEnergyResist is not None and Items.GetPropValue(item, "energy resist") < minEnergyResist:
                    keepItem = False
                if maxEnergyResist is not None and Items.GetPropValue(item, "energy resist") > maxEnergyResist:
                    keepItem = False  

                if keepItem:
                    print("Keeping item")
                    for keepContainer in keepContainers:
                        container = Items.FindBySerial(keepContainer)
                        if container.Contains.Count < 125:
                            Items.Move(item, keepContainer, 1)
                            Misc.Pause(itemMoveDelayMs)                
                            
                else:
                    print("Trashing item")
                    Items.Move(item, trashContainer, 1)
                    Misc.Pause(itemMoveDelayMs)       

        Misc.Pause(50)
        
run_craft_loop()