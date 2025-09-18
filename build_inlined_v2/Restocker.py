import sys

# Constants
SULPHUROUSASH = 3980
WHITE_PEARL = 12694
RESOURCE_HUE_BRONZE = 2418
MANDRAKEROOT = 3974
NOXCRYSTAL = 3982
RESOURCE_HUE_BARBED = 2129
STAR_SAPPHIRE = 3855
RESOURCE_HUE_DULL_COPPER = 2419
RESOURCE_HUE_SPINED = 2220
DAEMONBLOOD = 3965
AMETHYST = 3862
PIGIRON = 3978
CITRINE = 3861
RESOURCE_HUE_AGAPITE = 2425
RESOURCE_HUE_DEFAULT = 0
TURQUOISE = 12691
EMERALD = 3856
RESOURCE_HUE_FROSTWOOD = 1151
RESOURCE_HUE_ASH = 1191
AMBER = 3877
RESOURCE_HUE_HORNED = 2117
RESOURCE_HUE_COPPER = 2413
INGOT_STATIC_ID = 7154
RESOURCE_HUE_SHADOW_IRON = 2406
RESOURCE_HUE_BLOODWOOD = 1194
NIGHTSHADE = 3976
DIAMOND = 3878
GARLIC = 3972
RESOURCE_HUE_GOLD = 2213
LEATHER_STATIC_ID = 4225
SAPPHIRE = 3857
CLOTH_STATIC_ID = 5990
RESOURCE_HUE_VERITE = 2207
RESOURCE_HUE_YEW = 1192
TOURMALINE = 3864
RESOURCE_HUE_VALORITE = 2219
BATWING = 3960
BLOODMOSS = 3963
RESOURCE_HUE_HEARTWOOD = 1193
RESOURCE_HUE_OAK = 2010
PERFECT_EMERALD = 12692
BOARD_STATIC_ID = 7127
RUBY = 3859
SPIDERSILK = 3981
BLACKPEARL = 3962
GINSENG = 3973
FIRE_RUBY = 12695
GRAVEDUST = 3983

# Classes
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

# Functions
def get_amount_in_container(resource, containerSerial):
    amount = 0
    items = Items.FindAllByID(resource.itemId, resource.itemHue, containerSerial, 0)
    for item in items:
        amount = amount + item.Amount
    return amount
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

