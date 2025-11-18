# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-01-11
# Use at your own risk. 

from Scripts.omgarturo.src.fm_core.core_mobiles import get_enemies

from Scripts.omgarturo.src.fm_core.core_player import move_all_items_from_container
from Scripts.omgarturo.src.fm_core.core_items import LOG_STATIC_IDS, TREE_STATIC_IDS
from Scripts.omgarturo.src.fm_core.core_player import find_in_container_by_id

from Scripts.omgarturo.src.fm_core.core_player import move_item_to_container
from Scripts.omgarturo.src.fm_core.core_spells import get_fc_delay
from System.Collections.Generic import List
import sys
from System import Byte, Int32
import time


Player.HeadMessage(455, "start fc test")


HAS_PROTECTION = Player.BuffsExist("Protection")
FC_VAL = Player.FasterCasting
for i in range(0 , 10):
    Target.Cancel()
    Misc.Pause(2000)
    
    start = time.time()
    Spells.CastMagery("Energy Bolt")
    Target.WaitForTarget(5000)
    Target.TargetExecute(0x0001964A)
    total = time.time() - start
    
    print("number", i, "fc", FC_VAL, "protection", HAS_PROTECTION, "total", total)


sys.exit()    
    
# This is just me testing faster casting. Nothing to see here.

Player.HeadMessage(455, "start")


HAS_PROTECTION = Player.BuffsExist("Protection")
FC_VAL = Player.FasterCasting

# Energy bolt test
# 3 FC / 6 FCR
# 1.75 no prot


# 0 FC / 4 FCR
# 2.25 
mainStart = time.time()
for i in range(0 , 5):
    Target.Cancel()
    Misc.Pause(2000)
    

        
    
    start = time.time()
    Spells.CastMagery("Energy Bolt")
    Target.WaitForTarget(5000)
    Target.TargetExecute(0x0001964A)
    total = time.time() - start
    
    print("number", i, "fc", FC_VAL, "protection", HAS_PROTECTION, "total", total)
    
    
mainEnd = time.time() - mainStart
print(mainEnd / 5)
sys.exit()



###############################################
# Shield Bash (1000)    UO Alive
###############################################

# 0 FC w/ Protection    =   1.56    1.63    1.55    1.62    1.61
# 1 FC w/ Protection    =   1.30    1.33    1.33    1.39    1.39
# 4 FC w/ Protection    =   0.62    0.60    0.54    0.61    0.61

# 0 FC                  =   1.13    1.11    1.14    1.14    1.16
# 4 FC                  =   0.37    0.40    0.29    0.34    0.31


HAS_PROTECTION = Player.BuffsExist("Protection")
FC_VAL = Player.FasterCasting
res = " {} FC w/ Protection    =".format(FC_VAL) if HAS_PROTECTION else " {} FC                  =".format(FC_VAL)
for i in range(0 , 5):
    Target.Cancel()
    Misc.Pause(100)
    
    while Player.Mana < 30:
        Player.HeadMessage(38, "Waiting because mana is low")
        Misc.Pause(1000)
        
    while Player.BuffsExist("Shield Bash"):
        Player.HeadMessage(38, "Waiting because has buff already")
        Misc.Pause(1000)
        
    Misc.Pause(1000)
    start = time.time()
    Spells.CastMastery("Shield Bash")
    while not Player.BuffsExist("Shield Bash"):
        Misc.Pause(10)
    
    total = time.time() - start
    print("number", i, "fc", FC_VAL, "protection", HAS_PROTECTION, "total", total)
    res = res + "\t{:.2f}".format(total)
    Misc.Pause(1500)
print(res)
sys.exit()




