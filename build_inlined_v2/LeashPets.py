from System import Byte, Int32
from System.Collections.Generic import List
import time
item = find_in_container_by_id(itemID, sourceSerial, color=color, ignoreContainer=[])
PET_LEASH_STATIC_IDS = [4980]
blues = Mobiles.ApplyFilter(fil)
pet = pets[0]
foundItem = find_in_container_by_id(itemID, containerSerial=item.Serial, color=color, ignoreContainer=ignoreContainer, recursive=recursive)
pets = []
fil = Mobiles.Filter()
container = Items.FindBySerial(containerSerial)
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
leash = find_first_in_container_by_ids(PET_LEASH_STATIC_IDS)
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
pets = []
leash_pets()
