# Main code
CAST_TIMEOUT = 700
def SelfCast(spell, wait_for_target=True):
    Spells.CastMagery(spell)
    if wait_for_target:
        Target.WaitForTarget(10000, False)
        Target.Self()
def Meditate():
    if Player.Mana != Player.ManaMax:
        Player.UseSkill('Meditation')
    Misc.Pause(3000)
    while Player.BuffsExist('Meditation') and Player.Mana != Player.ManaMax:
        Misc.Pause(1000)
while Player.GetSkillValue('Magery') < Player.GetSkillCap('Magery'):
    if Player.Mana <= 23:
        Meditate()
    elif Player.GetSkillValue('Magery') < 45:
        SelfCast('Fireball')
        Misc.Pause(CAST_TIMEOUT)
    elif Player.GetSkillValue('Magery') < 60:
        SelfCast('Mana Drain')
        Misc.Pause(CAST_TIMEOUT)
    elif Player.GetSkillValue('Magery') < 80:
        SelfCast('Reveal')
        Misc.Pause(CAST_TIMEOUT)
    elif Player.GetSkillValue('Magery') < 80:
        SelfCast('Mana Vampire')
        Misc.Pause(CAST_TIMEOUT)
    else:
        Player.HeadMessage(123, 'Casing earthquake')
        Spells.CastMagery('Earthquake')
        Misc.Pause(5000)
