# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-11-07
# Use at your own risk.

# ##########################################################
# #                                                        #
# #              INLINED DEPENDENCIES                      #
# #                                                        #
# #  DO NOT EDIT THIS SECTION - AUTO-GENERATED CODE        #
# #                                                        #
# #  These are dependencies from fm_core that have been    #
# #  automatically inlined. For user-editable code,        #
# #  scroll down to the bottom of this file.               #
# #                                                        #
# ##########################################################

from System import Byte, Int32
from System.Collections.Generic import List
import re
import sys

ALCHEMY_TOOL_STATIC_ID = 0x0E9B

AMBER = 0x0F25

AMETHYST = 0x0F16

BASCINET_GRAPHIC_ID = 0x140C

BATWING = 0x0F78

BLACKPEARL = 0x0F7A

BLACKSMITHY_TOOL_STATIC_ID = 0x13E3

BLANK_SCROLL = 0x0EF3

BLOODMOSS = 0x0F7B

BOARD_STATIC_ID = 0x1BD7

BOLA_BALLS_STATIC_ID = 0x0E73

BONE = 0x0F7E

BROADSWORD_GRAPHIC_ID = 0x0F5E

CARPENTRY_TOOL_STATIC_ID = 0x1034

CAT_ALCHEMY_ENHANCEMENT = 8

CAT_ALCHEMY_EXPLOSIVE = 22

CAT_ALCHEMY_HEALING_AND_CURATIVE = 1

CAT_ALCHEMY_TOXIC = 15

CAT_BLACKSMITHY_AXES = 29

CAT_BLACKSMITHY_BASHING = 43

CAT_BLACKSMITHY_BLADED = 22

CAT_BLACKSMITHY_HELMETS = 8

CAT_BLACKSMITHY_METAL_ARMOR = 1

CAT_BLACKSMITHY_POLEARMS = 36

CAT_BLACKSMITHY_SHIELDS = 15

CAT_CARPENTRY_CONTAINERS = 15

CAT_CARPENTRY_FURNITURE = 8

CAT_CARPENTRY_INSTRUMENTS = 36

CAT_CARPENTRY_OTHER = 1

CAT_CARPENTRY_WEAPONS = 22

CAT_INSCRIPTION_FIFTH_SIXTH = 15

CAT_INSCRIPTION_FIRST_SECOND = 1

CAT_INSCRIPTION_NECRO = 29

CAT_INSCRIPTION_OTHER = 36

CAT_INSCRIPTION_SEVENTH_EIGTH = 22

CAT_INSCRIPTION_THIRD_FOURTH = 8

CAT_TAILORING_BONE_ARMOR = 64

CAT_TAILORING_FEMALE_ARMOR = 57

CAT_TAILORING_FOOTWEAR = 29

CAT_TAILORING_HATS = 8

CAT_TAILORING_LEATHER_ARMOR = 36

CAT_TAILORING_MISCELLANEOUS = 22

CAT_TAILORING_SHIRTS_AND_PANTS = 15

CAT_TAILORING_STUDDED_ARMOR = 50

CAT_TINKERING_ASSEMBLIES = 43

CAT_TINKERING_JEWELRY = 1

CAT_TINKERING_MISCELLANEOUS = 36

CAT_TINKERING_PARTS = 22

CAT_TINKERING_TOOLS = 15

CAT_TINKERING_UTENSILS = 29

CAT_TINKERING_WOODEN_ITEMS = 8

CITRINE = 0x0F15

CLOTH_STATIC_ID = 0x1766

CRAFTING_GUMP_ID = 0x38920abd

DAEMONBLOOD = 0x0F7D

DIAMOND = 0x0F26

EMERALD = 0x0F10

EMPTY_BOTTLE_STATIC_ID = 0x0F0E

FANCY_SHIRT_GRAPHIC_ID = 0x1EFD

FIRE_RUBY = 0x3197

FLOWER_GARLAND_GRAPHIC_ID =  0x2306

FOOT_STOOL_GRAPHIC_ID = 0x0B5E

GARLIC = 0x0F84

GATE_SCROLL = 0x1F60

GINSENG = 0x0F85

GRAVEDUST = 0x0F8F

HEATER_SHIELD_GRAPHIC_ID = 0x1B76

INGOT_STATIC_ID = 0x1BF2

INSCRIPTION_TOOL_STATIC_ID = 0x0FBF

KILT_GRAPHIC_ID = 0x1537

LAP_HARP_GRAPHIC_ID = 0x0EB2

