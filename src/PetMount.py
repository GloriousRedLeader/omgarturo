# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-02-24
# Use at your own risk. 

from Scripts.omgarturo.src.fm_core.core_mobiles import get_pets

# Will select one of your pets at random and attempt to mount it.
# Only works for tamed creatures, not statuettes in your pack.

pets = get_pets()

if len(pets) > 0:
    Mobiles.UseMobile(pets[0])