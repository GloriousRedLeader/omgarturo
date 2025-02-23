# GRL DID NOT WRITE THIS SCRIPT!
# Not written by me. Credit goes to wherever this came from. 
# Im hosting for safekeeping.

import sys # buy upto 40 in newhaven 3495, 2414

while Player.GetSkillValue('Bushido') < 100:
    Misc.Pause(1)
    Bushido = Player.GetSkillValue('Bushido')
    
    if Bushido >= 25 and Bushido < 60 and Player.Mana >= 10:
        Spells.CastBushido('Confidence')
        Misc.Pause(2500)
    elif Bushido >= 60 and Bushido < 77.5 and Player.Mana >= 10:
        Spells.CastBushido('Counter Attack')
        Misc.Pause(2500)
    elif Bushido >= 77.5 and Bushido != Player.GetSkillCap('Bushido') and Player.Mana >= 10:
        Spells.CastBushido('Evasion')
        Misc.Pause(2500)
        if Player.BuffsExist( 'Evasion' ):
            Misc.Pause(20100)
    if Bushido == Player.GetSkillCap('Bushido'):
        Misc.SendMessage("Skill cap reached, stopping script.",0x0044)
        Misc.Pause(100)
        sys.exit(90) 