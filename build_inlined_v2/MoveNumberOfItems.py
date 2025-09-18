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
print('How many items?')
Journal.Clear()
while True:
    res = Journal.GetTextByName(Player.Name)
    if len(res) > 0:
        maxNum = int(res[0])
        break
    Misc.Pause(250)
source = Target.PromptTarget('Pick source container')
destination = Target.PromptTarget('Pick target container')
Items.UseItem(source)
Misc.Pause(650)
Items.UseItem(destination)
Misc.Pause(650)
currentNum = 0
for item in Items.FindBySerial(source).Contains:
    Player.HeadMessage(455, 'Moving item #{}: {}'.format(currentNum, item.Name))
    Items.Move(item, destination, item.Amount)
    Misc.Pause(650)
    if currentNum >= maxNum:
        Player.HeadMessage(455, 'Done. Moved {}/{}'.format(currentNum, maxNum))
        break
    currentNum = currentNum + 1
