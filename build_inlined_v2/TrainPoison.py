items = items + Items.FindAllByID(itemID, -1, containerSerial, 1)
def find_all_in_container_by_id(itemID, containerSerial=Player.Backpack.Serial):
    return Items.FindAllByID(itemID, -1, containerSerial, 1)
POISON_POTION_STATIC_ID = 3850
KEG_STATIC_IDS = [6464]
def find_all_in_container_by_ids(itemIDs, containerSerial=Player.Backpack.Serial):
    items = []
    for itemID in itemIDs:
        items = items + Items.FindAllByID(itemID, -1, containerSerial, 1)
    return items
MAX_LEVEL = 120
mage = False
kegs = find_all_in_container_by_ids(KEG_STATIC_IDS, containerSerial=Player.Backpack.Serial)
for keg in kegs:
    print(keg)
weapon = Player.GetItemOnLayer('RightHand')
while Player.GetSkillValue('Poisoning') < MAX_LEVEL:
    for keg in kegs:
        poison = Items.FindByID(POISON_POTION_STATIC_ID, -1, Player.Backpack.Serial)
        if poison == None:
            Player.HeadMessage(58, 'No more poisons, making one')
            Items.UseItem(keg)
            Misc.Pause(1000)
        poison = Items.FindByID(POISON_POTION_STATIC_ID, -1, Player.Backpack.Serial)
        if poison == None:
            Player.HeadMessage(38, 'No more poisons, hopefully theres another keg')
            continue
        if mage == True:
            while Player.Poisoned:
                Spells.CastMagery('Arch Cure')
                Target.WaitForTarget(5000, True)
                Target.Self()
                Misc.Pause(1000)
                Player.EquipItem(weapon)
                Misc.Pause(1000)
            while Player.Hits < Player.HitsMax:
                Spells.CastMagery('Greater Heal')
                Target.WaitForTarget(5000, True)
                Target.Self()
                Misc.Pause(1000)
                Player.EquipItem(weapon)
                Misc.Pause(1000)
        if poison != None:
            Misc.Pause(1000)
            Player.UseSkill('Poisoning')
            Misc.Pause(1000)
            Target.WaitForTarget(10000, False)
            Target.TargetExecute(poison)
            Target.WaitForTarget(10000, False)
            Target.TargetExecute(weapon)
            Misc.Pause(8000)
