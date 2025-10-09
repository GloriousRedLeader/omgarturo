# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-10-08
# Use at your own risk.

# ##########################################################
# #                                                        #
# #              INLINED DEPENDENCIES                      #
# #                                                        #
# #  DO NOT EDIT THIS SECTION - AUTO-GENERATED CODE        #
# #                                                        #
# #  These are dependencies from fm_core that have been    #
# #  automatically inlined. For user-editable code,        #
# #  scroll down to the bottom of this file.               #
# #                                                        #
# ##########################################################

from System import Byte, Int32
from System.Collections.Generic import List

def get_yellows_in_range(range = 8):
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = range
    fil.Notorieties = List[Byte](bytes([7]))
    fil.IsGhost = False
    fil.Friend = False
    fil.CheckLineOfSight = False
    mobs = Mobiles.ApplyFilter(fil)

    return mobs

# ##########################################################
# #                                                        #
# #                 USER EDITABLE CODE                      #
# #                                                        #
# #  This is the original script code that you can         #
# #  modify and customize. Edit the parameters, logic,     #
# #  and function calls below as needed for your setup.    #
# #                                                        #
# #  The dependencies above have been automatically        #
# #  inlined and should not be modified.                   #
# ##########################################################

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
