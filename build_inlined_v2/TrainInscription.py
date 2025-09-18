from System.Collections.Generic import List

# Main code
GUMP_ID = 949095101
CIRCLES_3_4 = 8
TELEPORT_ID = 37
RECALL_ID = 107
CIRCLES_5_6 = 15
BLADE_SPIRITS_ID = 2
ENERGY_BOLT_ID = 65
CIRCLES_7_8 = 22
GATE_TRAVEL_ID = 23
RESURRECTION_ID = 72
stoCont = Target.PromptTarget('Target your resource chest')
Misc.Pause(100)
Items.UseItem(stoCont)
Misc.Pause(1100)
mandrakeroot = 3974
bloodmoss = 3963
sulphurousash = 3980
nightshade = 3976
blackpearl = 3962
spidersilk = 3974
ginseng = 3973
garlic = 3972
def checkRegs(reg1, reg2, reg3, reg4):
    global stoCont
    if Items.BackpackCount(reg1, 0) < 5:
        Misc.Pause(1100)
        Reg = Items.FindByID(reg1, -1, stoCont)
        Misc.Pause(100)
        Items.Move(Reg, Player.Backpack.Serial, 100)
        Misc.Pause(1100)
    if Items.BackpackCount(reg2, 0) < 5:
        Misc.Pause(1100)
        Reg = Items.FindByID(reg2, -1, stoCont)
        Misc.Pause(100)
        Items.Move(Reg, Player.Backpack.Serial, 100)
        Misc.Pause(1100)
    if Items.BackpackCount(reg3, 0) < 5:
        Misc.Pause(1100)
        Reg = Items.FindByID(reg3, -1, stoCont)
        Misc.Pause(100)
        Items.Move(Reg, Player.Backpack.Serial, 100)
        Misc.Pause(1100)
    if Items.BackpackCount(reg4, 0) < 5:
        Misc.Pause(1100)
        Reg = Items.FindByID(reg4, -1, stoCont)
        Misc.Pause(100)
        Items.Move(Reg, Player.Backpack.Serial, 100)
        Misc.Pause(1100)
    if Items.BackpackCount(3827, 0) < 5:
        Misc.Pause(1100)
        Reg = Items.FindByID(3827, 0, stoCont)
        Misc.Pause(100)
        Items.Move(Reg, Player.Backpack.Serial, 100)
        Misc.Pause(1100)