# Considers FC jewelry and protection spell. Add a buffer for lag.
def get_fc_delay2(
    # Each spell can have a different FC cap. Use constants above.
    fcCap,
    
    # Constants defined above for each spell
    baseDelayMs,
    
    # Milliseonds of extra delay. Fine tune this as needed.
    latencyMs = 100
):

    latency = 100
    fcOffset = 250 * (min(max(Player.FasterCasting - 2, 0), fcCap - 2) if Player.BuffsExist("Protection") else min(Player.FasterCasting, fcCap))
    delay = baseDelayMs - fcOffset
    if delay < 250:
        delay = 250
        
    delay = delay + latencyMs
    print("fc", Player.FasterCasting, "fcCap", fcCap, "protection", Player.BuffsExist("Protection"), "baseDelayMs", baseDelayMs, "fcOffset", fcOffset, "delay", delay)        
    return delay

print(get_fc_delay2(4, 1000, 100))
sys.exit()

##########################################################################
##########################################################################
############# ULTIMA FORMULA #############################################
##########################################################################
##########################################################################

fcCap = 4
baseDelayMs = 2500
for HAS_PROTECTION in [True, False]:
    for FC_VAL in range(0 , 5):
        latency = 0
        fcOffset = 250 * (min(max(FC_VAL - 2, 0), fcCap - 2) if HAS_PROTECTION else min(FC_VAL, fcCap))
        delay = baseDelayMs - fcOffset
        if delay < 250:
            delay = 250
            
        delay = delay + latency
        print("fc", FC_VAL, "fcCap", fcCap, "protection", HAS_PROTECTION, "baseDelayMs", baseDelayMs, "fcOffset", fcOffset, "delay", delay)
sys.exit()





###############################################
# Wildfire (2500)
###############################################

# 1 FC w/ Protection    =   2.53    2.52    2.53    2.52    2.53
# 2 FC w/ Protection    =   2.48    2.52    2.48    2.55    2.50
# 3 FC w/ Protection    =   2.28    2.27    2.28    2.27    2.28
# 4 FC w/ Protection    =   1.98    2.02    2.03    2.01    1.99

# 1 FC                  =   2.34    2.28    2.27    2.27    2.27
# 2 FC                  =   2.02    2.00    2.02    2.27    2.03
# 3 FC                  =   1.75    1.76    1.77    1.77    1.77
# 4 FC                  =   1.51    1.52    1.53    1.52    1.52

HAS_PROTECTION = Player.BuffsExist("Protection")
FC_VAL = Player.FasterCasting
res = " {} FC w/ Protection    =".format(FC_VAL) if HAS_PROTECTION else " {} FC                  =".format(FC_VAL)
for i in range(0 , 5):
    Target.Cancel()
    Misc.Pause(100)
    start = time.time()
    Spells.CastSpellweaving("Wildfire")
    Target.WaitForTarget(4000)
    total = time.time() - start
    print("number", i, "fc", FC_VAL, "protection", HAS_PROTECTION, "total", total)
    res = res + "\t{:.2f}".format(total)
    Misc.Pause(1500)
print(res)
sys.exit()





###############################################
# Death Ray (2250)
###############################################

# 0 FC w/ Protection    =    2.28    2.27    2.28    2.27    2.27
# 1 FC w/ Protection    =    2.24    2.27    2.27    2.27    2.27
# 2 FC w/ Protection    =    2.27    2.27    2.28    2.27    2.27
# 3 FC w/ Protection    =    2.26    2.28    2.22    2.28    2.26

# 1 FC                  =   2.03    2.01    1.98    2.02    2.02
# 2 FC                  =   1.74    1.76    1.78    1.77    1.78 
# 3 FC                  =   1.77    1.77    1.78    1.77    1.78 

HAS_PROTECTION = Player.BuffsExist("Protection")
FC_VAL = Player.FasterCasting
res = " {} FC w/ Protection    =".format(FC_VAL) if HAS_PROTECTION else " {} FC                  =".format(FC_VAL)
for i in range(0 , 5):
    Target.Cancel()
    Misc.Pause(100)
    start = time.time()
    Spells.CastMastery("Death Ray")
    Target.WaitForTarget(4000)
    total = time.time() - start
    print("number", i, "fc", FC_VAL, "protection", HAS_PROTECTION, "total", total)
    res = res + "\t{:.2f}".format(total)
    Misc.Pause(1500)