LEATHER_STATIC_ID = 0x1081

LUMINESCENT_FUNGI = 0x3191

MANDRAKEROOT = 0x0F86

NIGHTSHADE = 0x0F88

NOXCRYSTAL = 0x0F8E

PARASITIC_PLANT = 0x3190

PERFECT_EMERALD = 0x3194

PIGIRON = 0x0F8A

RECALL_SCROLL = 0x1F4C

RESOURCE_HUE_DEFAULT = 0x0000

RUBY = 0x0F13

SAPPHIRE = 0x0F11

SPIDERSILK = 0x0F8D

SPYGLASS_GRAPHIC_ID = 0x14F5

STAR_SAPPHIRE =  0x0F0F

STUDDED_BUSTIER_GRAPHIC_ID = 0x1C0C

SULPHUROUSASH = 0x0F8C

TAILORING_TOOL_STATIC_ID = 0x0F9D

TINKERING_TOOL_STATIC_ID = 0x1EBC

TOURMALINE = 0x0F18

TURQUOISE = 0x3193

UNMARKED_RUNE = 0x1F14

WHITE_PEARL = 0x3196

def find_in_container_by_id(itemID, containerSerial = Player.Backpack.Serial, color = -1, ignoreContainer = [], recursive = False):
    ignoreColor = False
    if color == -1:
        ignoreColor = True
        
    container = Items.FindBySerial(containerSerial)

    if isinstance( itemID, int ):
        foundItem = next( ( item for item in container.Contains if ( item.ItemID == itemID and ( ignoreColor or item.Hue == color ) ) ), None )
    elif isinstance( itemID, list ):
        foundItem = next( ( item for item in container.Contains if ( item.ItemID in itemID and ( ignoreColor or item.Hue == color ) ) ), None )
    else:
        raise ValueError( 'Unknown argument type for itemID passed to FindItem().', itemID, container )

    if foundItem != None:
        return foundItem        
    elif recursive == True:
        for item in container.Contains:
            if item.IsContainer:
                foundItem = find_in_container_by_id(itemID, containerSerial = item.Serial, color = color, ignoreContainer = ignoreContainer, recursive = recursive)
                if foundItem != None:
                    return foundItem

def get_pets(range = 10, checkLineOfSight = True, mobileId = None):
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

def get_yellows_in_range(range = 8):
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = range
    fil.Notorieties = List[Byte](bytes([7]))
    fil.IsGhost = False
    fil.Friend = False
    fil.CheckLineOfSight = False
    mobs = Mobiles.ApplyFilter(fil)

    return mobs

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
    SmallBodRecipe(False, "bola balls", CAT_TINKERING_PARTS, 51, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID, 10)] ),
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
    SmallBodRecipe(False, "bola", CAT_TINKERING_ASSEMBLIES, 44, TINKERING_TOOL_STATIC_ID, [SmallBodResource(LEATHER_STATIC_ID, 3), SmallBodResource(BOLA_BALLS_STATIC_ID, 4)] ),
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
    
    # Traps  - These dont produce an item
    #SmallBodRecipe(False, "dart trap", CAT_TINKERING_TRAPS, 2, TINKERING_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID), SmallBodResource(CROSSBOW_BOLT_GRAPHIC_ID)] ),    

    
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
    SmallBodRecipe(True, "wooden shelf", CAT_CARPENTRY_CONTAINERS, 37, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
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
    SmallBodRecipe(True, "quarter staff", CAT_CARPENTRY_WEAPONS, 9, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(True, "gnarled staff", CAT_CARPENTRY_WEAPONS, 16, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(True, "bokuto", CAT_CARPENTRY_WEAPONS, 23, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(True, "tetsubo", CAT_CARPENTRY_WEAPONS, 37, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(True, "wild staff", CAT_CARPENTRY_WEAPONS, 44, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID)] ),
    SmallBodRecipe(True, "arcanist's wild staff", CAT_CARPENTRY_WEAPONS, 58, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID), SmallBodResource(WHITE_PEARL, 1)] ), # '
    SmallBodRecipe(True, "ancient wild staff", CAT_CARPENTRY_WEAPONS, 65, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID), SmallBodResource(PERFECT_EMERALD, 1) ] ),
    SmallBodRecipe(True, "thorned wild staff", CAT_CARPENTRY_WEAPONS, 72, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID), SmallBodResource(FIRE_RUBY, 1) ] ),
    SmallBodRecipe(True, "hardened wild staff", CAT_CARPENTRY_WEAPONS, 79, CARPENTRY_TOOL_STATIC_ID, [SmallBodResource(BOARD_STATIC_ID), SmallBodResource(TURQUOISE, 1) ] ),
    
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
    SmallBodRecipe(True, "chainmail coif", CAT_BLACKSMITHY_METAL_ARMOR, 30, BLACKSMITHY_TOOL_STATIC_ID, [SmallBodResource(INGOT_STATIC_ID)] ),
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
    # A value of 0 means exactly 1 craft attempt (success or failure)
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

