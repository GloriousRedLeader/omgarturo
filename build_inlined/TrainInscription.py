# ===============================================
# Imports
# ===============================================
from System.Collections.Generic import List

# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2024-10-16
# Use at your own risk. 

# This one was taken from here:
# https://razorenhanced.net/dokuwiki/doku.php?id=inscription
# I removed the tinkering part. Just put a bunch of pens in your
# bag and set your reagents in a chest and stand by it. 
# For raising this or any other crafting skill, you can also use the
# CraftItems script. It will create an item in a loop. Once your skill
# gets high enough, change to another recipe.

#Inscription Trainer by Frank Castle
#
#What you need:
# 1 - 30.0+ Tinkering Skill. If you do not have it buy it up. 
# 1 - 30.0+ Inscription Skill. If you do not have it buy it up.
# 2 - a player made Tinker Tools
# 3 - a chest with plenty of iron ingots, reagents, and scrolls
# 
# Written and tested on OSI. 


# Set these because gumps can be different across free shards.
# It is a pain. In any case you can get these values by hitting 
# the record button, selecting the circle, then manually creating
# a scroll You will see output like this. This is me clicking on 
# a pen, clicking on third - fourth circle, then clicking create
# recall scroll:
#
#   Items.UseItem(0x400544FA)              - Your scribe pen (ignore)
#   Gumps.WaitForGump(0x38920abd, 10000)   - Ignore
#   Gumps.SendAction(0x38920abd, 8)        - 8 = CIRCLES_3_4
#   Gumps.WaitForGump(0x38920abd, 10000)   - Ignore
#   Gumps.SendAction(0x38920abd, 107)      - 107 = RECALL_ID
#
# You will also need to get the main gump id. In the case above 
# it is 0x38920abd
#
GUMP_ID = 0x38920abd

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

mandrakeroot = 0x0F86
bloodmoss = 0x0F7B
sulphurousash = 0x0F8C
nightshade = 0x0F88
blackpearl = 0x0F7A
spidersilk = 0x0F86
ginseng = 0x0F85
garlic = 0x0F84

