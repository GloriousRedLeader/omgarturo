def drop_all_items_from_pack_animal_to_floor():
    currentNum = 0
    packAnimals = get_pets()
    if len(packAnimals) > 0:
        for packAnimal in packAnimals:
            for item in Mobiles.FindBySerial(packAnimal.Serial).Backpack.Contains:
                Player.HeadMessage(455, 'Moving item #{} {}'.format(currentNum, item.Name))
                Items.MoveOnGround(item, 0, Player.Position.X - 1, Player.Position.Y + 1, 0)
                Misc.Pause(650)
                currentNum = currentNum + 1
item = find_in_container_by_id(itemID, sourceSerial, color=color, ignoreContainer=[])
foundItem = find_in_container_by_id(itemID, containerSerial=item.Serial, color=color, ignoreContainer=ignoreContainer, recursive=recursive)
packAnimals = get_pets()
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
currentNum = currentNum + 1
drop_all_items_from_pack_animal_to_floor(packAnimalNames=['two'])