print(res)
sys.exit()




###############################################
# Conduit (2250)
###############################################

# 0 FC                  =   2.23    2.27    2.27    2.27    2.27
# 4 FC                  =  1.52    1.53    1.52    1.53    1.52

HAS_PROTECTION = Player.BuffsExist("Protection")
FC_VAL = Player.FasterCasting
res = " {} FC w/ Protection    =".format(FC_VAL) if HAS_PROTECTION else " {} FC                  =".format(FC_VAL)
for i in range(0 , 5):
    Target.Cancel()
    Misc.Pause(100)
    start = time.time()
    Spells.CastMastery("Conduit")
    Target.WaitForTarget(3000)
    total = time.time() - start
    print("number", i, "fc", FC_VAL, "protection", HAS_PROTECTION, "total", total)
    res = res + "\t{:.2f}".format(total)
    Misc.Pause(1500)
print(res)
sys.exit()



###############################################
# Evil Omen (1000)
###############################################

# 4 FC                  =   0.25    0.27    0.27    0.27    0.27

HAS_PROTECTION = Player.BuffsExist("Protection")
FC_VAL = Player.FasterCasting
res = " {} FC w/ Protection    =".format(FC_VAL) if HAS_PROTECTION else " {} FC                  =".format(FC_VAL)
for i in range(0 , 5):
    Target.Cancel()
    Misc.Pause(100)
    start = time.time()
    Spells.CastNecro("Evil Omen")
    Target.WaitForTarget(3000)
    total = time.time() - start
    print("number", i, "fc", FC_VAL, "protection", HAS_PROTECTION, "total", total)
    res = res + "\t{:.2f}".format(total)
    Misc.Pause(1500)
print(res)
sys.exit()




###############################################
# Poison Strike Test (2000)
###############################################

# 0 FC w/ Protection    =    2.02    2.02    2.02    2.02    2.03
# 2 FC w/ Protection    =   2.01    2.02    2.02    2.02    2.02
# 3 FC w/ Protection    =   1.76    1.76    1.78    1.77    1.78
# 4 FC w/ Protection    =   1.78    1.77    1.77    1.78    1.75

# 0 FC                  =   2.02    2.02    2.02    2.02    1.98
# 1 FC                  =   1.73    1.77    1.78    1.78    1.77
# 2 FC                  =   1.54    1.53    1.60    1.52    1.52
# 3 FC                  =   1.26    1.27    1.27    1.27    1.27
# 4 FC                  =   1.23    1.27    1.28    1.27    1.28

HAS_PROTECTION = Player.BuffsExist("Protection")
FC_VAL = Player.FasterCasting
res = " {} FC w/ Protection    =".format(FC_VAL) if HAS_PROTECTION else " {} FC                  =".format(FC_VAL)
for i in range(0 , 5):
    Target.Cancel()
    Misc.Pause(100)
    start = time.time()
    Spells.CastNecro("Poison Strike")
    Target.WaitForTarget(3000)
    total = time.time() - start
    print("number", i, "fc", FC_VAL, "protection", HAS_PROTECTION, "total", total)
    res = res + "\t{:.2f}".format(total)
    Misc.Pause(1500)
print(res)
sys.exit()





###############################################
# Divine Fury Test (1000)
###############################################

# 0 FC w/ Protection    =   1.01    
# 1 FC w/ Protection    =   1.01    0.97    1.02
# 2 FC w/ Protection    =   1.00    1.00    1.04
# 3 FC w/ Protection    =   0.74    0.75    0.76
# 4 FC w/ Protection    =   0.50    0.49    0.53

# 0 FC                  =   0.99    0.98    1.00
# 1 FC                  =   0.72    0.78    0.75
# 2 FC                  =   0.51    0.51    0.52
# 3 FC                  =   0.31    0.23    0.29
# 4 FC                  =   0.25    0.23    0.66    0.29    0.25

