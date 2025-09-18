Player.HeadMessage(38, 'Training Spirit Speak')
while not Player.IsGhost and Player.GetSkillValue('Spirit Speak') < 120:
    Spells.CastNecro('Vampiric Embrace')
    Misc.Pause(3500)
