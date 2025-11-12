# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-11-12
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
import sys

BLUE_BEETLE_MOBILE_ID = 0x0317

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

        if item.IsContainer:
            move_items_from_container_recursive(item)

# Unload players
move_items_from_container_recursive(Player.Backpack)

# Unload pack animals
for packAnimal in get_pets(range = 2, checkLineOfSight = True, mobileId = BLUE_BEETLE_MOBILE_ID):
    move_items_from_container_recursive(packAnimal.Backpack)
