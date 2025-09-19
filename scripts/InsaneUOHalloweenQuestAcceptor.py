# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-09-19
# Use at your own risk.

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

cnt = 0
while True:
    cnt = cnt + 1
    Mobiles.UseMobile(0x0000035E)
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

print("Total count", cnt)