# Main code
commodityBoxSerial = 1082966558
minerResourceBoxSerial = 1073979729
reagentResourceBoxSerial = 1083126120
tailorResourceBoxSerial = 1088603211
logsAndBoardsResourceBoxSerial = 1076498434
mondainLegacyResourceBoxSerial = 1083503193
resources = [RestockItem(BLACKPEARL, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 100, 10000), RestockItem(BLOODMOSS, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 101, 10000), RestockItem(GARLIC, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 102, 10000), RestockItem(GINSENG, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 103, 10000), RestockItem(MANDRAKEROOT, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 104, 10000), RestockItem(NIGHTSHADE, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 105, 10000), RestockItem(SULPHUROUSASH, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 106, 10000), RestockItem(SPIDERSILK, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 107, 10000), RestockItem(BATWING, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 108, 10000), RestockItem(GRAVEDUST, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 109, 10000), RestockItem(DAEMONBLOOD, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 110, 10000), RestockItem(NOXCRYSTAL, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 111, 10000), RestockItem(PIGIRON, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 112, 10000), RestockItem(BOARD_STATIC_ID, RESOURCE_HUE_DEFAULT, logsAndBoardsResourceBoxSerial, 107, 10000), RestockItem(BOARD_STATIC_ID, RESOURCE_HUE_OAK, logsAndBoardsResourceBoxSerial, 108, 10000), RestockItem(BOARD_STATIC_ID, RESOURCE_HUE_ASH, logsAndBoardsResourceBoxSerial, 109, 10000), RestockItem(BOARD_STATIC_ID, RESOURCE_HUE_YEW, logsAndBoardsResourceBoxSerial, 110, 10000), RestockItem(BOARD_STATIC_ID, RESOURCE_HUE_HEARTWOOD, logsAndBoardsResourceBoxSerial, 111, 10000), RestockItem(BOARD_STATIC_ID, RESOURCE_HUE_BLOODWOOD, logsAndBoardsResourceBoxSerial, 112, 10000), RestockItem(BOARD_STATIC_ID, RESOURCE_HUE_FROSTWOOD, logsAndBoardsResourceBoxSerial, 113, 10000), RestockItem(INGOT_STATIC_ID, RESOURCE_HUE_DEFAULT, minerResourceBoxSerial, 101, 10000), RestockItem(INGOT_STATIC_ID, RESOURCE_HUE_DULL_COPPER, minerResourceBoxSerial, 101, 10000), RestockItem(INGOT_STATIC_ID, RESOURCE_HUE_SHADOW_IRON, minerResourceBoxSerial, 102, 10000), RestockItem(INGOT_STATIC_ID, RESOURCE_HUE_COPPER, minerResourceBoxSerial, 103, 10000), RestockItem(INGOT_STATIC_ID, RESOURCE_HUE_BRONZE, minerResourceBoxSerial, 104, 10000), RestockItem(INGOT_STATIC_ID, RESOURCE_HUE_GOLD, minerResourceBoxSerial, 105, 10000), RestockItem(INGOT_STATIC_ID, RESOURCE_HUE_AGAPITE, minerResourceBoxSerial, 106, 10000), RestockItem(INGOT_STATIC_ID, RESOURCE_HUE_VERITE, minerResourceBoxSerial, 107, 10000), RestockItem(INGOT_STATIC_ID, RESOURCE_HUE_VALORITE, minerResourceBoxSerial, 108, 10000), RestockItem(CLOTH_STATIC_ID, RESOURCE_HUE_DEFAULT, tailorResourceBoxSerial, 111, 10000), RestockItem(LEATHER_STATIC_ID, RESOURCE_HUE_DEFAULT, tailorResourceBoxSerial, 100, 10000), RestockItem(LEATHER_STATIC_ID, RESOURCE_HUE_SPINED, tailorResourceBoxSerial, 101, 10000), RestockItem(LEATHER_STATIC_ID, RESOURCE_HUE_HORNED, tailorResourceBoxSerial, 102, 10000), RestockItem(LEATHER_STATIC_ID, RESOURCE_HUE_BARBED, tailorResourceBoxSerial, 103, 10000), RestockItem(CITRINE, RESOURCE_HUE_DEFAULT, mondainLegacyResourceBoxSerial, 100, 1000), RestockItem(EMERALD, RESOURCE_HUE_DEFAULT, mondainLegacyResourceBoxSerial, 102, 1000), RestockItem(TOURMALINE, RESOURCE_HUE_DEFAULT, mondainLegacyResourceBoxSerial, 104, 1000), RestockItem(DIAMOND, RESOURCE_HUE_DEFAULT, mondainLegacyResourceBoxSerial, 106, 1000), RestockItem(SAPPHIRE, RESOURCE_HUE_DEFAULT, mondainLegacyResourceBoxSerial, 108, 1000), RestockItem(STAR_SAPPHIRE, RESOURCE_HUE_DEFAULT, mondainLegacyResourceBoxSerial, 109, 1000), RestockItem(RUBY, RESOURCE_HUE_DEFAULT, mondainLegacyResourceBoxSerial, 111, 1000), RestockItem(AMBER, RESOURCE_HUE_DEFAULT, mondainLegacyResourceBoxSerial, 113, 1000), RestockItem(AMETHYST, RESOURCE_HUE_DEFAULT, mondainLegacyResourceBoxSerial, 115, 1000), RestockItem(WHITE_PEARL, RESOURCE_HUE_DEFAULT, mondainLegacyResourceBoxSerial, 117, 100, 2)]
run_restocker(commodityBoxSerial=commodityBoxSerial, resources=resources, itemMoveDelayMs=1000, gumpDelayMs=500)
