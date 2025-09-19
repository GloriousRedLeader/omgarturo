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

from System import Byte, Int32
from System.Collections.Generic import List

def move_item_to_container(item, destinationSerial):
    Items.Move(item, destinationSerial, item.Amount)
    Misc.Pause(800)

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

# Move x number of items from container 1 to container 2
# Enter number of items to move via chat
# Prompt for source container
# Prompt for destination container
# Moves that number of items from source to destination

print("How many items?")
Journal.Clear()
while True:
    res = Journal.GetTextByName(Player.Name)
    if len(res) > 0:
        maxNum = int(res[0])
        break
    Misc.Pause(250)    

source = Target.PromptTarget("Pick source container")
destination = Target.PromptTarget("Pick target container")

Items.UseItem(source)
Misc.Pause(650)
Items.UseItem(destination)
Misc.Pause(650)

currentNum = 0
for item in Items.FindBySerial(source).Contains:
    Player.HeadMessage(455, "Moving item #{}: {}".format(currentNum, item.Name))
    Items.Move(item, destination, item.Amount)
    Misc.Pause(650)
    if currentNum >= maxNum:
        Player.HeadMessage(455, "Done. Moved {}/{}".format(currentNum, maxNum))
        break
    currentNum = currentNum + 1 
