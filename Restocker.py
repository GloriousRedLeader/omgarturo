# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/uo-razor-enhanced
#   2025-02-04
# Use at your own risk. 

from Scripts.omgarturo.fm_core.core_items import INGOT_STATIC_ID 
from Scripts.omgarturo.fm_core.core_items import BOARD_STATIC_ID 
from Scripts.omgarturo.fm_core.core_items import CLOTH_STATIC_ID 
from Scripts.omgarturo.fm_core.core_items import LEATHER_STATIC_ID 
from Scripts.omgarturo.fm_core.core_items import WHITE_PEARL
from Scripts.omgarturo.fm_core.core_items import FIRE_RUBY
from Scripts.omgarturo.fm_core.core_items import PERFECT_EMERALD
from Scripts.omgarturo.fm_core.core_items import TURQUOISE
from Scripts.omgarturo.fm_core.core_items import STAR_SAPPHIRE
from Scripts.omgarturo.fm_core.core_items import CITRINE 
from Scripts.omgarturo.fm_core.core_items import DIAMOND
from Scripts.omgarturo.fm_core.core_items import AMBER
from Scripts.omgarturo.fm_core.core_items import AMETHYST
from Scripts.omgarturo.fm_core.core_items import SAPPHIRE
from Scripts.omgarturo.fm_core.core_items import RUBY
from Scripts.omgarturo.fm_core.core_items import EMERALD
from Scripts.omgarturo.fm_core.core_items import TOURMALINE
from Scripts.omgarturo.fm_core.core_items import MANDRAKEROOT
from Scripts.omgarturo.fm_core.core_items import BLOODMOSS
from Scripts.omgarturo.fm_core.core_items import SULPHUROUSASH
from Scripts.omgarturo.fm_core.core_items import NIGHTSHADE
from Scripts.omgarturo.fm_core.core_items import BLACKPEARL
from Scripts.omgarturo.fm_core.core_items import SPIDERSILK
from Scripts.omgarturo.fm_core.core_items import GINSENG
from Scripts.omgarturo.fm_core.core_items import GARLIC
from Scripts.omgarturo.fm_core.core_items import PIGIRON
from Scripts.omgarturo.fm_core.core_items import BATWING
from Scripts.omgarturo.fm_core.core_items import NOXCRYSTAL
from Scripts.omgarturo.fm_core.core_items import DAEMONBLOOD
from Scripts.omgarturo.fm_core.core_items import GRAVEDUST
from Scripts.omgarturo.fm_core.core_items import RESOURCE_HUE_DEFAULT
from Scripts.omgarturo.fm_core.core_items import RESOURCE_HUE_DULL_COPPER
from Scripts.omgarturo.fm_core.core_items import RESOURCE_HUE_SHADOW_IRON
from Scripts.omgarturo.fm_core.core_items import RESOURCE_HUE_COPPER
from Scripts.omgarturo.fm_core.core_items import RESOURCE_HUE_BRONZE
from Scripts.omgarturo.fm_core.core_items import RESOURCE_HUE_GOLD
from Scripts.omgarturo.fm_core.core_items import RESOURCE_HUE_AGAPITE
from Scripts.omgarturo.fm_core.core_items import RESOURCE_HUE_VERITE
from Scripts.omgarturo.fm_core.core_items import RESOURCE_HUE_VALORITE
from Scripts.omgarturo.fm_core.core_items import RESOURCE_HUE_BARBED
from Scripts.omgarturo.fm_core.core_items import RESOURCE_HUE_SPINED
from Scripts.omgarturo.fm_core.core_items import RESOURCE_HUE_HORNED
from Scripts.omgarturo.fm_core.core_items import RESOURCE_HUE_OAK
from Scripts.omgarturo.fm_core.core_items import RESOURCE_HUE_ASH
from Scripts.omgarturo.fm_core.core_items import RESOURCE_HUE_YEW
from Scripts.omgarturo.fm_core.core_items import RESOURCE_HUE_HEARTWOOD
from Scripts.omgarturo.fm_core.core_items import RESOURCE_HUE_BLOODWOOD
from Scripts.omgarturo.fm_core.core_items import RESOURCE_HUE_FROSTWOOD
from Scripts.omgarturo.fm_core.core_crafting import RestockItem
from Scripts.omgarturo.fm_core.core_crafting import run_restocker

