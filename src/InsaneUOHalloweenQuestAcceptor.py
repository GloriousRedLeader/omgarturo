# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2024-03-26
# Use at your own risk. 

from Scripts.omgarturo.src.fm_core.core_mobiles import get_yellows_in_range
from System.Collections.Generic import List
from System import Byte, Int32

# The halloween quests are a PITA. This one searches for a particular combination
# of mobs to kill that are all in deceipt champ spawn (the ghouls and wraiths and such)
# Just let it run. It will stop when it gets the quest.
cnt = 0
while True:
    cnt = cnt + 1
    
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = 5
    fil.Name = "Van Helsing the Vampire Slayer"
    fil.Notorieties = List[Byte](bytes([7]))
    fil.IsGhost = False
    fil.Friend = False
    fil.CheckLineOfSight = False
    npcs = Mobiles.ApplyFilter(fil)
    
    
    if len(npcs) > 0:
        npc = npcs[0]
    
        Mobiles.UseMobile(npc)
        Gumps.WaitForGump( 0x4c4c6db0,10000)
        Misc.Pause(500)
        Gumps.SendAction(0x4c4c6db0,7)
        Gumps.WaitForGump( 0x4c4c6db0,10000)

        GOOD_MOBS = ["100 Wraith", "100 Spectre", "100 Bogle", "100 Shade", "100 Ghoul"]

        gd = Gumps.GetGumpData(0x4c4c6db0)
        print(gd)
        found = 0
        for g in gd.gumpData:
            print(g)
            for gm in GOOD_MOBS:
                if gm == g:
                    found = found + 1
                    
        if found == 3:
            print("DONE GOT IT!")
            break
                    
        Misc.Pause(500)
        print("FOUND", found)
    else:
        print("Get closer to  Van Helsing the Vampire Slayer")
        Misc.Pause(1000)
    

print("Total count", cnt)
