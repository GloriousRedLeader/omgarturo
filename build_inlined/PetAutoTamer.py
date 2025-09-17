# ===============================================
# Imports
# ===============================================
from System import Byte, Int32
from System.Collections.Generic import List

# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-08-25
# Use at your own risk. 


# Auto Tamer. Just tames things nearby. Nothing fancy.
# Noterieties:  blue = 1, green = 2, gray = 3, gray crim = 4, orange = 5, red = 6, yellow = 7

while True:
    pets = get_pets()
    if len(pets) < 5:
        fil = Mobiles.Filter()
        fil.Enabled = True
        fil.RangeMax = 5
        fil.Notorieties = List[Byte](bytes([3]))
        fil.IsGhost = False
        fil.Friend = False
        fil.CheckLineOfSight = True
        mobs = Mobiles.ApplyFilter(fil)
        if len(mobs) > 0:
            go_to_tile(mobs[0].Position.X, mobs[0].Position.Y, timeoutSeconds = 3,tileOffset = 0)
            
            Player.UseSkill("Animal Taming")
            Target.WaitForTarget(3000)
            Target.TargetExecute(mobs[0])
            Misc.Pause(3000)
        elif Timer.Check("tamerPingTimer") == False:
            Player.HeadMessage(68, "Waiting for critters...")
            Timer.Create("tamerPingTimer", 30000)
            
        Misc.Pause(1000)    
    else:
        Player.HeadMessage(128, "Finished Taming - No more slots available")
        Misc.Pause(1500)