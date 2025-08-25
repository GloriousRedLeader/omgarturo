# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-08-24
# Use at your own risk. 

from System.Collections.Generic import List
from System import Byte, Int32
import sys
from Scripts.omgarturo.fm_core.core_mobiles import get_yellows_in_range
from Scripts.omgarturo.fm_core.core_items import BOD_STATIC_ID
from Scripts.omgarturo.fm_core.core_items import BOD_BOOK_STATIC_ID

# Fires the closest cannon. Loads it. Preps it. Does it forever.
# TODO: Add more cannon graphic ids

CANNON_GRAPHIC_IDS = [0x421D]
CANNON_GUMP_ID = 0x40e8c348
LOAD_TIME_MS = 10000
FIRE_TIME_MS = 5000

# We could make the loop stop when the beacon is no longer visible,
# But I might want to use this for taking out ships as well.
#PLUNDER_BEACON_GRAPHIC_ID = 0x4724

filter = Items.Filter()
filter.Graphics = List[Int32](CANNON_GRAPHIC_IDS) 
filter.OnGround = True
filter.RangeMax = 2
items = Items.ApplyFilter(filter)

if len(items) > 0:
    while True:
        # Gets the cannon gump. Side effect opens cannon container.
        Items.UseItem(items[0])
        Gumps.WaitForGump(CANNON_GUMP_ID,3000)
        
        state = Gumps.LastGumpGetLine(1)
        print(state)
        if state == "Not Charged":
            Misc.SendMessage("Loading Cannon", 123)
            Gumps.SendAction(CANNON_GUMP_ID, 1)
            Misc.Pause(LOAD_TIME_MS)
        elif state == "UNLOAD":
            Misc.SendMessage("Firing Cannon", 123)
            Gumps.SendAction(CANNON_GUMP_ID, 6)
            Misc.Pause(FIRE_TIME_MS)
        else:
            Misc.Pause(1000)
