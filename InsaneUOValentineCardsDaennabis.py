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
    #for card in cards:
    #    print("Card", card.Name, "Color", card.Color)
    if len(cards) > 0:
        #print(cards[0].Color)
        return cards[0]
    #for card in cards:
    #    print("Card", card.Name, "Color", card.Color)
    #return Items.FindByID(0x9C14, 0x04EA, Player.Backpack.Serial, 0)

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
    

##################################################
######            In-Game Gump              ######

Misc.Pause(1000)
setX = 25 
setY = 50

def sendgump(count):
    
    status = ""
    color = 0x555
    if count >= 10:
        status = " Turn In!"
        color = 1370
    scripts = ["Valentines Event","---------------","Cards = " + str(count) + status]
    others = []
    sizeY = (len(scripts)+len(others))*30
    gd = Gumps.CreateGump(movable=True) 
    Gumps.AddPage(gd, 0)
    Gumps.AddBackground(gd, 0, 0, 150, sizeY, 30546)
    Gumps.AddAlphaRegion(gd,0, 0, 150, sizeY)
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
    
    #sendgump(countquest)
    
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
        if not queststatus:
            Mobiles.UseMobile(daniel)
            gumpid = Gumps.CurrentGump()
            Gumps.WaitForGump(gumpid, 10000)
            Gumps.SendAction(gumpid, 4)
            queststatus = True

        Gumps.SendAction(0x4c4c6db0, 0)
    else:
        print("Quitting. Stand closer to daniel!")
        break        
    
    if queststatus and (countcard > 0) and (countquest < 10) and (countcard + countquest >= 10):
        print("Quest progress {} / {} ({} cards remaining)".format(countquest, 10, countcard))
        card = findValCard()
        if card is None:
            print("Quitting. Out of cards and you dont have enough to complete quest ({}/{})".format(countquest, 10))
            break
            
        Misc.WaitForContext(Player.Serial, 10000)
        Misc.ContextReply(Player.Serial, 'toggle quest item')
        
        Target.WaitForTarget(4000, False)
        Target.TargetExecute(card)
        Misc.Pause(300)
        
        
        
        #for card in range(0, min(countcard - countquest, 10)):
        #    print("CARD", card)
        #    #c = findValCard()
        #    #print("HOOHAW", c.Name, c.Color)
        #    Target.WaitForTarget(4000, False)
        #    Target.TargetExecute(findValCard())
        #    Misc.Pause(300)
        #    #sendgump(countValCardQuest())
        Target.Cancel()
    elif countcard + countquest < 10:
        print("Quitting. Get more cards! ({}/{})".format(countquest + countcard, 10))
        break
    
        
    
    Misc.Pause(500)
    continue