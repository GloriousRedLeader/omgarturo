# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-02-04
# Use at your own risk. 

import sys
from Scripts.omgarturo.src.fm_core.core_items import AXE_STATIC_IDS
from Scripts.omgarturo.src.fm_core.core_items import LOG_STATIC_IDS
from Scripts.omgarturo.src.fm_core.core_items import TREE_STATIC_IDS
from Scripts.omgarturo.src.fm_core.core_items import DAGGER_STATIC_IDS
from Scripts.omgarturo.src.fm_core.core_items import BOARD_STATIC_IDS
from Scripts.omgarturo.src.fm_core.core_items import MINER_TOOLS_STATIC_IDS
from Scripts.omgarturo.src.fm_core.core_items import ORE_STATIC_IDS
from Scripts.omgarturo.src.fm_core.core_items import INGOT_STATIC_IDS
from Scripts.omgarturo.src.fm_core.core_items import STONE_STATIC_IDS
from Scripts.omgarturo.src.fm_core.core_items import REAGENT_STATIC_IDS
from Scripts.omgarturo.src.fm_core.core_items import ALCHEMY_TOOL_STATIC_IDS
from Scripts.omgarturo.src.fm_core.core_items import INGOT_STATIC_ID 
from Scripts.omgarturo.src.fm_core.core_items import BOARD_STATIC_ID 
from Scripts.omgarturo.src.fm_core.core_items import CLOTH_STATIC_ID 
from Scripts.omgarturo.src.fm_core.core_items import LEATHER_STATIC_ID 
from Scripts.omgarturo.src.fm_core.core_items import EMPTY_BOTTLE_STATIC_ID
from Scripts.omgarturo.src.fm_core.core_items import BONE
from Scripts.omgarturo.src.fm_core.core_items import UNMARKED_RUNE
from Scripts.omgarturo.src.fm_core.core_items import GATE_SCROLL
from Scripts.omgarturo.src.fm_core.core_items import RECALL_SCROLL
from Scripts.omgarturo.src.fm_core.core_items import BLANK_SCROLL
from Scripts.omgarturo.src.fm_core.core_items import PARASITIC_PLANT
from Scripts.omgarturo.src.fm_core.core_items import LUMINESCENT_FUNGI
from Scripts.omgarturo.src.fm_core.core_items import WHITE_PEARL
from Scripts.omgarturo.src.fm_core.core_items import FIRE_RUBY
from Scripts.omgarturo.src.fm_core.core_items import PERFECT_EMERALD
from Scripts.omgarturo.src.fm_core.core_items import TURQUOISE
from Scripts.omgarturo.src.fm_core.core_items import STAR_SAPPHIRE
from Scripts.omgarturo.src.fm_core.core_items import CITRINE 
from Scripts.omgarturo.src.fm_core.core_items import DIAMOND
from Scripts.omgarturo.src.fm_core.core_items import AMBER
from Scripts.omgarturo.src.fm_core.core_items import AMETHYST
from Scripts.omgarturo.src.fm_core.core_items import SAPPHIRE
from Scripts.omgarturo.src.fm_core.core_items import RUBY
from Scripts.omgarturo.src.fm_core.core_items import EMERALD
from Scripts.omgarturo.src.fm_core.core_items import TOURMALINE
from Scripts.omgarturo.src.fm_core.core_items import MANDRAKEROOT
from Scripts.omgarturo.src.fm_core.core_items import BLOODMOSS
from Scripts.omgarturo.src.fm_core.core_items import SULPHUROUSASH
from Scripts.omgarturo.src.fm_core.core_items import NIGHTSHADE
from Scripts.omgarturo.src.fm_core.core_items import BLACKPEARL
from Scripts.omgarturo.src.fm_core.core_items import SPIDERSILK
from Scripts.omgarturo.src.fm_core.core_items import GINSENG
from Scripts.omgarturo.src.fm_core.core_items import GARLIC
from Scripts.omgarturo.src.fm_core.core_items import PIGIRON
from Scripts.omgarturo.src.fm_core.core_items import BATWING
from Scripts.omgarturo.src.fm_core.core_items import NOXCRYSTAL
from Scripts.omgarturo.src.fm_core.core_items import DAEMONBLOOD
from Scripts.omgarturo.src.fm_core.core_items import GRAVEDUST
from Scripts.omgarturo.src.fm_core.core_items import RESOURCE_HUE_DEFAULT
from Scripts.omgarturo.src.fm_core.core_items import RESOURCE_HUE_DULL_COPPER
from Scripts.omgarturo.src.fm_core.core_items import RESOURCE_HUE_SHADOW_IRON
from Scripts.omgarturo.src.fm_core.core_items import RESOURCE_HUE_COPPER
from Scripts.omgarturo.src.fm_core.core_items import RESOURCE_HUE_BRONZE
from Scripts.omgarturo.src.fm_core.core_items import RESOURCE_HUE_GOLD
from Scripts.omgarturo.src.fm_core.core_items import RESOURCE_HUE_AGAPITE
from Scripts.omgarturo.src.fm_core.core_items import RESOURCE_HUE_VERITE
from Scripts.omgarturo.src.fm_core.core_items import RESOURCE_HUE_VALORITE
from Scripts.omgarturo.src.fm_core.core_items import RESOURCE_HUE_BARBED
from Scripts.omgarturo.src.fm_core.core_items import RESOURCE_HUE_SPINED
from Scripts.omgarturo.src.fm_core.core_items import RESOURCE_HUE_HORNED
from Scripts.omgarturo.src.fm_core.core_items import RESOURCE_HUE_OAK
from Scripts.omgarturo.src.fm_core.core_items import RESOURCE_HUE_ASH
from Scripts.omgarturo.src.fm_core.core_items import RESOURCE_HUE_YEW
from Scripts.omgarturo.src.fm_core.core_items import RESOURCE_HUE_HEARTWOOD
from Scripts.omgarturo.src.fm_core.core_items import RESOURCE_HUE_BLOODWOOD
from Scripts.omgarturo.src.fm_core.core_items import RESOURCE_HUE_FROSTWOOD
from Scripts.omgarturo.src.fm_core.core_items import BLACKSMITHY_TOOL_STATIC_ID
from Scripts.omgarturo.src.fm_core.core_items import TINKERING_TOOL_STATIC_ID
from Scripts.omgarturo.src.fm_core.core_items import ALCHEMY_TOOL_STATIC_ID
from Scripts.omgarturo.src.fm_core.core_items import TAILORING_TOOL_STATIC_ID
from Scripts.omgarturo.src.fm_core.core_items import CARPENTRY_TOOL_STATIC_ID
from Scripts.omgarturo.src.fm_core.core_items import INSCRIPTION_TOOL_STATIC_ID
from Scripts.omgarturo.src.fm_core.core_items import BOD_STATIC_ID
from Scripts.omgarturo.src.fm_core.core_items import BOD_BOOK_STATIC_ID
from Scripts.omgarturo.src.fm_core.core_items import HUE_BLACKSMITHY
from Scripts.omgarturo.src.fm_core.core_items import HUE_TAILORING
from Scripts.omgarturo.src.fm_core.core_items import HUE_CARPENTRY
from Scripts.omgarturo.src.fm_core.core_items import HUE_ALCHEMY
from Scripts.omgarturo.src.fm_core.core_items import HUE_INSCRIPTION
from Scripts.omgarturo.src.fm_core.core_items import HUE_TINKERING

################## ################## ################## ##################
#
#   Restocker (InsaneUO specific)
#
################## ################## ################## ##################

# Restockable item that lives inside of a specialized resource container.
# Arguments are as follows:
# itemId: Refer to constants, but represents things like item ids for ingots, boards, etc.
# itemHue: Some items have the same id but use different hues (leather, ingots, boards)
# resourceBoxSerial: Inspect your resource box with razor, get the serial, plug it in
# resourceBoxButton: This is the button id of the gump. You can use gump inspector. Starts at 100 and increments up.
# amount: The number of items you want in your commodityDeedBox.
# resourceBoxPage: (Optional) The gump has multiple pages. Starts at 1 (default screen). Most items are on page 1.
class RestockItem:
    def __init__(self, itemId, itemHue, resourceBoxSerial, resourceBoxButton, amount = 10000, resourceBoxPage = 1):
        self.itemId = itemId
        self.itemHue = itemHue
        self.resourceBoxSerial = resourceBoxSerial
        self.resourceBoxButton = resourceBoxButton
        self.amount = amount
        self.resourceBoxPage = resourceBoxPage
        
    def __str__(self):
        return "RestockItem(itemId='{}', itemHue={}, amount='{}', resourceBoxSerial='{}', resourceBoxButton='{}', resourceBoxPage='{}')".format(self.itemId, self.itemHue, self.amount, self.resourceBoxSerial, self.resourceBoxButton, self.resourceBoxPage)        

# User would define something like this and pass it as an arg to the run_restocker() function.
#resources = [
#    RestockItem(BLACKPEARL, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 100, 10000),
#    RestockItem(BLOODMOSS, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 101, 10000),
#    RestockItem(GARLIC, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 102, 10000),
#    RestockItem(GINSENG, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 103, 10000),
#    RestockItem(MANDRAKEROOT, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 104, 10000),
#    RestockItem(NIGHTSHADE, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 105, 10000),
#    RestockItem(SULPHUROUSASH, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 106, 10000),
#    RestockItem(SPIDERSILK, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 107, 10000),
#    RestockItem(BATWING, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 108, 10000),
#    RestockItem(GRAVEDUST, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 109, 10000),
#    RestockItem(DAEMONBLOOD, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 110, 10000),
#    RestockItem(NOXCRYSTAL, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 111, 10000),
#    RestockItem(PIGIRON, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 112, 10000),
#    RestockItem(BOARD_STATIC_ID, RESOURCE_HUE_DEFAULT, logsAndBoardsResourceBoxSerial, 107, 10000),
#    RestockItem(BOARD_STATIC_ID, RESOURCE_HUE_OAK, logsAndBoardsResourceBoxSerial, 108, 10000),
#    RestockItem(BOARD_STATIC_ID, RESOURCE_HUE_ASH, logsAndBoardsResourceBoxSerial, 109, 10000),
#    RestockItem(BOARD_STATIC_ID, RESOURCE_HUE_YEW, logsAndBoardsResourceBoxSerial, 110, 10000),
#    RestockItem(BOARD_STATIC_ID, RESOURCE_HUE_HEARTWOOD, logsAndBoardsResourceBoxSerial, 111, 10000),
#    RestockItem(BOARD_STATIC_ID, RESOURCE_HUE_BLOODWOOD, logsAndBoardsResourceBoxSerial, 112, 10000),
#    RestockItem(BOARD_STATIC_ID, RESOURCE_HUE_FROSTWOOD, logsAndBoardsResourceBoxSerial, 113, 10000),
#    RestockItem(INGOT_STATIC_ID, RESOURCE_HUE_DEFAULT, minerResourceBoxSerial, 101, 10000),
#    RestockItem(INGOT_STATIC_ID, RESOURCE_HUE_DULL_COPPER, minerResourceBoxSerial, 101, 10000),
#    RestockItem(INGOT_STATIC_ID, RESOURCE_HUE_SHADOW_IRON, minerResourceBoxSerial, 102, 10000),
#    RestockItem(INGOT_STATIC_ID, RESOURCE_HUE_COPPER, minerResourceBoxSerial, 103, 10000),
#    RestockItem(INGOT_STATIC_ID, RESOURCE_HUE_BRONZE, minerResourceBoxSerial, 104, 10000),
#    RestockItem(INGOT_STATIC_ID, RESOURCE_HUE_GOLD, minerResourceBoxSerial, 105, 10000),
#    RestockItem(INGOT_STATIC_ID, RESOURCE_HUE_AGAPITE, minerResourceBoxSerial, 106, 10000),
#    RestockItem(INGOT_STATIC_ID, RESOURCE_HUE_VERITE, minerResourceBoxSerial, 107, 10000),
#    RestockItem(INGOT_STATIC_ID, RESOURCE_HUE_VALORITE, minerResourceBoxSerial, 108, 10000),
#    RestockItem(CLOTH_STATIC_ID, RESOURCE_HUE_DEFAULT, tailorResourceBoxSerial, 111, 10000),
#    RestockItem(LEATHER_STATIC_ID, RESOURCE_HUE_DEFAULT, tailorResourceBoxSerial, 100, 10000),
#    RestockItem(LEATHER_STATIC_ID, RESOURCE_HUE_SPINED, tailorResourceBoxSerial, 101, 10000),
#    RestockItem(LEATHER_STATIC_ID, RESOURCE_HUE_HORNED, tailorResourceBoxSerial, 102, 10000),
#    RestockItem(LEATHER_STATIC_ID, RESOURCE_HUE_BARBED, tailorResourceBoxSerial, 103, 10000),
#    RestockItem(CITRINE, RESOURCE_HUE_DEFAULT, mondainLegacyResourceBoxSerial, 100, 1000),
#    RestockItem(EMERALD, RESOURCE_HUE_DEFAULT, mondainLegacyResourceBoxSerial, 102, 1000),
#    RestockItem(TOURMALINE, RESOURCE_HUE_DEFAULT, mondainLegacyResourceBoxSerial, 104, 1000),
#    RestockItem(DIAMOND, RESOURCE_HUE_DEFAULT, mondainLegacyResourceBoxSerial, 106, 1000),
#    RestockItem(SAPPHIRE, RESOURCE_HUE_DEFAULT, mondainLegacyResourceBoxSerial, 108, 1000),
#    RestockItem(STAR_SAPPHIRE, RESOURCE_HUE_DEFAULT, mondainLegacyResourceBoxSerial, 109, 1000),
#    RestockItem(RUBY, RESOURCE_HUE_DEFAULT, mondainLegacyResourceBoxSerial, 111, 1000),
#    RestockItem(AMBER, RESOURCE_HUE_DEFAULT, mondainLegacyResourceBoxSerial, 113, 1000),
#    RestockItem(AMETHYST, RESOURCE_HUE_DEFAULT, mondainLegacyResourceBoxSerial, 115, 1000),
#    RestockItem(WHITE_PEARL, RESOURCE_HUE_DEFAULT, mondainLegacyResourceBoxSerial, 117, 100, 2),
#]

# Helper that returns sum of all the stacks in a container, ideally there would just be one stack.
def get_amount_in_container(resource, containerSerial):
    amount = 0
    items = Items.FindAllByID(resource.itemId, resource.itemHue, containerSerial, 0)
    for item in items:
        amount = amount + item.Amount
    return amount
    
# Stand near resource boxes and load everything from a resource box into a real container.
# This is useful for use in conjunction with the BODBuilder.
# InsaneUO specific.
def run_restocker(

    # Green commodity deed box. Can be any container that can hold weight though.
    commodityBoxSerial,
    
    # An array of RestockItem, the resources you want to stock. This is how you configure it.
    # Include only those resources you wish to stock, the hue, the amount, the  gump button id, and page.
    # Page is the page on the gump menu.
    resources,
    
    # (Optional) Time to wait between item moves. Adjust with caution. Reducing this will increase speed
    # of the script, but you risk disconnects and other issues maintaining state. Default is 1 second.
    itemMoveDelayMs = 1000,    
    
    # (Optional) Timeout between  gump button presses. Configure based on server latency.
    gumpDelayMs = 500
):
    RESOURCE_BOX_GUMP_ID = 0x23d0f169
    
    Items.UseItem(commodityBoxSerial)
    Misc.Pause(itemMoveDelayMs)
    
    for resource in resources:
        print(resource)
        
        if Gumps.HasGump(RESOURCE_BOX_GUMP_ID):
            Gumps.CloseGump(RESOURCE_BOX_GUMP_ID)
                
        amountInBox = get_amount_in_container(resource, commodityBoxSerial)
        if amountInBox >= resource.amount:
            continue
        
        Items.UseItem(resource.resourceBoxSerial)
        Gumps.WaitForGump(RESOURCE_BOX_GUMP_ID, 3000)
        Misc.Pause(gumpDelayMs)
        
        for page in range(1, resource.resourceBoxPage):
            Gumps.SendAction(RESOURCE_BOX_GUMP_ID, 2)
            Gumps.WaitForGump(RESOURCE_BOX_GUMP_ID, 3000)
            Misc.Pause(gumpDelayMs * 4)
            
        while True:
            amountInBox = get_amount_in_container(resource, commodityBoxSerial)
            if amountInBox >= resource.amount:
                break
            
            Gumps.SendAction(RESOURCE_BOX_GUMP_ID, resource.resourceBoxButton)
            Gumps.WaitForGump(RESOURCE_BOX_GUMP_ID, 3000)
            Misc.Pause(gumpDelayMs)

            runAgain = True if Items.FindByID(resource.itemId, resource.itemHue, Player.Backpack.Serial, 0) is not None else False
            for r in resources:
                items = Items.FindAllByID(r.itemId, r.itemHue, Player.Backpack.Serial, 0)
                for item in items:
                    Items.Move(item, commodityBoxSerial, item.Amount)
                    Misc.Pause(itemMoveDelayMs)

            if not runAgain:
                break

################## ################## ################## ##################
#
#   run_bod_builder
#
################## ################## ################## ##################

# Crafting gump category button ids. Should be the same for all modern UO
# (hopefully) otherwise client may have a heart attack. I dunno.
CAT_BLACKSMITHY_METAL_ARMOR = 1
CAT_BLACKSMITHY_HELMETS = 8
CAT_BLACKSMITHY_SHIELDS = 15
CAT_BLACKSMITHY_BLADED = 22
CAT_BLACKSMITHY_AXES = 29
CAT_BLACKSMITHY_POLEARMS = 36
CAT_BLACKSMITHY_BASHING = 43
CAT_BLACKSMITHY_CANNONS = 50
CAT_BLACKSMITHY_THROWING = 57

