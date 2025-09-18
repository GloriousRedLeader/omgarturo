item = find_in_container_by_id(itemID, sourceSerial, color=color, ignoreContainer=[])
foundItem = find_in_container_by_id(itemID, containerSerial=item.Serial, color=color, ignoreContainer=ignoreContainer, recursive=recursive)
def move_all_items_from_container(sourceSerial, destinationSerial):
    for item in Items.FindBySerial(sourceSerial).Contains:
        Player.HeadMessage(455, 'Moving item {}'.format(item.Name))
        Items.Move(item, destinationSerial, item.Amount)
        Misc.Pause(800)
container = Items.FindBySerial(containerSerial)
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
sourceSerial = Target.PromptTarget('Pick source container')
destinationSerial = Target.PromptTarget('Pick target container')
Items.UseItem(sourceSerial)
Misc.Pause(650)
Items.UseItem(destinationSerial)
Misc.Pause(650)
move_all_items_from_container(sourceSerial, destinationSerial)
