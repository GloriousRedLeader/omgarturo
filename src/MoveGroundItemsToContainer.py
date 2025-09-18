# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2024-03-26
# Use at your own risk. 

from Scripts.omgarturo.src.fm_core.core_player import move_item_to_container
from System.Collections.Generic import List
from System import Byte, Int32

# Scans nearby items on ground and moves them to a container.
# Prompts for destination container.

destinationSerial = Target.PromptTarget("Pick destination container", 38)

filter = Items.Filter()
filter.Movable = 1
filter.OnGround = 1
filter.RangeMax = 2
items = Items.ApplyFilter(filter)

for item in items:
    print("Moving item", item.Name)
    move_item_to_container(item, destinationSerial)   