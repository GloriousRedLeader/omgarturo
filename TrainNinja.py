# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2024-03-26
# Use at your own risk. 

import sys

# I DID NOT WRITE THIS SCRIPT!
# Credit goes to wherever this came from. 
# Im hosting for safekeeping.
# Also, it may or may not work. I forget. Good luck.

print("Training Ninjitsu")

while Player.GetSkillValue("Ninjitsu") < Player.GetSkillCap('Ninjitsu'): 

    if Player.GetSkillValue("Ninjitsu") < 50:
        #Spells.CastNinjitsu("Animal Form")
        #Misc.Pause(2000)
        Spells.CastNinjitsu("Mirror Image")
        Misc.Pause(5000)
    elif Player.GetSkillValue("Ninjitsu") < 87:
        if Player.Visible:
            Target.Cancel()        
            Player.UseSkill("Hiding")
            Misc.Pause(3000)
            
        elif not Player.Visible: 
            Spells.CastNinjitsu("Shadowjump")
            Target.WaitForTarget(3000, False)
            print(Player.Position)
            Target.TargetExecute(Player.Position.X, Player.Position.Y + 1, Player.Position.Z, 1307)
            
        if not Player.Visible:
            Player.Walk("North")
            Player.Walk("North")
      
        if not Player.Visible:    
            Player.Walk("South")
            Player.Walk("South")
            
    elif Player.GetSkillValue("Ninjitsu") < 90:
        # had to attack guildie
        Spells.CastNinjitsu("Death Strike")
        Misc.Pause(2000)
    else:
        Spells.CastMastery("Shadow")
        
            
    Misc.Pause(400)

sys.exit()

Spells.CastNinjitsu("Shadowjump")
Target.WaitForTarget(10000, False)
Target.TargetExecute(2028, 2174 ,7 ,1307 )
#Target.TargetEx