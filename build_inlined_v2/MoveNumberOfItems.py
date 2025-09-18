from System import Byte, Int32
from System.Collections.Generic import List

# Functions
def move_item_to_container(item, destinationSerial):
    Items.Move(item, destinationSerial, item.Amount)
    Misc.Pause(800)

# Main code
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
