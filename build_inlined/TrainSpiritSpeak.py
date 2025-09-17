# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2024-03-26
# Use at your own risk. 

# Basically just spams spirit speak over and over. You can change it below
# to use vampiric embrace which might be better. I forget.

Player.HeadMessage(38, "Training Spirit Speak")

while not Player.IsGhost and Player.GetSkillValue('Spirit Speak') < 120:
    #Player.UseSkill("Spirit Speak")
    Spells.CastNecro('Vampiric Embrace')
    
    Misc.Pause(3500) 