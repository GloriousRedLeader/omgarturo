# ===============================================
# Imports
# ===============================================
from System.Collections.Generic import List
import sys
import time

# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2024-03-26
# Use at your own risk. 


# Used this for the spellweaving quest to get fish steaks I believe. Worthless otherwise.

Player.HeadMessage(455, "start")

AMOUNT_TO_MAKE = 100

for i in range(0, AMOUNT_TO_MAKE):
    Spells.CastMagery("Create Food")    
    Misc.Pause(3000)