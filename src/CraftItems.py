# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-02-04
# Use at your own risk. 

from Scripts.omgarturo.src.fm_core.core_crafting import run_craft_loop

# Crafts items in a loop. Useful for crafters who are looking for
# very specific pieces of gear like armor with 3 or fewer physical resist.
# Can be used to automate any recipe found in omgarturo.fm_core.core_crafting.RECIPES.
# But I find it most useful for crafters looking for very specific armor pieces
# before reforging. Sometimes it takes a lot of crafts to get the pieces you want.
#
# This will by default loop forever. You can set the maxCraftedItems to a number if you
# want it to stop after a certain point. Read the parameters below to configure.
#
# WARNING: IF YOU SET craftContainer AS YOUR BACKPACK, YOU RISK LOSING ITEMS.
#
# Requirements:
#   - Provide the recipe name
#   - You need a container to do work in (put a bag in your backpack)
#   - You need a container of resources (ingots, etc.)
#   - You need a container of tools
#   - You may need a forge and anvil nearby
#   - You need a container for items to keep
#   - You need a container for items to discard
#   - Optionally set the max number of items to craft
#   - Set options for filters to keep only equipment you want
run_craft_loop(

    # A string for the item name you want to craft like "leather sleeves" or "Recall" (note the caps). 
    # You can find the complete list of implemented recipes in the omgarturo.fm_core.core_crafting.RECIPES
    # array. Just grab the item name from that and plug it in here. If the recipe youre looking
    # for doesnt exist, then youre boned.
    #recipeName = "leather leggings",
    recipeName = "Gate Travel",

    # Serial of container to do work in. This container must be placed in your backpack. 
    # Get its serial and fill it in here. You *could* use your backpack, but your risk losing
    # things when filtering out unwanted items.
    # The script will move all tools and materials to this container. Crafted items will appear here.
    craftContainer = 0x406766F0,
    
    # Stash a bunch of tools in here and let it rip. Serial of container.
    toolContainer = 0x4042E100,
    
    # Serial of regular container / commodity deed box (not a special resource box like insaneuo).
    # Fill this with ingots, reagents, etc. Use the run_restocker() function to help fill it up.
    resourceContainer = 0x408CC21E,
    
    # An array of serials for containers where the items you want to keep will be stored.
    # Plop a container down, secure it, grab the serial, and plug it into this array.
    # Script will attempt to move items that DO meet filters after every craft attempt.
    # This is slow and should be optimized later based on weight.
    keepContainers = [0x4086CA21],
    
    # Serial of a container to dump trash in. This is where we put all
    # crafted items that are to be discarded (perhaps not enough resists, see filters).
    # I think you can use a trash bin. Maybe place on next to you.
    # "I wish to place a trash barrel"
    # Script will attempt to move items that do not meet filters after every craft attempt.
    trashContainer = 0x401DEA04,
    
    # (Optional) A number that marks the upper limit on crafted items.
    # Default is None which means keep crafting forever.
    maxItemsToCraft = 5000,
    
    # NOTE: NOT IMPLEMENTED. ONLY WORKS WITH DEFAULT MATERIALS LIKE IRON AND LEATHER
    # (Optional) Specific a material to use like Shadow Iron or Barbed Leather.
    # Default is to use the basic materials like leather or iron. Possible values are:
    # RESOURCE_HUE_DEFAULT, RESOURCE_HUE_COPPER, RESOURCE_HUE_SHADOW_IRON, RESOURCE_HUE_DULL_COPPER, RESOURCE_HUE_BRONZE, RESOURCE_HUE_GOLD, RESOURCE_HUE_AGAPITE, RESOURCE_HUE_VERITE, RESOURCE_HUE_VALORITE, RESOURCE_HUE_BARBED, RESOURCE_HUE_SPINED, RESOURCE_HUE_HORNED, RESOURCE_HUE_OAK, RESOURCE_HUE_ASH, RESOURCE_HUE_YEW, RESOURCE_HUE_HEARTWOOD, RESOURCE_HUE_BLOODWOOD, RESOURCE_HUE_FROSTWOOD 
    specialMaterialHue = None,
    
    # (Optional) Time to wait between item moves. Adjust with caution. Reducing this will increase speed
    # of the script, but you risk disconnects and other issues maintaining state. Defaults to 1000ms
    itemMoveDelayMs = 750,
    
    # (Optional) Reducing this will increase speed of script, but Id advise against it. Gump interactions are 
    # catastrophic. God save the queen.
    gumpDelayMs = 750,
    
    # Use these filters to only keep very specific items. This is the main
    # point of this script. Will keep things that match these filters. If not set,
    # will default to None which means that filter isnt considered. Values expected are 
    # numeric unless documented otherwise. Default is None which means ignore the fitler.
    # Set all of these to None if you just want 500 Recall scrolls.
    minPhysicalResist = None,
    maxPhysicalResist = None,
    minFireResist = None,
    maxFireResist = None,
    minColdResist = None,
    maxColdResist = None,
    minPoisonResist = None,
    maxPoisonResist = None,
    minEnergyResist = None,
    maxEnergyResist = None
)