# Main code
packAnimalSerial = Target.PromptTarget('Pick pack animal (must be in guild)')
itemSerial = Target.PromptTarget('Pick item to steal')
packAnimalBackpackSerial = Mobiles.FindBySerial(packAnimalSerial).Backpack.Serial
itemId = None
Items.UseItem(packAnimalBackpackSerial)
Misc.Pause(650)
while Player.GetSkillValue('Stealing') < Player.GetSkillCap('Stealing'):
    if itemId is None:
        item = Items.FindBySerial(itemSerial)
        if item is None:
            print('FAILED')
            Misc.Pause(1000)
            break
        else:
            itemId = item.ItemID
    item = Items.FindByID(itemId, -1, Player.Backpack.Serial, -1, False)
    if item is None:
        item = Items.FindByID(itemId, -1, packAnimalBackpackSerial, -1, False)
    if item.Container == packAnimalBackpackSerial:
        Player.UseSkill('Stealing')
        Target.WaitForTarget(300, True)
        Target.TargetExecute(item)
        print('Pausing 10s')
        Misc.Pause(10000)
    else:
        Items.Move(item, packAnimalBackpackSerial, item.Amount)
        print('Moving item back')
        Misc.Pause(1000)
