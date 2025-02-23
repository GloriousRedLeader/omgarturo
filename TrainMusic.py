from Scripts.omgarturo.fm_core.core_items import INSTRUMENT_STATIC_IDS
from Scripts.omgarturo.fm_core.core_player import find_first_in_container_by_ids

Player.HeadMessage(38, "Training Musicianship")
Player.HeadMessage(38, "Make sure you have instruments in your backpack.")

while not Player.IsGhost and Player.GetSkillValue('Musicianship') < 110:
    #instrument = find_first_in_container_by_ids(INSTRUMENT_STATIC_IDS, Player.Backpack)
    instruments = Items.FindAllByID(INSTRUMENT_STATIC_IDS, -1, Player.Backpack.Serial, 0)
    for instrument in instruments:
        Items.UseItem(instrument)
        Misc.Pause(3000)