# ##########################################################
# #                                                        #
# #                 USER EDITABLE CODE                      #
# #                                                        #
# #  This is the original script code that you can         #
# #  modify and customize. Edit the parameters, logic,     #
# #  and function calls below as needed for your setup.    #
# #                                                        #
# #  The dependencies above have been automatically        #
# #  inlined and should not be modified.                   #
# ##########################################################

# Does the heartwood quests. 
# You need a pack animal that contains all of your tools and resources.
# You can configure the quests you want to do / skip below.
# Just stand near an npc and hit play. This will craft things in your backpack.
# Make sure you dont have any valuable items that may have the same graphic id
# as the items you are crafting, e.g. spellbooks. Would hate to see one of those
# get turned in as a quest item.

pets = get_pets()
if len(pets) == 0:
    print("Terminating: You need a pack animal with all your tools and resources")
    sys.exit()

# Where crafting happens. Has to be different than the final "Keep" container
# otherwise my shit script gets confused.
CRAFT_CONTAINER_SERIAL = 0x406766F0

# Can set to any sub container. I just use backpack.
KEEP_CONTAINER_SERIAL = Player.Backpack.Serial

# You shouldnt change this. But if you really wanted to,
# you could have another pouch for  your stuff. 
RESOURCE_CONTAINER_SERIAL = pets[0].Backpack.Serial
TOOL_CONTAINER_SERIAL = pets[0].Backpack.Serial

# Configure quests you want to do. All quests in this list will be accepted.
QUESTS = [
    # Metal Weaver - just need iron ingots
    #[ "Cuts Both Ways", "broadsword", BROADSWORD_GRAPHIC_ID ],
    #[ "The Bulwark", "heater shield", HEATER_SHIELD_GRAPHIC_ID ],
    #[ "Nothing Fancy", "bascinet", BASCINET_GRAPHIC_ID ],
    
    # Cloth Weaver
    #[ "The King of Clothing", "kilt", KILT_GRAPHIC_ID ],
    #[ "The Puffy Shirt", "fancy shirt", FANCY_SHIRT_GRAPHIC_ID ],
    #[ "Hâute Couture", "flower garland", FLOWER_GARLAND_GRAPHIC_ID ],
    #[ "From the Gaultier Collection", "studded bustier", STUDDED_BUSTIER_GRAPHIC_ID ],
    
    # Bark Weaver
    #[ "Stop Harping on Me", "lap harp", LAP_HARP_GRAPHIC_ID ],
    
    # Trinket weaver
    #[ "The Far Eye", "spyglass", SPYGLASS_GRAPHIC_ID ]
    #[ "Arch Support", "foot stool", FOOT_STOOL_GRAPHIC_ID ]
    
    # Grape Tender - Scrappers compendium, pendant of the magi
    # Message in a bottle quest doesnt craft anything. Just put a lot of bottles
    # in your beetle.
    [ "Message in a Bottle", "empty bottle", EMPTY_BOTTLE_STATIC_ID ]
]

# Shouldnt have to touch this. This is crap like "Bob the builder" so
# the script knows which NPCs have heartwood quests.
ALLOWED_SUFFIXES = ["metal weaver", "cloth weaver", "bark weaver", "trinket weaver", "grape tender"]

QUEST_GUMP_ID = 0x4c4c6db0


QUEST_ITEM_HUE = 0x04EA

# Checks if suffix is in the npcs props
def is_quest_giver(npc):
    for prop in npc.Properties:
        if any(s in prop.ToString() for s in ALLOWED_SUFFIXES):
            return True
    return False
    
# Looks up the quest by our approved list of quest names and returns
# a throuple: questName, questItemName, questItemGraphic
def get_quest_details(gumpText):
    for quest in QUESTS:
        if quest[0] in gumpText:
            return quest[0], quest[1], quest[2]
    return None, None, None
    
