# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/uo-razor-enhanced
#   2024-03-26
# Use at your own risk. 

from System.Collections.Generic import List
from System import Byte, Int32

# Trick or treat event. Targets nearest yellow npc and does the needful.
# Iterates through NPCs and does the trick or treat stuff.
    
fil = Mobiles.Filter()
fil.Enabled = True
fil.RangeMax = 3
fil.Notorieties = List[Byte](bytes([7]))
fil.IsGhost = False
fil.Friend = False
fil.CheckLineOfSight = False
mobs = Mobiles.ApplyFilter(fil)

mob = Mobiles.Select(mobs,"Nearest")

if mob is not None:
    #Player.HeadMessage(38, "Targeting {}".format(mob.Name))
    Player.ChatSay("trick or treat")
    Target.WaitForTarget(4000, False)
    Target.TargetExecute(mob)