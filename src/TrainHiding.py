# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2024-03-26
# Use at your own risk. 

# Trains hiding and stealth apparently. Good luck.

while Player.GetSkillValue("Hiding") < Player.GetSkillCap('Hiding'):
    Player.UseSkill("Hiding")
    Misc.Pause(3000)
    
while Player.GetSkillValue("Stealth") < Player.GetSkillCap('Stealth'):
    if Player.Visible:
        Target.Cancel()        
        Player.UseSkill("Hiding")
        Misc.Pause(3000)
        
    if not Player.Visible:
        Player.UseSkill("Stealth")
        Misc.Pause(3000)

    Misc.Pause(400)    