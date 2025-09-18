import sys
WHITE_PEARL = 12694
CAT_TINKERING_TOOLS = 15
smallBodItems = []
RESOURCE_HUE_OAK = 2010
PROP_ID_BOD_EXCEPTIONAL = 1045141
specialMaterialPropId = prop.Number
BOARD_STATIC_ID = 7127
RESOURCE_HUE_BLOODWOOD = 1194
HUE_TINKERING = 1109
INGOT_STATIC_ID = 7154
EMERALD = 3856
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
            propList = prop.ToString().split(': ')
            recipeName = propList[0].strip()
            amountMade = int(propList[1])
            smallBodItems.append({'name': recipeName, 'amountMade': amountMade})
    if isLargeBod:
        return LargeBod(bod.Serial, isExceptional, amountToMake, specialMaterialPropId, smallBodItems)
RESOURCE_HUE_BRONZE = 2418
numCompleted = numCompleted + 1
propList = prop.ToString().split(': ')
def get_amount_in_container(resource, containerSerial):
    amount = 0
    items = Items.FindAllByID(resource.itemId, resource.itemHue, containerSerial, 0)
    for item in items:
        amount = amount + item.Amount
    return amount
NIGHTSHADE = 3976
largeBod = parse_large_bod(bod)
CLOTH_STATIC_ID = 5990
PROD_ID_LARGE_BULK_ORDER = 1060655
part3 = '|'.join(sorted(list(map(lambda smallBodItem: smallBodItem['name'], self.smallBodItems))))
RESOURCE_HUE_DULL_COPPER = 2419
AMETHYST = 3862
RUBY = 3859
runAgain = True if Items.FindByID(resource.itemId, resource.itemHue, Player.Backpack.Serial, 0) is not None else False
RESOURCE_HUE_BARBED = 2129
PERFECT_EMERALD = 12692
MANDRAKEROOT = 3974
SPECIAL_PROP_MATERIAL_MAP = {1045142: {'button': 13, 'hue': RESOURCE_HUE_DULL_COPPER, 'name': 'dull copper'}, 1045143: {'button': 20, 'hue': RESOURCE_HUE_SHADOW_IRON, 'name': 'shadow iron'}, 1045144: {'button': 27, 'hue': RESOURCE_HUE_COPPER, 'name': 'copper'}, 1045145: {'button': 34, 'hue': RESOURCE_HUE_BRONZE, 'name': 'bronze'}, 1045146: {'button': 41, 'hue': RESOURCE_HUE_GOLD, 'name': 'golden'}, 1045147: {'button': 48, 'hue': RESOURCE_HUE_AGAPITE, 'name': 'agapite'}, 1045148: {'button': 55, 'hue': RESOURCE_HUE_VERITE, 'name': 'verite'}, 1045149: {'button': 62, 'hue': RESOURCE_HUE_VALORITE, 'name': 'valorite'}, 1049348: {'button': 13, 'hue': RESOURCE_HUE_SPINED, 'name': 'spined'}, 1049349: {'button': 20, 'hue': RESOURCE_HUE_HORNED, 'name': 'horned'}, 1049350: {'button': 27, 'hue': RESOURCE_HUE_BARBED, 'name': 'barbed'}, 1071428: {'button': 13, 'hue': RESOURCE_HUE_OAK, 'name': 'oak'}, 1071429: {'button': 20, 'hue': RESOURCE_HUE_ASH, 'name': 'ash'}, 1071430: {'button': 27, 'hue': RESOURCE_HUE_YEW, 'name': 'yew'}, 1071432: {'button': 34, 'hue': RESOURCE_HUE_HEARTWOOD, 'name': 'heartwood'}, 1071431: {'button': 41, 'hue': RESOURCE_HUE_BLOODWOOD, 'name': 'bloodwood'}, 1071433: {'button': 48, 'hue': RESOURCE_HUE_FROSTWOOD, 'name': 'frostwood'}}
RESOURCE_HUE_FROSTWOOD = 1151
isExceptional = True
LEATHER_STATIC_ID = 4225
recipeName = propList[0].strip()
amountInBox = get_amount_in_container(resource, commodityBoxSerial)
HUE_CARPENTRY = 1512
smallBod = parse_small_bod(freshBod, recipes, True)
GRAVEDUST = 3983
RESOURCE_HUE_HEARTWOOD = 1193
class SmallBod:

    def __init__(self, bodSerial, amountMade, isExceptional, amountToMake, specialMaterialButton, specialMaterialHue, specialMaterialPropId, specialMaterialName, recipe):
        self.amountMade = amountMade
        self.isExceptional = isExceptional
        self.amountToMake = amountToMake
        self.specialMaterialButton = specialMaterialButton
        self.specialMaterialHue = specialMaterialHue
        self.specialMaterialPropId = specialMaterialPropId
        self.specialMaterialName = specialMaterialName
        self.recipe = recipe
        self.bodSerial = bodSerial

    def getNameInLargeBod(self):
        if self.recipe.recipeName == 'skillet':
            return 'frypan'
        return self.recipe.recipeName

    def getCraftedItemName(self):
        if self.recipe.recipeName == 'globe' and self.specialMaterialHue == RESOURCE_HUE_DEFAULT:
            return 'iron globe'
        if self.recipe.recipeName == 'wooden shelf':
            return 'empty bookcase'
        if self.recipe.recipeName in ['Large Crate', 'Medium Crate']:
            return 'crate'
        if self.recipe.toolId in [BLACKSMITHY_TOOL_STATIC_ID, TAILORING_TOOL_STATIC_ID]:
            return self.specialMaterialName + ' ' + self.recipe.recipeName if self.specialMaterialName is not None else self.recipe.recipeName
        if self.recipe.toolId == TINKERING_TOOL_STATIC_ID and self.recipe.gumpCategory in [CAT_TINKERING_UTENSILS, CAT_TINKERING_MISCELLANEOUS, CAT_TINKERING_TOOLS]:
            return self.specialMaterialName + ' ' + self.recipe.recipeName if self.specialMaterialName is not None else self.recipe.recipeName
        if self.recipe.toolId == CARPENTRY_TOOL_STATIC_ID and self.recipe.gumpCategory in [CAT_CARPENTRY_WEAPONS, CAT_CARPENTRY_ARMOR]:
            return self.specialMaterialName + ' ' + self.recipe.recipeName if self.specialMaterialName is not None else self.recipe.recipeName
        return self.recipe.recipeName

    def isComplete(self):
        return self.amountToMake == self.amountMade

    def __str__(self):
        return f"SmallBod(getCraftedItemName()='{self.getCraftedItemName()}',amountMade='{self.amountMade}', isExceptional={self.isExceptional}, amountToMake='{self.amountToMake}', specialMaterialButton='{self.specialMaterialButton}', specialMaterialHue='{self.specialMaterialHue}', specialMaterialPropId={self.specialMaterialPropId}, specialMaterialName={self.specialMaterialName}, recipe={self.recipe})"