CAT_TAILORING_MATERIALS = 1
CAT_TAILORING_HATS = 8
CAT_TAILORING_SHIRTS_AND_PANTS = 15
CAT_TAILORING_MISCELLANEOUS = 22
CAT_TAILORING_FOOTWEAR = 29
CAT_TAILORING_LEATHER_ARMOR = 36
CAT_TAILORING_CLOTH_ARMOR = 43
CAT_TAILORING_STUDDED_ARMOR = 50
CAT_TAILORING_FEMALE_ARMOR = 57
CAT_TAILORING_BONE_ARMOR = 64

CAT_CARPENTRY_OTHER = 1
CAT_CARPENTRY_FURNITURE = 8
CAT_CARPENTRY_CONTAINERS = 15
CAT_CARPENTRY_WEAPONS = 22
CAT_CARPENTRY_ARMOR = 29
CAT_CARPENTRY_INSTRUMENTS = 36
CAT_CARPENTRY_MISC_ADDONS = 43
CAT_CARPENTRY_TAILORING_AND_COOKING = 50
CAT_CARPENTRY_ANVILS_AND_FORGES = 57
CAT_CARPENTRY_TRAINING = 64

CAT_ALCHEMY_HEALING_AND_CURATIVE = 1
CAT_ALCHEMY_ENHANCEMENT = 8
CAT_ALCHEMY_TOXIC = 15
CAT_ALCHEMY_EXPLOSIVE = 22
CAT_ALCHEMY_STRANGE_BREW = 29
CAT_ALCHEMY_INGREDIENTS = 36

CAT_INSCRIPTION_FIRST_SECOND = 1
CAT_INSCRIPTION_THIRD_FOURTH = 8
CAT_INSCRIPTION_FIFTH_SIXTH = 15
CAT_INSCRIPTION_SEVENTH_EIGTH = 22
CAT_INSCRIPTION_NECRO = 29
CAT_INSCRIPTION_OTHER = 36
CAT_INSCRIPTION_MYSTICISM = 43

CAT_TINKERING_JEWELRY = 1
CAT_TINKERING_WOODEN_ITEMS = 8
CAT_TINKERING_TOOLS = 15
CAT_TINKERING_PARTS = 22
CAT_TINKERING_UTENSILS = 29
CAT_TINKERING_MISCELLANEOUS = 36
CAT_TINKERING_ASSEMBLIES = 43
CAT_TINKERING_TRAPS = 50
CAT_TINKERING_MAGIC_JEWELRY = 57

# Internal data structure for storing ingredients for a recipe.
class SmallBodResource:
    def __init__(self, resourceId, amount = 35):
        self.resourceId = resourceId
        self.amount = amount
        
    def canOverrideHue(self):
        return self.resourceId in [INGOT_STATIC_ID, BOARD_STATIC_ID, LEATHER_STATIC_ID ]
        
    # So we can pull extra from the resourceContainer in one pass instead of on each
    # craft attempt. This is an optimization.
    def getOptimizedAmout(self):
        # Heavy stuff and you need a lot typically, 1 stone each
        if self.resourceId in [BOARD_STATIC_ID, LEATHER_STATIC_ID, BONE]:
            return self.amount * 5
            
        # Heavy stuff but you only need 1 or 2 mostly, 1 stone each
        if self.resourceId in [EMPTY_BOTTLE_STATIC_ID, CLOTH_STATIC_ID, INGOT_STATIC_ID, UNMARKED_RUNE, GATE_SCROLL, RECALL_SCROLL, BLANK_SCROLL, PARASITIC_PLANT, LUMINESCENT_FUNGI, WHITE_PEARL, FIRE_RUBY, PERFECT_EMERALD, TURQUOISE]:
            return self.amount * 25            
            
        # Light things like reagents < 1 stone
        if self.resourceId in [MANDRAKEROOT, BLOODMOSS, SULPHUROUSASH, NIGHTSHADE, BLACKPEARL, SPIDERSILK, GINSENG, GARLIC, PIGIRON, BATWING, NOXCRYSTAL, DAEMONBLOOD, GRAVEDUST]:
            return self.amount * 50

        # Light things like gems  
        if self.resourceId in [STAR_SAPPHIRE, CITRINE, TURQUOISE, DIAMOND, AMBER, AMETHYST, SAPPHIRE, RUBY, EMERALD, TOURMALINE]:
            return self.amount * 50      
            
        return self.amount
        
    def __str__(self):
        return "SmallBodResource(resourceId='{}', amount={}, canOverrideHue='{}')".format(self.resourceId, self.amount, self.canOverrideHue())        

# Recipe template. Pass an array of these to the run_bod_builder function.
# hasLargeBod: (NOT IMPLEMENTED) This small bod can be part of a large bod (several cannot)
# recipeName: Name of crafted item as it appears in the small bod (very bottom last line), e.g. mace
# gumpCategory: Represents a gump category button id. Use one of the constants above.
# gumpSelection: The create now button specific to an item. Goes in increments of 7.
# toolId: The tool item id you want to craft with to open the gump. See constants like BLACKSMITHY_TOOL_STATIC_ID
# resources: Array of SmallBodResource
class SmallBodRecipe:
    def __init__(self, hasLargeBod, recipeName, gumpCategory, gumpSelection, toolId, resources):
        self.hasLargeBod = hasLargeBod
        self.recipeName = recipeName
        self.gumpCategory = gumpCategory
        self.gumpSelection = gumpSelection
        self.toolId = toolId
        self.resources = resources
        
    def canSalvage(self):
        if self.toolId in [BLACKSMITHY_TOOL_STATIC_ID]:
            return True
        if self.toolId == TAILORING_TOOL_STATIC_ID and not any(resource.resourceId == BONE for resource in self.resources):
            return True
        return False
    def __str__(self):
        return "SmallBodRecipe(hasLargeBod={},recipeName='{}', gumpCategory='{}', gumpSelection='{}', toolId='{}', resources='{}')".format(self.hasLargeBod, self.recipeName, self.gumpCategory, self.gumpSelection, self.toolId, self.resources)        
        
# Internal data structure used in our main method. Represents a bod and its recipe. 
class SmallBod:
    
    #prefixes = {
    #        RESOURCE_HUE_DULL_COPPER: "dull copper",
    #        RESOURCE_HUE_SHADOW_IRON: "shadow iron",
    #        RESOURCE_HUE_COPPER: "copper",
    #        RESOURCE_HUE_BRONZE: "bronze",
    #        RESOURCE_HUE_GOLD: "golden",
    #        RESOURCE_HUE_AGAPITE: "agapite",
    #        RESOURCE_HUE_VERITE: "verite",
    #        RESOURCE_HUE_VALORITE: "valorite",
    #        RESOURCE_HUE_SPINED: "spined",
    #        RESOURCE_HUE_HORNED: "horned",
    #        RESOURCE_HUE_BARBED: "barbed",
    #        RESOURCE_HUE_OAK: "oak",
    #        RESOURCE_HUE_ASH: "ash",
    #        RESOURCE_HUE_YEW: "yew",
    #        RESOURCE_HUE_HEARTWOOD: "heartwood",
    #        RESOURCE_HUE_BLOODWOOD: "bloodwood",
    #        RESOURCE_HUE_FROSTWOOD: "frostwood"
    #}    
    
    def __init__(self, bodSerial, amountMade, isExceptional, amountToMake, specialMaterialButton, specialMaterialHue, specialMaterialPropId, specialMaterialName, recipe):
        #self.craftedItemName = craftedItemName
        self.amountMade = amountMade
        self.isExceptional = isExceptional
        self.amountToMake = amountToMake
        self.specialMaterialButton = specialMaterialButton
        self.specialMaterialHue = specialMaterialHue
        self.specialMaterialPropId = specialMaterialPropId
        self.specialMaterialName = specialMaterialName
        self.recipe = recipe
        self.bodSerial = bodSerial
        
    # For the most part the names of items needed in small bods matches
    # what is listed in large bods. There are exceptions. Thats what this is for.
    def getNameInLargeBod(self):
        
        # smallbod this is skillet, in largebod this is frypan
        if self.recipe.recipeName == "skillet":
            return "frypan"

        return self.recipe.recipeName

    # Not used
#    def getSpecialMaterialPrefix(self):
#        # Blacksmithy weapons all turn into "plate helm" (normal iron ingots) or "dull copper plate helm" (dull copper)
#        if self.recipe.toolId in [BLACKSMITHY_TOOL_STATIC_ID, TAILORING_TOOL_STATIC_ID, TINKERING_TOOL_STATIC_ID] and self.specialMaterialHue in prefixes:
#            return prefixes[self.specialMaterialHue] + " "
    
    # So we can find crafted items either to salvage, trash, or combine with deed.
    # Have to account for special materials, e.g. plate helm becomes shadow iron plate helm
    # And for carpentry, get this: Large Crate becomes crate, Medium Crate becomes crate, and
    # Small Crate becomes small crate.
    # Most of the time, this matches the recipe name. But caps get weird. Sometimes they use them,
    # sometimes they dont, e.g. the recipe for "Wooden Throne" is caps and others are lower.
    def getCraftedItemName(self):
        
        # Tinkering puts iron in front of some items. Be careful with tings like "iron key" which
        # is the real name, we dont want to make it "iron iron key"
        if self.recipe.recipeName == "globe" and self.specialMaterialHue == RESOURCE_HUE_DEFAULT:
            return "iron globe"
        
        # Carpentry strikes again
        if self.recipe.recipeName == "wooden shel":
            return "empty bookcase"
            
        # Large and Small crates turn into "crate"
        if self.recipe.recipeName in ["Large Crate", "Medium Crate"]:
            return "crate"
            
        # Blacksmithy weapons all turn into "plate helm" (normal iron ingots) or "dull copper plate helm" (dull copper)
        if self.recipe.toolId in [BLACKSMITHY_TOOL_STATIC_ID, TAILORING_TOOL_STATIC_ID]:
            return self.specialMaterialName + " " + self.recipe.recipeName if self.specialMaterialName is not None else self.recipe.recipeName

        # Tinkering only some categories have this prefix
        if self.recipe.toolId == TINKERING_TOOL_STATIC_ID and self.recipe.gumpCategory in [CAT_TINKERING_UTENSILS, CAT_TINKERING_MISCELLANEOUS, CAT_TINKERING_TOOLS]:
            return self.specialMaterialName + " " + self.recipe.recipeName if self.specialMaterialName is not None else self.recipe.recipeName            
            
        # Carpentry weapons and armo will turn into "oak gnarled sta" - but not furniture or containers or instruments, praise be
        if self.recipe.toolId == CARPENTRY_TOOL_STATIC_ID and self.recipe.gumpCategory in [CAT_CARPENTRY_WEAPONS, CAT_CARPENTRY_ARMOR]:
            return self.specialMaterialName + " " + self.recipe.recipeName if self.specialMaterialName is not None else self.recipe.recipeName            

        # Default is to just use the exact recipe name that matches crafted item, e.g. "Deadly Poison potion"
        return self.recipe.recipeName        

    def isComplete(self):
        return self.amountToMake == self.amountMade

    def __str__(self):
        return "SmallBod(getCraftedItemName()='{}',amountMade='{}', isExceptional={}, amountToMake='{}', specialMaterialButton='{}', specialMaterialHue='{}', specialMaterialPropId={}, specialMaterialName={}, recipe={})".format(self.getCraftedItemName(), self.amountMade, self.isExceptional, self.amountToMake, self.specialMaterialButton, self.specialMaterialHue, self.specialMaterialPropId, self.specialMaterialName, self.recipe)        
        
# Internal data structure used for filling LBODS.
class LargeBod:
    def __init__(self, bodSerial, isExceptional, amountToMake, specialMaterialPropId, smallBodItems):
        self.isExceptional = isExceptional
        self.amountToMake = amountToMake
        self.specialMaterialPropId = specialMaterialPropId
        self.smallBodItems = smallBodItems
        self.bodSerial = bodSerial

    # Use this to identify similar bods (material, exceptional, and items required)
    # Need this to stort when filling large bods so we complete those with the most progress first
    def getId(self):
        part1 = "1" if self.isExceptional else "0"
        part2 = str(self.specialMaterialPropId) if self.specialMaterialPropId is not None else "0"
        part3 = "|".join(sorted(list(map(lambda smallBodItem: smallBodItem["name"], self.smallBodItems))))
        return part1 + "|" + part2 + "|" + part3
        
    def numComplete(self):
        numCompleted = 0
        for smallBodItem in self.smallBodItems:
            if smallBodItem['amountMade'] == self.amountToMake:
                numCompleted = numCompleted + 1
        return numCompleted
        
    def isComplete(self):
        isComplete = False
        numCompleted = 0
        for smallBodItem in self.smallBodItems:
            if smallBodItem['amountMade'] == self.amountToMake:
                numCompleted = numCompleted + 1
        return numCompleted == len(self.smallBodItems)

    def __str__(self):
        return "LargeBod(isExceptional='{}', amountToMake='{}', specialMaterialPropId={}, smallBodItems={}, isComplete={}, numComplete={})".format(self.isExceptional, self.amountToMake, self.specialMaterialPropId, self.smallBodItems, self.isComplete(), self.numComplete())                

# Just for reporting in conjunction with the report() function.
class BodReport:
    def __init__(self, name):
        self.name = name
        self.numIncompleteSmallBods = 0
        self.numCompleteSmallBods = 0
        self.numIncompleteLargeBods = 0
        self.numCompleteLargeBods = 0
        self.numInWrongContainer = 0
        self.numMissingRecipe = 0
        self.numMissingResources = 0

    def incrementNumIncompleteSmallBods(self):
        self.numIncompleteSmallBods = self.numIncompleteSmallBods + 1
        
    def incrementNumCompleteSmallBods(self):
        self.numCompleteSmallBods = self.numCompleteSmallBods + 1        
        
    def incrementNumIncompleteLargeBods(self):
        self.numIncompleteLargeBods = self.numIncompleteLargeBods + 1
        
    def incrementNumCompleteLargeBods(self):
        self.numCompleteLargeBods = self.numCompleteLargeBods + 1  
  
    def incrementNumInWrongContainer(self):
        self.numInWrongContainer = self.numInWrongContainer + 1
        
    def incrementNumMissingRecipe(self):
        self.numMissingRecipe = self.numMissingRecipe + 1
        
    def incrementNumMissingResources(self):
        self.numMissingResources = self.numMissingResources + 1
        
    def __str__(self):
        totalSmall = self.numIncompleteSmallBods + self.numCompleteSmallBods + self.numMissingRecipe
        totalLarge = self.numIncompleteLargeBods + self.numCompleteLargeBods
        #incompleteSmall = self.numIncompleteSmallBods - self.numMissingRecipe
        return "{}:\t\tSmall ({}/{})\t\tLarge ({}/{})\tWrong Container ({})\tNo Recipe ({})\tNo Resources ({})".format(self.name, self.numCompleteSmallBods, totalSmall, self.numCompleteLargeBods, totalLarge, self.numInWrongContainer, self.numMissingRecipe, self.numMissingResources)

