# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2024-03-26
# Use at your own risk. 

# I DID NOT WRITE THIS SCRIPT!
# Credit goes to wherever this came from. 
# Im hosting for safekeeping.
# Also, it may or may not work. I forget. Good luck.

Misc.SendMessage("Training Chiv")

while Player.GetRealSkillValue("Chivalry") < 90:
    skillValue = Player.GetRealSkillValue("Chivalry")
    
    if skillValue < 45:
        Spells.CastChivalry("Consecrate Weapon")
    elif skillValue < 60:
        Spells.CastChivalry("Divine Fury")
    elif skillValue < 70:
        Spells.CastChivalry("Enemy of One")
    elif skillValue < 90:
        Spells.CastChivalry("Holy Light")
    elif skillValue < 120:
        Spells.CastChivalry("Nobile Sacrifice")
    else:
        break
        
    Misc.Pause(2000)

Misc.SendMessage("Done training")