# Insane UO Specific. Transfer resources from resource box to a commodity box.
# Use this to prepare your box in conjunction with the BODBuilder.
# Automates resource transferring for use.
# See the configuration section below

# Main container that will house a bunch of resources.
# Works well with commodity deed box but can be any container.
commodityBoxSerial = 0x408CC21E

# Set these serials to your InsaneUO resource boxes.
minerResourceBoxSerial = 0x4003A151
reagentResourceBoxSerial = 0x408F3168
tailorResourceBoxSerial = 0x40E2C44B
logsAndBoardsResourceBoxSerial = 0x402A1002
mondainLegacyResourceBoxSerial = 0x4094F259

#minerResourceBoxSerial = 0x4007D963
#tailorResourceBoxSerial = 0x409A3EA9
#logsAndBoardsResourceBoxSerial = 0x4022E8ED

# Main configuration. Set the resources you want to stock here and their amounts.
# Restockable item that lives inside of a specialized resource container.
# Arguments are as follows:
# itemId: Refer to constants, but represents things like item ids for ingots, boards, etc.
# itemHue: Some items have the same id but use different hues (leather, ingots, boards)
# resourceBoxSerial: Inspect your resource box with razor, get the serial, plug it in
# resourceBoxButton: This is the button id of the gump. You can use gump inspector. Starts at 100 and increments up.
# amount: The number of items you want in your commodityDeedBox.
# resourceBoxPage: (Optional) The gump has multiple pages. Starts at 0. Most items are on page 0.
resources = [
    RestockItem(BLACKPEARL, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 100, 10000),
    RestockItem(BLOODMOSS, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 101, 10000),
    RestockItem(GARLIC, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 102, 10000),
    RestockItem(GINSENG, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 103, 10000),
    RestockItem(MANDRAKEROOT, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 104, 10000),
    RestockItem(NIGHTSHADE, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 105, 10000),
    RestockItem(SULPHUROUSASH, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 106, 10000),
    RestockItem(SPIDERSILK, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 107, 10000),
    RestockItem(BATWING, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 108, 10000),
    RestockItem(GRAVEDUST, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 109, 10000),
    RestockItem(DAEMONBLOOD, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 110, 10000),
    RestockItem(NOXCRYSTAL, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 111, 10000),
    RestockItem(PIGIRON, RESOURCE_HUE_DEFAULT, reagentResourceBoxSerial, 112, 10000),
    RestockItem(BOARD_STATIC_ID, RESOURCE_HUE_DEFAULT, logsAndBoardsResourceBoxSerial, 107, 10000),
    RestockItem(BOARD_STATIC_ID, RESOURCE_HUE_OAK, logsAndBoardsResourceBoxSerial, 108, 10000),
    RestockItem(BOARD_STATIC_ID, RESOURCE_HUE_ASH, logsAndBoardsResourceBoxSerial, 109, 10000),
    RestockItem(BOARD_STATIC_ID, RESOURCE_HUE_YEW, logsAndBoardsResourceBoxSerial, 110, 10000),
    RestockItem(BOARD_STATIC_ID, RESOURCE_HUE_HEARTWOOD, logsAndBoardsResourceBoxSerial, 111, 10000),
    RestockItem(BOARD_STATIC_ID, RESOURCE_HUE_BLOODWOOD, logsAndBoardsResourceBoxSerial, 112, 10000),
    RestockItem(BOARD_STATIC_ID, RESOURCE_HUE_FROSTWOOD, logsAndBoardsResourceBoxSerial, 113, 10000),
    RestockItem(INGOT_STATIC_ID, RESOURCE_HUE_DEFAULT, minerResourceBoxSerial, 101, 10000),
    RestockItem(INGOT_STATIC_ID, RESOURCE_HUE_DULL_COPPER, minerResourceBoxSerial, 101, 10000),
    RestockItem(INGOT_STATIC_ID, RESOURCE_HUE_SHADOW_IRON, minerResourceBoxSerial, 102, 10000),
    RestockItem(INGOT_STATIC_ID, RESOURCE_HUE_COPPER, minerResourceBoxSerial, 103, 10000),
    RestockItem(INGOT_STATIC_ID, RESOURCE_HUE_BRONZE, minerResourceBoxSerial, 104, 10000),
    RestockItem(INGOT_STATIC_ID, RESOURCE_HUE_GOLD, minerResourceBoxSerial, 105, 10000),
    RestockItem(INGOT_STATIC_ID, RESOURCE_HUE_AGAPITE, minerResourceBoxSerial, 106, 10000),
    RestockItem(INGOT_STATIC_ID, RESOURCE_HUE_VERITE, minerResourceBoxSerial, 107, 10000),
    RestockItem(INGOT_STATIC_ID, RESOURCE_HUE_VALORITE, minerResourceBoxSerial, 108, 10000),
    RestockItem(CLOTH_STATIC_ID, RESOURCE_HUE_DEFAULT, tailorResourceBoxSerial, 111, 10000),
    RestockItem(LEATHER_STATIC_ID, RESOURCE_HUE_DEFAULT, tailorResourceBoxSerial, 100, 10000),
    RestockItem(LEATHER_STATIC_ID, RESOURCE_HUE_SPINED, tailorResourceBoxSerial, 101, 10000),
    RestockItem(LEATHER_STATIC_ID, RESOURCE_HUE_HORNED, tailorResourceBoxSerial, 102, 10000),
    RestockItem(LEATHER_STATIC_ID, RESOURCE_HUE_BARBED, tailorResourceBoxSerial, 103, 10000),
    RestockItem(CITRINE, RESOURCE_HUE_DEFAULT, mondainLegacyResourceBoxSerial, 100, 1000),
    RestockItem(EMERALD, RESOURCE_HUE_DEFAULT, mondainLegacyResourceBoxSerial, 102, 1000),
    RestockItem(TOURMALINE, RESOURCE_HUE_DEFAULT, mondainLegacyResourceBoxSerial, 104, 1000),
    RestockItem(DIAMOND, RESOURCE_HUE_DEFAULT, mondainLegacyResourceBoxSerial, 106, 1000),
    RestockItem(SAPPHIRE, RESOURCE_HUE_DEFAULT, mondainLegacyResourceBoxSerial, 108, 1000),
    RestockItem(STAR_SAPPHIRE, RESOURCE_HUE_DEFAULT, mondainLegacyResourceBoxSerial, 109, 1000),
    RestockItem(RUBY, RESOURCE_HUE_DEFAULT, mondainLegacyResourceBoxSerial, 111, 1000),
    RestockItem(AMBER, RESOURCE_HUE_DEFAULT, mondainLegacyResourceBoxSerial, 113, 1000),
    RestockItem(AMETHYST, RESOURCE_HUE_DEFAULT, mondainLegacyResourceBoxSerial, 115, 1000),
    RestockItem(WHITE_PEARL, RESOURCE_HUE_DEFAULT, mondainLegacyResourceBoxSerial, 117, 100, 2),
]

# Stand near resource boxes and load everything from a resource box into a real container.
# This is useful for use in conjunction with the BODBuilder.
# InsaneUO specific.
run_restocker(

    # Green commodity deed box. Can be any container that can hold weight though.
    commodityBoxSerial = commodityBoxSerial,
    
    # An array of RestockItem, the resources you want to stock. This is how you configure it.
    # Include only those resources you wish to stock, the hue, the amount, the  gump button id, and page.
    # Page is the page on the gump menu.
    resources = resources,
    
    # Time to wait between item moves. Adjust with caution. Reducing this will increase speed
    # of the script, but you risk disconnects and other issues maintaining state
    itemMoveDelayMs = 1000, 
    
    # (Optional) Timeout between  gump button presses. Configure based on server latency.
    gumpDelayMs = 500
)