def selectCraft():
    global GUMP_ID
    global CIRCLES_3_4
    global TELEPORT_ID
    global RECALL_ID
    global CIRCLES_5_6
    global BLADE_SPIRITS_ID
    global ENERGY_BOLT_ID
    global CIRCLES_7_8
    global GATE_TRAVEL_ID
    global RESURRECTION_ID
    Inscription = Player.GetSkillValue('Inscribe')
    if Inscription < 30:
        while Player.Mana < 11:
            Player.UseSkill('Meditation')
            Misc.Pause(8100)
        checkRegs(mandrakeroot, bloodmoss, mandrakeroot, mandrakeroot)
        pen = Items.FindByID(4031, -1, Player.Backpack.Serial)
        Misc.Pause(100)
        Items.UseItem(pen)
        Gumps.WaitForGump(GUMP_ID, 10000)
        Gumps.SendAction(GUMP_ID, CIRCLES_3_4)
        Gumps.WaitForGump(GUMP_ID, 10000)
        Gumps.SendAction(GUMP_ID, TELEPORT_ID)
        Gumps.WaitForGump(GUMP_ID, 10000)
        Misc.Pause(100)
    if Inscription < 55 and Inscription >= 30:
        lastScroll = Items.FindByID(8002, -1, Player.Backpack.Serial)
        if lastScroll:
            Items.Move(lastScroll, stoCont, 0)
            Misc.Pause(1100)
        while Player.Mana < 11:
            Player.UseSkill('Meditation')
            Misc.Pause(8100)
        checkRegs(mandrakeroot, bloodmoss, blackpearl, mandrakeroot)
        pen = Items.FindByID(4031, -1, Player.Backpack.Serial)
        Misc.Pause(100)
        Items.UseItem(pen)
        Gumps.WaitForGump(GUMP_ID, 10000)
        Gumps.SendAction(GUMP_ID, CIRCLES_3_4)
        Gumps.WaitForGump(GUMP_ID, 10000)
        Gumps.SendAction(GUMP_ID, RECALL_ID)
        Gumps.WaitForGump(GUMP_ID, 10000)
        Misc.Pause(100)
    if Inscription >= 55 and Inscription < 65:
        lastScroll = Items.FindByID(8012, -1, Player.Backpack.Serial)
        if lastScroll:
            Items.Move(lastScroll, stoCont, 0)
            Misc.Pause(1100)
        while Player.Mana < 16:
            Player.UseSkill('Meditation')
            Misc.Pause(8100)
        checkRegs(mandrakeroot, nightshade, blackpearl, mandrakeroot)
        pen = Items.FindByID(4031, -1, Player.Backpack.Serial)
        Misc.Pause(100)
        Items.UseItem(pen)
        Gumps.WaitForGump(GUMP_ID, 10000)
        Gumps.SendAction(GUMP_ID, CIRCLES_5_6)
        Gumps.WaitForGump(GUMP_ID, 10000)
        Gumps.SendAction(GUMP_ID, BLADE_SPIRITS_ID)
        Gumps.WaitForGump(GUMP_ID, 10000)
        Misc.Pause(100)
    if Inscription >= 65 and Inscription < 85:
        lastScroll = Items.FindByID(8013, -1, Player.Backpack.Serial)
        if lastScroll:
            Items.Move(lastScroll, stoCont, 0)
            Misc.Pause(1100)
        while Player.Mana < 20:
            Player.UseSkill('Meditation')
            Misc.Pause(8100)
        checkRegs(blackpearl, nightshade, blackpearl, blackpearl)
        pen = Items.FindByID(4031, -1, Player.Backpack.Serial)
        Misc.Pause(100)
        Items.UseItem(pen)
        Gumps.WaitForGump(GUMP_ID, 10000)
        Gumps.SendAction(GUMP_ID, CIRCLES_5_6)
        Gumps.WaitForGump(GUMP_ID, 10000)
        Gumps.SendAction(GUMP_ID, ENERGY_BOLT_ID)
        Gumps.WaitForGump(GUMP_ID, 10000)
        Misc.Pause(100)
    if Inscription >= 85 and Inscription < 94:
        lastScroll = Items.FindByID(8022, -1, Player.Backpack.Serial)
        if lastScroll:
            Items.Move(lastScroll, stoCont, 0)
            Misc.Pause(1100)
        while Player.Mana < 40:
            Player.UseSkill('Meditation')
            Misc.Pause(8100)
        checkRegs(blackpearl, mandrakeroot, sulphurousash, sulphurousash)
        pen = Items.FindByID(4031, -1, Player.Backpack.Serial)
        Misc.Pause(100)
        Items.UseItem(pen)
        Gumps.WaitForGump(GUMP_ID, 10000)
        Gumps.SendAction(GUMP_ID, CIRCLES_7_8)
        Gumps.WaitForGump(GUMP_ID, 10000)
        Gumps.SendAction(GUMP_ID, GATE_TRAVEL_ID)
        Gumps.WaitForGump(GUMP_ID, 10000)
        Misc.Pause(100)
    if Inscription >= 94 and Inscription < 100:
        lastScroll = Items.FindByID(8032, -1, Player.Backpack.Serial)
        if lastScroll:
            Items.Move(lastScroll, stoCont, 0)
            Misc.Pause(1100)
        while Player.Mana < 50:
            Player.UseSkill('Meditation')
            Misc.Pause(8100)
        checkRegs(bloodmoss, garlic, ginseng, ginseng)
        pen = Items.FindByID(4031, -1, Player.Backpack.Serial)
        Misc.Pause(100)
        Items.UseItem(pen)
        Gumps.WaitForGump(GUMP_ID, 10000)
        Gumps.SendAction(GUMP_ID, CIRCLES_7_8)
        Gumps.WaitForGump(GUMP_ID, 10000)
        Gumps.SendAction(GUMP_ID, RESURRECTION_ID)
        Gumps.WaitForGump(GUMP_ID, 10000)
        Misc.Pause(100)
    if Inscription == Player.GetSkillCap('Inscribe'):
        lastScroll = Items.FindByID(8039, -1, Player.Backpack.Serial)
        if lastScroll:
            Items.Move(lastScroll, stoCont, 0)
            Misc.Pause(1100)
        Misc.ScriptStopAll()
    Misc.Pause(1100)
while Player.GetSkillValue('Inscribe') < Player.GetSkillCap('Inscribe'):
    selectCraft()
    Player.HeadMessage(38, 'Running Inscribe Trainer')
    Misc.Pause(1000)
