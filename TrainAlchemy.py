import sys

#keg = Target.PromptTarget('Select keg')

waitTarget = 200

while True:
    
    mortar = Items.FindByID(0x0E9B,-1,Player.Backpack.Serial)
    Player.HeadMessage(38, "HI")
    if Items.BackpackCount(0x0F88) < 10:
        Misc.SendMessage('Not enough Nightshade',34)
        Player.HeadMessage(38, "Not enough nightshade")
        Misc.NoOperation()
        
  
    if Items.BackpackCount(0x0F0E) >= 1:
        if mortar:
            Items.UseItem(mortar)
        else:
            Misc.SendMessage('No mortar found', 34)
            Player.HeadMessage(38, "No mortar?")
            Misc.NoOperation()
        Gumps.WaitForGump(949095101, waitTarget)

        if Player.GetSkillValue('Alchemy') < 55:
            Gumps.SendAction(949095101, 10) #poison
            Player.HeadMessage(68, "Making poison")
        elif Player.GetSkillValue('Poisoning') < 90:
            Gumps.SendAction(949095101, 17) #greater poison
            Player.HeadMessage(68, "Making greater poison")
        elif Player.GetSkillValue('Poisoning') < 120:
            Player.HeadMessage(68, "Making deadly poison")
            Gumps.SendAction(949095101, 24) #deadly poison 
            
        Gumps.WaitForGump(304105006, waitTarget)
        #Gumps.SendAction(304105006, 3) #make max
        #Gumps.WaitForGump(304105006, waitTarget)
        #Gumps.CloseGump(949095101)
    else:
        Player.HeadMessage(38, "No bottles?")

    Misc.Pause(100)
    
    sys.exit()
    
def fill_Keg():
    make_Poison()
    for item in Player.Backpack.Contains:
        if item.ItemID == 0x0F0A:
            poisonPotion = item
        if item.ItemID == 0x1940:
            keg = item
        
    Items.Move(poisonPotion, keg, 1)
    return

            



if Player.GetSkillValue('Alchemy') < 30:
    Misc.SendMessage('Increase alchemy  skill from NPC')
    Misc.NoOperation()



