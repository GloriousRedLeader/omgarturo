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
LOG_STATIC_IDS = [7133]
direction = Player.Direction
playerY = Player.Position.Y
container = Items.FindBySerial(containerSerial)
item = find_in_container_by_id(itemID, sourceSerial, color=color, ignoreContainer=[])
playerX = Player.Position.X
AXE_STATIC_IDS = [3913, 3911]
foundItem = find_in_container_by_id(itemID, containerSerial=item.Serial, color=color, ignoreContainer=ignoreContainer, recursive=recursive)
ANIMATE_DEAD_MOBILE_NAMES = ['a gore fiend', 'a lich', 'a flesh golem', 'a mummy', 'a skeletal dragon', 'a lich lord', 'a skeletal knight', 'a bone knight', 'a skeletal mage', 'a bone mage', 'a patchwork skeleton', 'a mound of maggots', 'a wailing banshee', 'a wraith', 'a hellsteed', 'a skeletal steed', 'an Undead Gargoyle', 'a skeletal drake', 'a putrid undead gargoyle', 'a blade spirit', 'an energy vortex', 'a skeletal drake']
fil = Mobiles.Filter()
ignoreColor = True
def find_in_container_by_id(itemID, containerSerial=Player.Backpack.Serial, color=-1, ignoreContainer=[], recursive=False):
    ignoreColor = False
    if color == -1:
        ignoreColor = True
    container = Items.FindBySerial(containerSerial)
    if isinstance(itemID, int):
        foundItem = next((item for item in container.Contains if item.ItemID == itemID and (ignoreColor or item.Hue == color)), None)
    elif isinstance(itemID, list):
        foundItem = next((item for item in container.Contains if item.ItemID in itemID and (ignoreColor or item.Hue == color)), None)
    else:
        raise ValueError('Unknown argument type for itemID passed to FindItem().', itemID, container)
    if foundItem != None:
        return foundItem
    elif recursive == True:
        for item in container.Contains:
            if item.IsContainer:
                foundItem = find_in_container_by_id(itemID, containerSerial=item.Serial, color=color, ignoreContainer=ignoreContainer, recursive=recursive)
                if foundItem != None:
                    return foundItem
tileY = playerY
TREE_STATIC_IDS = [3221, 3222, 3225, 3227, 3228, 3229, 3210, 3238, 3240, 3242, 3243, 3267, 3268, 3272, 3273, 3275, 3276, 3277, 3280, 3283, 3286, 3288, 3290, 3293, 3296, 3299, 3302, 3320, 3323, 3326, 3329, 3365, 3367, 3381, 3383, 3384, 3394, 3395, 3417, 3440, 3461, 3476, 3478, 3480, 3482, 3484, 3486, 3488, 3490, 3492, 3496]
tileX = Player.Position.X + distance
delay = 250
mobs = Mobiles.ApplyFilter(fil)
def move_item_to_container(item, destinationSerial):
    Items.Move(item, destinationSerial, item.Amount)
    Misc.Pause(800)
def get_fc_delay(baseDelayMs, fcCap, latencyMs=200):
    latency = 100
    fcOffset = 250 * (min(max(Player.FasterCasting - 2, 0), fcCap - 2) if Player.BuffsExist('Protection') else min(Player.FasterCasting, fcCap))
    delay = baseDelayMs - fcOffset
    if delay < 250:
        delay = 250
    return delay + latencyMs
tileZ = playerZ
def get_enemies(range=10, serialsToExclude=[]):
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = range
    fil.Notorieties = List[Byte](bytes([3, 4, 5, 6]))
    fil.IsGhost = False
    fil.Friend = False
    fil.CheckLineOfSight = True
    mobs = Mobiles.ApplyFilter(fil)
    if len(mobs) > 0:
        mobsList = List[type(mobs[0])]([mob for mob in mobs if not (mob.Name in ANIMATE_DEAD_MOBILE_NAMES and mob.Notoriety == 6) and mob.Serial not in serialsToExclude])
        return mobsList
    return mobs
def move_all_items_from_container(sourceSerial, destinationSerial):
    for item in Items.FindBySerial(sourceSerial).Contains:
        Player.HeadMessage(455, 'Moving item {}'.format(item.Name))
        Items.Move(item, destinationSerial, item.Amount)
        Misc.Pause(800)
mobsList = List[type(mobs[0])]([mob for mob in mobs if not (mob.Name in ANIMATE_DEAD_MOBILE_NAMES and mob.Notoriety == 6) and mob.Serial not in serialsToExclude])
fcOffset = 250 * (min(max(Player.FasterCasting - 2, 0), fcCap - 2) if Player.BuffsExist('Protection') else min(Player.FasterCasting, fcCap))
playerZ = Player.Position.Z
def get_tile_in_front(distance=1):
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
    return (tileX, tileY, tileZ)
TRASH_NAMES = ['Helm of Swiftness', 'Talon Bite', 'Fey Leggings', 'Soul Seeker', 'Blade Dance', 'Quiver of the Elements', 'Quiver of Rage', 'Flesh Ripper', 'Aegis of Grace', 'Pads of the Cu Sidhe', 'Totem of the Void', 'Bonesmasher', 'Robe of the Equinox', 'Robe of the Eclipse', 'Righteous Anger', 'Boomstick', 'Bloodwood Spirit', 'Windsong', 'Wildfire Bow', "Raed's Glory", 'Brightsight Lenses', "Burglar's Bandana", 'Orcish Visage', 'Gloves of the Pugilist', 'Blaze of Death', 'Arctic Death Dealer', 'Staff of Power', 'Violet Courage', 'Gold Bricks', "Lord Blackthorn's Exemplar", 'Wrath of the Dryad', "Jaana's Staff", "Sentinel's Guard", 'a map of the known world', '10th Anniversary Sculpture', "Katrina's Crook", 'Pixie Swatter', "Dragon's End", 'Heart of the Lion', 'Luna Lance', 'Breastplate of Justice (Virtue Armor Set)', 'Gorget of Honesty (Virtue Armor Set)', 'Legs of Honor (Virtue Armor Set)', 'Helm of Spirituality (Virtue Armor Set)', "Gwenno's Harp", 'Sollerets of Sacrifice (Virtue Armor Set)', 'Gauntlets of Valor (Virtue Armor Set)', 'Arms of Compassion (Virtue Armor Set)', "Alchemist's Bauble", "Night's Kiss", 'Bow of the Juka King']
Timer.Create('pingTimer', 1)
while True:
    if Timer.Check('pingTimer') == False:
        Player.HeadMessage(128, 'Ground Dropper Running...')
        Timer.Create('pingTimer', 25000)
    for trashName in TRASH_NAMES:
        item = Items.FindByName(trashName, -1, Player.Backpack.Serial, range=0)
        if item is not None:
            print('Drop item {}'.format(item.Name))
            x, y, z = get_tile_in_front(distance=1)
            Items.MoveOnGround(item.Serial, item.Amount, x, y, z)
            Misc.Pause(750)
    Misc.Pause(1000)
