# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2024-03-26
# Use at your own risk. 

# This is a very basic single target heal loop script. 
# Use case is despise boss. Works with magery and chivalry.
# WHen it starts, you select all the mobiles you want to heal. Hit escape when done
# selecting mobiles. Mobiles can be yourself, other players, and pets.
# Works with chiv healing and magery healing.

isMage = True if Player.GetSkillValue("Magery") > 75 else False

petSerials = []
while True:
    petSerial = Target.PromptTarget("Select a target to heal (hit escape when done)", 38)
    if petSerial > -1:
        petSerials.append(petSerial)
    else:
        break

while True:
    
    if Timer.Check( 'singleTargetPingTimer' ) == False:
        Player.HeadMessage( 99, "Single Target Healing Running..." )
        Timer.Create( 'singleTargetPingTimer', 3000 )
    
    for petSerial in petSerials:
        pet = Mobiles.FindBySerial(petSerial)
        
        if pet is None or pet.Hits is None or pet.Hits == 0 or pet.HitsMax is None or pet.HitsMax == 0 or Player.DistanceTo(pet) > 10:
            Misc.Pause(500)
            continue
            
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