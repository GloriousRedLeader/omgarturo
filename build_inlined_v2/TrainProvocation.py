from System import Byte
from System import Byte, Int32
from System.Collections.Generic import List
import math
import sys
import time
LAP_HARP_GRAPHIC_ID = 3762
item = find_in_container_by_id(itemID, sourceSerial, color=color, ignoreContainer=[])
foundItem = find_in_container_by_id(itemID, containerSerial=item.Serial, color=color, ignoreContainer=ignoreContainer, recursive=recursive)
INSTRUMENT_STATIC_IDS = [3740, 10245, 3763, LAP_HARP_GRAPHIC_ID, 3761, 3742, 3741]
container = Items.FindBySerial(containerSerial)
def find_first_in_container_by_ids(itemIDs, containerSerial=Player.Backpack.Serial):
    for itemID in itemIDs:
        item = find_in_container_by_id(itemID, containerSerial)
        if item != None:
            return item
    return None
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
"\nAuthor: TheWarDoctor95\nOther Contributors:\nLast Contribution By: TheWarDoctor95 - March 23, 2019\n\nDescription: Uses the instruments from the player's backpack and the selected or\n    auto-selected target to train Provocation to its cap\n"
Player.HeadMessage(38, 'Training Provocation')
autoSelectTarget = True
provocationTimerMilliseconds = 10200
journalEntryDelayMilliseconds = 200
targetClearDelayMilliseconds = 200
colors = {'green': 65, 'cyan': 90, 'orange': 43, 'red': 1100, 'yellow': 52}
def GetEnemies(Mobiles, minRange=0, maxRange=12, ignoreSerial=None):
    """
    Returns a list of the nearby enemies with the specified notorieties
    """
    notorieties = List[Byte](bytes([3, 4, 5, 6]))
    if Mobiles == None:
        raise ValueError('Mobiles was not passed to GetEnemies')
    enemyFilter = Mobiles.Filter()
    enemyFilter.Enabled = True
    enemyFilter.RangeMin = minRange
    enemyFilter.RangeMax = maxRange
    enemyFilter.Notorieties = notorieties
    enemyFilter.CheckIgnoreObject = True
    enemyFilter.Friend = False
    enemies = Mobiles.ApplyFilter(enemyFilter)
    if ignoreSerial is not None:
        ignoreEnemies = [enemy for enemy in enemies if enemy.Serial == ignoreSerial]
        for ignoreEnemy in ignoreEnemies:
            enemies.Remove(ignoreEnemy)
    return enemies
def TrainProvocation():
    """
    Trains Musicianship by using the instruments in the player's bag
    Transitions to a new instrument if the one being used runs out of uses
    """
    global autoSelectTarget
    global provocationTimerMilliseconds
    Timer.Create('provocationTimer', 1)
    instrument = find_first_in_container_by_ids(INSTRUMENT_STATIC_IDS, Player.Backpack.Serial)
    if instrument == None:
        Misc.SendMessage('No instruments to train with', colors['red'])
        return
    provocationTarget = None
    while instrument != None and Player.GetSkillValue('Provocation') < 120 and (not Player.IsGhost):
        if provocationTarget == None:
            if autoSelectTarget:
                enemies = GetEnemies(Mobiles, 0, 8)
                provocationTarget = Mobiles.Select(enemies, 'Nearest')
            else:
                provocationTarget = Target.PromptTarget('Select target to train provo on')
                provocationTarget = Mobiles.FindBySerial(provocationTarget)
            if provocationTarget != None:
                Mobiles.Message(provocationTarget, colors['cyan'], 'Selected for provocation training')
        else:
            provocationTarget = Mobiles.FindBySerial(provocationTarget.Serial)
        if autoSelectTarget and provocationTarget == None:
            Misc.Pause(100)
            continue
        enemies = GetEnemies(Mobiles, 0, 12, provocationTarget.Serial)
        provocationTarget2 = None
        distanceApart = None
        for enemy in enemies:
            if provocationTarget2 is None:
                distanceApart = -1
                provocationTarget2 = enemy
            else:
                dist = math.sqrt((enemy.Position.X - provocationTarget2.Position.X) ** 2 + (enemy.Position.Y - provocationTarget2.Position.Y) ** 2)
                if dist < distanceApart:
                    distanceApart = dist
                    provocationTarget2 = enemy
        if not Timer.Check('provocationTimer') and provocationTarget is not None and (provocationTarget2 is not None):
            Journal.Clear()
            Player.UseSkill('Provocation')
            Misc.Pause(journalEntryDelayMilliseconds)
            if Journal.Search('What instrument shall you play?'):
                instrument = FindInstrument(Player.Backpack)
                if instrument == None:
                    Target.Cancel()
                    Misc.SendMessage('Ran out of instruments to train with', colors['red'])
                    return
                else:
                    Target.WaitForTarget(2000, True)
                    Target.TargetExecute(instrument.Serial)
            print('Main target ', provocationTarget.Name, '(', provocationTarget.Serial, ')')
            Target.WaitForTarget(2000, True)
            Target.TargetExecute(provocationTarget)
            print('Seco target ', provocationTarget2.Name, '(', provocationTarget2.Serial, ')')
            Target.WaitForTarget(2000, True)
            Target.TargetExecute(provocationTarget2)
            Timer.Create('provocationTimer', provocationTimerMilliseconds)
        Misc.Pause(500)
        provocationTarget = None
TrainProvocation()
