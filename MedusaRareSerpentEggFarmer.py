# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-01-11
# Use at your own risk. 

from System.Collections.Generic import List 
from System import Byte, Int32
from Scripts.omgarturo.fm_core.core_items import RARE_SERPENT_EGG_STATIC_ID
from Scripts.omgarturo.fm_core.core_items import SERPENT_NEST_STATIC_ID
from Scripts.omgarturo.fm_core.core_items import SNAKE_CHARMER_FLUTE_STATIC_ID
from Scripts.omgarturo.fm_core.core_mobiles import SILVER_SERPENT_MOBILE_ID
from Scripts.omgarturo.fm_core.core_mobiles import GIANT_SERPENT_MOBILE_ID

# Run this in the background and it will direct snakes to egg nests.
# This is to get the eggs for the Peerless boss Medusa. I think you need
# four of them. You will need one or more snake charming flutes in your inventory.
# It will look for nests and nearby snakes and then attempt to charm them to go the 
# nest. May not play nicely with other scripts.
# Will also auto loot eggs if you are within 2 tiles.
#
# My strategy: Run in and stand on a nest. Immediatley hide.
# The script works while you are hidden.

while True:
        
    if Player.IsGhost:
        break
    
    flute = Items.FindByID(SNAKE_CHARMER_FLUTE_STATIC_ID, -1, Player.Backpack.Serial, 1)
    if flute is None:
        print("Unable to find snake charmer flute. Quitting.")
        break
    
    filter = Items.Filter()
    filter.Movable = 0
    filter.OnGround = True
    filter.RangeMax = 10
    filter.Graphics = List[Int32]([SERPENT_NEST_STATIC_ID]) 
    nests = Items.ApplyFilter(filter)
    nest = Items.Select(nests, "Nearest")
    
    if nest is not None:
        if Timer.Check("nestPingTimer") == False:
            Items.Message(nest, 68, "^ nest ^")
            Timer.Create("nestPingTimer", 3500)
        fil = Mobiles.Filter()
        fil.Enabled = True
        fil.RangeMax = 10
        fil.Notorieties = List[Byte](bytes([3, 4, 5, 6]))
        fil.IsGhost = False
        fil.Friend = False
        fil.CheckLineOfSight = True
        fil.Bodies = List[Int32]([SILVER_SERPENT_MOBILE_ID, GIANT_SERPENT_MOBILE_ID]) 
        mobiles = Mobiles.ApplyFilter(fil)
        closestMobile = None
        closestMobileDistance = None
        for mobile in mobiles:
            
            distance = Misc.Distance(nest.Position.X, nest.Position.Y, mobile.Position.X, mobile.Position.Y)
            if closestMobile == None or (closestMobileDistance > distance):
                closestMobile = mobile
                closestMobileDistance = distance
        
        if closestMobile is not None and Timer.Check("snakeCharmTimer") == False:
            Items.UseItem(flute)
            Target.WaitForTarget(1000)
            Target.TargetExecute(mobile)
            Target.WaitForTarget(1000)
            Target.TargetExecute(nest)
            Timer.Create("snakeCharmTimer", 6000)
            
            
    filter = Items.Filter()
    filter.Movable = 1
    filter.OnGround = True
    filter.RangeMax = 10
    filter.Graphics = List[Int32]([RARE_SERPENT_EGG_STATIC_ID]) 
    eggs = Items.ApplyFilter(filter)

    for egg in eggs:
        if Timer.Check("eggPingTimer") == False:
            Items.Message(egg, 38, "^ egg ^")
            Timer.Create("eggPingTimer", 3500)

        if Player.DistanceTo(egg) < 3:
            Items.Move(egg, Player.Backpack.Serial, 1)
            Misc.Pause(800)
        
    Misc.Pause(500)