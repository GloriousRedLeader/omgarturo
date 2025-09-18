INSTRUMENT_STATIC_IDS = [3740, 10245, 3763, 3762, 3761, 3742, 3741]
Player.HeadMessage(38, 'Training Musicianship')
Player.HeadMessage(38, 'Make sure you have instruments in your backpack.')
while not Player.IsGhost and Player.GetSkillValue('Musicianship') < 110:
    instruments = Items.FindAllByID(INSTRUMENT_STATIC_IDS, -1, Player.Backpack.Serial, 0)
    for instrument in instruments:
        Items.UseItem(instrument)
        Misc.Pause(3000)
