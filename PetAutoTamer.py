# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-08-25
# Use at your own risk. 

from Scripts.omgarturo.fm_core.core_mobiles import get_pets
from Scripts.omgarturo.fm_core.core_mobiles import get_enemies
from Scripts.omgarturo.fm_core.core_rails import go_to_tile
from System.Collections.Generic import List
from System import Byte, Int32

# Auto Tamer. Just tames things nearby. Nothing fancy.
# Noterieties:  blue = 1, green = 2, gray = 3, gray crim = 4, orange = 5, red = 6, yellow = 7

while True:
    pets = get_pets()
    if len(pets) < 5:
        #serialsToExclude = [mob.Serial for mob in mobs])        
        #serialsToExclude = []
        #mobs = get_enemies(range = 4, serialsToExclude = serialsToExclude):
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
        Misc.Pause(1000)    
    else:
        break
        
for i in range(1, 30):
    Player.HeadMessage(128, "Finished Taming")
    Misc.Pause(250)