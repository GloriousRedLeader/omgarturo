import sys

# Main code
waitTarget = 200
while True:
    mortar = Items.FindByID(3739, -1, Player.Backpack.Serial)
    Player.HeadMessage(38, 'HI')
    if Items.BackpackCount(3976) < 10:
        Misc.SendMessage('Not enough Nightshade', 34)
        Player.HeadMessage(38, 'Not enough nightshade')
        Misc.NoOperation()
    if Items.BackpackCount(3854) >= 1:
        if mortar:
            Items.UseItem(mortar)
        else:
            Misc.SendMessage('No mortar found', 34)
            Player.HeadMessage(38, 'No mortar?')
            Misc.NoOperation()
        Gumps.WaitForGump(949095101, waitTarget)
        if Player.GetSkillValue('Alchemy') < 55:
            Gumps.SendAction(949095101, 10)
            Player.HeadMessage(68, 'Making poison')
        elif Player.GetSkillValue('Poisoning') < 90:
            Gumps.SendAction(949095101, 17)
            Player.HeadMessage(68, 'Making greater poison')
        elif Player.GetSkillValue('Poisoning') < 120:
            Player.HeadMessage(68, 'Making deadly poison')
            Gumps.SendAction(949095101, 24)
        Gumps.WaitForGump(304105006, waitTarget)
    else:
        Player.HeadMessage(38, 'No bottles?')
    Misc.Pause(100)
    sys.exit()
def fill_Keg():
    make_Poison()
    for item in Player.Backpack.Contains:
        if item.ItemID == 3850:
            poisonPotion = item
        if item.ItemID == 6464:
            keg = item
    Items.Move(poisonPotion, keg, 1)
    return
if Player.GetSkillValue('Alchemy') < 30:
    Misc.SendMessage('Increase alchemy  skill from NPC')
    Misc.NoOperation()
