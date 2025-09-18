from System import Byte, Int32
from System.Collections.Generic import List

# Functions
def get_yellows_in_range(range=8):
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = range
    fil.Notorieties = List[Byte](bytes([7]))
    fil.IsGhost = False
    fil.Friend = False
    fil.CheckLineOfSight = False
    mobs = Mobiles.ApplyFilter(fil)
    return mobs

# Main code
TALK_CONTEXT = 5376
npcs = get_yellows_in_range(range=1)
if len(npcs) > 0:
    print(npcs[0].Name)
    Misc.UseContextMenu(npcs[0].Serial, 'Talk', 3000)
    Misc.Pause(1000)
