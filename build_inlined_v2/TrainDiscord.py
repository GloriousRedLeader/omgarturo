from System import Byte, Int32
from System.Collections.Generic import List
import sys
import time
Misc.SendMessage('Training Discoteca')
INSTRUMENT_STATIC_IDS = [3740, 10245, 3763, 3762, 3761, 3742, 3741]
while Player.GetRealSkillValue('Discordance') < Player.GetSkillCap('Discordance'):
    Target.Cancel()
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = 8
    fil.Notorieties = List[Byte](bytes([3, 4, 5, 6]))
    fil.IsGhost = False
    fil.Friend = False
    fil.CheckLineOfSight = False
    fil.Name = 'a cu sidhe'
    mobs = Mobiles.ApplyFilter(fil)
    mob = Mobiles.Select(mobs, 'Nearest')
    if mob != None:
        instruments = Items.FindAllByID(itemids=INSTRUMENT_STATIC_IDS, color=-1, container=Player.Backpack.Serial, range=1)
        if len(instruments) > 0:
            Items.UseItem(instruments[0])
            Misc.Pause(1000)
            Player.UseSkill('Discordance')
            Target.WaitForTarget(1500)
            Target.TargetExecute(mob)
            Misc.Pause(4000)
        else:
            print('No instrument found, quitting')
            sys.exit()
    else:
        print('No monsters found')
        Misc.Pause(30000)
    Misc.Pause(1500)
