from System import Byte, Int32
from System.Collections.Generic import List

# Inlined dependencies (topologically sorted)
def move_item_to_container(item, destinationSerial):
    Items.Move(item, destinationSerial, item.Amount)
    Misc.Pause(800)

# Main code
destinationSerial = Target.PromptTarget('Pick destination container', 38)
filter = Items.Filter()
filter.Movable = 1
filter.OnGround = 1
filter.RangeMax = 2
items = Items.ApplyFilter(filter)
for item in items:
    print('Moving item', item.Name)
    move_item_to_container(item, destinationSerial)