# Extra parsing needed for the quantity of items to craft
def get_quest_amount(gumpText):
    #print("*********")
    #print(gumpText)
    #print("*********")
    #pattern = r"(\d+)\s+{}s".format(re.escape(questItemName))
    pattern = r"(\d+)\s+{}s?".format(re.escape(questItemName))
    match = re.search(pattern, gumpText)
    if match:
        return int(match.groups()[0])
        
        
# Cancel all quests that currently active
Gumps.CloseGump(QUEST_GUMP_ID)
Player.QuestButton()
Gumps.WaitForGump(QUEST_GUMP_ID, 3500) 

if Gumps.LastGumpTextExist("Quest Log"):
    gumpText = Gumps.GetGumpText(QUEST_GUMP_ID)
    
    questButtonId = len(gumpText) + 10
    for g in gumpText:
        print("Checking ", questButtonId, " ", g)
        for q in QUESTS:
            if q[0] == g:
                print("\tShould abandon quest ", q[0], g)
                Gumps.SendAction(QUEST_GUMP_ID, questButtonId)
                Gumps.WaitForGump(QUEST_GUMP_ID, 3500) 
                Gumps.SendAction(QUEST_GUMP_ID, 3)
                
                # Confirm Quest Cancelleation
                Gumps.WaitForGump(0x135b22a4, 3500) 
                inSwitches = List[Int32]([1])
                Gumps.SendAdvancedAction(0x135b22a4, 1, inSwitches)
                Misc.Pause(1000)
                
                Gumps.WaitForGump(QUEST_GUMP_ID,3500)
                 
        questButtonId = questButtonId - 1
    


