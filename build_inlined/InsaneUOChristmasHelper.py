# ===============================================
# Imports
# ===============================================
from System import Byte, Int32
from System.Collections.Generic import List

# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2024-12-17
# Use at your own risk. 


# InsaneUO Christmas Helper
# 1. Loots stockings
# 2. Picks up snowballs and throws them at bad guys.

STOCKING_ID = 0x2BDC
SNOWMAN_SERIAL = 0x401706EE
SNOWBALL_ID = 0x0913
HOW_OFTEN_TO_PING_MS = 3000

Timer.Create( 'journalAlertPingTimer', 1 )

while True:
    
    # Stockings
    items = Items.FindAllByID(STOCKING_ID,-1, -1, 10, False)
    for item in items:
        Journal.Clear()
        Misc.WaitForContext(item.Serial, 10000)
        Misc.ContextReply(item.Serial, 0)
        Misc.Pause(750)    
        if Journal.Search("minutes before you can use this item"):  
            pass
        else:
            Player.HeadMessage(28, "Stocking used")
    
    # Snowballs
    snowballs = Items.FindAllByID(SNOWBALL_ID, -1, Player.Backpack.Serial, 1)
    if Timer.Check( 'journalAlertPingTimer' ) == False:
        Player.HeadMessage(58, "{} / 10 snowballs".format(len(snowballs)))
        Timer.Create( 'journalAlertPingTimer', HOW_OFTEN_TO_PING_MS )

    if len(snowballs) < 10:
        snowman = Items.FindBySerial(SNOWMAN_SERIAL)
        if snowman is not None:
            if Player.DistanceTo(snowman) < 15:
                Items.UseItem(snowman.Serial)
                Timer.Create( 'journalAlertPingTimer', 1 )
                Misc.Pause(100)
        
    filter = Items.Filter()
    filter.Movable = 1
    filter.OnGround = True
    filter.RangeMax = 2
    filter.Name = "Pile of Snowballs"
    items = Items.ApplyFilter(filter)
    if len(items) > 0:
        Timer.Create( 'journalAlertPingTimer', 1 )
        Items.Move(items[0], Player.Backpack.Serial, items[0].Amount)
        Misc.Pause(200)
                
    snowballs = Items.FindAllByID(SNOWBALL_ID, -1, Player.Backpack.Serial, 1)
    if len(snowballs) > 0:
        fil = Mobiles.Filter()
        fil.Name = "a wintertide spirit"
        fil.Enabled = True
        fil.RangeMax = 7
        fil.Notorieties = List[Byte](bytes([3, 4]))
        fil.IsGhost = False
        fil.Friend = False
        fil.CheckLineOfSight = False
        mobs = Mobiles.ApplyFilter(fil)
        mob = Mobiles.Select(mobs,"Nearest")

        if mob is not None:
            Items.UseItem(snowballs[0])
            Target.WaitForTarget(1000, True)
            Target.TargetExecute(mob)
            Timer.Create( 'journalAlertPingTimer', 1 )
            Misc.Pause(250)
            
    Misc.Pause(100)