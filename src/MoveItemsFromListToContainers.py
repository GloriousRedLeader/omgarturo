# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2024-11-21
# Use at your own risk. 

from System.Collections.Generic import List
import sys
from System import Byte, Int32
from Scripts.omgarturo.src.fm_core.core_mobiles import BLUE_BEETLE_MOBILE_ID
from Scripts.omgarturo.src.fm_core.core_mobiles import get_pets

# Scans backpack for "of the three", "of wildfire", etc. 
# and moves to a container. This is just a dumper script.
# I like to turn in my arties on just one char, so my other
# chars use this to offload. Too lazy to click and drag
# or even use taz uo alt + click.

BARREL_IN_FRONT_OF_HOUSE = 0x40000CFF
RESOURCE_CONTAINER = 0x408CC21E

# You can add multiple destination containers, e.g. dump coins into 
# a barrel on porch of house 1 or a chest upstairs. It will check
# for the first one in range and use that.

ITEMS_TO_MOVE = [

    # Event Arties to their own containers
    [ "of the archlich",        0x40CBB649],
    [ "swords of prosperity",   0x40442169],
    [ "of doom",                0x40DC1238],
    [ "of minax",               0x4004BF76],
    [ "fellowship insignia",    0x400E1D0C],
    [ "of the shogun",          0x4004BF75 ],
    
    # Hunting
    [ "gold coin",              BARREL_IN_FRONT_OF_HOUSE],      
    
    # Resources
    [ "ingots",                 BARREL_IN_FRONT_OF_HOUSE, RESOURCE_CONTAINER],
    [ "cut leather",            BARREL_IN_FRONT_OF_HOUSE, RESOURCE_CONTAINER],
    [ "dragon scales",          BARREL_IN_FRONT_OF_HOUSE, RESOURCE_CONTAINER],  
    [ "jade stone",             BARREL_IN_FRONT_OF_HOUSE, RESOURCE_CONTAINER],
    [ "blackrock",              BARREL_IN_FRONT_OF_HOUSE, RESOURCE_CONTAINER],
    [ "bloodwood board",        BARREL_IN_FRONT_OF_HOUSE, RESOURCE_CONTAINER],
    [ "heartwood board",        BARREL_IN_FRONT_OF_HOUSE, RESOURCE_CONTAINER],
    [ "frostwood board",        BARREL_IN_FRONT_OF_HOUSE, RESOURCE_CONTAINER],
    [ "ash board",              BARREL_IN_FRONT_OF_HOUSE, RESOURCE_CONTAINER],
    [ "oak board",              BARREL_IN_FRONT_OF_HOUSE, RESOURCE_CONTAINER],
    [ "yew board",              BARREL_IN_FRONT_OF_HOUSE, RESOURCE_CONTAINER],
    [ "brilliant amber",        BARREL_IN_FRONT_OF_HOUSE, RESOURCE_CONTAINER],
    [ "luminescent fungi",      BARREL_IN_FRONT_OF_HOUSE, RESOURCE_CONTAINER],
    [ "switch",                 BARREL_IN_FRONT_OF_HOUSE, RESOURCE_CONTAINER],
    [ "bark fragment",          BARREL_IN_FRONT_OF_HOUSE, RESOURCE_CONTAINER],
    [ "blackrock",              BARREL_IN_FRONT_OF_HOUSE, RESOURCE_CONTAINER],
    [ "parasitic plant",        BARREL_IN_FRONT_OF_HOUSE, RESOURCE_CONTAINER],
    [ "crystal shards",         BARREL_IN_FRONT_OF_HOUSE, RESOURCE_CONTAINER],
    [ "ecru citrine",           BARREL_IN_FRONT_OF_HOUSE, RESOURCE_CONTAINER],
    [ "turquoise",              BARREL_IN_FRONT_OF_HOUSE, RESOURCE_CONTAINER],
    [ "fire ruby",              BARREL_IN_FRONT_OF_HOUSE, RESOURCE_CONTAINER],
    [ "dark sapphire",          BARREL_IN_FRONT_OF_HOUSE, RESOURCE_CONTAINER],
    [ "blue diamond",           BARREL_IN_FRONT_OF_HOUSE, RESOURCE_CONTAINER],
    [ "perfect emerald",        BARREL_IN_FRONT_OF_HOUSE, RESOURCE_CONTAINER],
    [ "white pearl",            BARREL_IN_FRONT_OF_HOUSE, RESOURCE_CONTAINER],
    [ "boards",                 BARREL_IN_FRONT_OF_HOUSE, RESOURCE_CONTAINER],
    [ "toxic venom sac",        BARREL_IN_FRONT_OF_HOUSE, RESOURCE_CONTAINER],
]

PAUSE_DELAY = 750

def move_items_from_container_recursive(container):
    for item in container.Contains:
        for s in ITEMS_TO_MOVE:
            foundAndMoved = False
            if item.Name is not None and s[0].lower() in item.Name.lower():
                for destContainerSerial in s[1:]:
                    
                    destContainer = Items.FindBySerial(destContainerSerial)
                    if destContainer is not None and Player.DistanceTo(destContainer) < 2:
                        Items.Move(item, destContainerSerial, item.Amount);
                        Misc.Pause(PAUSE_DELAY)
                        foundAndMoved = True
                        break    
            if foundAndMoved:
                print(item.Name, " moved to ", destContainer.Name)
                break

        if item.IsContainer:
            move_items_from_container_recursive(item)

# Unload players
move_items_from_container_recursive(Player.Backpack)

# Unload pack animals
for packAnimal in get_pets(range = 2, checkLineOfSight = True, mobileId = BLUE_BEETLE_MOBILE_ID):
    move_items_from_container_recursive(packAnimal.Backpack)