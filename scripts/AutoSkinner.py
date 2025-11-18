# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-11-17
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
from ctypes import wintypes
import ctypes
import sys
import time

DAGGER_STATIC_ID = 0x0F52

GATHERERS_PACK_GRAPHIC_ID = 0xAD77

HARVESTERS_BLADE_STATIC_ID = 0x2D20

LEATHER_STATIC_ID = 0x1081

PILE_OF_HIDES_STATIC_ID = 0x1079

SCISSORS_GRAPHIC_ID = 0x0F9F

def get_tile_in_front(distance = 1):
    direction = Player.Direction
    playerX = Player.Position.X
    playerY = Player.Position.Y
    playerZ = Player.Position.Z
    
    if direction == 'Up':
        tileX = playerX - distance
        tileY = playerY - distance
        tileZ = playerZ
    elif direction == 'North':
        tileX = playerX
        tileY = playerY - distance
        tileZ = playerZ
    elif direction == 'Right':
        tileX = playerX + distance
        tileY = playerY - distance
        tileZ = playerZ
    elif direction == 'East':
        tileX = playerX + distance
        tileY = playerY
        tileZ = playerZ
    elif direction == 'Down':
        tileX = playerX + distance
        tileY = playerY + distance
        tileZ = playerZ
    elif direction == 'South':
        tileX = playerX
        tileY = playerY + distance
        tileZ = playerZ
    elif direction == 'Left':
        tileX = playerX - distance
        tileY = playerY + distance
        tileZ = playerZ
    elif direction == 'West':
        tileX = playerX - distance
        tileY = playerY
        tileZ = playerZ
    return tileX, tileY, tileZ

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

# Auto skinner
# 
# Original author: https://razorenhanced.net/dokuwiki/doku.php?id=toolscripts
# 
# Mine is much worse than the original. It requires Lootmaster or at least auto open corpses
# as this script will no longer open corpses. It will attempt to carve the corpse forever.
# It only carves corpses within 1 tiles.
# You need a plain dagger.
# You need scissors.

# Store leather in a Gatherers pack if it is found. This is a container that reduces leather
# weight by 50%. It is obtained from the huntmaster challenge monthly rewards.
# This must be placed in top level of backpack.
gatherersPack = Items.FindByID(GATHERERS_PACK_GRAPHIC_ID, -1, Player.Backpack.Serial, 0)
leatherContainerSerial = gatherersPack.Serial if gatherersPack is not None else Player.Backpack.Serial
   
dagger = Items.FindByID(HARVESTERS_BLADE_STATIC_ID, -1, Player.Backpack.Serial, 0)
if dagger is None:
    print("You should get a dagger")
    sys.exit()

scissors = Items.FindByID(SCISSORS_GRAPHIC_ID, 0, Player.Backpack.Serial, 0)
if scissors is None:
    print("You should get some scissors")
    sys.exit()
    
def cut_leather(scissors, leatherContainerSerial):
    hides = Items.FindByID(PILE_OF_HIDES_STATIC_ID, -1, leatherContainerSerial, 0)
    if hides is not None:
        Items.UseItem(scissors)
        Target.WaitForTarget(1000)
        Target.TargetExecute(hides)
        Misc.Pause(100)

# Some extra stuff gets looted like meat
JUNK_TO_DISCARD = [
    "cut of raw ribs"
]

while True:
    skin = Items.Filter()
    skin.Enabled = True
    skin.RangeMin = 0
    skin.RangeMax = 2
    skin.IsCorpse = True
    corpses = Items.ApplyFilter(skin)
    for corpse in corpses:
        Items.UseItem(dagger)
        Target.WaitForTarget(1000)
        Target.TargetExecute(corpse)
        Misc.Pause(250)
        
        # Should only happen when using regular dagger
        hides = Items.FindByID(PILE_OF_HIDES_STATIC_ID, -1, corpse.Serial, 0)
        if hides is not None and hides.Hue != 0x0000:
            Items.Move(hides, leatherContainerSerial, hides.Amount)
            Misc.Pause(650)
            cut_leather(scissors, leatherContainerSerial)

    cut_leather(scissors, leatherContainerSerial)
    
    # When using harvesters blade, leather gets autolooted and added to backpack.
    # Here is where we can check if there is any cut leather in backpack and move it.
    leathers = Items.FindAllByID(LEATHER_STATIC_ID, -1, Player.Backpack.Serial, 0)
    for leather in leathers:
        if leather.Hue != 0:
            Items.Move(leather, leatherContainerSerial, leather.Amount)
            Misc.Pause(650)
        
    for item in Player.Backpack.Contains:
        for junkName in JUNK_TO_DISCARD:
            if junkName.lower() in item.Name.lower():
                print("Drop item {}".format(item.Name))
                x, y, z = get_tile_in_front(distance = 1)
                Items.MoveOnGround(item.Serial, item.Amount,x,y,z)
                Misc.Pause(750)
                break
        if item.ItemID == LEATHER_STATIC_ID and item.Hue == 0:
            print("Drop item {}".format(item.Name))
            x, y, z = get_tile_in_front(distance = 1)
            Items.MoveOnGround(item.Serial, item.Amount,x,y,z)
            Misc.Pause(750)

    Misc.Pause(250)
