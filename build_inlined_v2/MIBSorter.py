from System import Byte, Int32
from System.Collections.Generic import List
import re
import time

# Constants
PET_LEASH_STATIC_IDS = [4980]

# Functions
def get_pets(range=10, checkLineOfSight=True, mobileId=None):
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
def leash_pets():
    leash = find_first_in_container_by_ids(PET_LEASH_STATIC_IDS)
    if leash == None:
        Player.HeadMessage(38, 'You do not have a leash in backpack.')
        return False
    for pet in get_pets():
        if Player.DistanceTo(pet) <= 5:
            Items.UseItem(leash)
            Target.WaitForTarget(3000)
            Player.HeadMessage(88, 'Leashing fluffy {}'.format(pet.Name))
            Target.TargetExecute(pet)
            Misc.Pause(1000)

# Main code
SOURCE_CONTAINER_ID = Target.PromptTarget('Pick source container', 38)
WEST_CONTAINER_ID = 1074838099
CENTRAL_CONTAINER_ID = 1075775532
EAST_CONTAINER_ID = 1082135863
SCROLL_ITEM_ID = 5358
MIB_ITEM_ID = 2463
mibs = Items.FindAllByID(MIB_ITEM_ID, -1, SOURCE_CONTAINER_ID, 1)
for mib in mibs:
    Items.UseItem(mib)
    Misc.Pause(250)
scrolls = Items.FindAllByID(SCROLL_ITEM_ID, -1, SOURCE_CONTAINER_ID, 1)
for scroll in scrolls:
    for prop in scroll.Properties:
        match = re.match('(.*){1}\\:\\s\\((\\d+){1}, (\\d+){1}\\)', prop.ToString())
        if match is not None:
            facet = match.group(1)
            x = int(match.group(2))
            y = int(match.group(3))
            if facet == 'Felucca':
                if x < 1500:
                    print(facet, x, y, 'Moving to west')
                    Items.Move(scroll, WEST_CONTAINER_ID, scroll.Amount)
                elif x < 3500:
                    print(facet, x, y, 'Moving to central')
                    Items.Move(scroll, CENTRAL_CONTAINER_ID, scroll.Amount)
                else:
                    print(facet, x, y, 'Moving to east')
                    Items.Move(scroll, EAST_CONTAINER_ID, scroll.Amount)
                Misc.Pause(650)
