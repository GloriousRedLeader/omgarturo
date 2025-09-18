# Functions
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

# Main code
drop_all_items_from_pack_animal_to_floor(packAnimalNames=['two'])