CAT_CARPENTRY_ARMOR = 29
HUE_TAILORING = 1155
amountMade = int(propList[1])
RESOURCE_HUE_SPINED = 2220
amountToMake = int(prop.Args)
part2 = str(self.specialMaterialPropId) if self.specialMaterialPropId is not None else '0'
TAILORING_TOOL_STATIC_ID = 3997
CAT_CARPENTRY_WEAPONS = 22
BATWING = 3960
RESOURCE_HUE_YEW = 1192
class RestockItem:

    def __init__(self, itemId, itemHue, resourceBoxSerial, resourceBoxButton, amount=10000, resourceBoxPage=1):
        self.itemId = itemId
        self.itemHue = itemHue
        self.resourceBoxSerial = resourceBoxSerial
        self.resourceBoxButton = resourceBoxButton
        self.amount = amount
        self.resourceBoxPage = resourceBoxPage

    def __str__(self):
        return f"RestockItem(itemId='{self.itemId}', itemHue={self.itemHue}, amount='{self.amount}', resourceBoxSerial='{self.resourceBoxSerial}', resourceBoxButton='{self.resourceBoxButton}', resourceBoxPage='{self.resourceBoxPage}')"
SAPPHIRE = 3857
RESOURCE_HUE_VERITE = 2207
BLOODMOSS = 3963
BLACKPEARL = 3962
BLACKSMITHY_TOOL_STATIC_ID = 5091
specialMaterialHue = SPECIAL_PROP_MATERIAL_MAP[prop.Number]['hue']
class LargeBod:

    def __init__(self, bodSerial, isExceptional, amountToMake, specialMaterialPropId, smallBodItems):
        self.isExceptional = isExceptional
        self.amountToMake = amountToMake
        self.specialMaterialPropId = specialMaterialPropId
        self.smallBodItems = smallBodItems
        self.bodSerial = bodSerial

    def getId(self):
        part1 = '1' if self.isExceptional else '0'
        part2 = str(self.specialMaterialPropId) if self.specialMaterialPropId is not None else '0'
        part3 = '|'.join(sorted(list(map(lambda smallBodItem: smallBodItem['name'], self.smallBodItems))))
        return part1 + '|' + part2 + '|' + part3

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
        return f"LargeBod(isExceptional='{self.isExceptional}', amountToMake='{self.amountToMake}', specialMaterialPropId={self.specialMaterialPropId}, smallBodItems={self.smallBodItems}, isComplete={self.isComplete()}, numComplete={self.numComplete()})"
