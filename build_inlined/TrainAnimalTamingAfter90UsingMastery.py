# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-02-04
# Use at your own risk. 

# Cheese your animal taming from 90 - 120. You must be
# at 90 skill to use this. Plug in your pets serial here.

Player.HeadMessage(38, "Training Animal Taming Using Mastery")

PET_SERIAL = 0x000EB0F7;

while not Player.IsGhost:
    Spells.CastMastery("Combat Training")
    Target.WaitForTarget(10000, False)
    Target.TargetExecute(PET_SERIAL)
    Misc.Pause(5000)
    
    
