# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-09-19
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
from pathlib import Path
import __main__
import ctypes
import inspect
import os
import re
import sys
import time

ANIMATE_DEAD_MOBILE_NAMES = [
    "a gore fiend",
    "a lich",
    "a flesh golem",
    "a mummy",
    "a skeletal dragon",
    "a lich lord",
    "a skeletal knight",
    "a bone knight",
    "a skeletal mage",
    "a bone mage",
    "a patchwork skeleton",
    "a mound of maggots",
    "a wailing banshee",
    "a wraith",
    "a hellsteed",
    "a skeletal steed",
    "an Undead Gargoyle",
    "a skeletal drake",
    "a putrid undead gargoyle",
    "a blade spirit",
    "an energy vortex",
    "a skeletal drake"
]

AXE_STATIC_IDS = [0x0F49, 0x0F47]

LOG_STATIC_IDS = [0x1BDD]

TREE_STATIC_IDS = [ 0x0C95, 0x0C96, 0x0C99, 0x0C9B, 0x0C9C, 0x0C9D, 0x0C8A, 0x0CA6,
    0x0CA8, 0x0CAA, 0x0CAB, 0x0CC3, 0x0CC4, 0x0CC8, 0x0CC9, 0x0CCB,
    0x0CCC, 0x0CCD, 0x0CD0, 0x0CD3, 0x0CD6, 0x0CD8, 0x0CDA, 0x0CDD, 0x0CE0,
    0x0CE3, 0x0CE6, 0x0CF8, 0x0CFB, 0x0CFE, 0x0D01, 0x0D25, 0x0D27, 0x0D35,
    0x0D37, 0x0D38, 0x0D42, 0x0D43, 0x0D59, 0x0D70, 0x0D85, 0x0D94, 0x0D96,
    0x0D98, 0x0D9A, 0x0D9C, 0x0D9E, 0x0DA0, 0x0DA2, 0x0DA4, 0x0DA8 ]

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

def get_fc_delay (

    # Constants defined above for each spell
    baseDelayMs,
    
    # Each spell can have a different FC cap. Use constants above.
    fcCap,
    
    # Milliseonds of extra delay when computing cast time to account for internet fuzz. Fine tune this as needed.
    latencyMs = 200
):

    latency = 100
    fcOffset = 250 * (min(max(Player.FasterCasting - 2, 0), fcCap - 2) if Player.BuffsExist("Protection") else min(Player.FasterCasting, fcCap))
    delay = baseDelayMs - fcOffset
    if delay < 250:
        delay = 250
        
    #delay = delay + latencyMs
    #print("fc", Player.FasterCasting, "fcCap", fcCap, "protection", Player.BuffsExist("Protection"), "baseDelayMs", baseDelayMs, "fcOffset", fcOffset, "delay", delay)        
    return delay + latencyMs

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

def move_all_items_from_container(sourceSerial, destinationSerial):
    for item in Items.FindBySerial(sourceSerial).Contains:
        Player.HeadMessage(455, "Moving item {}".format(item.Name))
        Items.Move(item, destinationSerial, item.Amount)
        Misc.Pause(800)

def move_item_to_container(item, destinationSerial):
    Items.Move(item, destinationSerial, item.Amount)
    Misc.Pause(800)

def get_enemies(range = 10, serialsToExclude = []):
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = range
    fil.Notorieties = List[Byte](bytes([3,4,5,6]))
    fil.IsGhost = False
    fil.Friend = False
    fil.CheckLineOfSight = True
    mobs = Mobiles.ApplyFilter(fil)
    
    # need to remove Animate dead summons. There are a handfull of MobileIDs that match
    # the regular mobs, however these are red from animate dead when they are normally gray.
    if len(mobs) > 0:
        #for mob in mobs:
            #print(mob.Name, mob.Name not in ANIMATE_DEAD_MOBILE_NAMES and mob.Notoriety != 6 and mob.Serial not in serialsToExclude)
            #print("is in animate dead", mob.Name not in ANIMATE_DEAD_MOBILE_NAMES)
            
        mobsList = List[type(mobs[0])]([mob for mob in mobs if not (mob.Name in ANIMATE_DEAD_MOBILE_NAMES and mob.Notoriety == 6) and mob.Serial not in serialsToExclude])
#        if len(mobsList) == 0:
#            print("No mobs found")
        return mobsList

    return mobs

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

# Drops everything in the list below to the ground so it doesnt clutter your bags.
# Its like and inverse auto looter. Use this for all those pesky bag drops you dont want.

TRASH_NAMES = [
    "Helm of Swiftness",
    "Talon Bite",
    "Fey Leggings",
    "Soul Seeker",
    "Blade Dance",
    "Quiver of the Elements",
    "Quiver of Rage",
    "Flesh Ripper",
    "Aegis of Grace",
    "Pads of the Cu Sidhe",
    "Totem of the Void",
    "Bonesmasher",
    "Robe of the Equinox",
    "Robe of the Eclipse",
    "Righteous Anger",
    "Boomstick",
    "Bloodwood Spirit",
    "Windsong",
    "Wildfire Bow",
    "Raed's Glory",
    "Brightsight Lenses",
    "Burglar's Bandana",
    "Orcish Visage",
    "Gloves of the Pugilist",
    "Blaze of Death",
    "Arctic Death Dealer",
    "Staff of Power",
    "Violet Courage",
    "Gold Bricks",
    "Lord Blackthorn's Exemplar", # '
    "Wrath of the Dryad",
    "Jaana's Staf", #"
    "Sentinel's Guard", #'
    "a map of the known world",
    "10th Anniversary Sculpture",
    "Katrina's Crook", #'
    "Pixie Swatter",
    "Dragon's End", #'
    "Heart of the Lion",
    "Luna Lance",
    "Breastplate of Justice (Virtue Armor Set)",
    "Gorget of Honesty (Virtue Armor Set)",
    "Legs of Honor (Virtue Armor Set)",
    "Helm of Spirituality (Virtue Armor Set)",
    "Gwenno's Harp", #'
    "Sollerets of Sacrifice (Virtue Armor Set)",
    "Gauntlets of Valor (Virtue Armor Set)",
    "Arms of Compassion (Virtue Armor Set)",
    "Alchemist's Bauble", #'
    "Night's Kiss", #'
    "Bow of the Juka King",
]

Timer.Create( 'pingTimer', 1 )

while True:
    if Timer.Check( 'pingTimer' ) == False:
        Player.HeadMessage( 128, "Ground Dropper Running...")
        Timer.Create( 'pingTimer', 25000)   
        
    for trashName in TRASH_NAMES:
        item = Items.FindByName(trashName, -1, Player.Backpack.Serial, range = 0)
        if item is not None:
            print("Drop item {}".format(item.Name))
            x, y, z = get_tile_in_front(distance = 1)
            Items.MoveOnGround(item.Serial, item.Amount,x,y,z)
            Misc.Pause(750)

    Misc.Pause(1000)        