# Default list of recipes. See SmallBodRecipe. You can use these, edit these, or just define your own.
RECIPES = [

    ############################ Tinkering ############################
    
    # Jewelry
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_JEWELRY, 2, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_JEWELRY, 9, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_JEWELRY, 16, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_JEWELRY, 23, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_JEWELRY, 30, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(1000000000, 1)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_JEWELRY, 37, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(1000000000, 1)] ),
    SmallBodRecipe(True, "star sapphire ring", CAT_TINKERING_JEWELRY, 44, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(STAR_SAPPHIRE, 1)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_JEWELRY, 51, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(1000000000, 1)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_JEWELRY, 58, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(1000000000, 1)] ),
    SmallBodRecipe(True, "star sapphire earrings", CAT_TINKERING_JEWELRY, 65, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(STAR_SAPPHIRE, 1)] ),
    
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_JEWELRY, 72, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(1000000000, 1)] ),
    SmallBodRecipe(True, "star sapphire bracelet", CAT_TINKERING_JEWELRY, 79, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(STAR_SAPPHIRE, 1)] ),
    SmallBodRecipe(True, "emerald ring", CAT_TINKERING_JEWELRY, 86, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(EMERALD, 1)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_JEWELRY, 93, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(1000000000, 1)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_JEWELRY, 100, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(1000000000, 1)] ),
    SmallBodRecipe(True, "emerald earrings", CAT_TINKERING_JEWELRY, 107, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(EMERALD, 1)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_JEWELRY, 114, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(1000000000, 1)] ),
    SmallBodRecipe(True, "emerald bracelet", CAT_TINKERING_JEWELRY, 121, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(EMERALD, 1)] ),
    SmallBodRecipe(True, "sapphire ring", CAT_TINKERING_JEWELRY, 128, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(SAPPHIRE, 1)] ),   
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_JEWELRY, 135, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(1000000000, 1)] ),   
    
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_JEWELRY, 142, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(1000000000, 1)] ),   
    SmallBodRecipe(True, "sapphire earrings", CAT_TINKERING_JEWELRY, 149, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(SAPPHIRE, 1)] ),   
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_JEWELRY, 156, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(1000000000, 1)] ),   
    SmallBodRecipe(True, "sapphire bracelet", CAT_TINKERING_JEWELRY, 163, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(SAPPHIRE, 1)] ),   
    SmallBodRecipe(True, "ruby ring", CAT_TINKERING_JEWELRY, 170, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(RUBY, 1)] ),   
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_JEWELRY, 177, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(1000000000, 1)] ),   
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_JEWELRY, 184, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(1000000000, 1)] ),   
    SmallBodRecipe(True, "ruby earrings", CAT_TINKERING_JEWELRY, 191, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(RUBY, 1)] ),   
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_JEWELRY, 198, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(1000000000, 1)] ),   
    SmallBodRecipe(True, "ruby bracelet", CAT_TINKERING_JEWELRY, 205, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(RUBY, 1)] ),   
    
    SmallBodRecipe(True, "citrine ring", CAT_TINKERING_JEWELRY, 212, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(CITRINE, 1)] ),   
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_JEWELRY, 219, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(1000000000, 1)] ),   
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_JEWELRY, 226, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(1000000000, 1)] ),   
    SmallBodRecipe(True, "citrine earrings", CAT_TINKERING_JEWELRY, 233, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(CITRINE, 1)] ),   
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_JEWELRY, 240, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(1000000000, 1)] ),   
    SmallBodRecipe(True, "citrine bracelet", CAT_TINKERING_JEWELRY, 247, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(CITRINE, 1)] ),   
    SmallBodRecipe(True, "amethyst ring", CAT_TINKERING_JEWELRY, 254, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(AMETHYST, 1)] ),   
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_JEWELRY, 261, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(1000000000, 1)] ),   
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_JEWELRY, 268, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(1000000000, 1)] ),   
    SmallBodRecipe(True, "amethyst earrings", CAT_TINKERING_JEWELRY, 275, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(AMETHYST, 1)] ),   
    
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_JEWELRY, 282, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(1000000000, 1)] ),   
    SmallBodRecipe(True, "amethyst bracelet", CAT_TINKERING_JEWELRY, 289, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(AMETHYST, 1)] ),   
    SmallBodRecipe(False, "tourmaline ring", CAT_TINKERING_JEWELRY, 296, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(TOURMALINE, 1)] ),   
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_JEWELRY, 303, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(1000000000, 1)] ),   
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_JEWELRY, 310, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(1000000000, 1)] ),   
    SmallBodRecipe(True, "tourmaline earrings", CAT_TINKERING_JEWELRY, 317, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(TOURMALINE, 1)] ),   
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_JEWELRY, 324, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(1000000000, 1)] ),   
    SmallBodRecipe(True, "tourmaline bracelet", CAT_TINKERING_JEWELRY, 331, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(TOURMALINE, 1)] ),   
    SmallBodRecipe(True, "amber ring", CAT_TINKERING_JEWELRY, 338, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(AMBER, 1)] ),   
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_JEWELRY, 345, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(1000000000, 1)] ),   
    
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_JEWELRY, 352, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(1000000000, 1)] ),   
    SmallBodRecipe(True, "amber earrings", CAT_TINKERING_JEWELRY, 359, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(AMBER, 1)] ),   
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_JEWELRY, 366, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(1000000000, 1)] ),   
    SmallBodRecipe(True, "amber bracelet", CAT_TINKERING_JEWELRY, 373, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(AMBER, 1)] ),   
    SmallBodRecipe(False, "diamond ring", CAT_TINKERING_JEWELRY, 380, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(DIAMOND, 1)] ),   
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_JEWELRY, 387, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(1000000000, 1)] ),   
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_JEWELRY, 394, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(1000000000, 1)] ),   
    SmallBodRecipe(True, "diamond earrings", CAT_TINKERING_JEWELRY, 401, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(DIAMOND, 1)] ),   
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_JEWELRY, 408, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(1000000000, 1)] ),   
    SmallBodRecipe(True, "diamond bracelet", CAT_TINKERING_JEWELRY, 415, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2), SmallBodResource(DIAMOND, 1)] ),   
    
    # Wodden Items
    SmallBodRecipe(False, "nunchaku", CAT_TINKERING_WOODEN_ITEMS, 2, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 3), SmallBodResource(BOARD_STATIC_ID, 8)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_WOODEN_ITEMS, 9, TINKERING_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_WOODEN_ITEMS, 16, TINKERING_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_WOODEN_ITEMS, 23, TINKERING_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(False, "clock frame", CAT_TINKERING_WOODEN_ITEMS, 30, TINKERING_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID, 6)] ),
    SmallBodRecipe(False, "axle", CAT_TINKERING_WOODEN_ITEMS, 37, TINKERING_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID, 2)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_WOODEN_ITEMS, 44, TINKERING_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_WOODEN_ITEMS, 51, TINKERING_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_WOODEN_ITEMS, 58, TINKERING_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_WOODEN_ITEMS, 65, TINKERING_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_WOODEN_ITEMS, 72, TINKERING_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_WOODEN_ITEMS, 79, TINKERING_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_WOODEN_ITEMS, 86, TINKERING_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_WOODEN_ITEMS, 93, TINKERING_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_WOODEN_ITEMS, 100, TINKERING_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_WOODEN_ITEMS, 107, TINKERING_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_WOODEN_ITEMS, 114, TINKERING_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_WOODEN_ITEMS, 121, TINKERING_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_WOODEN_ITEMS, 128, TINKERING_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    
    # Tools
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_TOOLS, 2, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(True, "mortar and pestle", CAT_TINKERING_TOOLS, 9, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 3)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_TOOLS, 16, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_TOOLS, 23, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "hatchet", CAT_TINKERING_TOOLS, 30, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 4)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_TOOLS, 37, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(True, "sewing kit", CAT_TINKERING_TOOLS, 44, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2)] ),
    SmallBodRecipe(False, "saw", CAT_TINKERING_TOOLS, 51, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 4)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_TOOLS, 58, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "froe", CAT_TINKERING_TOOLS, 65, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_TOOLS, 72, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_TOOLS, 79, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "tongs", CAT_TINKERING_TOOLS, 86, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 1)] ),
    SmallBodRecipe(True, "smith's hammer", CAT_TINKERING_TOOLS, 93, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 4)] ), #'
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_TOOLS, 100, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_TOOLS, 107, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "pickaxe", CAT_TINKERING_TOOLS, 114, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 4)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_TOOLS, 121, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    # This goddamned thing is a killet in smallbods (item name is skillet too) but a frypan in large bods
    SmallBodRecipe(True, "skillet", CAT_TINKERING_TOOLS, 128, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 4)] ),   
    SmallBodRecipe(False, "flour sifter", CAT_TINKERING_TOOLS, 135, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 3)] ),   
    SmallBodRecipe(True, "arrow fletching", CAT_TINKERING_TOOLS, 142, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 3)] ),   
    SmallBodRecipe(False, "clippers", CAT_TINKERING_TOOLS, 163, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 4)] ),   
    SmallBodRecipe(False, "pitchfork", CAT_TINKERING_TOOLS, 177, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 4)] ),   
   
    # Parts
    SmallBodRecipe(False, "gears", CAT_TINKERING_PARTS, 2, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2)] ),
    SmallBodRecipe(False, "clock parts", CAT_TINKERING_PARTS, 9, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 1)] ),
    SmallBodRecipe(False, "barrel tap", CAT_TINKERING_PARTS, 16, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2)] ),
    SmallBodRecipe(False, "springs", CAT_TINKERING_PARTS, 23, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2)] ),
    SmallBodRecipe(False, "sextant parts", CAT_TINKERING_PARTS, 30, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 4)] ),
    SmallBodRecipe(False, "barrel hoops", CAT_TINKERING_PARTS, 37, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 5)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_PARTS, 44, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_PARTS, 51, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_PARTS, 58, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_PARTS, 65, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_PARTS, 72, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_PARTS, 79, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_PARTS, 86, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_PARTS, 93, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_PARTS, 100, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_PARTS, 107, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_PARTS, 114, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_PARTS, 121, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_PARTS, 128, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ), 

    # Utensils
    SmallBodRecipe(True, "butcher knife", CAT_TINKERING_UTENSILS, 2, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2)] ),
    SmallBodRecipe(True, "spoon", CAT_TINKERING_UTENSILS, 9, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 1)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_UTENSILS, 16, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(True, "plate", CAT_TINKERING_UTENSILS, 23, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2)] ),
    SmallBodRecipe(True, "fork", CAT_TINKERING_UTENSILS, 30, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 1)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_UTENSILS, 37, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "cleaver", CAT_TINKERING_UTENSILS, 44, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 3)] ),
    SmallBodRecipe(True, "knife", CAT_TINKERING_UTENSILS, 51, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 1)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_UTENSILS, 58, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(True, "goblet", CAT_TINKERING_UTENSILS, 65, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2)] ),
    SmallBodRecipe(False, "pewter mug", CAT_TINKERING_UTENSILS, 72, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_UTENSILS, 79, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_UTENSILS, 86, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_UTENSILS, 93, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_UTENSILS, 100, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_UTENSILS, 107, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_UTENSILS, 114, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_UTENSILS, 121, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_UTENSILS, 128, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ), 
   
    # Miscellaneous
    SmallBodRecipe(True, "key ring", CAT_TINKERING_MISCELLANEOUS, 2, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2)] ),
    SmallBodRecipe(False, "candelabra", CAT_TINKERING_MISCELLANEOUS, 9, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 4)] ),
    SmallBodRecipe(False, "scales", CAT_TINKERING_MISCELLANEOUS, 16, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 4)] ),
    SmallBodRecipe(True, "iron key", CAT_TINKERING_MISCELLANEOUS, 23, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 3)] ),
    SmallBodRecipe(True, "globe", CAT_TINKERING_MISCELLANEOUS, 30, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 4)] ),
    SmallBodRecipe(False, "spyglass", CAT_TINKERING_MISCELLANEOUS, 37, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 4)] ),
    SmallBodRecipe(False, "lantern", CAT_TINKERING_MISCELLANEOUS, 44, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 2)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_MISCELLANEOUS, 51, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_MISCELLANEOUS, 58, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_MISCELLANEOUS, 65, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_MISCELLANEOUS, 72, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_MISCELLANEOUS, 79, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_MISCELLANEOUS, 86, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_MISCELLANEOUS, 93, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_MISCELLANEOUS, 100, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_MISCELLANEOUS, 107, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_MISCELLANEOUS, 114, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_MISCELLANEOUS, 121, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_MISCELLANEOUS, 128, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),   
 
    # Assemblies
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_ASSEMBLIES, 2, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_ASSEMBLIES, 9, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_ASSEMBLIES, 16, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_ASSEMBLIES, 23, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_ASSEMBLIES, 30, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_ASSEMBLIES, 37, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_ASSEMBLIES, 44, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_ASSEMBLIES, 51, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_ASSEMBLIES, 58, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_ASSEMBLIES, 65, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_ASSEMBLIES, 72, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_ASSEMBLIES, 79, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_ASSEMBLIES, 86, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_ASSEMBLIES, 93, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_ASSEMBLIES, 100, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_ASSEMBLIES, 107, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_ASSEMBLIES, 114, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_ASSEMBLIES, 121, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "00000000000", CAT_TINKERING_ASSEMBLIES, 128, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),    

    
    ############################ Tailoring ############################
    
    SmallBodRecipe(True, "skullcap", CAT_TAILORING_HATS, 2, TAILORING_TOOL_STATIC_ID, [SmallBodResource(CLOTH_STATIC_ID)] ),
    SmallBodRecipe(True, "bandana", CAT_TAILORING_HATS, 9, TAILORING_TOOL_STATIC_ID, [SmallBodResource(CLOTH_STATIC_ID)] ),
    SmallBodRecipe(True, "floppy hat", CAT_TAILORING_HATS, 16, TAILORING_TOOL_STATIC_ID, [SmallBodResource(CLOTH_STATIC_ID)] ),
    SmallBodRecipe(True, "cap", CAT_TAILORING_HATS, 23, TAILORING_TOOL_STATIC_ID, [SmallBodResource(CLOTH_STATIC_ID)] ),
    SmallBodRecipe(True, "wide-brim hat", CAT_TAILORING_HATS, 30, TAILORING_TOOL_STATIC_ID, [SmallBodResource(CLOTH_STATIC_ID)] ),
    SmallBodRecipe(True, "straw hat", CAT_TAILORING_HATS, 37, TAILORING_TOOL_STATIC_ID, [SmallBodResource(CLOTH_STATIC_ID)] ),
    SmallBodRecipe(True, "tall straw hat", CAT_TAILORING_HATS, 44, TAILORING_TOOL_STATIC_ID, [SmallBodResource(CLOTH_STATIC_ID)] ),
    SmallBodRecipe(True, "wizard's hat", CAT_TAILORING_HATS, 51, TAILORING_TOOL_STATIC_ID, [SmallBodResource(CLOTH_STATIC_ID)] ), # grr'
    SmallBodRecipe(False, "bonnet", CAT_TAILORING_HATS, 58, TAILORING_TOOL_STATIC_ID, [SmallBodResource(CLOTH_STATIC_ID)] ),
    SmallBodRecipe(True, "feathered hat", CAT_TAILORING_HATS, 65, TAILORING_TOOL_STATIC_ID, [SmallBodResource(CLOTH_STATIC_ID)] ),
    SmallBodRecipe(True, "tricorne hat", CAT_TAILORING_HATS, 72, TAILORING_TOOL_STATIC_ID, [SmallBodResource(CLOTH_STATIC_ID)] ), # should be 72
    SmallBodRecipe(True, "jester hat", CAT_TAILORING_HATS, 79, TAILORING_TOOL_STATIC_ID, [SmallBodResource(CLOTH_STATIC_ID)] ),
    SmallBodRecipe(False, "flower garland", CAT_TAILORING_HATS, 86, TAILORING_TOOL_STATIC_ID, [SmallBodResource(CLOTH_STATIC_ID)] ),
    
    SmallBodRecipe(True, "doublet", CAT_TAILORING_SHIRTS_AND_PANTS, 2, TAILORING_TOOL_STATIC_ID, [SmallBodResource(CLOTH_STATIC_ID)] ),
    SmallBodRecipe(True, "shirt", CAT_TAILORING_SHIRTS_AND_PANTS, 9, TAILORING_TOOL_STATIC_ID, [SmallBodResource(CLOTH_STATIC_ID)] ),
    SmallBodRecipe(True, "fancy shirt", CAT_TAILORING_SHIRTS_AND_PANTS, 16, TAILORING_TOOL_STATIC_ID, [SmallBodResource(CLOTH_STATIC_ID)] ),
    SmallBodRecipe(True, "tunic", CAT_TAILORING_SHIRTS_AND_PANTS, 23, TAILORING_TOOL_STATIC_ID, [SmallBodResource(CLOTH_STATIC_ID)] ),
    SmallBodRecipe(True, "surcoat", CAT_TAILORING_SHIRTS_AND_PANTS, 30, TAILORING_TOOL_STATIC_ID, [SmallBodResource(CLOTH_STATIC_ID)] ),
    SmallBodRecipe(True, "plain dress", CAT_TAILORING_SHIRTS_AND_PANTS, 37, TAILORING_TOOL_STATIC_ID, [SmallBodResource(CLOTH_STATIC_ID)] ),
    SmallBodRecipe(True, "fancy dress", CAT_TAILORING_SHIRTS_AND_PANTS, 44, TAILORING_TOOL_STATIC_ID, [SmallBodResource(CLOTH_STATIC_ID)] ),
    SmallBodRecipe(True, "cloak", CAT_TAILORING_SHIRTS_AND_PANTS, 51, TAILORING_TOOL_STATIC_ID, [SmallBodResource(CLOTH_STATIC_ID)] ),
    SmallBodRecipe(True, "robe", CAT_TAILORING_SHIRTS_AND_PANTS, 58, TAILORING_TOOL_STATIC_ID, [SmallBodResource(CLOTH_STATIC_ID)] ),
    SmallBodRecipe(True, "jester suit", CAT_TAILORING_SHIRTS_AND_PANTS, 65, TAILORING_TOOL_STATIC_ID, [SmallBodResource(CLOTH_STATIC_ID)] ),
    SmallBodRecipe(False, "fur cape", CAT_TAILORING_SHIRTS_AND_PANTS, 72, TAILORING_TOOL_STATIC_ID, [SmallBodResource(CLOTH_STATIC_ID)] ),
    SmallBodRecipe(True, "short pants", CAT_TAILORING_SHIRTS_AND_PANTS, 135, TAILORING_TOOL_STATIC_ID, [SmallBodResource(CLOTH_STATIC_ID)] ),
    SmallBodRecipe(True, "long pants", CAT_TAILORING_SHIRTS_AND_PANTS, 142, TAILORING_TOOL_STATIC_ID, [SmallBodResource(CLOTH_STATIC_ID)] ),
    SmallBodRecipe(True, "kilt", CAT_TAILORING_SHIRTS_AND_PANTS, 149, TAILORING_TOOL_STATIC_ID, [SmallBodResource(CLOTH_STATIC_ID)] ),
    SmallBodRecipe(True, "skirt", CAT_TAILORING_SHIRTS_AND_PANTS, 156, TAILORING_TOOL_STATIC_ID, [SmallBodResource(CLOTH_STATIC_ID)] ),
    
    SmallBodRecipe(True, "body sash", CAT_TAILORING_MISCELLANEOUS, 2, TAILORING_TOOL_STATIC_ID, [SmallBodResource(CLOTH_STATIC_ID)] ),
    SmallBodRecipe(False, "half apron", CAT_TAILORING_MISCELLANEOUS, 9, TAILORING_TOOL_STATIC_ID, [SmallBodResource(CLOTH_STATIC_ID)] ),
    SmallBodRecipe(True, "full apron", CAT_TAILORING_MISCELLANEOUS, 16, TAILORING_TOOL_STATIC_ID, [SmallBodResource(CLOTH_STATIC_ID)] ),
    
    SmallBodRecipe(False, "elven boots", CAT_TAILORING_FOOTWEAR, 2, TAILORING_TOOL_STATIC_ID, [SmallBodResource(LEATHER_STATIC_ID)] ),
    SmallBodRecipe(False, "fur boots", CAT_TAILORING_FOOTWEAR, 9, TAILORING_TOOL_STATIC_ID, [SmallBodResource(CLOTH_STATIC_ID)] ),
    SmallBodRecipe(True, "sandals", CAT_TAILORING_FOOTWEAR, 30, TAILORING_TOOL_STATIC_ID, [SmallBodResource(LEATHER_STATIC_ID)] ),
    SmallBodRecipe(True, "shoes", CAT_TAILORING_FOOTWEAR, 37, TAILORING_TOOL_STATIC_ID, [SmallBodResource(LEATHER_STATIC_ID)] ),
    SmallBodRecipe(True, "boots", CAT_TAILORING_FOOTWEAR, 44, TAILORING_TOOL_STATIC_ID, [SmallBodResource(LEATHER_STATIC_ID)] ),
    SmallBodRecipe(True, "thigh boots", CAT_TAILORING_FOOTWEAR, 51, TAILORING_TOOL_STATIC_ID, [SmallBodResource(LEATHER_STATIC_ID)] ),
    SmallBodRecipe(False, "jester shoes", CAT_TAILORING_FOOTWEAR, 65, TAILORING_TOOL_STATIC_ID, [SmallBodResource(LEATHER_STATIC_ID)] ),
    
    SmallBodRecipe(True, "leather gorget", CAT_TAILORING_LEATHER_ARMOR, 23, TAILORING_TOOL_STATIC_ID, [SmallBodResource(LEATHER_STATIC_ID)] ),
    SmallBodRecipe(True, "leather cap", CAT_TAILORING_LEATHER_ARMOR, 30, TAILORING_TOOL_STATIC_ID, [SmallBodResource(LEATHER_STATIC_ID)] ),
    SmallBodRecipe(True, "leather gloves", CAT_TAILORING_LEATHER_ARMOR, 37, TAILORING_TOOL_STATIC_ID, [SmallBodResource(LEATHER_STATIC_ID)] ),
    SmallBodRecipe(True, "leather sleeves", CAT_TAILORING_LEATHER_ARMOR, 44, TAILORING_TOOL_STATIC_ID, [SmallBodResource(LEATHER_STATIC_ID)] ),
    SmallBodRecipe(True, "leather leggings", CAT_TAILORING_LEATHER_ARMOR, 51, TAILORING_TOOL_STATIC_ID, [SmallBodResource(LEATHER_STATIC_ID)] ),
    SmallBodRecipe(True, "leather tunic", CAT_TAILORING_LEATHER_ARMOR, 58, TAILORING_TOOL_STATIC_ID, [SmallBodResource(LEATHER_STATIC_ID)] ),
    
    SmallBodRecipe(True, "studded gorget", CAT_TAILORING_STUDDED_ARMOR, 2, TAILORING_TOOL_STATIC_ID, [SmallBodResource(LEATHER_STATIC_ID)] ),
    SmallBodRecipe(True, "studded gloves", CAT_TAILORING_STUDDED_ARMOR, 9, TAILORING_TOOL_STATIC_ID, [SmallBodResource(LEATHER_STATIC_ID)] ),
    SmallBodRecipe(True, "studded sleeves", CAT_TAILORING_STUDDED_ARMOR, 16, TAILORING_TOOL_STATIC_ID, [SmallBodResource(LEATHER_STATIC_ID)] ),
    SmallBodRecipe(True, "studded leggings", CAT_TAILORING_STUDDED_ARMOR, 23, TAILORING_TOOL_STATIC_ID, [SmallBodResource(LEATHER_STATIC_ID)] ),
    SmallBodRecipe(True, "studded tunic", CAT_TAILORING_STUDDED_ARMOR, 30, TAILORING_TOOL_STATIC_ID, [SmallBodResource(LEATHER_STATIC_ID)] ),
    
    SmallBodRecipe(True, "leather shorts", CAT_TAILORING_FEMALE_ARMOR, 2, TAILORING_TOOL_STATIC_ID, [SmallBodResource(LEATHER_STATIC_ID)] ),
    SmallBodRecipe(True, "leather skirt", CAT_TAILORING_FEMALE_ARMOR, 9, TAILORING_TOOL_STATIC_ID, [SmallBodResource(LEATHER_STATIC_ID)] ),
    SmallBodRecipe(True, "leather bustier", CAT_TAILORING_FEMALE_ARMOR, 16, TAILORING_TOOL_STATIC_ID, [SmallBodResource(LEATHER_STATIC_ID)] ),
    SmallBodRecipe(True, "studded bustier", CAT_TAILORING_FEMALE_ARMOR, 23, TAILORING_TOOL_STATIC_ID, [SmallBodResource(LEATHER_STATIC_ID)] ),
    SmallBodRecipe(True, "female leather armor", CAT_TAILORING_FEMALE_ARMOR, 30, TAILORING_TOOL_STATIC_ID, [SmallBodResource(LEATHER_STATIC_ID)] ),
    SmallBodRecipe(True, "studded armor", CAT_TAILORING_FEMALE_ARMOR, 37, TAILORING_TOOL_STATIC_ID, [SmallBodResource(LEATHER_STATIC_ID)] ),
    
    SmallBodRecipe(True, "bone helmet", CAT_TAILORING_BONE_ARMOR, 2, TAILORING_TOOL_STATIC_ID, [SmallBodResource(LEATHER_STATIC_ID, 4), SmallBodResource(BONE, 2)] ),
    SmallBodRecipe(True, "bone gloves", CAT_TAILORING_BONE_ARMOR, 9, TAILORING_TOOL_STATIC_ID, [SmallBodResource(LEATHER_STATIC_ID, 6), SmallBodResource(BONE, 2)] ),
    SmallBodRecipe(True, "bone arms", CAT_TAILORING_BONE_ARMOR, 16, TAILORING_TOOL_STATIC_ID, [SmallBodResource(LEATHER_STATIC_ID, 8), SmallBodResource(BONE, 4)] ),
    SmallBodRecipe(True, "bone leggings", CAT_TAILORING_BONE_ARMOR, 23, TAILORING_TOOL_STATIC_ID, [SmallBodResource(LEATHER_STATIC_ID, 10), SmallBodResource(BONE, 6)] ),
    SmallBodRecipe(True, "bone armor", CAT_TAILORING_BONE_ARMOR, 30, TAILORING_TOOL_STATIC_ID, [SmallBodResource(LEATHER_STATIC_ID, 12), SmallBodResource(BONE, 10)] ),
    

    ############################ Alchemy ############################
    
    SmallBodRecipe(True, "Refresh potion", CAT_ALCHEMY_HEALING_AND_CURATIVE, 2, ALCHEMY_TOOL_STATIC_ID, [SmallBodResource(EMPTY_BOTTLE_STATIC_ID, 1), SmallBodResource(BLACKPEARL, 1) ] ),
    SmallBodRecipe(True, "Greater Refreshment potion", CAT_ALCHEMY_HEALING_AND_CURATIVE, 9, ALCHEMY_TOOL_STATIC_ID, [SmallBodResource(EMPTY_BOTTLE_STATIC_ID, 1), SmallBodResource(BLACKPEARL, 5) ] ),
    SmallBodRecipe(True, "Lesser Heal potion", CAT_ALCHEMY_HEALING_AND_CURATIVE, 16, ALCHEMY_TOOL_STATIC_ID, [SmallBodResource(EMPTY_BOTTLE_STATIC_ID, 1), SmallBodResource(GINSENG, 1) ] ),
    SmallBodRecipe(True, "Heal potion", CAT_ALCHEMY_HEALING_AND_CURATIVE, 23, ALCHEMY_TOOL_STATIC_ID, [SmallBodResource(EMPTY_BOTTLE_STATIC_ID, 1), SmallBodResource(GINSENG, 3) ] ),
    SmallBodRecipe(False, "Greater Heal potion", CAT_ALCHEMY_HEALING_AND_CURATIVE, 30, ALCHEMY_TOOL_STATIC_ID, [SmallBodResource(EMPTY_BOTTLE_STATIC_ID, 1), SmallBodResource(GINSENG, 7) ] ),
    SmallBodRecipe(True, "Lesser Cure potion", CAT_ALCHEMY_HEALING_AND_CURATIVE, 37, ALCHEMY_TOOL_STATIC_ID, [SmallBodResource(EMPTY_BOTTLE_STATIC_ID, 1), SmallBodResource(GARLIC, 1) ] ),
    SmallBodRecipe(True, "Cure potion", CAT_ALCHEMY_HEALING_AND_CURATIVE, 44, ALCHEMY_TOOL_STATIC_ID, [SmallBodResource(EMPTY_BOTTLE_STATIC_ID, 1), SmallBodResource(GARLIC, 3) ] ),
    SmallBodRecipe(False, "Greater Cure potion", CAT_ALCHEMY_HEALING_AND_CURATIVE, 51, ALCHEMY_TOOL_STATIC_ID, [SmallBodResource(EMPTY_BOTTLE_STATIC_ID, 1), SmallBodResource(GARLIC, 6) ] ),

    SmallBodRecipe(False, "Agility potion", CAT_ALCHEMY_ENHANCEMENT, 2, ALCHEMY_TOOL_STATIC_ID, [SmallBodResource(EMPTY_BOTTLE_STATIC_ID, 1), SmallBodResource(BLOODMOSS, 1) ] ),
    SmallBodRecipe(True, "Greater Agility potion", CAT_ALCHEMY_ENHANCEMENT, 9, ALCHEMY_TOOL_STATIC_ID, [SmallBodResource(EMPTY_BOTTLE_STATIC_ID, 1), SmallBodResource(BLOODMOSS, 3) ] ),
    SmallBodRecipe(False, "Night Sight potion", CAT_ALCHEMY_ENHANCEMENT, 16, ALCHEMY_TOOL_STATIC_ID, [SmallBodResource(EMPTY_BOTTLE_STATIC_ID, 1), SmallBodResource(SPIDERSILK, 1) ] ),
    SmallBodRecipe(False, "Strength potion", CAT_ALCHEMY_ENHANCEMENT, 23, ALCHEMY_TOOL_STATIC_ID, [SmallBodResource(EMPTY_BOTTLE_STATIC_ID, 1), SmallBodResource(MANDRAKEROOT, 2) ] ),
    SmallBodRecipe(True, "Greater Strength potion", CAT_ALCHEMY_ENHANCEMENT, 30, ALCHEMY_TOOL_STATIC_ID, [SmallBodResource(EMPTY_BOTTLE_STATIC_ID, 1), SmallBodResource(MANDRAKEROOT, 5) ] ),
    SmallBodRecipe(False, "Invisibility potion", CAT_ALCHEMY_ENHANCEMENT, 37, ALCHEMY_TOOL_STATIC_ID, [SmallBodResource(EMPTY_BOTTLE_STATIC_ID, 1), SmallBodResource(BLOODMOSS, 4), SmallBodResource(NIGHTSHADE, 3) ] ),

    SmallBodRecipe(True, "Lesser Poison potion", CAT_ALCHEMY_TOXIC, 2, ALCHEMY_TOOL_STATIC_ID, [SmallBodResource(EMPTY_BOTTLE_STATIC_ID, 1), SmallBodResource(NIGHTSHADE, 1) ] ),
    SmallBodRecipe(True, "Poison potion", CAT_ALCHEMY_TOXIC, 9, ALCHEMY_TOOL_STATIC_ID, [SmallBodResource(EMPTY_BOTTLE_STATIC_ID, 1), SmallBodResource(NIGHTSHADE, 2) ] ),
    SmallBodRecipe(True, "Greater Poison potion", CAT_ALCHEMY_TOXIC, 16, ALCHEMY_TOOL_STATIC_ID, [SmallBodResource(EMPTY_BOTTLE_STATIC_ID, 1), SmallBodResource(NIGHTSHADE, 4) ] ),
    SmallBodRecipe(True, "Deadly Poison potion", CAT_ALCHEMY_TOXIC, 23, ALCHEMY_TOOL_STATIC_ID, [SmallBodResource(EMPTY_BOTTLE_STATIC_ID, 1), SmallBodResource(NIGHTSHADE, 8) ] ),
    SmallBodRecipe(True, "Parasitic potion", CAT_ALCHEMY_TOXIC, 30, ALCHEMY_TOOL_STATIC_ID, [SmallBodResource(EMPTY_BOTTLE_STATIC_ID, 1), SmallBodResource(PARASITIC_PLANT, 5) ] ),
    SmallBodRecipe(True, "Darkglow potion", CAT_ALCHEMY_TOXIC, 37, ALCHEMY_TOOL_STATIC_ID, [SmallBodResource(EMPTY_BOTTLE_STATIC_ID, 1), SmallBodResource(LUMINESCENT_FUNGI, 5) ] ),
  
    SmallBodRecipe(True, "Lesser Explosion potion", CAT_ALCHEMY_EXPLOSIVE, 2, ALCHEMY_TOOL_STATIC_ID, [SmallBodResource(EMPTY_BOTTLE_STATIC_ID, 1), SmallBodResource(SULPHUROUSASH, 3) ] ),
    SmallBodRecipe(True, "Explosion potion", CAT_ALCHEMY_EXPLOSIVE, 9, ALCHEMY_TOOL_STATIC_ID, [SmallBodResource(EMPTY_BOTTLE_STATIC_ID, 1), SmallBodResource(SULPHUROUSASH, 5) ] ),
    SmallBodRecipe(True, "Greater Explosion potion", CAT_ALCHEMY_EXPLOSIVE, 16, ALCHEMY_TOOL_STATIC_ID, [SmallBodResource(EMPTY_BOTTLE_STATIC_ID, 1), SmallBodResource(SULPHUROUSASH, 10) ] ),
    SmallBodRecipe(True, "conflagration potion", CAT_ALCHEMY_EXPLOSIVE, 23, ALCHEMY_TOOL_STATIC_ID, [SmallBodResource(EMPTY_BOTTLE_STATIC_ID, 1), SmallBodResource(GRAVEDUST, 5) ] ),
    SmallBodRecipe(True, "greater conflagration potion", CAT_ALCHEMY_EXPLOSIVE, 30, ALCHEMY_TOOL_STATIC_ID, [SmallBodResource(EMPTY_BOTTLE_STATIC_ID, 1), SmallBodResource(GRAVEDUST, 10) ] ),
    SmallBodRecipe(True, "confusion blast", CAT_ALCHEMY_EXPLOSIVE, 37, ALCHEMY_TOOL_STATIC_ID, [SmallBodResource(EMPTY_BOTTLE_STATIC_ID, 1), SmallBodResource(PIGIRON, 5) ] ),
    SmallBodRecipe(True, "greater confusion blast", CAT_ALCHEMY_EXPLOSIVE, 44, ALCHEMY_TOOL_STATIC_ID, [SmallBodResource(EMPTY_BOTTLE_STATIC_ID, 1), SmallBodResource(PIGIRON, 10) ] ),
    
    ############################ Inscription ############################
    
    SmallBodRecipe(False, "Reactive Armor", CAT_INSCRIPTION_FIRST_SECOND, 2, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(GARLIC, 1), SmallBodResource(SPIDERSILK, 1), SmallBodResource(SULPHUROUSASH, 1) ] ),
    SmallBodRecipe(True, "Clumsy", CAT_INSCRIPTION_FIRST_SECOND, 9, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BLOODMOSS, 1), SmallBodResource(NIGHTSHADE, 1) ] ),
    SmallBodRecipe(False, "Create Food", CAT_INSCRIPTION_FIRST_SECOND, 16, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(GARLIC, 1), SmallBodResource(GINSENG, 1), SmallBodResource(MANDRAKEROOT, 1) ] ),
    SmallBodRecipe(True, "Feeblemind", CAT_INSCRIPTION_FIRST_SECOND, 23, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(NIGHTSHADE, 1), SmallBodResource(GINSENG, 1) ] ),
    SmallBodRecipe(True, "Heal", CAT_INSCRIPTION_FIRST_SECOND, 30, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(GARLIC, 1), SmallBodResource(GINSENG, 1), SmallBodResource(SPIDERSILK, 1) ] ),
    SmallBodRecipe(False, "Magic Arrow", CAT_INSCRIPTION_FIRST_SECOND, 37, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(SULPHUROUSASH, 1) ] ),
    SmallBodRecipe(False, "Night Sight", CAT_INSCRIPTION_FIRST_SECOND, 44, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(SPIDERSILK, 1), SmallBodResource(SULPHUROUSASH, 1) ] ),
    SmallBodRecipe(True, "Weaken", CAT_INSCRIPTION_FIRST_SECOND, 51, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(NIGHTSHADE, 1), SmallBodResource(GARLIC, 1) ] ),
    SmallBodRecipe(True, "Agility", CAT_INSCRIPTION_FIRST_SECOND, 58, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BLOODMOSS, 1), SmallBodResource(MANDRAKEROOT, 1) ] ),
    SmallBodRecipe(True, "Cunning", CAT_INSCRIPTION_FIRST_SECOND, 65, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(NIGHTSHADE, 1), SmallBodResource(MANDRAKEROOT, 1) ] ),
    SmallBodRecipe(True, "Cure", CAT_INSCRIPTION_FIRST_SECOND, 72, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(GARLIC, 1), SmallBodResource(GINSENG, 1) ] ),
    SmallBodRecipe(False, "Harm", CAT_INSCRIPTION_FIRST_SECOND, 79, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(NIGHTSHADE, 1), SmallBodResource(SPIDERSILK, 1) ] ),
    SmallBodRecipe(False, "Magic Trap", CAT_INSCRIPTION_FIRST_SECOND, 86, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(GARLIC, 1), SmallBodResource(SPIDERSILK, 1), SmallBodResource(SULPHUROUSASH, 1) ] ),
    SmallBodRecipe(False, "Magic Untrap", CAT_INSCRIPTION_FIRST_SECOND, 93, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BLOODMOSS, 1), SmallBodResource(SULPHUROUSASH, 1) ] ),
    SmallBodRecipe(False, "Protection", CAT_INSCRIPTION_FIRST_SECOND, 100, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(GARLIC, 1), SmallBodResource(GINSENG, 1), SmallBodResource(SULPHUROUSASH, 1) ] ),
    SmallBodRecipe(True, "Strength", CAT_INSCRIPTION_FIRST_SECOND, 107, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(NIGHTSHADE, 1), SmallBodResource(MANDRAKEROOT, 1) ] ),
    
    SmallBodRecipe(False, "Bless", CAT_INSCRIPTION_THIRD_FOURTH, 2, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(GARLIC, 1), SmallBodResource(MANDRAKEROOT, 1) ] ),
    SmallBodRecipe(False, "Fireball", CAT_INSCRIPTION_THIRD_FOURTH, 9, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BLACKPEARL, 1) ] ),
    SmallBodRecipe(False, "Magic Lock", CAT_INSCRIPTION_THIRD_FOURTH, 16, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BLOODMOSS, 1), SmallBodResource(GARLIC, 1), SmallBodResource(SULPHUROUSASH, 1) ] ),
    SmallBodRecipe(False, "Poison", CAT_INSCRIPTION_THIRD_FOURTH, 23, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(NIGHTSHADE, 1) ] ),
    SmallBodRecipe(False, "Telekinesis", CAT_INSCRIPTION_THIRD_FOURTH, 30, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BLOODMOSS, 1), SmallBodResource(MANDRAKEROOT, 1)] ),
    SmallBodRecipe(False, "Teleport", CAT_INSCRIPTION_THIRD_FOURTH, 37, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BLOODMOSS, 1), SmallBodResource(MANDRAKEROOT, 1)] ),
    SmallBodRecipe(False, "Unlock", CAT_INSCRIPTION_THIRD_FOURTH, 44, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BLOODMOSS, 1), SmallBodResource(SULPHUROUSASH, 1) ] ),
    SmallBodRecipe(False, "Wall of Stone", CAT_INSCRIPTION_THIRD_FOURTH, 51, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BLOODMOSS, 1), SmallBodResource(GARLIC, 1) ] ),
    SmallBodRecipe(False, "Arch Cure", CAT_INSCRIPTION_THIRD_FOURTH, 58, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(GARLIC, 1), SmallBodResource(GINSENG, 1), SmallBodResource(MANDRAKEROOT, 1) ] ),
    SmallBodRecipe(False, "Arch Protection", CAT_INSCRIPTION_THIRD_FOURTH, 65, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(GARLIC, 1), SmallBodResource(GINSENG, 1), SmallBodResource(MANDRAKEROOT, 1), SmallBodResource(SULPHUROUSASH, 1) ] ),
    SmallBodRecipe(True, "Curse", CAT_INSCRIPTION_THIRD_FOURTH, 72, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(GARLIC, 1), SmallBodResource(NIGHTSHADE, 1), SmallBodResource(SULPHUROUSASH, 1) ] ),
    SmallBodRecipe(False, "Fire Field", CAT_INSCRIPTION_THIRD_FOURTH, 79, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BLACKPEARL, 1), SmallBodResource(SPIDERSILK, 1), SmallBodResource(SULPHUROUSASH, 1) ] ),
    SmallBodRecipe(True, "Greater Heal", CAT_INSCRIPTION_THIRD_FOURTH, 86, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(GARLIC, 1), SmallBodResource(SPIDERSILK, 1), SmallBodResource(MANDRAKEROOT, 1), SmallBodResource(GINSENG, 1) ] ),
    SmallBodRecipe(False, "Lightning", CAT_INSCRIPTION_THIRD_FOURTH, 93, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(MANDRAKEROOT, 1), SmallBodResource(SULPHUROUSASH, 1) ] ),
    SmallBodRecipe(False, "Mana Drain", CAT_INSCRIPTION_THIRD_FOURTH, 100, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BLACKPEARL, 1), SmallBodResource(SPIDERSILK, 1), SmallBodResource(MANDRAKEROOT, 1) ] ),
    SmallBodRecipe(True, "Recall", CAT_INSCRIPTION_THIRD_FOURTH, 107, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BLACKPEARL, 1), SmallBodResource(BLOODMOSS, 1), SmallBodResource(MANDRAKEROOT, 1) ] ),
    
    SmallBodRecipe(True, "Blade Spirits", CAT_INSCRIPTION_FIFTH_SIXTH, 2, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BLACKPEARL, 1), SmallBodResource(NIGHTSHADE, 1), SmallBodResource(MANDRAKEROOT, 1) ] ),
    SmallBodRecipe(True, "Dispel Field", CAT_INSCRIPTION_FIFTH_SIXTH, 9, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BLACKPEARL, 1), SmallBodResource(GARLIC, 1), SmallBodResource(SPIDERSILK, 1), SmallBodResource(SULPHUROUSASH, 1) ] ),
    SmallBodRecipe(False, "Incognito", CAT_INSCRIPTION_FIFTH_SIXTH, 16, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BLOODMOSS, 1), SmallBodResource(GARLIC, 1), SmallBodResource(NIGHTSHADE, 1) ] ),
    SmallBodRecipe(True, "Magic Reflection", CAT_INSCRIPTION_FIFTH_SIXTH, 23, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(GARLIC, 1), SmallBodResource(MANDRAKEROOT, 1), SmallBodResource(SPIDERSILK, 1) ] ),
    SmallBodRecipe(False, "Mind Blast", CAT_INSCRIPTION_FIFTH_SIXTH, 30, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BLACKPEARL, 1), SmallBodResource(MANDRAKEROOT, 1), SmallBodResource(NIGHTSHADE, 1), SmallBodResource(SULPHUROUSASH, 1) ] ),
    SmallBodRecipe(True, "Paralyze", CAT_INSCRIPTION_FIFTH_SIXTH, 37, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(GARLIC, 1), SmallBodResource(MANDRAKEROOT, 1), SmallBodResource(SPIDERSILK, 1) ] ),
    SmallBodRecipe(False, "Poison Field", CAT_INSCRIPTION_FIFTH_SIXTH, 44, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BLACKPEARL, 1), SmallBodResource(NIGHTSHADE, 1), SmallBodResource(SPIDERSILK, 1) ] ),
    SmallBodRecipe(True, "Summon Creature", CAT_INSCRIPTION_FIFTH_SIXTH, 51, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BLOODMOSS, 1), SmallBodResource(MANDRAKEROOT, 1), SmallBodResource(SPIDERSILK, 1) ] ),
    SmallBodRecipe(False, "Dispel", CAT_INSCRIPTION_FIFTH_SIXTH, 58, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(GARLIC, 1), SmallBodResource(MANDRAKEROOT, 1), SmallBodResource(SULPHUROUSASH, 1) ] ),
    SmallBodRecipe(False, "Energy Bolt", CAT_INSCRIPTION_FIFTH_SIXTH, 65, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BLACKPEARL, 1), SmallBodResource(NIGHTSHADE, 1) ] ),
    SmallBodRecipe(False, "Explosion", CAT_INSCRIPTION_FIFTH_SIXTH, 72, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BLOODMOSS, 1), SmallBodResource(MANDRAKEROOT, 1) ] ),
    SmallBodRecipe(False, "Invisibility", CAT_INSCRIPTION_FIFTH_SIXTH, 79, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BLOODMOSS, 1), SmallBodResource(NIGHTSHADE, 1) ] ),
    SmallBodRecipe(False, "Mark", CAT_INSCRIPTION_FIFTH_SIXTH, 86, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BLOODMOSS, 1), SmallBodResource(BLACKPEARL, 1), SmallBodResource(MANDRAKEROOT, 1) ] ),
    SmallBodRecipe(False, "Mass Curse", CAT_INSCRIPTION_FIFTH_SIXTH, 93, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(GARLIC, 1), SmallBodResource(MANDRAKEROOT, 1), SmallBodResource(NIGHTSHADE, 1), SmallBodResource(SULPHUROUSASH, 1) ] ),
    SmallBodRecipe(False, "Paralyze Field", CAT_INSCRIPTION_FIFTH_SIXTH, 100, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BLACKPEARL, 1), SmallBodResource(GINSENG, 1), SmallBodResource(SPIDERSILK, 1) ] ),
    SmallBodRecipe(False, "Reveal", CAT_INSCRIPTION_FIFTH_SIXTH, 107, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BLOODMOSS, 1), SmallBodResource(SULPHUROUSASH, 1) ] ),
    
    SmallBodRecipe(True, "Chain Lightning", CAT_INSCRIPTION_SEVENTH_EIGTH, 2, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BLACKPEARL, 1), SmallBodResource(BLOODMOSS, 1), SmallBodResource(MANDRAKEROOT, 1), SmallBodResource(SULPHUROUSASH, 1) ] ),
    SmallBodRecipe(False, "Energy Field", CAT_INSCRIPTION_SEVENTH_EIGTH, 9, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BLACKPEARL, 1), SmallBodResource(MANDRAKEROOT, 1), SmallBodResource(SPIDERSILK, 1), SmallBodResource(SULPHUROUSASH, 1) ] ),
    SmallBodRecipe(True, "Flamestrike", CAT_INSCRIPTION_SEVENTH_EIGTH, 16, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(SPIDERSILK, 1), SmallBodResource(SULPHUROUSASH, 1) ] ),
    SmallBodRecipe(False, "Gate Travel", CAT_INSCRIPTION_SEVENTH_EIGTH, 23, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BLACKPEARL, 1), SmallBodResource(MANDRAKEROOT, 1), SmallBodResource(SULPHUROUSASH, 1) ] ),
    SmallBodRecipe(True, "Mana Vampire", CAT_INSCRIPTION_SEVENTH_EIGTH, 30, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BLACKPEARL, 1), SmallBodResource(BLOODMOSS, 1), SmallBodResource(MANDRAKEROOT, 1), SmallBodResource(SPIDERSILK, 1) ] ),
    SmallBodRecipe(False, "Mass Dispel", CAT_INSCRIPTION_SEVENTH_EIGTH, 37, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BLACKPEARL, 1), SmallBodResource(GARLIC, 1), SmallBodResource(MANDRAKEROOT, 1), SmallBodResource(SULPHUROUSASH, 1) ] ),
    SmallBodRecipe(True, "Meteor Swarm", CAT_INSCRIPTION_SEVENTH_EIGTH, 44, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BLOODMOSS, 1), SmallBodResource(MANDRAKEROOT, 1), SmallBodResource(SULPHUROUSASH, 1), SmallBodResource(SPIDERSILK, 1) ] ),
    SmallBodRecipe(True, "Polymorph", CAT_INSCRIPTION_SEVENTH_EIGTH, 51, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BLOODMOSS, 1), SmallBodResource(MANDRAKEROOT, 1), SmallBodResource(SPIDERSILK, 1) ] ),
    SmallBodRecipe(False, "Earthquake", CAT_INSCRIPTION_SEVENTH_EIGTH, 58, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BLOODMOSS, 1), SmallBodResource(MANDRAKEROOT, 1), SmallBodResource(GINSENG, 1), SmallBodResource(SULPHUROUSASH, 1) ] ),
    SmallBodRecipe(False, "Energy Vortex", CAT_INSCRIPTION_SEVENTH_EIGTH, 65, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BLACKPEARL, 1), SmallBodResource(BLOODMOSS, 1), SmallBodResource(MANDRAKEROOT, 1), SmallBodResource(NIGHTSHADE, 1) ] ),
    SmallBodRecipe(False, "Resurrection", CAT_INSCRIPTION_SEVENTH_EIGTH, 72, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BLOODMOSS, 1), SmallBodResource(GARLIC, 1), SmallBodResource(GINSENG, 1) ] ),
    SmallBodRecipe(True, "Summon Air Elemental", CAT_INSCRIPTION_SEVENTH_EIGTH, 79, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BLOODMOSS, 1), SmallBodResource(MANDRAKEROOT, 1), SmallBodResource(SPIDERSILK, 1) ] ),
    SmallBodRecipe(True, "Summon Daemon", CAT_INSCRIPTION_SEVENTH_EIGTH, 86, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BLOODMOSS, 1), SmallBodResource(MANDRAKEROOT, 1), SmallBodResource(SPIDERSILK, 1), SmallBodResource(SULPHUROUSASH, 1) ] ),
    SmallBodRecipe(True, "Summon Earth Elemental", CAT_INSCRIPTION_SEVENTH_EIGTH, 93, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BLOODMOSS, 1), SmallBodResource(MANDRAKEROOT, 1), SmallBodResource(SPIDERSILK, 1) ] ),
    SmallBodRecipe(True, "Summon Fire Elemental", CAT_INSCRIPTION_SEVENTH_EIGTH, 100, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BLOODMOSS, 1), SmallBodResource(MANDRAKEROOT, 1), SmallBodResource(SPIDERSILK, 1), SmallBodResource(SULPHUROUSASH, 1) ] ),
    SmallBodRecipe(True, "Summon Water Elemental", CAT_INSCRIPTION_SEVENTH_EIGTH, 107, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BLOODMOSS, 1), SmallBodResource(MANDRAKEROOT, 1), SmallBodResource(SPIDERSILK, 1) ] ),
    
    SmallBodRecipe(True, "animate dead", CAT_INSCRIPTION_NECRO, 2, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(GRAVEDUST, 1), SmallBodResource(DAEMONBLOOD, 1) ] ),
    SmallBodRecipe(True, "blood oath", CAT_INSCRIPTION_NECRO, 9, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(DAEMONBLOOD, 1) ] ),
    SmallBodRecipe(True, "corpse skin", CAT_INSCRIPTION_NECRO, 16, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BATWING, 1), SmallBodResource(GRAVEDUST, 1) ] ),
    SmallBodRecipe(True, "curse weapon", CAT_INSCRIPTION_NECRO, 23, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(PIGIRON, 1) ] ),
    SmallBodRecipe(True, "evil omen", CAT_INSCRIPTION_NECRO, 30, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BATWING, 1), SmallBodResource(NOXCRYSTAL, 1) ] ),
    SmallBodRecipe(True, "horrific beast", CAT_INSCRIPTION_NECRO, 37, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BATWING, 1), SmallBodResource(DAEMONBLOOD, 3) ] ),
    SmallBodRecipe(False, "lich form", CAT_INSCRIPTION_NECRO, 44, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(GRAVEDUST, 1), SmallBodResource(DAEMONBLOOD, 3), SmallBodResource(NOXCRYSTAL, 3) ] ),
    SmallBodRecipe(True, "mind rot", CAT_INSCRIPTION_NECRO, 51, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BATWING, 1), SmallBodResource(DAEMONBLOOD, 1), SmallBodResource(PIGIRON, 1) ] ),
    SmallBodRecipe(True, "pain spike", CAT_INSCRIPTION_NECRO, 58, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(GRAVEDUST, 1), SmallBodResource(PIGIRON, 1) ] ),
    SmallBodRecipe(True, "poison strike", CAT_INSCRIPTION_NECRO, 65, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(NOXCRYSTAL, 1) ] ),
    SmallBodRecipe(True, "strangle", CAT_INSCRIPTION_NECRO, 72, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(DAEMONBLOOD, 1), SmallBodResource(NOXCRYSTAL, 1) ] ),
    SmallBodRecipe(True, "summon familiar", CAT_INSCRIPTION_NECRO, 79, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BATWING, 1), SmallBodResource(GRAVEDUST, 1), SmallBodResource(DAEMONBLOOD, 1) ] ),
    SmallBodRecipe(False, "vampiric embrace", CAT_INSCRIPTION_NECRO, 86, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BATWING, 1), SmallBodResource(NOXCRYSTAL, 1), SmallBodResource(PIGIRON, 1) ] ),
    SmallBodRecipe(False, "vengeful spirit", CAT_INSCRIPTION_NECRO, 93, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(BATWING, 1), SmallBodResource(GRAVEDUST, 1), SmallBodResource(PIGIRON, 1) ] ),
    SmallBodRecipe(True, "wither", CAT_INSCRIPTION_NECRO, 100, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(GRAVEDUST, 1), SmallBodResource(NOXCRYSTAL, 1), SmallBodResource(PIGIRON, 1) ] ),
    SmallBodRecipe(False, "wraith form", CAT_INSCRIPTION_NECRO, 107, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 1), SmallBodResource(NOXCRYSTAL, 1), SmallBodResource(PIGIRON, 1) ] ),
    
    SmallBodRecipe(True, "Runebook", CAT_INSCRIPTION_OTHER, 16, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 8), SmallBodResource(UNMARKED_RUNE, 1), SmallBodResource(RECALL_SCROLL, 1), SmallBodResource(GATE_SCROLL, 1) ] ),
    SmallBodRecipe(True, "Spellbook", CAT_INSCRIPTION_OTHER, 30, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 10) ] ),
    SmallBodRecipe(True, "Necromancer Spellbook", CAT_INSCRIPTION_OTHER, 58, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 10) ] ),
    SmallBodRecipe(True, "Runic Atlas", CAT_INSCRIPTION_OTHER, 107, INSCRIPTION_TOOL_STATIC_ID, [SmallBodResource(BLANK_SCROLL, 24), SmallBodResource(UNMARKED_RUNE, 3), SmallBodResource(RECALL_SCROLL, 3), SmallBodResource(GATE_SCROLL, 3) ] ),
    
    ############################ Carpentry ############################
    
    SmallBodRecipe(False, "barrel staves", CAT_CARPENTRY_OTHER, 2, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(False, "barrel lid", CAT_CARPENTRY_OTHER, 9, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    
    SmallBodRecipe(False, "foot stool", CAT_CARPENTRY_FURNITURE, 2, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(False, "stool", CAT_CARPENTRY_FURNITURE, 9, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(False, "straw chair", CAT_CARPENTRY_FURNITURE, 16, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(False, "wooden chair", CAT_CARPENTRY_FURNITURE, 23, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(True, "wooden bench", CAT_CARPENTRY_FURNITURE, 44, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(True, "Wooden Throne", CAT_CARPENTRY_FURNITURE, 51, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(False, "smal table", CAT_CARPENTRY_FURNITURE, 65, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(False, "large table", CAT_CARPENTRY_FURNITURE, 86, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    
    SmallBodRecipe(True, "wooden box", CAT_CARPENTRY_CONTAINERS, 2, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(False, "Small Crate", CAT_CARPENTRY_CONTAINERS, 9, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(False, "Medium Crate", CAT_CARPENTRY_CONTAINERS, 16, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(False, "Large Crate", CAT_CARPENTRY_CONTAINERS, 23, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(False, "wooden chest", CAT_CARPENTRY_CONTAINERS, 30, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(True, "wooden shel", CAT_CARPENTRY_CONTAINERS, 37, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(False, "armoire", CAT_CARPENTRY_CONTAINERS, 51, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(True, "plain wooden chest", CAT_CARPENTRY_CONTAINERS, 58, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(True, "ornate wooden chest", CAT_CARPENTRY_CONTAINERS, 65, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(True, "gilded wooden chest", CAT_CARPENTRY_CONTAINERS, 72, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(True, "wooden footlocker", CAT_CARPENTRY_CONTAINERS, 79, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(True, "finished wooden chest", CAT_CARPENTRY_CONTAINERS, 86, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(True,"tall cabinet", CAT_CARPENTRY_CONTAINERS, 93, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(True,"short cabinet", CAT_CARPENTRY_CONTAINERS, 100, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(True,"red armoire", CAT_CARPENTRY_CONTAINERS, 107, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID, 40)] ),
    SmallBodRecipe(True,"elegant armoire", CAT_CARPENTRY_CONTAINERS, 114, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(True,"maple armoire", CAT_CARPENTRY_CONTAINERS, 121, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(True,"cherry armoire", CAT_CARPENTRY_CONTAINERS, 128, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    
    SmallBodRecipe(True, "shepherd's crook", CAT_CARPENTRY_WEAPONS, 2, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ), #'
    SmallBodRecipe(True, "quarter sta", CAT_CARPENTRY_WEAPONS, 9, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(True, "gnarled sta", CAT_CARPENTRY_WEAPONS, 16, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(True, "bokuto", CAT_CARPENTRY_WEAPONS, 23, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(True, "tetsubo", CAT_CARPENTRY_WEAPONS, 37, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(True, "wild sta", CAT_CARPENTRY_WEAPONS, 44, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(True, "arcanist's wild sta", CAT_CARPENTRY_WEAPONS, 58, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID), SmallBodResource(WHITE_PEARL, 1)] ), # "
    SmallBodRecipe(True, "ancient wild sta", CAT_CARPENTRY_WEAPONS, 65, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID), SmallBodResource(PERFECT_EMERALD, 1) ] ),
    SmallBodRecipe(True, "thorned wild sta", CAT_CARPENTRY_WEAPONS, 72, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID), SmallBodResource(FIRE_RUBY, 1) ] ),
    SmallBodRecipe(True, "hardened wild sta", CAT_CARPENTRY_WEAPONS, 79, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID), SmallBodResource(TURQUOISE, 1) ] ),
    
    SmallBodRecipe(True, "lap harp", CAT_CARPENTRY_INSTRUMENTS, 2, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID, 20), SmallBodResource(CLOTH_STATIC_ID, 10) ] ),
    SmallBodRecipe(True, "standing harp", CAT_CARPENTRY_INSTRUMENTS, 9, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID, 35), SmallBodResource(CLOTH_STATIC_ID, 15) ] ),
    SmallBodRecipe(True, "drum", CAT_CARPENTRY_INSTRUMENTS, 16, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID, 20), SmallBodResource(CLOTH_STATIC_ID, 10)] ),
    SmallBodRecipe(True, "lute", CAT_CARPENTRY_INSTRUMENTS, 23, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID, 25), SmallBodResource(CLOTH_STATIC_ID, 10) ] ),
    
    ############################ Blacksmith ############################
    
    # Metal Armor
    SmallBodRecipe(True, "ringmail gloves", CAT_BLACKSMITHY_METAL_ARMOR, 2, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(True, "ringmail leggings", CAT_BLACKSMITHY_METAL_ARMOR, 9, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(True, "ringmail sleeves", CAT_BLACKSMITHY_METAL_ARMOR, 16, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(True, "ringmail tunic", CAT_BLACKSMITHY_METAL_ARMOR, 23, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(True, "chainmail coi", CAT_BLACKSMITHY_METAL_ARMOR, 30, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(True, "chainmail leggings", CAT_BLACKSMITHY_METAL_ARMOR, 37, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(True, "chainmail tunic", CAT_BLACKSMITHY_METAL_ARMOR, 44, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(True, "platemail arms", CAT_BLACKSMITHY_METAL_ARMOR, 51, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(True, "platemail gloves", CAT_BLACKSMITHY_METAL_ARMOR, 58, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(True, "platemail gorget", CAT_BLACKSMITHY_METAL_ARMOR, 65, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(True, "platemail legs", CAT_BLACKSMITHY_METAL_ARMOR, 72, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(True, "platemail tunic", CAT_BLACKSMITHY_METAL_ARMOR, 79, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "female plate", CAT_BLACKSMITHY_METAL_ARMOR, 86, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    
    # Helmets
    SmallBodRecipe(False, "bascinet", CAT_BLACKSMITHY_HELMETS, 2, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "close helmet", CAT_BLACKSMITHY_HELMETS, 9, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "helmet", CAT_BLACKSMITHY_HELMETS, 16, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "norse helm", CAT_BLACKSMITHY_HELMETS, 23, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(True, "plate helm", CAT_BLACKSMITHY_HELMETS, 30, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    
    # Shields
    SmallBodRecipe(False, "buckler", CAT_BLACKSMITHY_SHIELDS, 2, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "bronze shield", CAT_BLACKSMITHY_SHIELDS, 9, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "heater shield", CAT_BLACKSMITHY_SHIELDS, 16, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "metal shield", CAT_BLACKSMITHY_SHIELDS, 23, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "metal kite shield", CAT_BLACKSMITHY_SHIELDS, 30, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "tear kite shield", CAT_BLACKSMITHY_SHIELDS, 37, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "chaos shield", CAT_BLACKSMITHY_SHIELDS, 44, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "order shield", CAT_BLACKSMITHY_SHIELDS, 51, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "small plate shield", CAT_BLACKSMITHY_SHIELDS, 58, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "large plate shield", CAT_BLACKSMITHY_SHIELDS, 72, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "medium plate shield", CAT_BLACKSMITHY_SHIELDS, 79, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    
    # Bladed
    SmallBodRecipe(True, "broadsword", CAT_BLACKSMITHY_BLADED, 9, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(True, "cutlass", CAT_BLACKSMITHY_BLADED, 23, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(True, "dagger", CAT_BLACKSMITHY_BLADED, 30, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(True, "katana", CAT_BLACKSMITHY_BLADED, 37, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(True, "kryss", CAT_BLACKSMITHY_BLADED, 44, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(True, "longsword", CAT_BLACKSMITHY_BLADED, 51, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(True, "scimitar", CAT_BLACKSMITHY_BLADED, 58, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(True, "viking sword", CAT_BLACKSMITHY_BLADED, 65, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    
    # Axes
    SmallBodRecipe(True, "axe", CAT_BLACKSMITHY_AXES, 2, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(True, "battle axe", CAT_BLACKSMITHY_AXES, 9, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(True, "double axe", CAT_BLACKSMITHY_AXES, 16, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(True, "executioner's axe", CAT_BLACKSMITHY_AXES, 23, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ), #'
    SmallBodRecipe(True, "large battle axe", CAT_BLACKSMITHY_AXES, 30, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(True, "two handed axe", CAT_BLACKSMITHY_AXES, 37, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(True, "war axe", CAT_BLACKSMITHY_AXES, 44, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ), # This one says its in maces on official uo site
    
    # Polearms
    SmallBodRecipe(True, "bardiche", CAT_BLACKSMITHY_POLEARMS, 2, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "bladed sta", CAT_BLACKSMITHY_POLEARMS, 9, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "double bladed sta", CAT_BLACKSMITHY_POLEARMS, 16, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(True, "halberd", CAT_BLACKSMITHY_POLEARMS, 23, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "lance", CAT_BLACKSMITHY_POLEARMS, 30, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "pike", CAT_BLACKSMITHY_POLEARMS, 37, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(True, "short spear", CAT_BLACKSMITHY_POLEARMS, 44, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "scythe", CAT_BLACKSMITHY_POLEARMS, 51, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(True, "spear", CAT_BLACKSMITHY_POLEARMS, 58, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(True, "war fork", CAT_BLACKSMITHY_POLEARMS, 65, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    
    # Bashing
    SmallBodRecipe(True, "hammer pick", CAT_BLACKSMITHY_BASHING, 2, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(True, "mace", CAT_BLACKSMITHY_BASHING, 9, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(True, "maul", CAT_BLACKSMITHY_BASHING, 16, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(False, "scepter", CAT_BLACKSMITHY_BASHING, 23, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(True, "war mace", CAT_BLACKSMITHY_BASHING, 30, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
    SmallBodRecipe(True, "war hammer", CAT_BLACKSMITHY_BASHING, 37, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
]

# Item property Number for important props within a bod item in game
PROD_ID_LARGE_BULK_ORDER = 1060655
PROP_ID_SMALL_BULK_ORDER = 1060654 
PROP_ID_AMOUNT_TO_MAKE = 1060656
PROP_ID_BOD_EXCEPTIONAL = 1045141
PROP_ID_ITEM_TEXT = 1060658

# GUMPS
CRAFTING_GUMP_ID = 0x38920abd
SMALL_BOD_GUMP_ID = 0x5afbd742
LARGE_BOD_GUMP_ID = 0xa125b54a

# This goes prop.Number -> { gump button id, special resource hue, item name }
# ServUO\Scripts\Services\BulkOrders\SmallBODs\SmallBODGump.cs
# Tried doing a regex by special material name, e.g. All items must be made
# with Dull Copper Ingots, but it didnt follow that convetion for carpenty.
# It just said "Oak". So, I got mad and just did an exact match for the 
# Propert.Number. Whatever.
SPECIAL_PROP_MATERIAL_MAP = {
    1045142: { "button": 13, "hue": RESOURCE_HUE_DULL_COPPER,   "name": "dull copper" },    # Dull Copper
    1045143: { "button": 20, "hue": RESOURCE_HUE_SHADOW_IRON,   "name": "shadow iron" },    # Shadow Iron
    1045144: { "button": 27, "hue": RESOURCE_HUE_COPPER,        "name": "copper" },         # Copper
    1045145: { "button": 34, "hue": RESOURCE_HUE_BRONZE,        "name": "bronze" },         # Bronze
    1045146: { "button": 41, "hue": RESOURCE_HUE_GOLD,          "name": "golden" },           # Gold
    1045147: { "button": 48, "hue": RESOURCE_HUE_AGAPITE,       "name": "agapite" },        # Agapite
    1045148: { "button": 55, "hue": RESOURCE_HUE_VERITE,        "name": "verite" },         # Verite
    1045149: { "button": 62, "hue": RESOURCE_HUE_VALORITE,      "name": "valorite" },       # Valorite
    1049348: { "button": 13, "hue": RESOURCE_HUE_SPINED,        "name": "spined" },         # Spined
    1049349: { "button": 20, "hue": RESOURCE_HUE_HORNED,        "name": "horned" },         # Horned
    1049350: { "button": 27, "hue": RESOURCE_HUE_BARBED,        "name": "barbed" },         # Barbed
    1071428: { "button": 13, "hue": RESOURCE_HUE_OAK,           "name": "oak" },             # Oak
    1071429: { "button": 20, "hue": RESOURCE_HUE_ASH,           "name": "ash"},             # Ash
    1071430: { "button": 27, "hue": RESOURCE_HUE_YEW,           "name": "yew" },             # Yew
    1071432: { "button": 34, "hue": RESOURCE_HUE_HEARTWOOD,     "name": "heartwood" },       # Heartwood
    1071431: { "button": 41, "hue": RESOURCE_HUE_BLOODWOOD,     "name": "bloodwood" },       # Bloodwood
    1071433: { "button": 48, "hue": RESOURCE_HUE_FROSTWOOD,     "name": "frostwood" },       # Frostwood
}
    
# Internal: Helper method to generate a small bod data structure.
def parse_small_bod(bod, recipes, alertMissingRecipe = False):
    isExceptional = False
    amountToMake = 0
    amountMade = 0
    recipe = None
    isSmallBod = False
    specialMaterialButton = 6 if bod.Color in [HUE_BLACKSMITHY, HUE_TAILORING, HUE_CARPENTRY, HUE_TINKERING] else 0
    specialMaterialHue = RESOURCE_HUE_DEFAULT
    specialMaterialPropId = None
    specialMaterialName = None
    for prop in bod.Properties:
        if prop.Number == PROP_ID_SMALL_BULK_ORDER:
            isSmallBod = True
        if prop.Number == PROP_ID_BOD_EXCEPTIONAL:
            isExceptional = True
        if prop.Number == PROP_ID_AMOUNT_TO_MAKE:
            amountToMake = int(prop.Args)
        if prop.Number in SPECIAL_PROP_MATERIAL_MAP:
            specialMaterialPropId = prop.Number
            specialMaterialButton = SPECIAL_PROP_MATERIAL_MAP[prop.Number]["button"]
            specialMaterialHue = SPECIAL_PROP_MATERIAL_MAP[prop.Number]["hue"]
            specialMaterialName = SPECIAL_PROP_MATERIAL_MAP[prop.Number]["name"]
        if prop.Number == PROP_ID_ITEM_TEXT:
            propList = prop.ToString().split(": ")
            recipeName = propList[0].strip() # buckler looks like "buckler : <amount>" instead of "buckler: <amount>"
            amountMade = int(propList[1])
            if recipeName in recipes:
                recipe = recipes[recipeName]
                
    if recipe is not None and isSmallBod:
        return SmallBod(bod.Serial, amountMade, isExceptional, amountToMake, specialMaterialButton, specialMaterialHue, specialMaterialPropId, specialMaterialName, recipe)
    elif isSmallBod == True and alertMissingRecipe:
        print("Warning: Skipping because not in recipe list")
        for prop in bod.Properties:
            print("\t", prop.ToString(), "(", prop.Number, ")")

# Internal: Build a data structure to check progress and get dependencies of large bod
def parse_large_bod(bod):
    isLargeBod = False
    smallBodItems = []
    specialMaterialPropId = None
    isExceptional = False
    amountToMake = 0
    for prop in bod.Properties:
        if prop.Number == PROD_ID_LARGE_BULK_ORDER:
            isLargeBod = True
        if prop.Number == PROP_ID_BOD_EXCEPTIONAL:
            isExceptional = True
        if prop.Number == PROP_ID_AMOUNT_TO_MAKE:
            amountToMake = int(prop.Args)
        if prop.Number in SPECIAL_PROP_MATERIAL_MAP:
            specialMaterialPropId = prop.Number
        if prop.Number in range(PROP_ID_ITEM_TEXT, PROP_ID_ITEM_TEXT + 6):    
            propList = prop.ToString().split(": ")
            recipeName = propList[0].strip() # buckler looks like "buckler : <amount>" instead of "buckler: <amount>"
            amountMade = int(propList[1])
            smallBodItems.append({ "name": recipeName, "amountMade": amountMade })
    if isLargeBod:
        return LargeBod(bod.Serial, isExceptional, amountToMake, specialMaterialPropId, smallBodItems)

# Helper method to get a tool from the toolContainer. You dont need to worry about this.  
# Also puts away unused tools.
def get_tool(craftContainer, toolId, toolContainer, itemMoveDelayMs):
    tool = Items.FindByID(toolId, RESOURCE_HUE_DEFAULT, craftContainer, -1)
    if tool is None:
        tool = Items.FindByID(toolId, RESOURCE_HUE_DEFAULT, toolContainer, -1)
        if tool is not None:
            Items.Move(tool, craftContainer, 1)
            Misc.Pause(itemMoveDelayMs)
            
    for toolId in [BLACKSMITHY_TOOL_STATIC_ID, TINKERING_TOOL_STATIC_ID, ALCHEMY_TOOL_STATIC_ID, TAILORING_TOOL_STATIC_ID, CARPENTRY_TOOL_STATIC_ID, INSCRIPTION_TOOL_STATIC_ID]:
        toolsToPutAway = Items.FindAllByID(toolId, -1, craftContainer, 0)
        for toolToPutAway in toolsToPutAway:
            if tool is None or tool.Serial != toolToPutAway.Serial:
                Items.Move(toolToPutAway, toolContainer, 1)
                Misc.Pause(itemMoveDelayMs)
                
    return tool
    
# Helper method to get resources from the resourceContainer. Ignore me.
#def check_resources(craftContainer, smallBod, resourceContainer, itemMoveDelayMs):
def check_resources(craftContainer, smallBodResources, resourceContainer, itemMoveDelayMs, specialMaterialHue = None):
    itemsToMove = []
    for resource in smallBodResources:
        hue = specialMaterialHue if resource.canOverrideHue() and specialMaterialHue is not None else RESOURCE_HUE_DEFAULT    
        items = Items.FindAllByID(resource.resourceId, hue, craftContainer, 0)
        amountBackpack = sum(item.Amount for item in items)
        
        if amountBackpack > resource.amount:
            continue
            
        amountNeeded = max(0, resource.getOptimizedAmout() - amountBackpack)
        
        items = Items.FindAllByID(resource.resourceId, hue, resourceContainer, -1)
        for item in items:
            if amountNeeded == 0:
                break
        
            amountRequested = item.Amount if item.Amount <= amountNeeded else amountNeeded
            itemsToMove.append({ "Serial": item.Serial, "Amount": amountRequested })
            amountNeeded = max(0, amountNeeded - amountRequested)                

        if amountNeeded > 0:
            return False
        
    # Only move resources if we have enough (did not return early above)
    for itemToMove in itemsToMove:
        Items.Move(itemToMove["Serial"], craftContainer, itemToMove["Amount"])
        Misc.Pause(itemMoveDelayMs)

    return True
    
# Internal: Helper method to salvage stuff.
def cleanup(craftContainer, salvageBag, trashContainer, resourceContainer, itemMoveDelayMs, smallBod = None):
    if smallBod is not None:
        if salvageBag is not None and smallBod.recipe.canSalvage():
            found = False        
            while True:
                item = Items.FindByName(smallBod.getCraftedItemName(), smallBod.specialMaterialHue, craftContainer, 0)
                if item is None:
                    break
                found = True
                Items.Move(item, salvageBag, item.Amount)
                Misc.Pause(itemMoveDelayMs)

            if found:
                Misc.WaitForContext(salvageBag, 10000)
                Misc.ContextReply(salvageBag, 2)   
                Misc.Pause(1000)
        elif trashContainer is not None:
            while True:
                item = Items.FindByName(smallBod.getCraftedItemName(), smallBod.specialMaterialHue, craftContainer, 0)
                if item is None:
                    break
                Items.Move(item, trashContainer, item.Amount)
                Misc.Pause(itemMoveDelayMs)
            
    ALL_RESOURCES = [INGOT_STATIC_ID, BOARD_STATIC_ID, CLOTH_STATIC_ID, LEATHER_STATIC_ID, MANDRAKEROOT, BLOODMOSS, SULPHUROUSASH, NIGHTSHADE, BLACKPEARL, SPIDERSILK, GINSENG, GARLIC, PIGIRON, BATWING, NOXCRYSTAL, DAEMONBLOOD, GRAVEDUST, EMPTY_BOTTLE_STATIC_ID, BONE, UNMARKED_RUNE, GATE_SCROLL, RECALL_SCROLL, BLANK_SCROLL, PARASITIC_PLANT, LUMINESCENT_FUNGI, WHITE_PEARL, FIRE_RUBY, PERFECT_EMERALD, TURQUOISE, STAR_SAPPHIRE, CITRINE, TURQUOISE, DIAMOND, AMBER, AMETHYST, SAPPHIRE, RUBY, EMERALD, TOURMALINE ]

    # Cleanup nonessentials, move to resource crate. If a smallBod is present, dont clean up the resources we are workign with
    for resourceId in ALL_RESOURCES:
        items = Items.FindAllByID(resourceId, -1, craftContainer, 0)
        for item in items:
            keep = False
            if smallBod is not None:
                for resource in smallBod.recipe.resources:
                    hue = smallBod.specialMaterialHue if resource.canOverrideHue() and smallBod.specialMaterialHue is not None else RESOURCE_HUE_DEFAULT    
                    if item.ItemID == resource.resourceId and item.Color == hue:
                        keep = True
                        break
            if not keep:
                Items.Move(item, resourceContainer, item.Amount)    
                Misc.Pause(itemMoveDelayMs)        
    
# Internal: Build database of small bods using recipeName (not craftedItemName as PK)
# Data is structed as:
# "kryss": [ {SmallBod, SmallBod, ... ],
# "cutlass": [ SmallBod, SmallBod, ... ],
def build_complete_small_bod_db(smallBodWaitingForLargeBodContainers, recipes):
    db = {}
    itemsInDb = 0
    for smallBodWaitingForLargeBodContainer in smallBodWaitingForLargeBodContainers:
        bods = Items.FindAllByID(BOD_STATIC_ID, -1, smallBodWaitingForLargeBodContainer, 1)
        for bod in bods:
            smallBod = parse_small_bod(bod, recipes)
            if smallBod is not None and smallBod.isComplete():
                smallBod.getNameInLargeBod()
                if smallBod.getNameInLargeBod() not in db:
                    db[smallBod.getNameInLargeBod()] = []
                db[smallBod.getNameInLargeBod()].append(smallBod)
                
                #if smallBod.recipe.recipeName not in db:
                #    db[smallBod.recipe.recipeName] = []
                #db[smallBod.recipe.recipeName].append(smallBod)
                itemsInDb = itemsInDb + 1    
                    
    print("Database built with {} complete small bods".format(itemsInDb))
    return db

# Internal: Search our DB for a completed small bod
def search_complete_small_bod_db(db, largeBod, fillNormalLargeBodsWithExceptionalSmallBods):
    entries = []
    for smallBodItem in largeBod.smallBodItems:
        if smallBodItem["amountMade"] == largeBod.amountToMake:
            continue
        if smallBodItem["name"] in db:
            index = 0
            found = False
            for smallBod in db[smallBodItem["name"]]:
                if fillNormalLargeBodsWithExceptionalSmallBods and (largeBod.isExceptional == False or smallBod.isExceptional == largeBod.isExceptional) and smallBod.amountMade == largeBod.amountToMake and smallBod.specialMaterialPropId == largeBod.specialMaterialPropId:                    
                    entries.append(smallBod)
                    found = True
                    break
                if smallBod.isExceptional == largeBod.isExceptional and smallBod.amountMade == largeBod.amountToMake and smallBod.specialMaterialPropId == largeBod.specialMaterialPropId:                    
                    entries.append(smallBod)
                    found = True
                    break
                index = index + 1
            if found:
                del db[smallBodItem["name"]][index]
    return entries

# Internal: Helper that summarizes final state of bods
def report_final_metrics(reports, recipes, incompleteBodContainers, smallBodWaitingForLargeBodContainers, completeSmallBodContainer, completeLargeBodContainer):
    for incompleteBodContainer in incompleteBodContainers:
        bods = Items.FindAllByID(BOD_STATIC_ID, -1, incompleteBodContainer, 1)
        for bod in bods:
            smallBod = parse_small_bod(bod, recipes)
            if smallBod is not None:
                if smallBod.isComplete():
                    reports[bod.Color].incrementNumCompleteSmallBods()
                    reports[bod.Color].incrementNumInWrongContainer()
                    print("Warning: This small bod should not be in the incomplete container! {}".format(smallBod))
                else:
                    reports[bod.Color].incrementNumIncompleteSmallBods()
                continue
            
            largeBod = parse_large_bod(bod)
            if largeBod is not None:
                if largeBod.isComplete():
                    reports[bod.Color].incrementNumCompleteLargeBods()
                    reports[bod.Color].incrementNumInWrongContainer()
                    print("Warning: This large bod should not be in the incomplete container! {}".format(largeBod))
                else:
                    reports[bod.Color].incrementNumIncompleteLargeBods()
                continue

            reports[bod.Color].incrementNumMissingRecipe()
                    
    for smallBodWaitingForLargeBodContainer in smallBodWaitingForLargeBodContainers:
        bods = Items.FindAllByID(BOD_STATIC_ID, -1, smallBodWaitingForLargeBodContainer, 1)
        for bod in bods:
            smallBod = parse_small_bod(bod, recipes)
            if smallBod is not None:
                if smallBod.isComplete() and smallBod.recipe.hasLargeBod:
                    reports[bod.Color].incrementNumCompleteSmallBods()
                else:
                    reports[bod.Color].incrementNumIncompleteSmallBods()
                    reports[bod.Color].incrementNumInWrongContainer()
                    print("Warning: This small bod should not be in the small bod waiting container! {}".format(smallBod))
                continue
            
            largeBod = parse_large_bod(bod)
            if largeBod is not None:
                if largeBod.isComplete():
                    reports[bod.Color].incrementNumCompleteLargeBods()
                    reports[bod.Color].incrementNumInWrongContainer()
                    print("Warning: This large bod should not be in the small bod waiting container! {}".format(largeBod))
                else:
                    reports[bod.Color].incrementNumIncompleteLargeBods()                    
                    reports[bod.Color].incrementNumInWrongContainer()
                    print("Warning: This large bod should not be in the small bod waiting container! {}".format(largeBod))
                continue

            reports[bod.Color].incrementNumMissingRecipe()
            
    bods = Items.FindAllByID(BOD_STATIC_ID, -1, completeSmallBodContainer, 1)
    for bod in bods:
        smallBod = parse_small_bod(bod, recipes)
        if smallBod is not None:
            if smallBod.isComplete() and not smallBod.recipe.hasLargeBod:
                reports[bod.Color].incrementNumCompleteSmallBods()
            else:
                reports[bod.Color].incrementNumIncompleteSmallBods()
                reports[bod.Color].incrementNumInWrongContainer()
                print("Warning: This small bod should not be in the complete small bod container! {}".format(smallBod))
            continue
        
        largeBod = parse_large_bod(bod)
        if largeBod is not None:
            if largeBod.isComplete():
                reports[bod.Color].incrementNumCompleteLargeBods()
                reports[bod.Color].incrementNumInWrongContainer()
                print("Warning: This large bod should not be in the complete small bod container! {}".format(largeBod))
            else:
                reports[bod.Color].incrementNumIncompleteLargeBods()                    
                reports[bod.Color].incrementNumInWrongContainer()
                print("Warning: This large bod should not be in the complete small bod container! {}".format(largeBod))
            continue

        reports[bod.Color].incrementNumMissingRecipe()            
                
    bods = Items.FindAllByID(BOD_STATIC_ID, -1, completeLargeBodContainer, 1)
    for bod in bods:
        smallBod = parse_small_bod(bod, recipes)
        if smallBod is not None:
            if smallBod.isComplete():
                reports[bod.Color].incrementNumCompleteSmallBods()
                reports[bod.Color].incrementNumInWrongContainer()
                print("Warning: This small bod should not be in the complete large bod container! {}".format(smallBod))
            else:
                reports[bod.Color].incrementNumIncompleteSmallBods()
                reports[bod.Color].incrementNumInWrongContainer()
                print("Warning: This small bod should not be in the complete large bod container! {}".format(smallBod))
            continue
        
        largeBod = parse_large_bod(bod)
        if largeBod is not None:
            if largeBod.isComplete():
                reports[bod.Color].incrementNumCompleteLargeBods()
            else:
                reports[bod.Color].incrementNumIncompleteLargeBods()                    
                reports[bod.Color].incrementNumInWrongContainer()                    
                print("Warning: This large bod should not be in the complete large bod container! {}".format(largeBod))
            continue
                            
        reports[bod.Color].incrementNumMissingRecipe()     

    largeBodsReadyForTurnIn = Items.FindBySerial(completeLargeBodContainer).Contains.Count
    smallBodsReadyForTurnIn = Items.FindBySerial(completeSmallBodContainer).Contains.Count
        
    print("\n****************************************** Final Report *****************************************")        
    for k in reports:
        print(reports[k])
    print("\nReady for turn in:\n\n\t* Small:\t{}\n\t* Large:\t{}".format(smallBodsReadyForTurnIn, largeBodsReadyForTurnIn))
        
# Internal: Need this to stort when filling large bods so we complete those with the most progress first.
# Makes a key that matche all bods based on exceptional, material, and type of items needed. Arranges them
# so the ones that have the most number of complete items are first.
def sort_large_bods(incompleteBodContainers):
    largeBods = []
    for incompleteBodContainer in incompleteBodContainers:
        bods = Items.FindAllByID(BOD_STATIC_ID, -1, incompleteBodContainer, 1)
        for bod in bods:
            largeBod = parse_large_bod(bod)
            if largeBod is not None: 
                largeBods.append(largeBod)
    
    largeBods = sorted(largeBods, key = lambda largeBod: (largeBod.getId(), -ord(str(largeBod.numComplete()))))
    return largeBods
                
# Automate bod building (both small and large). You just dump all your bods into the starting
# container and it will sort them, craft items, fill small bods, combine large bods, etc. 
#
# WARNING: IF  YOU SET craftContainer AS YOUR BACKPACK IT YOU RISK LOSING ITEMS.
#
# Quirks:
#   - If you fail to create an alchemy potion, it drops the bottle in your backpack for some reason. 
#
# Requirements:
#   - You need a container to do work in (put a bag in your backpack)
#   - You need a container of resources (ingots, etc.)
#   - You need a container of tools
#   - You need a forge and anvil nearby
#   - You need containers for incomplete (unsorted or not started bods), dump all bods here (large and small)
#   - You need a container for complete small bods (solo)
#   - You need containers for complete small bods (part of larger bods)
#   - You need a container for complete large bods
#
# You just need to specify a few containers, have a resource container fully stocked, 
# have a container of tools, and you are good to go. Supports: Blacksmithing, Tailoring,
# Alchemy, Inscription, Carpentry. Has these features:
#   - auto crafts items
#   - cleans up crafted items that dont meet requirements (non exceptional)
#   - puts completed large bods and solo small bods in containers for easy access and turn-in
#   - If you only want inscription bods to be complete, just put inscription bods in the incompleteBodsContainer.
#   
# General flow:
# 1. Small Bods
#   - selects small bods from incompleBodContainer and craftContainer
#   - filters for only those that match your list of recipes (see recipes param below)
#   - filters for only those bods that have allowed resources (e.g. normal iron ingot bods only)
#   - One craft cycle includes:
#       1. getting resources from resourceContainer
#       2. getting / using tool, setting resource in gump, setting category in gump
#       3. attempting craft
#       4. attempting to add crafted item to small bod
#       5. attempt cleanup: salvage or dump waste into a container (trash bin recommended)
#   - Puts completed small bod in either completeSmallBodContainer or smallBodWaitingForLargeBodContainer
#   - (the above depends on whether this is a solo small bod or is part of a large bod)
#   - Note: Will attempt to meditate if mana is low for inscription
#
# 2. Large Bods
#   - Creates a database of all small bods
#   - Gets large bods from the incompleBodContainer, sorts them by "most complete"
#   - (the above happens so we focus on completion and dont spread too thin)
#   - Looks up small bods in db, transfers to backpack, attempts to combine
#   - If complete, moves to completeLargeBodContainer, otherwise back to incompleBodContainer
#
# Based on:
# https://github.com/matsamilla/Razor-Enhanced/blob/master/NoxBodFiles/Smithbodgod.py
def run_bod_builder(

    # Serial of container to do work in. This container must be placed in your backpack. 
    # Get its serial and fill it in here. You *could* use your backpack, but your risk losing
    # things when combining items into large bods (your spellbook for example when crafting spellbooks). 
    # The script will move all tools, bods, and materials to this container. Crafted items will appear here.
    craftContainer,
    
    # Array of serials for containers to put your bods in to start things off (both small and large).
    # You put your brand new or partially complete bods in here.
    incompleteBodContainers,
    
    # Array of serials for containers to store completed small bods
    # that are part of a large bod. This can take time. So store them here
    # until the can be combined.
    smallBodWaitingForLargeBodContainers,
    
    # Serial of container to put completed SOLO small bods. These
    # are small bods that do not have a corresponding large bod. They are ready
    # for turn-in.
    completeSmallBodContainer,
    
    # Serial of container for completed LBODs. This is where you can pick them
    # up and then go turn them in. 
    completeLargeBodContainer,
    
    # Stash a bunch of tools in here and let it rip. Serial of container.
    toolContainer,
    
    # Serial of regular container / commodity deed box (not a special resource box like insaneuo).
    # Fill this with ingots, reagents, etc. Use the run_restocker() function to help fill it up.
    resourceContainer,
    
    # (Optional) Your salvage bag which is used for tailoring and blacksmithy rejects.
    # You get a little resource refund. I keep mine in my craftContainer. But you will need a pair
    # of scissors and a smiths hammer in the root level of your backpack. This is a salvage bag quirk.
    # Its just how it works. 
    salvageBag = None,
    
    # (Optional) Serial of a container to dump trash in that cant be salvaged. 
    # For non blacksmith/tailoring professions, dumps non-exceptional items here,
    # e.g. if you need exceptional footlockers and only get ordinary ones. Dont need that junk.
    # I think you can use a trash bin. Maybe place on next to you.
    # "I wish to place a trash barrel"
    trashContainer = None,
    
    # (Optional) Array of SmallBodRecipe. If not in this list, the bod will be skipped.
    # Only build bods that want these items. Can be of any profession.
    # Defaults to all the recipes I know about and was willing to implement.
    recipes = RECIPES,
    
    # (Optional) Array of colors that governs whether bods that require special materials are 
    # allowed (e.g. shadow iron, # frostwood, spined leather, etc.). Only this on this list will 
    # be crafted, otherwise those bods will be skipped. By default all special materials are allowed. 
    allowedResourceHues = [RESOURCE_HUE_DEFAULT, RESOURCE_HUE_COPPER, RESOURCE_HUE_SHADOW_IRON, RESOURCE_HUE_DULL_COPPER, RESOURCE_HUE_BRONZE, RESOURCE_HUE_GOLD, RESOURCE_HUE_AGAPITE, RESOURCE_HUE_VERITE, RESOURCE_HUE_VALORITE, RESOURCE_HUE_BARBED, RESOURCE_HUE_SPINED, RESOURCE_HUE_HORNED, RESOURCE_HUE_OAK, RESOURCE_HUE_ASH, RESOURCE_HUE_YEW, RESOURCE_HUE_HEARTWOOD, RESOURCE_HUE_BLOODWOOD, RESOURCE_HUE_FROSTWOOD ],
    
    # (Optional) Flag governs whether an exceptional small bod can be used to fill
    # a normal (non-exceptional) large bod. Its a real hassle trying to match these.
    # Default value is true which means exceptional small bods are incldued. Set to 
    # False to disable this.
    fillNormalLargeBodsWithExceptionalSmallBods = True,
    
    # (Optional)Time to wait between item moves. Adjust with caution. Reducing this will increase speed
    # of the script, but you risk disconnects and other issues maintaining state. Defaults to 1000ms
    itemMoveDelayMs = 1000,
    
    # (Optional) Reducing this will increase speed of script, but Id advise against it. Gump interactions are 
    # catastrophic. God save the queen.
    gumpDelayMs = 1000
):
    print("Opening containers, this may take a moment...")
    # Open containers because we may not have that item data yet. Sorry for the spam,
    # but these containers will show 0 items unless theyre loaded.
    for incompleteBodContainer in incompleteBodContainers:
        Items.UseItem(incompleteBodContainer)
        Misc.Pause(itemMoveDelayMs)
    for smallBodWaitingForLargeBodContainer in smallBodWaitingForLargeBodContainers:
        Items.UseItem(smallBodWaitingForLargeBodContainer)
        Misc.Pause(itemMoveDelayMs)
    Items.UseItem(completeSmallBodContainer)
    Misc.Pause(itemMoveDelayMs)   
    Items.UseItem(completeLargeBodContainer)
    Misc.Pause(itemMoveDelayMs)       
    Items.UseItem(toolContainer)
    Misc.Pause(itemMoveDelayMs)
    Items.UseItem(resourceContainer)
    Misc.Pause(itemMoveDelayMs)    
    Items.UseItem(craftContainer)
    Misc.Pause(itemMoveDelayMs)    
    
    #CRAFTING_GUMP_ID = 0x38920abd
    #SMALL_BOD_GUMP_ID = 0x5afbd742
    #LARGE_BOD_GUMP_ID = 0xa125b54a
    
    # Turn this array into a dictionary keyed on item name. Its just easier that way.
    # So instead of [SmallBodRecipe, SmallBodRecipe...] we get:
    # { "cutlass": SmallBodRecipe, "platemail helm": SmallBodRecipe...
    recipes = {recipes[i].recipeName: recipes[i] for i in range(len(recipes))}
    
    # Just for tracking, can remove this crap.
    reports = {
        HUE_BLACKSMITHY:    BodReport("Blacksmithy"),
        HUE_TAILORING:      BodReport("Tailoring  "),
        HUE_CARPENTRY:      BodReport("Carpentry  "),
        HUE_ALCHEMY:        BodReport("Alchemy    "),
        HUE_INSCRIPTION:    BodReport("Inscription"),
        HUE_TINKERING:      BodReport("Tinkering  ")
    }    
    
    print("============================================================")
    for incompleteBodContainer in [craftContainer] + incompleteBodContainers:
        print("OMG: " , incompleteBodContainer)


    
    print("****************************************** Start Small BOD ******************************************")
    for incompleteBodContainer in [craftContainer] + incompleteBodContainers:
        bods = Items.FindAllByID(BOD_STATIC_ID, -1, incompleteBodContainer, 1)
        for bod in bods:
            craftGumpSet = False
            while True:
                # Get fresh version of bod
                freshBod = Items.FindBySerial(bod.Serial)
                smallBod = parse_small_bod(freshBod, recipes, True)
                
                if smallBod is not None:
                    if smallBod.specialMaterialHue not in allowedResourceHues:
                        print("Warning: Skipping because material is not in allowed list: {}".format(smallBod.getCraftedItemName()))
                        break
                    
                    if smallBod.isComplete():
                        print("Filled small BOD! ", smallBod.getCraftedItemName(), " has large bod? ", smallBod.recipe.hasLargeBod)
                        if smallBod.recipe.hasLargeBod:
                            foundSuitableContainer = False
                            for smallBodWaitingForLargeBodContainer in smallBodWaitingForLargeBodContainers:
                                container = Items.FindBySerial(smallBodWaitingForLargeBodContainer)
                                if container.Contains.Count < 125:
                                    foundSuitableContainer = True
                                    Items.Move(freshBod, smallBodWaitingForLargeBodContainer, 1)
                                    Misc.Pause(itemMoveDelayMs)
                                    break
                            if not foundSuitableContainer:
                                print("ERROR: No more space to put complete small bods! Add more container serials to smallBodWaitingForLargeBodContainers")
                                return
                        else:
                            print("Moving to solo container")
                            Items.Move(freshBod, completeSmallBodContainer, 1)
                            Misc.Pause(itemMoveDelayMs)                
                        break
                    else:
                        
                        foundCraftedItem = False
                        for craftedItem in Items.FindBySerial(craftContainer).Contains:
                            if smallBod.getCraftedItemName().lower() in craftedItem.Name.lower():
                                if smallBod.isExceptional and not any(prop.ToString().lower() == "exceptional" for prop in craftedItem.Properties):
                                    continue
                                    
                                if smallBod.specialMaterialHue != RESOURCE_HUE_DEFAULT and smallBod.specialMaterialHue != craftedItem.Color:
                                    print("This color is different smallbod special material hue: {} crafted item color: {}".format(smallBod.specialMaterialHue, craftedItem.Color))
                                    continue
                                    
                                foundCraftedItem = True
                                
                                # All sorts of drama if crafted items can be stacked. The BOD
                                # will not be able to combine them if they are instacks that are
                                # greater than the number requested. E.g. you need 10 poison potions
                                # but only have a stack of 65... So, we will do our best to separate
                                # large stacks of items (when appropriate) into smaller ones.
                                # Note: Short of storing all the crafted item ids (jesus christ) we can just look up
                                # by item name as best we can. This doesnt work for stacks of potions where the Item
                                # name chages to <stack amount> <item name>. So, we have the for construct below that
                                # checks each item for a substring. There may be misses
                                if craftedItem.Amount > 1:
                                    # Have to provide x, y coordinates inside bag or else it will just stack on itself
                                    # and we will be right back where we started, praise mao.
                                    print("Splitting stack of {} ({})".format(smallBod.getCraftedItemName(), craftedItem.Amount))
                                    Items.Move(craftedItem, craftContainer, 1, craftedItem.Position.X, craftedItem.Position.Y)
                                    # This needs extra time apparently when you split stacks as it generates a new item.
                                    Misc.Pause(itemMoveDelayMs + 1000)
                                    break

                        if foundCraftedItem:
                            # The bod might already be in the craftContainer, but check anyway. We dont really need it for crafting
                            # only above when combining the deed with items. But I like to know which bod Im working on.
                            if freshBod.Container != craftContainer:
                                Items.Move(freshBod, craftContainer, 1)
                                Misc.Pause(itemMoveDelayMs) 
                                
                            # Open small bod gump
                            Items.UseItem(freshBod)
                            Gumps.WaitForGump(SMALL_BOD_GUMP_ID, 10000)
                            Misc.Pause(int(gumpDelayMs/2))#250 before
                            Target.Cancel()
                            
                            # Combine with contained items (craftContainer)
                            Gumps.SendAction(SMALL_BOD_GUMP_ID, 4) 
                            Target.WaitForTarget(10000)
                            Target.TargetExecute(craftContainer)
                            Gumps.WaitForGump(SMALL_BOD_GUMP_ID, 10000)
                            Misc.Pause(gumpDelayMs)#1000 before
                            Target.Cancel()
                            Gumps.CloseGump(SMALL_BOD_GUMP_ID)                        
                            
                        else:
                            print("Bod progress: craftedItemName={}, recipeName={} {}/{}".format(smallBod.getCraftedItemName(), smallBod.recipe.recipeName, smallBod.amountMade, smallBod.amountToMake))
                            
                            cleanup(craftContainer, salvageBag, trashContainer, resourceContainer, itemMoveDelayMs, smallBod)
                            
                            if not check_resources(craftContainer, smallBod.recipe.resources, resourceContainer, itemMoveDelayMs, smallBod.specialMaterialHue):
                            #if not check_resources(craftContainer, smallBod, resourceContainer, itemMoveDelayMs):
                                print("Warning: Out of resources, skipping {}".format(smallBod.getCraftedItemName()))
                                reports[freshBod.Color].incrementNumMissingResources()
                                if freshBod.Container != incompleteBodContainer:
                                    Items.Move(freshBod, incompleteBodContainer, 1)
                                    Misc.Pause(itemMoveDelayMs)
                                break
                            
                            tool = get_tool(craftContainer, smallBod.recipe.toolId, toolContainer, itemMoveDelayMs)
                            if tool is None:
                                print("Error: Cannot find tool")
                                sys.exit()
                                
                            if freshBod.Container != craftContainer:
                                Items.Move(freshBod, craftContainer, 1)
                                Misc.Pause(itemMoveDelayMs)

                            Items.UseItem(tool)
                            Gumps.WaitForGump(CRAFTING_GUMP_ID, 5000)
                            Misc.Pause(int(gumpDelayMs / 2)) #always gump delay (250)
                            if not Gumps.HasGump(CRAFTING_GUMP_ID):
                                Misc.Pause(gumpDelayMs * 2)
                                continue
                                
                            # Set material (not every profession has it, e.g. alchemy)
                            if not craftGumpSet:
                                
                                if smallBod.specialMaterialButton > 0:
                                    # The menu button to select material
                                    Gumps.SendAction(CRAFTING_GUMP_ID, 7)
                                    Gumps.WaitForGump(CRAFTING_GUMP_ID, 5000)
                                    Misc.Pause(gumpDelayMs)#1000 before
                                    if not Gumps.HasGump(CRAFTING_GUMP_ID):
                                        continue                    
                                        
                                    # The actual special material button
                                    Gumps.SendAction(CRAFTING_GUMP_ID, smallBod.specialMaterialButton)
                                    Gumps.WaitForGump(CRAFTING_GUMP_ID, 5000)
                                    Misc.Pause(gumpDelayMs)#1000 before
                                    if not Gumps.HasGump(CRAFTING_GUMP_ID):
                                        continue 
                                      
                                # Sets category
                                Gumps.SendAction(CRAFTING_GUMP_ID, smallBod.recipe.gumpCategory)
                                Gumps.WaitForGump(CRAFTING_GUMP_ID, 10000)
                                Misc.Pause(gumpDelayMs)
                                if not Gumps.HasGump(CRAFTING_GUMP_ID):
                                    continue                                        
                                    
                                craftGumpSet = True
                                  
                            if freshBod.Color == HUE_INSCRIPTION and Player.Mana < 40:
                                while Player.Mana < Player.ManaMax:
                                    if Timer.Check("meditationTimer") == False and not Player.BuffsExist("Meditation"):
                                        print("Mana is low, attempting meditation")
                                        Player.UseSkill("Meditation")
                                        Timer.Create("meditationTimer", 10000)
                                    Misc.Pause(500)
                                    
                            # Actually does crafting
                            Gumps.SendAction(CRAFTING_GUMP_ID, smallBod.recipe.gumpSelection)                    
                            Gumps.WaitForGump(CRAFTING_GUMP_ID, 10000)
                            Misc.Pause(gumpDelayMs) #1000 before

                else:
                    break
                    
                Misc.Pause(250)
                
            cleanup(craftContainer, salvageBag, trashContainer, resourceContainer, itemMoveDelayMs, smallBod)

    print("****************************************** Start Large BOD ******************************************")
    db = build_complete_small_bod_db(smallBodWaitingForLargeBodContainers, recipes)
    largeBods = sort_large_bods([craftContainer] + incompleteBodContainers)
    for largeBod in largeBods:
        if largeBod is not None: 
            bod = Items.FindBySerial(largeBod.bodSerial)
            if largeBod.isComplete() and bod.Container in [craftContainer] + incompleteBodContainers:
                print("Found a misplaced (but complete) large bod, moving to right container! :))")
                Items.Move(largeBod.bodSerial, completeLargeBodContainer, 1)
                Misc.Pause(itemMoveDelayMs)
                continue
            
            smallBods = search_complete_small_bod_db(db, largeBod, fillNormalLargeBodsWithExceptionalSmallBods)
            
            if len(smallBods) > 0:
                print("Found matches for a large bod, attempting to complete...")
                    
                Items.Move(largeBod.bodSerial, craftContainer, 1)
                Misc.Pause(itemMoveDelayMs)
                for smallBod in smallBods:
                    Items.Move(smallBod.bodSerial, craftContainer, 1)
                    Misc.Pause(itemMoveDelayMs)
                    
                
                   
                # Open Large bod gump
                Target.Cancel()
                Items.UseItem(largeBod.bodSerial)
                Gumps.WaitForGump(LARGE_BOD_GUMP_ID, 3000)
                Target.Cancel()
                Misc.Pause(gumpDelayMs) #1000 before
                
                # Combine with contained items (backpack)
                Gumps.SendAction(LARGE_BOD_GUMP_ID, 4) 
                Target.WaitForTarget(5000)
                Target.TargetExecute(craftContainer)
                Gumps.WaitForGump(LARGE_BOD_GUMP_ID, 3000)
                Misc.Pause(gumpDelayMs * 2) # 1500 before
                Target.Cancel()
                Gumps.CloseGump(LARGE_BOD_GUMP_ID)
                
                bod = Items.FindBySerial(largeBod.bodSerial)
                freshLargeBod = parse_large_bod(bod)
                    
                if freshLargeBod.isComplete():
                    print("\t...large BOD filled! :)")
                    Items.Move(largeBod.bodSerial, completeLargeBodContainer, 1)
                    Misc.Pause(itemMoveDelayMs)
                elif bod.Container == craftContainer:
                    print("\t...large BOD back to incompleteBodContainer :(")
                    for incompleteBodContainer in incompleteBodContainers:
                        container = Items.FindBySerial(incompleteBodContainer)
                        if container.Contains.Count < 125:
                            Items.Move(bod, incompleteBodContainer, 1)
                            Misc.Pause(itemMoveDelayMs)                
                            break                    
                
    print("Checked {} Large Bods".format(len(largeBods)))                

    report_final_metrics(reports, recipes, incompleteBodContainers, smallBodWaitingForLargeBodContainers, completeSmallBodContainer, completeLargeBodContainer)

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
#
def run_craft_loop(

    # A string for the item name you want to craft like "leather sleeves" or "Recall" (note the caps). 
    # You can find the complete list of implemented recipes in the omgarturo.fm_core.core_crafting.RECIPES
    # array. Just grab the item name from that and plug it in here. If the recipe youre looking
    # for doesnt exist, then youre boned.
    recipeName,

    # Serial of container to do work in. This container must be placed in your backpack. 
    # Get its serial and fill it in here. You *could* use your backpack, but your risk losing
    # things when filtering out unwanted items.
    # The script will move all tools and materials to this container. Crafted items will appear here.
    craftContainer,
    
    # Stash a bunch of tools in here and let it rip. Serial of container.
    toolContainer,
    
    # Serial of regular container / commodity deed box (not a special resource box like insaneuo).
    # Fill this with ingots, reagents, etc. Use the run_restocker() function to help fill it up.
    resourceContainer,
    
    # An array of serials for containers where the items you want to keep will be stored.
    # Plop a container down, secure it, grab the serial, and plug it into this array.
    # Script will attempt to move items that DO meet filters after every craft attempt.
    # This is slow and should be optimized later based on weight.
    keepContainers,
    
    # Serial of a container to dump trash in. This is where we put all
    # crafted items that are to be discarded (perhaps not enough resists, see filters).
    # I think you can use a trash bin. Maybe place on next to you.
    # "I wish to place a trash barrel"
    # Script will attempt to move items that do not meet filters after every craft attempt.
    trashContainer,
    
    # (Optional) A number that marks the upper limit on crafted items.
    # Default is None which means keep crafting forever.
    maxItemsToCraft = None,
    
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
    print("Found Recipe {}".format(recipe))
    craftGumpSet = False
    totalCrafted = 0
    totalKept = 0
    while True:
        tool = get_tool(craftContainer, recipe.toolId, toolContainer, itemMoveDelayMs)
        if tool is None:
            print("Error: Cannot find tool")
            sys.exit()

        if not check_resources(craftContainer, recipe.resources, resourceContainer, itemMoveDelayMs, specialMaterialHue):            
            print("Error: Out of resources")
            sys.exit()
            
        # Meditation for inscription crafting
        while Player.Mana < Player.ManaMax * 0.5:
            if Timer.Check("meditationTimer") == False and not Player.BuffsExist("Meditation"):
                print("Mana is low, attempting meditation")
                Player.UseSkill("Meditation")
                Timer.Create("meditationTimer", 10000)
            Misc.Pause(500)            
            
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
                #for prop in item.Properties:
                #    print(prop, prop.ToString().lower(), prop.Args, prop.Number)
                    
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

                totalCrafted = totalCrafted + 1
                
                if keepItem:
                    totalKept = totalKept + 1
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
                    
        if maxItemsToCraft is not None and totalKept >= maxItemsToCraft:
            print("All done. Crafted {} items".format(totalKept))
            return 
            
        print("Crafted: {}\tKept: {}".format(totalCrafted, totalKept))
        Misc.Pause(50)