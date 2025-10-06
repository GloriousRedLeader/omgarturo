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

# Auto skinner
# Just storing this. 
# Original author: https://razorenhanced.net/dokuwiki/doku.php?id=toolscripts
# 2025-10-06: Made some changes so it is more aggressive now. Currently only works 
# with daggers as well.
   
dagger = Items.FindByID(DAGGER_STATIC_ID, 0, Player.Backpack.Serial, 0)
if dagger is None:
    print("You should get a dagger")
    sys.exit()

scissors = Items.FindByID(SCISSORS_GRAPHIC_ID, 0, Player.Backpack.Serial, 0)
if scissors is None:
    print("You should get some scissors")
    sys.exit()
    
def cut_leather(scissors):
    hides = Items.FindByID(PILE_OF_HIDES_STATIC_ID, -1, Player.Backpack.Serial, 0)
    if hides is not None:
        Items.UseItem(scissors)
        Target.WaitForTarget(3000)
        Target.TargetExecute(hides)
        Misc.Pause(650)

while True:
    
    skin = Items.Filter()
    skin.Enabled = True
    skin.RangeMin = 0
    skin.RangeMax = 1
    skin.IsCorpse = True
    corpses = Items.ApplyFilter(skin)
    for corpse in corpses:
        #Items.UseItem(corpse)
        #Misc.Pause(650)
        Items.UseItem(dagger)
        Target.WaitForTarget(3000)
        Target.TargetExecute(corpse)
        Misc.Pause(650)
        hides = Items.FindByID(PILE_OF_HIDES_STATIC_ID, -1, corpse.Serial, 0)
        if hides is not None and hides.Hue != 0x0000:
            Items.Move(hides, Player.Backpack.Serial, hides.Amount)
            Misc.Pause(650)
            cut_leather(scissors)

    cut_leather(scissors)
    
    Misc.Pause(250)