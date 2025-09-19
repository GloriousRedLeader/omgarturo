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

while Player.GetSkillValue('Necromancy') < Player.GetSkillCap('Necromancy'):
    Necro = Player.GetSkillValue('Necromancy')
    if Necro < 35 and Player.Mana > 7:
        Spells.CastNecro('Curse Weapon')
        Misc.Pause(2000)
        
    elif Necro >= 35 and Necro < 50 and Player.Mana > 5:
        Spells.CastNecro('Pain Spike')
        Target.WaitForTarget(4000,False)
        Target.Self()
        Misc.Pause(2000)   
   
    elif Necro >= 50 and Necro < 65  and Player.Mana > 11:
        Spells.CastNecro('Horrific Beast')
        Misc.Pause(3500)  
       
    elif Necro >= 65 and Necro < 85  and Player.Mana > 23:
        if Player.BuffsExist('Horrific Beast'):      
            Misc.Pause (400)
            Spells.CastNecro("Horrific Beast")
            Misc.Pause(3500)
        else:    
            Spells.CastNecro('Wither')
            Misc.Pause(4000)

    elif Necro >= 85 and Necro < 100  and Player.Mana > 23:
        Spells.CastNecro('Lich Form')
        Misc.Pause(4000) 

    elif Necro >= 100 and Necro != Player.GetSkillCap('Necromancy') and Player.Mana > 23:
        Spells.CastNecro('Vampiric Embrace')
        Misc.Pause(8000)         
   
    elif Necro == Player.GetSkillCap('Necromancy'):
        break
        

while True:
    SS = Player.GetSkillValue('Spirit Speak')
    if SS < Player.GetSkillCap('Spirit Speak'):
        Player.UseSkill("Spirit Speak")
        Misc.Pause(8000)
    else:
        break
