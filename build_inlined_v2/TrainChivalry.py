# Main code
Misc.SendMessage('Training Chiv')
while Player.GetRealSkillValue('Chivalry') < 90:
    skillValue = Player.GetRealSkillValue('Chivalry')
    if skillValue < 45:
        Spells.CastChivalry('Consecrate Weapon')
    elif skillValue < 60:
        Spells.CastChivalry('Divine Fury')
    elif skillValue < 70:
        Spells.CastChivalry('Enemy of One')
    elif skillValue < 90:
        Spells.CastChivalry('Holy Light')
    elif skillValue < 120:
        Spells.CastChivalry('Nobile Sacrifice')
    else:
        break
    Misc.Pause(2000)
Misc.SendMessage('Done training')
