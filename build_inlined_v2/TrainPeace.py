from System.Collections.Generic import List

# Constants
LAP_HARP_GRAPHIC_ID = 3762
INSTRUMENT_STATIC_IDS = [3740, 10245, 3763, LAP_HARP_GRAPHIC_ID, 3761, 3742, 3741]

# Functions
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
def find_first_in_container_by_ids(itemIDs, containerSerial=Player.Backpack.Serial):
    for itemID in itemIDs:
        item = find_in_container_by_id(itemID, containerSerial)
        if item != None:
            return item
    return None

# Main code
'\nAuthor: TheWarDoctor95\nOther Contributors:\nLast Contribution By: TheWarDoctor95 - March 23, 2019\n\nDescription: Uses the Peacemaking skill on the player to train Peacemaking to GM\n'
Player.HeadMessage(38, 'Training Peacemaking')
peacemakingTimerMilliseconds = 10200
journalEntryDelayMilliseconds = 200
targetClearDelayMilliseconds = 200
def TrainPeacemaking():
    """
    Trains Peacemaking to GM
    """
    global peacemakingTimerMilliseconds
    peacemakingHandled = False
    if Player.GetRealSkillValue('Peacemaking') == Player.GetSkillCap('Peacemaking'):
        Misc.SendMessage("You've already maxed out Peacemaking!", 65)
        return
    Timer.Create('peacemakingTimer', 1)
    Journal.Clear()
    Misc.ClearIgnore()
    while not Player.IsGhost and Player.GetRealSkillValue('Peacemaking') < Player.GetSkillCap('Peacemaking'):
        if not Timer.Check('peacemakingTimer'):
            Target.ClearLastandQueue()
            Misc.Pause(targetClearDelayMilliseconds)
            instrument = find_first_in_container_by_ids(INSTRUMENT_STATIC_IDS, Player.Backpack)
            if instrument == None:
                Misc.Message('No instrument to peacemake with.', 1100)
                return
            Items.UseItem(instrument)
            Misc.Pause(1000)
            Player.UseSkill('Peacemaking')
            Target.WaitForTarget(2000, True)
            Target.TargetExecute(Player.Serial)
            Misc.Pause(journalEntryDelayMilliseconds)
            if Journal.SearchByType('You play hypnotic music, calming your target.', 'Regular') or Journal.SearchByType('You play your hypnotic music, stopping the battle.', 'Regular') or Journal.SearchByType('You attempt to calm everyone, but fail.', 'Regular') or Journal.SearchByType('You play hypnotic music, but there is nothing in range for you to calm.', 'Regular') or Journal.SearchByType('You attempt to calm your target, but fail.', 'Regular'):
                Timer.Create('peacemakingTimer', peacemakingTimerMilliseconds)
            elif Journal.SearchByType('You have no chance of calming that creature', 'Regular'):
                Timer.Create('peacemakingTimer', 1)
            else:
                Timer.Create('peacemakingTimer', 1)
            Journal.Clear()
        Misc.Pause(50)
TrainPeacemaking()
