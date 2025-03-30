# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2024-11-14
# Use at your own risk. 

while Player.GetSkillValue("Meditation") < Player.GetSkillCap('Meditation'):
#    Items.Move(0x40592F27, 0x41095E16, 1)
#    Misc.Pause(1000)
#    Player.EquipItem(0x40592F27)
#    Misc.Pause(3000)



    Spells.CastMagery("Earthquake")
    Misc.Pause(5000)
    Player.UseSkill("Meditation")
    Misc.Pause(3000)
    while Player.BuffsExist('Meditation') and Player.Mana != Player.ManaMax:
        Misc.Pause(1000)
    



