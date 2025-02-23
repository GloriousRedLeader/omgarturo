# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/uo-razor-enhanced
#   2024-03-26
# Use at your own risk. 

# This is a very basic single target heal loop script. 
# Use case is despise boss.
# Works with magery and chivalry.

isMage = True if Player.GetSkillValue("Magery") > 75 else False

petSerials = []
while True:
    petSerial = Target.PromptTarget("Select your pet", 38)
    if petSerial > -1:
        petSerials.append(petSerial)
    else:
        break
#petSerial = Target.PromptTarget("Select your pet", 38)

while True:
    for petSerial in petSerials:
        pet = Mobiles.FindBySerial(petSerial)
        if pet.Poisoned:
            if isMage:
                Spells.CastMagery("Arch Cure")
                Target.WaitForTarget(10000, False)
                Target.TargetExecute(petSerial)    
            else:
                Spells.CastChivalry("Cleanse by Fire")
                Target.WaitForTarget(10000, False)
                Target.TargetExecute(petSerial)
        elif pet.Hits / pet.HitsMax < 0.85 and not pet.Poisoned:
            if isMage:
                Spells.CastMagery("Greater Heal")
                Target.WaitForTarget(10000, False)
                Target.TargetExecute(petSerial)
            else:
                Spells.CastChivalry("Close Wounds")
                Target.WaitForTarget(10000, False)
                Target.TargetExecute(petSerial)            
        Misc.Pause(500)