from System import Byte, Int32
from System.Collections.Generic import List
while True:
    items = Items.FindAllByID(3577, -1, Player.Backpack.Serial, -1, False)
    if len(items) > 0:
        Items.UseItem(items[0])
        Target.WaitForTarget(10000, False)
        Target.TargetExecute(1076461274)
        Misc.Pause(5000)
    else:
        break