while True:
    npcs = get_yellows_in_range(range = 8)
    npc = Mobiles.Select(npcs, "Nearest")

    if npc is not None and is_quest_giver(npc):
        Mobiles.UseMobile(npc)
        Gumps.WaitForGump(QUEST_GUMP_ID,3000)
        
        if Gumps.LastGumpTextExist("Quest Offer"):
            # Quest is available. Lets check it out. If its good, well begin crafting
            # and go all the way until were done. Otherwise refuse it and try again.

            gumpText = "".join(Gumps.GetGumpText(QUEST_GUMP_ID))
            questName, questItemName, questItemGraphic = get_quest_details(gumpText)
            
            print("QuestItemName: ", questItemName)
            if questItemName is not None:
                Gumps.SendAction(QUEST_GUMP_ID, 7)
                Gumps.WaitForGump(QUEST_GUMP_ID, 3000)
                Misc.Pause(3000)
                
                
                gumpText2 = "".join([str for str in Gumps.GetGumpData(QUEST_GUMP_ID).stringList if str is not None])
                amountNeeded = get_quest_amount(gumpText2)

                if amountNeeded is not None:
                    #print(match.groups())
                    print("Quest: ", questName)
                    print("Item: ", questItemName)
                    #amountToMake = int(match.groups()[0])

                    print("Amount: ", amountNeeded)
                    Gumps.SendAction(QUEST_GUMP_ID, 4)
                    
                    Misc.Pause(3000)
                    
                    # Dont craft bottles, just turn them in.
                    # Put a bunch in your beetle.
                    if questItemGraphic == EMPTY_BOTTLE_STATIC_ID:
                        print("bottlequest")
                        
                        Items.UseItem(RESOURCE_CONTAINER_SERIAL)
                        Misc.Pause(650)
                        Items.UseItem(KEEP_CONTAINER_SERIAL)
                        Misc.Pause(650)
                        Items.UseItem(CRAFT_CONTAINER_SERIAL)
                        Misc.Pause(650)
                        
                        craftedItems = Items.FindAllByID(questItemGraphic, 0, KEEP_CONTAINER_SERIAL, 0)
                        amountWeHave = sum(craftedItem.Amount for craftedItem in craftedItems)
                        print("amountWeHave: ", amountWeHave)
                        print("amountNeeded: ", amountNeeded)
                        
                        if amountWeHave < amountNeeded:
                            emptyBottles = Items.FindByID(questItemGraphic,0,RESOURCE_CONTAINER_SERIAL,0)
                            if emptyBottles is None:
                                print("Not enough ", questItemName)
                                sys.exit()
                            print("transferring ", ( amountNeeded - amountWeHave))
                            Items.Move(emptyBottles,KEEP_CONTAINER_SERIAL, amountNeeded - amountWeHave)
                            Misc.Pause(1500)
                            
                        print("Toggling quest items")
                        Misc.WaitForContext(Player.Serial, 10000)
                        Misc.ContextReply(Player.Serial, 7)
                        finalAmountWeHave = 0
                        craftedItems = Items.FindAllByID(questItemGraphic, 0, KEEP_CONTAINER_SERIAL, 0)
                        for craftedItem in craftedItems:
                            finalAmountWeHave = finalAmountWeHave + craftedItem.Amount
                            Target.WaitForTarget(10000, False)
                            Target.TargetExecute(craftedItem.Serial)
                            Misc.Pause(250)
                        Target.Cancel()
                        
                        if finalAmountWeHave < amountNeeded:
                            print("Not enough ", questItemName)
                            sys.exit()
                        
                    else:
                    
                    
                    
                        craftedItems = Items.FindAllByID(questItemGraphic, 0, KEEP_CONTAINER_SERIAL, 0)
                        amountToMake = amountNeeded - len(craftedItems) + 1
                        print("Amount we already have in backpack: ", len(craftedItems))
                        print("Net amount needed: ", amountToMake)
                        if amountToMake > 0:
                            run_craft_loop(
                                recipeName = questItemName,
                                craftContainer = CRAFT_CONTAINER_SERIAL,
                                toolContainer = TOOL_CONTAINER_SERIAL, # Bag inside beetle
                                resourceContainer = RESOURCE_CONTAINER_SERIAL, 
                                keepContainers = [KEEP_CONTAINER_SERIAL],
                                trashContainer = None,
                                maxItemsToCraft = amountToMake, 
                                specialMaterialHue = None,
                                itemMoveDelayMs = 750,
                                gumpDelayMs = 750,
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
                        

                        # 0x000E0EDD
                        print("Toggling quest items")
                        Misc.WaitForContext(Player.Serial, 10000)
                        Misc.ContextReply(Player.Serial, 7)
                        craftedItems = Items.FindAllByID(questItemGraphic, 0, KEEP_CONTAINER_SERIAL, 0)
                        for craftedItem in craftedItems:
                            Target.WaitForTarget(10000, False)
                            Target.TargetExecute(craftedItem.Serial)
                            Misc.Pause(250)
                        Target.Cancel()
                        
                        craftedItems = Items.FindAllByID(questItemGraphic, QUEST_ITEM_HUE, KEEP_CONTAINER_SERIAL, 0)
                        if len(craftedItems) < amountNeeded:
                            print("We only have ", len(craftedItems), " but we need ", amountNeeded)
                            sys.exit()
                        
                    print("Turning in quest")                
                    Misc.Pause(3000)
                    Mobiles.UseMobile(npc)
                    Gumps.WaitForGump(QUEST_GUMP_ID, 3000)
                    
                    Gumps.SendAction(QUEST_GUMP_ID, 8)
                    Gumps.WaitForGump(QUEST_GUMP_ID, 3000)
                    Gumps.SendAction(QUEST_GUMP_ID, 5)
                    Misc.Pause(1500)
                        
            else:
                print("Not taking this quest.")
                Gumps.SendAction(QUEST_GUMP_ID, 2)
                Gumps.WaitForGump(QUEST_GUMP_ID, 3000)
                Gumps.SendAction(QUEST_GUMP_ID, 0)
                Misc.Pause(3000)
                
                
        elif Gumps.LastGumpTextExist("Enjoy my thanks for your service"):
            # I think this is a rare case where someone may already be on a quest
            # AND have their items toggled as quest items.
          
            Gumps.SendAction(QUEST_GUMP_ID, 8)
            Gumps.WaitForGump(QUEST_GUMP_ID, 3000)
            Gumps.SendAction(QUEST_GUMP_ID, 5)
            Misc.Pause(3000)
            
        elif Gumps.LastGumpTextExist("I will be in your debt"):
            # Person is on a quest and in the middle of it. Need to abandon
            # and restart script. Kind of crappy, but I dont know how to get
            # current amount of items crafted from the quest if they are already
            # on it. I could parse chat logs and such, but too fat.
            print("You are already on a quest for this npc and need to abandon it and restart this script.")
            print("Quest: ", Gumps.GetGumpText(QUEST_GUMP_ID)[1])
            
            gumpText2 = "".join([str for str in Gumps.GetGumpText(QUEST_GUMP_ID) if str is not None])

            pattern = r"I will be in your debt if you bring me (.+)s"
            match = re.search(pattern, gumpText2)
            if match:
                print("Objective: Craft ", match.groups()[0])
                
            sys.exit()
            
        elif Gumps.LastGumpTextExist("Quest Conversation"):
            print("Something bad happened")
            sys.exit()
            
            
        Misc.Pause(1500)
