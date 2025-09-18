# Main code
Player.HeadMessage(38, 'Training Animal Taming Using Mastery')
PET_SERIAL = 962807
while not Player.IsGhost:
    Spells.CastMastery('Combat Training')
    Target.WaitForTarget(10000, False)
    Target.TargetExecute(PET_SERIAL)
    Misc.Pause(5000)
