# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/uo-razor-enhanced
#   2024-03-26
# Use at your own risk. 

#from Scripts.omgarturo.fm_core.core_player import move_number_of_items_from_container
from Scripts.omgarturo.fm_core.core_player import move_item_to_container
from System.Collections.Generic import List
from System import Byte, Int32

# Move x number of items from container 1 to container 2
# Enter number of items to move via chat
# Prompt for source container
# Prompt for destination container
# Moves that number of items from source to destination
#move_number_of_items_from_container()

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