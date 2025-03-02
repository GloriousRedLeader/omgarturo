from System.Collections.Generic import List
from System import Byte

def findDaniel():
    danielFilter = Mobiles.Filter()
    danielFilter.RangeMax = 2
    danielFilter.Name = "Daniel The Lonely"
    danielList = Mobiles.ApplyFilter(danielFilter)
    if danielList:
        return danielList[0]
    return None
   
def findValCard():
    cards = Items.FindAllByID(0x9C14,0x0490,Player.Backpack.Serial, 0)
    if len(cards) > 0:
        return cards[0]

def findValCard_ORIGINAL():
    valcardFilter = Items.Filter()
    valcardFilter.OnGround = 0
    valcardFilter.Name = "Lost Valentines Card"
    valcardList = Items.ApplyFilter(valcardFilter)
    #Hue filtering doesnt work here, not sure why
    if valcardList:
        for item in valcardList:
            if Items.GetPropValueString(item.Serial,"Quest Item"):
                continue
            return item
    return None

# Not Completed (purple) 1168
def countValCard():
    valcardCount = 0
    valcardCount = Items.BackpackCount(0x9C14, 0x0490)
    return valcardCount

# Completed (orange) 1258
def countValCardQuest():
    valcardquestCount = 0
    valcardquestCount = Items.BackpackCount(0x9C14, 0x04EA)
    return valcardquestCount
    
def findQuestStatus():
    #try to limit calls to this function
    Player.QuestButton()
    Misc.Pause(500)
    if Gumps.LastGumpTextExist("Lost Valentine Cards"):
        Gumps.SendAction(Gumps.CurrentGump(), 0)
        return True
    Gumps.SendAction(Gumps.CurrentGump(), 0)
    return False
    
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

def sendgump(countquest, countcard):
    
    status = ""
    color = 0x555
    if countquest >= 10:
        status = " Turn In!"
        color = 1370
    scripts = ["Valentines Event","-------------------------","Cards = " + str(countcard), "Ready for turn in = " + str(countquest)]
    others = []
    sizeY = (len(scripts)+len(others))*35
    gd = Gumps.CreateGump(movable=True) 
    Gumps.AddPage(gd, 0)
    Gumps.AddBackground(gd, 0, 0, 225, sizeY, 30546)
    Gumps.AddAlphaRegion(gd,0, 0, 225, sizeY)
    for i in range(len(scripts)):
        Gumps.AddLabel(gd,25,5+i*30,color,scripts[i])
    for i in range(len(others)):
        Gumps.AddLabel(gd,25,5+(i+len(scripts))*30,0x555,others[i])

    #Send Gump#
    Gumps.SendGump(987655, Player.Serial, setX, setY, gd.gumpDefinition, gd.gumpStrings)

##################################################
queststatus = findQuestStatus()    
print(queststatus)
while True:
    daniel = findDaniel()
    countcard = countValCard()
    countquest = countValCardQuest()
    sendgump(countquest, countcard)
    
    if daniel:
        if queststatus and countquest >= 10:
            Mobiles.UseMobile(daniel)
            gumpid = Gumps.CurrentGump()
            Gumps.WaitForGump(gumpid, 10000)
            Misc.Pause(1000)
            Gumps.SendAction(gumpid, 8)
            Misc.Pause(1000) #pause is important here, otherwise you won't get reward
            Gumps.SendAction(gumpid, 5)
            queststatus = False
            Gumps.SendAction(0x4c4c6db0, 0)
        if not queststatus:
            Mobiles.UseMobile(daniel)
            gumpid = Gumps.CurrentGump()
            Gumps.WaitForGump(gumpid, 10000)
            Gumps.SendAction(gumpid, 4)
            queststatus = True
            Gumps.SendAction(0x4c4c6db0, 0)
    
    if queststatus and (countcard > 0) and (countquest < 10) and not isPlayerInCombat(): # and (countcard + countquest >= 10):
        card = findValCard()
        if card is not None:
            Misc.WaitForContext(Player.Serial, 10000)
            Misc.ContextReply(Player.Serial, 'toggle quest item')
            Target.WaitForTarget(4000, False)
            Target.TargetExecute(card)
            Misc.Pause(300)
            Target.Cancel()
            continue

    Misc.Pause(500)