start = time.time()
Spells.CastChivalry("Divine Fury")
while not Player.BuffsExist("Divine Fury"):
    Misc.Pause(10)
print("fc", Player.FasterCasting, "protection", Player.BuffsExist("Protection"), "delay", time.time() - start)
sys.exit()





###############################################
# Consecrate Weapon Test (500)
###############################################

# 0 FC w/ Protection    =   0.48    0.50    0.50
# 1 FC w/ Protection    =   0.51    0.52    0.53
# 2 FC w/ Protection    =   0.49    0.51    0.50
# 3 FC w/ Protection    =   0.23    0.26    0.22
# 4 FC w/ Protection    =   0.24    0.27    0.26

# 0 FC                  =   0.48    0.47    0.50
# 1 FC                  =   0.27    0.30    0.28
# 2 FC                  =   0.23    0.25    0.26
# 3 FC                  =   0.23    0.27    0.25
# 4 FC                  =   0.22    0.28    0.27

start = time.time()
Spells.CastChivalry("Consecrate Weapon")
while not Player.BuffsExist("Consecrate Weapon"):
    Misc.Pause(10)
print("fc", Player.FasterCasting, "protection", Player.BuffsExist("Protection"), "delay", time.time() - start)
sys.exit()





###############################################
# Shield Bash Test (1000
###############################################
    
# 0 FC w/ Protection    =   0.97    1.00    0.99
# 1 FC w/ Protection    =   0.98    1.01    0.99
# 2 FC w/ Protection    =   1.03    1.01    0.99
# 3 FC w/ Protection    =   0.75    0.75    0.73
# 4 FC w/ Protection    =   0.52    0.50

# 0 FC                  =   1.03    0.97    1.04    1.01    
# 1 FC                  =   0.83    0.83    0.77    0.82    0.76    0.77    0.75    0.77
# 2 FC                  =   0.53    0.53    0.53    0.50
# 3 FC                  =   0.26    0.31    0.25    0.27    0.28
# 4 FC                  =   0.23    0.28    0.24    0.26    0.24    0.26    0.27

start = time.time()
Spells.CastMastery("Shield Bash")
while not Player.BuffsExist("Shield Bash"):
    Misc.Pause(10)
print("Total", time.time() - start)
sys.exit()





SHIELD_BASH_FC_NO_PROTECTION_VALUES = [1100, 900, 600, 400, 300]
SHIELD_BASH_FC_YES_PROTECTION_VALUES = [1100, 1100, 1100, 800, 600]

for HAS_PROTECTION in [True, False]:
    for FC_VAL in range(0 , 5):
        delay = SHIELD_BASH_FC_YES_PROTECTION_VALUES[FC_VAL] if HAS_PROTECTION else SHIELD_BASH_FC_NO_PROTECTION_VALUES[FC_VAL]
        #delay = 250 * (min(abs(Player.FasterCasting - 2), FC_CAP_SHIELD_BASH - 2) if Player.BuffsExist("Protection") else min(Player.FasterCasting, FC_CAP_SHIELD_BASH))
        print("fc", FC_VAL, "protection", HAS_PROTECTION, "delay", delay)
sys.exit()

for HAS_PROTECTION in [True, False]:
    for FC_VAL in range(0 , 5):
        FC_CAP_SHIELD_BASH = 4
        #HAS_PROTECTION = False
        baseDelayMs = 1000
        latency = 100
        fcOffset = 250 * (min(abs(FC_VAL - 2), FC_CAP_SHIELD_BASH - 2) if HAS_PROTECTION else min(FC_VAL, FC_CAP_SHIELD_BASH - 1))
        delay = baseDelayMs + latency - fcOffset
        #delay = 250 * (min(abs(Player.FasterCasting - 2), FC_CAP_SHIELD_BASH - 2) if Player.BuffsExist("Protection") else min(Player.FasterCasting, FC_CAP_SHIELD_BASH))
        print("fc", FC_VAL, "protection", HAS_PROTECTION, "delay", delay)
sys.exit()












