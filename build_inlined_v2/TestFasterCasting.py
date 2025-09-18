from System import Byte, Int32
from System.Collections.Generic import List
from pathlib import Path
import __main__
import inspect
import os
import re
import sys
import time

# Constants
TREE_STATIC_IDS = [3221, 3222, 3225, 3227, 3228, 3229, 3210, 3238, 3240, 3242, 3243, 3267, 3268, 3272, 3273, 3275, 3276, 3277, 3280, 3283, 3286, 3288, 3290, 3293, 3296, 3299, 3302, 3320, 3323, 3326, 3329, 3365, 3367, 3381, 3383, 3384, 3394, 3395, 3417, 3440, 3461, 3476, 3478, 3480, 3482, 3484, 3486, 3488, 3490, 3492, 3496]
AXE_STATIC_IDS = [3913, 3911]
LOG_STATIC_IDS = [7133]
ANIMATE_DEAD_MOBILE_NAMES = ['a gore fiend', 'a lich', 'a flesh golem', 'a mummy', 'a skeletal dragon', 'a lich lord', 'a skeletal knight', 'a bone knight', 'a skeletal mage', 'a bone mage', 'a patchwork skeleton', 'a mound of maggots', 'a wailing banshee', 'a wraith', 'a hellsteed', 'a skeletal steed', 'an Undead Gargoyle', 'a skeletal drake', 'a putrid undead gargoyle', 'a blade spirit', 'an energy vortex', 'a skeletal drake']

# Functions
def get_fc_delay(baseDelayMs, fcCap, latencyMs=200):
    latency = 100
    fcOffset = 250 * (min(max(Player.FasterCasting - 2, 0), fcCap - 2) if Player.BuffsExist('Protection') else min(Player.FasterCasting, fcCap))
    delay = baseDelayMs - fcOffset
    if delay < 250:
        delay = 250
    return delay + latencyMs
def move_all_items_from_container(sourceSerial, destinationSerial):
    for item in Items.FindBySerial(sourceSerial).Contains:
        Player.HeadMessage(455, 'Moving item {}'.format(item.Name))
        Items.Move(item, destinationSerial, item.Amount)
        Misc.Pause(800)
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
def move_item_to_container(item, destinationSerial):
    Items.Move(item, destinationSerial, item.Amount)
    Misc.Pause(800)
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

# Main code
Player.HeadMessage(455, 'start fc test')
HAS_PROTECTION = Player.BuffsExist('Protection')
FC_VAL = Player.FasterCasting
for i in range(0, 10):
    Target.Cancel()
    Misc.Pause(2000)
    start = time.time()
    Spells.CastMagery('Energy Bolt')
    Target.WaitForTarget(5000)
    Target.TargetExecute(104010)
    total = time.time() - start
    print('number', i, 'fc', FC_VAL, 'protection', HAS_PROTECTION, 'total', total)
sys.exit()
Player.HeadMessage(455, 'start')
HAS_PROTECTION = Player.BuffsExist('Protection')
FC_VAL = Player.FasterCasting
mainStart = time.time()
for i in range(0, 5):
    Target.Cancel()
    Misc.Pause(2000)
    start = time.time()
    Spells.CastMagery('Energy Bolt')
    Target.WaitForTarget(5000)
    Target.TargetExecute(104010)
    total = time.time() - start
    print('number', i, 'fc', FC_VAL, 'protection', HAS_PROTECTION, 'total', total)
mainEnd = time.time() - mainStart
print(mainEnd / 5)
sys.exit()
HAS_PROTECTION = Player.BuffsExist('Protection')
FC_VAL = Player.FasterCasting
res = ' {} FC w/ Protection    ='.format(FC_VAL) if HAS_PROTECTION else ' {} FC                  ='.format(FC_VAL)
for i in range(0, 5):
    Target.Cancel()
    Misc.Pause(100)
    while Player.Mana < 30:
        Player.HeadMessage(38, 'Waiting because mana is low')
        Misc.Pause(1000)
    while Player.BuffsExist('Shield Bash'):
        Player.HeadMessage(38, 'Waiting because has buff already')
        Misc.Pause(1000)
    Misc.Pause(1000)
    start = time.time()
    Spells.CastMastery('Shield Bash')
    while not Player.BuffsExist('Shield Bash'):
        Misc.Pause(10)
    total = time.time() - start
    print('number', i, 'fc', FC_VAL, 'protection', HAS_PROTECTION, 'total', total)
    res = res + f'\t{total:.2f}'
    Misc.Pause(1500)
print(res)
sys.exit()
def get_fc_delay2(fcCap, baseDelayMs, latencyMs=100):
    latency = 100
    fcOffset = 250 * (min(max(Player.FasterCasting - 2, 0), fcCap - 2) if Player.BuffsExist('Protection') else min(Player.FasterCasting, fcCap))
    delay = baseDelayMs - fcOffset
    if delay < 250:
        delay = 250
    delay = delay + latencyMs
    print('fc', Player.FasterCasting, 'fcCap', fcCap, 'protection', Player.BuffsExist('Protection'), 'baseDelayMs', baseDelayMs, 'fcOffset', fcOffset, 'delay', delay)
    return delay
print(get_fc_delay2(4, 1000, 100))
sys.exit()
fcCap = 4
baseDelayMs = 2500
for HAS_PROTECTION in [True, False]:
    for FC_VAL in range(0, 5):
        latency = 0
        fcOffset = 250 * (min(max(FC_VAL - 2, 0), fcCap - 2) if HAS_PROTECTION else min(FC_VAL, fcCap))
        delay = baseDelayMs - fcOffset
        if delay < 250:
            delay = 250
        delay = delay + latency
        print('fc', FC_VAL, 'fcCap', fcCap, 'protection', HAS_PROTECTION, 'baseDelayMs', baseDelayMs, 'fcOffset', fcOffset, 'delay', delay)
