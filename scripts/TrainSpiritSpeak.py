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

Player.HeadMessage(38, "Training Spirit Speak")

while not Player.IsGhost and Player.GetSkillValue('Spirit Speak') < 120:
    #Player.UseSkill("Spirit Speak")
    Spells.CastNecro('Vampiric Embrace')
    
    Misc.Pause(3500) 
