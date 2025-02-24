# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/uo-razor-enhanced
#   2025-02-24
# Use at your own risk. 

from Scripts.omgarturo.fm_core.core_mobiles import get_pets

# Will select one of your pets at random and attempt to mount it.

pets = get_pets()

if len(pets) > 0:
    Mobiles.UseMobile(pets[0])