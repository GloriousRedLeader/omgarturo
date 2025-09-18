import sys

# Main code
while Player.GetSkillValue('Bushido') < 100:
    Misc.Pause(1)
    Bushido = Player.GetSkillValue('Bushido')
    if Bushido >= 25 and Bushido < 60 and (Player.Mana >= 10):
        Spells.CastBushido('Confidence')
        Misc.Pause(2500)
    elif Bushido >= 60 and Bushido < 77.5 and (Player.Mana >= 10):
        Spells.CastBushido('Counter Attack')
        Misc.Pause(2500)
    elif Bushido >= 77.5 and Bushido != Player.GetSkillCap('Bushido') and (Player.Mana >= 10):
        Spells.CastBushido('Evasion')
        Misc.Pause(2500)
        if Player.BuffsExist('Evasion'):
            Misc.Pause(20100)
    if Bushido == Player.GetSkillCap('Bushido'):
        Misc.SendMessage('Skill cap reached, stopping script.', 68)
        Misc.Pause(100)
        sys.exit(90)
