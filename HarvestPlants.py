# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-08-29
# Use at your own risk. 

from System.Collections.Generic import List 
from System import Byte, Int32
from Scripts.omgarturo.fm_core.core_items import RARE_SERPENT_EGG_STATIC_ID
from Scripts.omgarturo.fm_core.core_items import SERPENT_NEST_STATIC_ID
from Scripts.omgarturo.fm_core.core_items import SNAKE_CHARMER_FLUTE_STATIC_ID
from Scripts.omgarturo.fm_core.core_mobiles import SILVER_SERPENT_MOBILE_ID
from Scripts.omgarturo.fm_core.core_mobiles import GIANT_SERPENT_MOBILE_ID

# Looks for nearby plants inside of garden beds and attempts
# to loot resources, seeds, and then sets them to decorative.
#
# Warning: Not thoroughly tested. Good luck. It matches plants to
# harvest by looking for "A Vibrant" in its name. Thats it. Not sophisticated.

# This will remove the plant and put it in your bag.
SET_TO_DECORATIVE = True

# Best if we keep this small. I suppose we could harvest the whole screen.
RANGE = 5

PLANT_GUMP =  0xa9b90129
REPRODUCTION_GUMP = 0x66e3f765
DECORATIVE_GUMP =  0xdd77bd84

filter = Items.Filter()
filter.Movable = -1
filter.OnGround = True
filter.RangeMax = RANGE
plants = Items.ApplyFilter(filter)
plants = [plant for plant in plants if "a vibrant" in plant.Name]
    
#plants = List[type(plants[0])](plants)
#plant = Items.Select(plants, "Nearest")

for plant in plants:
    print("Harvesting ", plant.Name)
    
    Items.UseItem(plant)
    Gumps.WaitForGump(PLANT_GUMP, 3000)

    # Takes you to reproduction bump
    Gumps.SendAction(PLANT_GUMP, 1) 
    Gumps.WaitForGump(REPRODUCTION_GUMP, 3000)
    
    # Harvest resources / petals
    Gumps.SendAction(REPRODUCTION_GUMP, 7) 
    Gumps.WaitForGump(REPRODUCTION_GUMP, 3000)
    
    # Get seeds
    Gumps.SendAction(REPRODUCTION_GUMP, 8) 
    Gumps.WaitForGump(REPRODUCTION_GUMP, 3000)
    
    if SET_TO_DECORATIVE:
        Gumps.SendAction(REPRODUCTION_GUMP, 2) 
        Gumps.WaitForGump(DECORATIVE_GUMP, 3000)
        
        # Confirmation yes
        Gumps.SendAction(DECORATIVE_GUMP, 3) 
        Misc.Pause(650)
    
    # Close gump
    Gumps.CloseGump(PLANT_GUMP)
    Gumps.CloseGump(REPRODUCTION_GUMP) 
    Gumps.CloseGump(DECORATIVE_GUMP) 
            
    Misc.Pause(1000)