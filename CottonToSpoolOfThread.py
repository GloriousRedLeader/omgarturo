# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-01-11
# Use at your own risk. 

from System.Collections.Generic import List
from System import Byte, Int32

# Change serials. This needs work to make it usable by anyone.
# Converts cotton via a loom to spools of thread.

while True:
    items = Items.FindAllByID(0x0DF9, -1, Player.Backpack.Serial, -1, False)
    if len(items) > 0:
        Items.UseItem(items[0])
        Target.WaitForTarget(10000, False)
        Target.TargetExecute(0x40297EDA)
        Misc.Pause(5000)
    else:
        break