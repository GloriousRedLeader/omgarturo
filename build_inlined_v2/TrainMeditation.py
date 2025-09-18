# Main code
while Player.GetSkillValue('Meditation') < Player.GetSkillCap('Meditation'):
    Spells.CastMagery('Earthquake')
    Misc.Pause(5000)
    Player.UseSkill('Meditation')
    Misc.Pause(3000)
    while Player.BuffsExist('Meditation') and Player.Mana != Player.ManaMax:
        Misc.Pause(1000)
