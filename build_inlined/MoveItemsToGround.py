# ===============================================
# Auto-generated inlined code. Do not edit
# ===============================================

# ===== Inlined block from core_player.py =====
# ---- drop_all_items_from_pack_animal_to_floor (from core_player.py)
def drop_all_items_from_pack_animal_to_floor():
    currentNum = 0        
    packAnimals = get_pets()
    if len(packAnimals) > 0:
        for packAnimal in packAnimals:
            for item in Mobiles.FindBySerial( packAnimal.Serial ).Backpack.Contains:
                Player.HeadMessage(455, "Moving item #{} {}".format(currentNum, item.Name))
                Items.MoveOnGround(item, 0, Player.Position.X - 1, Player.Position.Y + 1, 0)
                Misc.Pause(650)
                currentNum = currentNum + 1

# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2024-11-05
# Use at your own risk. 


# Provide pack animal names as an array
# Drops the contents of their backpack to the floor
# Note: Not sure if this still works.
drop_all_items_from_pack_animal_to_floor(packAnimalNames = ["two"])