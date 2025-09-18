# Functions
def move_item_to_container_by_id(itemID, sourceSerial, destinationSerial, color=-1):
    while True:
        item = find_in_container_by_id(itemID, sourceSerial, color=color, ignoreContainer=[])
        if item is not None:
            move_item_to_container(item, destinationSerial)
        else:
            break
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

# Main code
itemSerial = Target.PromptTarget('Which item type? Click one.')
destinationSerial = Target.PromptTarget('Pick target container')
Items.UseItem(destinationSerial)
Misc.Pause(650)
item = Items.FindBySerial(itemSerial)
if item is not None:
    sourceSerial = Items.FindBySerial(item.Container).Serial
    move_item_to_container_by_id(item.ItemID, sourceSerial, destinationSerial, item.Color)