def checkRegs(reg1, reg2, reg3, reg4):
    
    global stoCont
    if Items.BackpackCount(reg1,0x0000) < 5:
        Misc.Pause(1100)
        Reg = Items.FindByID(reg1,-1,stoCont)
        Misc.Pause(100)
        Items.Move(Reg,Player.Backpack.Serial,100)
        Misc.Pause(1100)
        
    if Items.BackpackCount(reg2,0x0000) < 5:
        Misc.Pause(1100)
        Reg = Items.FindByID(reg2,-1,stoCont)
        Misc.Pause(100)
        Items.Move(Reg,Player.Backpack.Serial,100)
        Misc.Pause(1100)

    if Items.BackpackCount(reg3,0x0000) < 5:
        Misc.Pause(1100)
        Reg = Items.FindByID(reg3,-1,stoCont)
        Misc.Pause(100)
        Items.Move(Reg,Player.Backpack.Serial,100)
        Misc.Pause(1100)

    if Items.BackpackCount(reg4,0x0000) < 5:
        Misc.Pause(1100)
        Reg = Items.FindByID(reg4,-1,stoCont)
        Misc.Pause(100)
        Items.Move(Reg,Player.Backpack.Serial,100)
        Misc.Pause(1100)

    # scrolls
    if Items.BackpackCount(0x0EF3,0x0000) < 5:
        Misc.Pause(1100)
        Reg = Items.FindByID(0x0EF3,0x0000,stoCont)
        Misc.Pause(100)
        Items.Move(Reg,Player.Backpack.Serial,100)
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
    
    # Teleport
    if Inscription < 30:
        while Player.Mana < 11:
            Player.UseSkill('Meditation')
            Misc.Pause(8100)
        checkRegs(mandrakeroot, bloodmoss, mandrakeroot, mandrakeroot)
        pen = Items.FindByID(0x0FBF,-1,Player.Backpack.Serial)
        Misc.Pause(100)
        Items.UseItem(pen)
        Gumps.WaitForGump(GUMP_ID, 10000)
        #Gumps.SendAction(GUMP_ID, 22)   #MAKE TELEPORT
        Gumps.SendAction(GUMP_ID, CIRCLES_3_4)
        Gumps.WaitForGump(GUMP_ID, 10000)
        Gumps.SendAction(GUMP_ID, TELEPORT_ID)
        Gumps.WaitForGump(GUMP_ID, 10000)
        
        #makeLast(30, 0x1F42, mandrakeroot, bloodmoss, mandrakeroot, mandrakeroot,11)
        Misc.Pause(100)

    # Recall
    if Inscription < 55 and Inscription >= 30 :
        lastScroll = Items.FindByID(0x1F42, -1, Player.Backpack.Serial)
        if lastScroll:
            Items.Move(lastScroll,stoCont,0)
            Misc.Pause(1100)
        while Player.Mana < 11:
            Player.UseSkill('Meditation')
            Misc.Pause(8100)
        checkRegs(mandrakeroot, bloodmoss, blackpearl, mandrakeroot)
        pen = Items.FindByID(0x0FBF,-1,Player.Backpack.Serial)
        Misc.Pause(100)
        Items.UseItem(pen)
        #Gumps.WaitForGump(GUMP_ID, 10000)
        #Gumps.SendAction(GUMP_ID, 32)   #MAKE RECALL
        #makeLast(55, 0x1F4C, mandrakeroot, bloodmoss, blackpearl, mandrakeroot, 11)
        Gumps.WaitForGump(GUMP_ID, 10000)
        Gumps.SendAction(GUMP_ID, CIRCLES_3_4)
        Gumps.WaitForGump(GUMP_ID, 10000)
        Gumps.SendAction(GUMP_ID, RECALL_ID)
        Gumps.WaitForGump(GUMP_ID, 10000)
        Misc.Pause(100)        
        
    # Blade Spirits
    if Inscription >= 55 and Inscription < 65 :
        lastScroll = Items.FindByID(0x1F4C, -1, Player.Backpack.Serial)
        if lastScroll:
            Items.Move(lastScroll,stoCont,0)
            Misc.Pause(1100)
        while Player.Mana < 16:
            Player.UseSkill('Meditation')
            Misc.Pause(8100)
        checkRegs(mandrakeroot, nightshade, blackpearl, mandrakeroot)
        pen = Items.FindByID(0x0FBF,-1,Player.Backpack.Serial)
        Misc.Pause(100)
        Items.UseItem(pen)
        #Gumps.WaitForGump(GUMP_ID, 10000)
        #Gumps.SendAction(GUMP_ID, 33)   #MAKE BLADE SPIRITS
        #makeLast(65, 0x1F4D, mandrakeroot, nightshade, blackpearl, mandrakeroot, 16)
        Gumps.WaitForGump(GUMP_ID, 10000)
        Gumps.SendAction(GUMP_ID, CIRCLES_5_6)
        Gumps.WaitForGump(GUMP_ID, 10000)
        Gumps.SendAction(GUMP_ID, BLADE_SPIRITS_ID)
        Gumps.WaitForGump(GUMP_ID, 10000)
        Misc.Pause(100)
        
    # Energy bolt
    if Inscription >= 65 and Inscription < 85 :
        lastScroll = Items.FindByID(0x1F4D, -1, Player.Backpack.Serial)
        if lastScroll:
            Items.Move(lastScroll,stoCont,0)
            Misc.Pause(1100)
        while Player.Mana < 20:
            Player.UseSkill('Meditation')
            Misc.Pause(8100)
        checkRegs(blackpearl, nightshade, blackpearl, blackpearl)
        pen = Items.FindByID(0x0FBF,-1,Player.Backpack.Serial)
        Misc.Pause(100)
        Items.UseItem(pen)
        #Gumps.WaitForGump(GUMP_ID, 10000)
        #Gumps.SendAction(GUMP_ID, 42)   #MAKE ENERGY BOLT
        #makeLast(85, 0x1F56,blackpearl, nightshade, blackpearl, blackpearl, 20)
        Gumps.WaitForGump(GUMP_ID, 10000)
        Gumps.SendAction(GUMP_ID, CIRCLES_5_6)
        Gumps.WaitForGump(GUMP_ID, 10000)
        Gumps.SendAction(GUMP_ID, ENERGY_BOLT_ID)
        Gumps.WaitForGump(GUMP_ID, 10000)
        Misc.Pause(100)
        
    # Gate Travel
    if Inscription >= 85 and Inscription < 94 :
        lastScroll = Items.FindByID(0x1F56, -1, Player.Backpack.Serial)
        if lastScroll:
            Items.Move(lastScroll,stoCont,0)
            Misc.Pause(1100)
        while Player.Mana < 40:
            Player.UseSkill('Meditation')
            Misc.Pause(8100)
        checkRegs(blackpearl, mandrakeroot, sulphurousash, sulphurousash)
        pen = Items.FindByID(0x0FBF,-1,Player.Backpack.Serial)
        Misc.Pause(100)
        Items.UseItem(pen)
        #Gumps.WaitForGump(GUMP_ID, 10000)
        #Gumps.SendAction(GUMP_ID, 52)   #MAKE GATE TRAVEL
        #makeLast(94, 0x1F60, blackpearl, mandrakeroot, sulphurousash, sulphurousash, 40)
        Gumps.WaitForGump(GUMP_ID, 10000)
        Gumps.SendAction(GUMP_ID, CIRCLES_7_8)
        Gumps.WaitForGump(GUMP_ID, 10000)
        Gumps.SendAction(GUMP_ID, GATE_TRAVEL_ID)
        Gumps.WaitForGump(GUMP_ID, 10000)
        Misc.Pause(100)       
        
    # Resurrection
    if Inscription >= 94 and Inscription < 100 :
        lastScroll = Items.FindByID(0x1F60, -1, Player.Backpack.Serial)
        if lastScroll:
            Items.Move(lastScroll,stoCont,0)
            Misc.Pause(1100)
        while Player.Mana < 50:
            Player.UseSkill('Meditation')
            Misc.Pause(8100)
        checkRegs(bloodmoss, garlic, ginseng, ginseng)
        pen = Items.FindByID(0x0FBF,-1,Player.Backpack.Serial)
        Misc.Pause(100)
        Items.UseItem(pen)
        #Gumps.WaitForGump(GUMP_ID, 10000)
        #Gumps.SendAction(GUMP_ID, 59)   #MAKE RESURRECTION
        #makeLast(100 ,0x1F67, bloodmoss, garlic, ginseng, ginseng, 50)
        Gumps.WaitForGump(GUMP_ID, 10000)
        Gumps.SendAction(GUMP_ID, CIRCLES_7_8)
        Gumps.WaitForGump(GUMP_ID, 10000)
        Gumps.SendAction(GUMP_ID, RESURRECTION_ID)
        Gumps.WaitForGump(GUMP_ID, 10000)
        Misc.Pause(100) 

        
    if Inscription == Player.GetSkillCap('Inscribe'):
        lastScroll = Items.FindByID(0x1F67, -1, Player.Backpack.Serial)
        if lastScroll:
            Items.Move(lastScroll,stoCont,0)
            Misc.Pause(1100)
        Misc.ScriptStopAll()
        
    Misc.Pause(1100)

while Player.GetSkillValue("Inscribe") < Player.GetSkillCap('Inscribe'):
    selectCraft()
    Player.HeadMessage(38, "Running Inscribe Trainer")
    Misc.Pause(1000)