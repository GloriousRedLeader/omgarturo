# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-08-24
# Use at your own risk. 

from Scripts.omgarturo.fm_core.core_mobiles import get_pets

# Clicks the hitching post and targets a pet at moonglow zoo
# so you dont have to.
# WARNING: THIS SCRIPT IS DANGEROUS! You can lose your pet!

pets = get_pets()

for pet in pets:
    Items.UseItem(0x401C023F)
    Target.WaitForTarget(3000)
    Target.TargetExecute(pet)
    Gumps.WaitForGump( 0x4a47a6eb,3000)
    Gumps.SendAction(0x4a47a6eb,1)
    Misc.Pause(1000)