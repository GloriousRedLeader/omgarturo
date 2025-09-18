cnt = 0
while True:
    cnt = cnt + 1
    Mobiles.UseMobile(862)
    Gumps.WaitForGump(1280077232, 10000)
    Misc.Pause(500)
    Gumps.SendAction(1280077232, 7)
    Gumps.WaitForGump(1280077232, 10000)
    GOOD_MOBS = ['100 Wraith', '100 Spectre', '100 Bogle', '100 Shade', '100 Ghoul']
    gd = Gumps.GetGumpData(1280077232)
    print(gd)
    found = 0
    for g in gd.gumpData:
        print(g)
        for gm in GOOD_MOBS:
            if gm == g:
                found = found + 1
    if found == 3:
        print('DONE GOT IT!')
        break
    Misc.Pause(500)
    print('FOUND', found)
print('Total count', cnt)
