from System import Byte, Int32
from System.Collections.Generic import List
item = find_in_container_by_id(itemID, sourceSerial, color=color, ignoreContainer=[])
foundItem = find_in_container_by_id(itemID, containerSerial=item.Serial, color=color, ignoreContainer=ignoreContainer, recursive=recursive)
container = Items.FindBySerial(containerSerial)
def move_item_to_container(item, destinationSerial):
    Items.Move(item, destinationSerial, item.Amount)
    Misc.Pause(800)
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
destinationSerial = Target.PromptTarget('Pick destination container', 38)
filter = Items.Filter()
filter.Movable = 1
filter.OnGround = 1
filter.RangeMax = 2
items = Items.ApplyFilter(filter)
for item in items:
    print('Moving item', item.Name)
    move_item_to_container(item, destinationSerial)
