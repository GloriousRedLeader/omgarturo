from Scripts.omgarturo.fm_core.core_items import INSTRUMENT_STATIC_IDS
from Scripts.omgarturo.fm_core.core_player import find_first_in_container_by_ids

Player.HeadMessage(38, "Training Spirit Speak")

while not Player.IsGhost and Player.GetSkillValue('Spirit Speak') < 120:
    #Player.UseSkill("Spirit Speak")
    #Misc.Pause(3000)
    
    Spells.CastNecro('Vampiric Embrace')
    Misc.Pause(3500) 