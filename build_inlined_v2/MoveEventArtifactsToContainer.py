from System import Byte, Int32
from System.Collections.Generic import List
import sys

# Main code
ITEMS_TO_MOVE = [['of the archlich', 1087092297], ['swords of prosperity', 1078206825], ['of doom', 1088164408]]
PAUSE_DELAY = 750
for item in Items.FindBySerial(Player.Backpack.Serial).Contains:
    for s in ITEMS_TO_MOVE:
        if item.Name is not None and s[0].lower() in item.Name.lower():
            Misc.SendMessage('Moving ', item.Name)
            Items.Move(item, s[1], 1)
            Misc.Pause(PAUSE_DELAY)
            break
