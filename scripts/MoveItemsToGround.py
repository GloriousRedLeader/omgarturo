# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-09-19
# Use at your own risk.

# ##########################################################
# #                                                        #
# #              INLINED DEPENDENCIES                      #
# #                                                        #
# #  DO NOT EDIT THIS SECTION - AUTO-GENERATED CODE        #
# #                                                        #
# #  These are dependencies from fm_core that have been    #
# #  automatically inlined. For user-editable code,        #
# #  scroll down to the bottom of this file.               #
# #                                                        #
# ##########################################################

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

# ##########################################################
# #                                                        #
# #                 USER EDITABLE CODE                      #
# #                                                        #
# #  This is the original script code that you can         #
# #  modify and customize. Edit the parameters, logic,     #
# #  and function calls below as needed for your setup.    #
# #                                                        #
# #  The dependencies above have been automatically        #
# #  inlined and should not be modified.                   #
# ##########################################################

# Provide pack animal names as an array
# Drops the contents of their backpack to the floor
# Note: Not sure if this still works.
drop_all_items_from_pack_animal_to_floor(packAnimalNames = ["two"])
