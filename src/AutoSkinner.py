# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2024-11-21
# Use at your own risk. 

from System.Collections.Generic import List
import sys
from System import Byte, Int32
from Scripts.omgarturo.src.fm_core.core_items import DAGGER_STATIC_ID
from Scripts.omgarturo.src.fm_core.core_items import LEATHER_STATIC_ID
from Scripts.omgarturo.src.fm_core.core_items import PILE_OF_HIDES_STATIC_ID
from Scripts.omgarturo.src.fm_core.core_items import SCISSORS_GRAPHIC_ID
from Scripts.omgarturo.src.fm_core.core_items import GATHERERS_PACK_GRAPHIC_ID
from Scripts.omgarturo.src.fm_core.core_items import HARVESTERS_BLADE_STATIC_ID
from Scripts.omgarturo.src.fm_core.core_rails import get_tile_in_front

# Auto skinner
# 
# Original author: https://razorenhanced.net/dokuwiki/doku.php?id=toolscripts
# 
# Mine is much worse than the original. It requires Lootmaster or at least auto open corpses
# as this script will no longer open corpses. It will attempt to carve the corpse forever.
# It only carves corpses within 1 tiles.
# You need a plain dagger.
# You need scissors.

# Store leather in a Gatherers pack if it is found. This is a container that reduces leather
# weight by 50%. It is obtained from the huntmaster challenge monthly rewards.
# This must be placed in top level of backpack.
gatherersPack = Items.FindByID(GATHERERS_PACK_GRAPHIC_ID, -1, Player.Backpack.Serial, 0)
leatherContainerSerial = gatherersPack.Serial if gatherersPack is not None else Player.Backpack.Serial
   
dagger = Items.FindByID(HARVESTERS_BLADE_STATIC_ID, -1, Player.Backpack.Serial, 0)
if dagger is None:
    print("You should get a dagger")
    sys.exit()

scissors = Items.FindByID(SCISSORS_GRAPHIC_ID, 0, Player.Backpack.Serial, 0)
if scissors is None:
    print("You should get some scissors")
    sys.exit()
    
def cut_leather(scissors, leatherContainerSerial):
    hides = Items.FindByID(PILE_OF_HIDES_STATIC_ID, -1, leatherContainerSerial, 0)
    if hides is not None:
        Items.UseItem(scissors)
        Target.WaitForTarget(1000)
        Target.TargetExecute(hides)
        Misc.Pause(100)

# Some extra stuff gets looted like meat
JUNK_TO_DISCARD = [
    "cut of raw ribs"
]

while True:
    skin = Items.Filter()
    skin.Enabled = True
    skin.RangeMin = 0
    skin.RangeMax = 2
    skin.IsCorpse = True
    corpses = Items.ApplyFilter(skin)
    for corpse in corpses:
        Items.UseItem(dagger)
        Target.WaitForTarget(1000)
        Target.TargetExecute(corpse)
        Misc.Pause(250)
        
        # Should only happen when using regular dagger
        hides = Items.FindByID(PILE_OF_HIDES_STATIC_ID, -1, corpse.Serial, 0)
        if hides is not None and hides.Hue != 0x0000:
            Items.Move(hides, leatherContainerSerial, hides.Amount)
            Misc.Pause(650)
            cut_leather(scissors, leatherContainerSerial)

    cut_leather(scissors, leatherContainerSerial)
    
    # When using harvesters blade, leather gets autolooted and added to backpack.
    # Here is where we can check if there is any cut leather in backpack and move it.
    leathers = Items.FindAllByID(LEATHER_STATIC_ID, -1, Player.Backpack.Serial, 0)
    for leather in leathers:
        if leather.Hue != 0:
            Items.Move(leather, leatherContainerSerial, leather.Amount)
            Misc.Pause(650)
        
    for item in Player.Backpack.Contains:
        for junkName in JUNK_TO_DISCARD:
            if junkName.lower() in item.Name.lower():
                print("Drop item {}".format(item.Name))
                x, y, z = get_tile_in_front(distance = 1)
                Items.MoveOnGround(item.Serial, item.Amount,x,y,z)
                Misc.Pause(750)
                break
        if item.ItemID == LEATHER_STATIC_ID and item.Hue == 0:
            print("Drop item {}".format(item.Name))
            x, y, z = get_tile_in_front(distance = 1)
            Items.MoveOnGround(item.Serial, item.Amount,x,y,z)
            Misc.Pause(750)

    Misc.Pause(250)