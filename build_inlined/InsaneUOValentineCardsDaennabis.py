# ===============================================
# Imports
# ===============================================
from System import Byte
from System.Collections.Generic import List

# By Daennabis
# Just storing at this repo for safe keeping
# https://github.com/GloriousRedLeader/omgarturo/blob/master/InsaneUOValentineCardsDaennabis.py


# This beautiful thing is useful on the InsaneUO shard during the valentine event.

def findDaniel():
    danielFilter = Mobiles.Filter()
    danielFilter.RangeMax = 2
    danielFilter.Name = "Daniel The Lonely"
    danielList = Mobiles.ApplyFilter(danielFilter)
    if danielList:
        return danielList[0]
    return None

def findValCard():
    cards = Items.FindAllByID(0x9C14, 0x0490, Player.Backpack.Serial, 0)
    if len(cards) > 0:
        return cards[0]

    
def countValCard():
    valcardCount = 0
    valcardCount = Items.BackpackCount(0x9C14, 0x0490)
    return valcardCount

def countValCardQuest():
    valcardquestCount = 0
    valcardquestCount = Items.BackpackCount(0x9C14, 0x04EA)
    return valcardquestCount

def countArrows():
    arrowsCount = 0
    arrowsCount = Items.FindByID(0x4F7A, 0x0490, Player.Backpack.Serial, True, False)
    return arrowsCount.Weight

def findQuestStatus(NPC):
    Mobiles.UseMobile(NPC)
    gumpid = Gumps.CurrentGump()
    Gumps.WaitForGump(gumpid, 10000)
    if Gumps.LastGumpTextExist("Quest Offer"):
        Gumps.SendAction(gumpid, 0)
        return False #quest not accepted
    else:
        Gumps.SendAction(gumpid, 0)
        return True #quest accepted
    
# Dont convert cards if character is possibly in combat
# No real way to determine this, but we can check hits
# to make sure we are at a reasonable health and check
# if bad buys are nearby. The reason this is here is
# potential conflict with other scripts casting spell
# and confusing the reticle.
def isPlayerInCombat():
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = 6
    fil.Notorieties = List[Byte](bytes([3,4,5,6]))
    fil.IsGhost = False
    fil.Friend = False
    fil.CheckLineOfSight = False
    mobs = Mobiles.ApplyFilter(fil)    
    return len(mobs) > 0 or Player.Hits / Player.HitsMax < 0.90



##################################################
######            In-Game Gump              ######

Misc.Pause(1000)
setX = 25 
setY = 50

def sendgump(cards,arrows):
    
    status = [""]*2
    color = [0x555]*2
    if cards >= 10:
        status[0] = " Turn In!"
        color[0] = 1370
    if arrows >= 100:
        status[1] = " Turn In!"
        color[1] = 1370
    scripts = ["Valentines Event","---------------"]
    others = ["Cards = " + str(cards) + status[0],
              "Arrows = " + str(arrows) + status[1]]
    sizeY = 10 + (len(scripts)+len(others))*20
    gd = Gumps.CreateGump(movable=True) 
    Gumps.AddPage(gd, 0)
    Gumps.AddBackground(gd, 0, 0, 150, sizeY, 30546)
    Gumps.AddAlphaRegion(gd,0, 0, 150, sizeY)
    for i in range(len(scripts)):
        Gumps.AddLabel(gd,25,5+i*20,0x555,scripts[i])
    for i in range(len(others)):
        Gumps.AddLabel(gd,25,5+(i+len(scripts))*20,color[i],others[i])

    #Send Gump#
    Gumps.SendGump(987666, Player.Serial, setX, setY, gd.gumpDefinition, gd.gumpStrings)

##################################################
queststatusd = 0
while True:
    daniel = findDaniel()
    countcard = countValCard()
    countquest = countValCardQuest()
    countarrow = countArrows()
    
    sendgump(countquest+countcard,countarrow)
#DANIEL PART
    if daniel:
        if queststatusd == 0:
            queststatusd = findQuestStatus(daniel)
            print(queststatusd)
        if queststatusd and countquest >= 10:
            Mobiles.UseMobile(daniel)
            gumpid = Gumps.CurrentGump()
            Gumps.WaitForGump(gumpid, 10000)
            Misc.Pause(1000)
            Gumps.SendAction(gumpid, 8)
            Misc.Pause(1000) #pause is important here, otherwise you won't get reward
            Gumps.SendAction(gumpid, 5)
            Gumps.SendAction(gumpid, 0)
            queststatusd = False
        if not queststatusd:
            Mobiles.UseMobile(daniel)
            gumpid = Gumps.CurrentGump()
            Gumps.WaitForGump(gumpid, 10000)
            Gumps.SendAction(gumpid, 4)
            Gumps.SendAction(gumpid, 0)
            queststatusd = True
    
    if queststatusd and (countcard > 0) and (countquest < 10) and not isPlayerInCombat(): 
        Misc.WaitForContext(Player.Serial, 10000)
        Misc.ContextReply(Player.Serial, 'toggle quest item')
        for card in range(min(countcard, 10)):
            Target.WaitForTarget(4000, False)
            Target.TargetExecute(findValCard())
            Misc.Pause(300)
        Target.Cancel()
    
    
    Misc.Pause(500)
    continue