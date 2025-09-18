from System import Byte, Int32
from System.Collections.Generic import List

# Main code
fil = Mobiles.Filter()
fil.Enabled = True
fil.RangeMax = 3
fil.Notorieties = List[Byte](bytes([7]))
fil.IsGhost = False
fil.Friend = False
fil.CheckLineOfSight = False
mobs = Mobiles.ApplyFilter(fil)
mob = Mobiles.Select(mobs, 'Nearest')
if mob is not None:
    Player.ChatSay('trick or treat')
    Target.WaitForTarget(4000, False)
    Target.TargetExecute(mob)
