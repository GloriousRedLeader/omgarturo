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

Player.HeadMessage(38, "Training Resisting Spells")
Player.HeadMessage(38, "NOT IMPLEMENTED YET")


while Player.GetRealSkillValue("Resisting Spells") < 100:
    skillValue = Player.GetRealSkillValue("Resisting Spells")
