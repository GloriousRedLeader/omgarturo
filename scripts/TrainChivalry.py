# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-09-19
# Use at your own risk.

# ##########################################################
# #                                                        #
# #                 USER EDITABLE CODE                      #
# #                                                        #
# #  This is the original script code that you can         #
# #  modify and customize. Edit the parameters, logic,     #
# #  and function calls below as needed for your setup.    #
# #                                                        #
# #  The dependencies above have been automatically        #
# #  inlined and should not be modified.                   #
# ##########################################################

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