sys.exit()
HAS_PROTECTION = Player.BuffsExist('Protection')
FC_VAL = Player.FasterCasting
res = ' {} FC w/ Protection    ='.format(FC_VAL) if HAS_PROTECTION else ' {} FC                  ='.format(FC_VAL)
for i in range(0, 5):
    Target.Cancel()
    Misc.Pause(100)
    start = time.time()
    Spells.CastSpellweaving('Wildfire')
    Target.WaitForTarget(4000)
    total = time.time() - start
    print('number', i, 'fc', FC_VAL, 'protection', HAS_PROTECTION, 'total', total)
    res = res + f'\t{total:.2f}'
    Misc.Pause(1500)
print(res)
sys.exit()
HAS_PROTECTION = Player.BuffsExist('Protection')
FC_VAL = Player.FasterCasting
res = ' {} FC w/ Protection    ='.format(FC_VAL) if HAS_PROTECTION else ' {} FC                  ='.format(FC_VAL)
for i in range(0, 5):
    Target.Cancel()
    Misc.Pause(100)
    start = time.time()
    Spells.CastMastery('Death Ray')
    Target.WaitForTarget(4000)
    total = time.time() - start
    print('number', i, 'fc', FC_VAL, 'protection', HAS_PROTECTION, 'total', total)
    res = res + f'\t{total:.2f}'
    Misc.Pause(1500)
print(res)
sys.exit()
HAS_PROTECTION = Player.BuffsExist('Protection')
FC_VAL = Player.FasterCasting
res = ' {} FC w/ Protection    ='.format(FC_VAL) if HAS_PROTECTION else ' {} FC                  ='.format(FC_VAL)
for i in range(0, 5):
    Target.Cancel()
    Misc.Pause(100)
    start = time.time()
    Spells.CastMastery('Conduit')
    Target.WaitForTarget(3000)
    total = time.time() - start
    print('number', i, 'fc', FC_VAL, 'protection', HAS_PROTECTION, 'total', total)
    res = res + f'\t{total:.2f}'
    Misc.Pause(1500)
print(res)
sys.exit()
HAS_PROTECTION = Player.BuffsExist('Protection')
FC_VAL = Player.FasterCasting
res = ' {} FC w/ Protection    ='.format(FC_VAL) if HAS_PROTECTION else ' {} FC                  ='.format(FC_VAL)
for i in range(0, 5):
    Target.Cancel()
    Misc.Pause(100)
    start = time.time()
    Spells.CastNecro('Evil Omen')
    Target.WaitForTarget(3000)
    total = time.time() - start
    print('number', i, 'fc', FC_VAL, 'protection', HAS_PROTECTION, 'total', total)
    res = res + f'\t{total:.2f}'
    Misc.Pause(1500)
print(res)
sys.exit()
HAS_PROTECTION = Player.BuffsExist('Protection')
FC_VAL = Player.FasterCasting
res = ' {} FC w/ Protection    ='.format(FC_VAL) if HAS_PROTECTION else ' {} FC                  ='.format(FC_VAL)
for i in range(0, 5):
    Target.Cancel()
    Misc.Pause(100)
    start = time.time()
    Spells.CastNecro('Poison Strike')
    Target.WaitForTarget(3000)
    total = time.time() - start
    print('number', i, 'fc', FC_VAL, 'protection', HAS_PROTECTION, 'total', total)
    res = res + f'\t{total:.2f}'
    Misc.Pause(1500)
print(res)
sys.exit()
start = time.time()
Spells.CastChivalry('Divine Fury')
while not Player.BuffsExist('Divine Fury'):
    Misc.Pause(10)
print('fc', Player.FasterCasting, 'protection', Player.BuffsExist('Protection'), 'delay', time.time() - start)
sys.exit()
start = time.time()
Spells.CastChivalry('Consecrate Weapon')
while not Player.BuffsExist('Consecrate Weapon'):
    Misc.Pause(10)
print('fc', Player.FasterCasting, 'protection', Player.BuffsExist('Protection'), 'delay', time.time() - start)
sys.exit()
start = time.time()
Spells.CastMastery('Shield Bash')
while not Player.BuffsExist('Shield Bash'):
    Misc.Pause(10)
print('Total', time.time() - start)
sys.exit()
SHIELD_BASH_FC_NO_PROTECTION_VALUES = [1100, 900, 600, 400, 300]
SHIELD_BASH_FC_YES_PROTECTION_VALUES = [1100, 1100, 1100, 800, 600]
for HAS_PROTECTION in [True, False]:
    for FC_VAL in range(0, 5):
        delay = SHIELD_BASH_FC_YES_PROTECTION_VALUES[FC_VAL] if HAS_PROTECTION else SHIELD_BASH_FC_NO_PROTECTION_VALUES[FC_VAL]
        print('fc', FC_VAL, 'protection', HAS_PROTECTION, 'delay', delay)
sys.exit()
for HAS_PROTECTION in [True, False]:
    for FC_VAL in range(0, 5):
        FC_CAP_SHIELD_BASH = 4
        baseDelayMs = 1000
        latency = 100
        fcOffset = 250 * (min(abs(FC_VAL - 2), FC_CAP_SHIELD_BASH - 2) if HAS_PROTECTION else min(FC_VAL, FC_CAP_SHIELD_BASH - 1))
        delay = baseDelayMs + latency - fcOffset
        print('fc', FC_VAL, 'protection', HAS_PROTECTION, 'delay', delay)
sys.exit()
