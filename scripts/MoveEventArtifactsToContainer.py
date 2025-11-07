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
import sys

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

ITEMS_TO_MOVE = [
    [ "of the archlich", 0x40CBB649],
    [ "swords of prosperity", 0x40442169],
    [ "of doom", 0x40DC1238],
    [ "of minax", 0x4004BF76],
    [ "fellowship insignia", 0x400E1D0C],
    [ "of the shogun", 0x4004BF75 ],
    [ "cut leather", 0x40000CFF],
    [ "dragon scales", 0x40000CFF],  
    [ "gold coin", 0x40000CFF],      
]

PAUSE_DELAY = 750

def move_items_from_container_recursive(container):
    for item in container.Contains:
        for s in ITEMS_TO_MOVE:
            if item.Name is not None and s[0].lower() in item.Name.lower():
                print("Moving ", item.Name)
                Items.Move(item, s[1], item.Amount);
                Misc.Pause(PAUSE_DELAY)
                break    
            
        if item.IsContainer:
            move_items_from_container_recursive(item)

move_items_from_container_recursive(Player.Backpack)