def parse_small_bod(bod, recipes, alertMissingRecipe=False):
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
            specialMaterialButton = SPECIAL_PROP_MATERIAL_MAP[prop.Number]['button']
            specialMaterialHue = SPECIAL_PROP_MATERIAL_MAP[prop.Number]['hue']
            specialMaterialName = SPECIAL_PROP_MATERIAL_MAP[prop.Number]['name']
        if prop.Number == PROP_ID_ITEM_TEXT:
            propList = prop.ToString().split(': ')
            recipeName = propList[0].strip()
            amountMade = int(propList[1])
            if recipeName in recipes:
                recipe = recipes[recipeName]
    if recipe is not None and isSmallBod:
        return SmallBod(bod.Serial, amountMade, isExceptional, amountToMake, specialMaterialButton, specialMaterialHue, specialMaterialPropId, specialMaterialName, recipe)
    elif isSmallBod == True and alertMissingRecipe:
        print('Warning: Skipping because not in recipe list')
        for prop in bod.Properties:
            print('\t', prop.ToString(), '(', prop.Number, ')')
RESOURCE_HUE_DEFAULT = 0
TOURMALINE = 3864
isSmallBod = True
amount = amount + item.Amount
GINSENG = 3973
def run_restocker(commodityBoxSerial, resources, itemMoveDelayMs=1000, gumpDelayMs=500):
    RESOURCE_BOX_GUMP_ID = 600895849
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
items = Items.FindAllByID(r.itemId, r.itemHue, Player.Backpack.Serial, 0)
CITRINE = 3861
RESOURCE_HUE_AGAPITE = 2425
NOXCRYSTAL = 3982
PROP_ID_AMOUNT_TO_MAKE = 1060656
AMBER = 3877
FIRE_RUBY = 12695
CAT_TINKERING_UTENSILS = 29
CARPENTRY_TOOL_STATIC_ID = 4148
PIGIRON = 3978
RESOURCE_HUE_GOLD = 2213
recipe = recipes[recipeName]
recipes = {recipes[i].recipeName: recipes[i] for i in range(len(recipes))}
RESOURCE_HUE_COPPER = 2413
RESOURCE_HUE_SHADOW_IRON = 2406
STAR_SAPPHIRE = 3855
PROP_ID_SMALL_BULK_ORDER = 1060654
TINKERING_TOOL_STATIC_ID = 7868
isLargeBod = True
HUE_BLACKSMITHY = 1102
part1 = '1' if self.isExceptional else '0'
RESOURCE_BOX_GUMP_ID = 600895849
RESOURCE_HUE_VALORITE = 2219
freshBod = Items.FindBySerial(bod.Serial)
RESOURCE_HUE_HORNED = 2117
GARLIC = 3972
DIAMOND = 3878
RESOURCE_HUE_ASH = 1191
TURQUOISE = 12691
CAT_TINKERING_MISCELLANEOUS = 36
bod = Items.FindBySerial(largeBod.bodSerial)
specialMaterialButton = SPECIAL_PROP_MATERIAL_MAP[prop.Number]['button']
PROP_ID_ITEM_TEXT = 1060658
SULPHUROUSASH = 3980
specialMaterialName = SPECIAL_PROP_MATERIAL_MAP[prop.Number]['name']
DAEMONBLOOD = 3965
SPIDERSILK = 3981
item = Items.FindByName(smallBod.getCraftedItemName(), smallBod.specialMaterialHue, craftContainer, 0)
commodityBoxSerial = 1082966558
minerResourceBoxSerial = 1073979729
reagentResourceBoxSerial = 1083126120
tailorResourceBoxSerial = 1088603211
logsAndBoardsResourceBoxSerial = 1076498434
mondainLegacyResourceBoxSerial = 1083503193
resources = [RestockItem(BLACKPEARL, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 100, 10000), RestockItem(BLOODMOSS, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 101, 10000), RestockItem(GARLIC, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 102, 10000), RestockItem(GINSENG, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 103, 10000), RestockItem(MANDRAKEROOT, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 104, 10000), RestockItem(NIGHTSHADE, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 105, 10000), RestockItem(SULPHUROUSASH, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 106, 10000), RestockItem(SPIDERSILK, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 107, 10000), RestockItem(BATWING, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 108, 10000), RestockItem(GRAVEDUST, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 109, 10000), RestockItem(DAEMONBLOOD, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 110, 10000), RestockItem(NOXCRYSTAL, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 111, 10000), RestockItem(PIGIRON, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 112, 10000), RestockItem(BOARD_STATIC_ID, RESOURCE_HUE_DEFAULT, logsAndBoardsResourceBoxSerial, 107, 10000), RestockItem(BOARD_STATIC_ID, RESOURCE_HUE_OAK, logsAndBoardsResourceBoxSerial, 108, 10000), RestockItem(BOARD_STATIC_ID, RESOURCE_HUE_ASH, logsAndBoardsResourceBoxSerial, 109, 10000), RestockItem(BOARD_STATIC_ID, RESOURCE_HUE_YEW, logsAndBoardsResourceBoxSerial, 110, 10000), RestockItem(BOARD_STATIC_ID, RESOURCE_HUE_HEARTWOOD, logsAndBoardsResourceBoxSerial, 111, 10000), RestockItem(BOARD_STATIC_ID, RESOURCE_HUE_BLOODWOOD, logsAndBoardsResourceBoxSerial, 112, 10000), RestockItem(BOARD_STATIC_ID, RESOURCE_HUE_FROSTWOOD, logsAndBoardsResourceBoxSerial, 113, 10000), RestockItem(INGOT_STATIC_ID, RESOURCE_HUE_DEFAULT, minerResourceBoxSerial, 101, 10000), RestockItem(INGOT_STATIC_ID, RESOURCE_HUE_DULL_COPPER, minerResourceBoxSerial, 101, 10000), RestockItem(INGOT_STATIC_ID, RESOURCE_HUE_SHADOW_IRON, minerResourceBoxSerial, 102, 10000), RestockItem(INGOT_STATIC_ID, RESOURCE_HUE_COPPER, minerResourceBoxSerial, 103, 10000), RestockItem(INGOT_STATIC_ID, RESOURCE_HUE_BRONZE, minerResourceBoxSerial, 104, 10000), RestockItem(INGOT_STATIC_ID, RESOURCE_HUE_GOLD, minerResourceBoxSerial, 105, 10000), RestockItem(INGOT_STATIC_ID, RESOURCE_HUE_AGAPITE, minerResourceBoxSerial, 106, 10000), RestockItem(INGOT_STATIC_ID, RESOURCE_HUE_VERITE, minerResourceBoxSerial, 107, 10000), RestockItem(INGOT_STATIC_ID, RESOURCE_HUE_VALORITE, minerResourceBoxSerial, 108, 10000), RestockItem(CLOTH_STATIC_ID, RESOURCE_HUE_DEFAULT, tailorResourceBoxSerial, 111, 10000), RestockItem(LEATHER_STATIC_ID, RESOURCE_HUE_DEFAULT, tailorResourceBoxSerial, 100, 10000), RestockItem(LEATHER_STATIC_ID, RESOURCE_HUE_SPINED, tailorResourceBoxSerial, 101, 10000), RestockItem(LEATHER_STATIC_ID, RESOURCE_HUE_HORNED, tailorResourceBoxSerial, 102, 10000), RestockItem(LEATHER_STATIC_ID, RESOURCE_HUE_BARBED, tailorResourceBoxSerial, 103, 10000), RestockItem(CITRINE, RESOURCE_HUE_DEFAULT, mondainLegacyResourceBoxSerial, 100, 1000), RestockItem(EMERALD, RESOURCE_HUE_DEFAULT, mondainLegacyResourceBoxSerial, 102, 1000), RestockItem(TOURMALINE, RESOURCE_HUE_DEFAULT, mondainLegacyResourceBoxSerial, 104, 1000), RestockItem(DIAMOND, RESOURCE_HUE_DEFAULT, mondainLegacyResourceBoxSerial, 106, 1000), RestockItem(SAPPHIRE, RESOURCE_HUE_DEFAULT, mondainLegacyResourceBoxSerial, 108, 1000), RestockItem(STAR_SAPPHIRE, RESOURCE_HUE_DEFAULT, mondainLegacyResourceBoxSerial, 109, 1000), RestockItem(RUBY, RESOURCE_HUE_DEFAULT, mondainLegacyResourceBoxSerial, 111, 1000), RestockItem(AMBER, RESOURCE_HUE_DEFAULT, mondainLegacyResourceBoxSerial, 113, 1000), RestockItem(AMETHYST, RESOURCE_HUE_DEFAULT, mondainLegacyResourceBoxSerial, 115, 1000), RestockItem(WHITE_PEARL, RESOURCE_HUE_DEFAULT, mondainLegacyResourceBoxSerial, 117, 100, 2)]
run_restocker(commodityBoxSerial=commodityBoxSerial, resources=resources, itemMoveDelayMs=1000, gumpDelayMs=500)
