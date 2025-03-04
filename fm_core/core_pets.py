# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2024-03-26
# Use at your own risk. 

# Took some of this from Smaptastic from the UOAlive scripts channel on discord March 12th 2024.
# Not sure if he/she/they/them/thee/thy/thine has a github.
# I have made a few changes from original script. First, I removed 95% of the stuff
# and am just focusing on pet heals.
# 
# Known Issues: Most likely doesnt play nice with heal agent or other scripts that 
# block actions, e.g. "You must wait to do this". No idea how that stuff works.

# Advanced configuration:
#
# All loop functions in this framework should honor a shared variable that 
# will pause the loops. Anything that loops should do this. They should respond to the
# change within 1000ms. You can pause all scripts by setting this vairable:
#
#   core_loops_enabled
#       (1) Enabled
#       (0) Disabled
#
# This will not stop the script, it will just sit in a loop and wait until the variable
# is once again set to 1. This is useful for teleporting and use with other scripts at the same time.
# You could also just manually stop / start your attack loop script. 
# But if youre playing different characters on different servers with different 
# script names, that becomes hard to track. So instead we can use this shared variable.
import time
from Scripts.omgarturo.fm_core.core_items import PET_LEASH_STATIC_IDS
from Scripts.omgarturo.fm_core.core_player import find_first_in_container_by_ids
from Scripts.omgarturo.fm_core.core_mobiles import get_pets

Timer.Create("vetLoopPetWarning", 1)

LAST_PET_REZZED = { "serial": None, "ready": None }

# Bandages the pet if youre close enough and its either poisoned or below the 
# specified health percentage.
# You should not use this method, instead use run_vet_bot() below which will
# loop and do all the good stuff.
def vet_pets( healthPercent, petSerials, containerSerial, bandageDelayMs, rezDelayMs, healSpellName = None ):

    global LAST_PET_REZZED
    
    atLeastOnePetFound = False
    atLeastOnePetMissing = False
    
    pets = []
    for petSerial in petSerials:
        pet = Mobiles.FindBySerial(petSerial)
        if pet == None:
            atLeastOnePetMissing = True
            continue
        atLeastOnePetFound = True
        pets.append(pet)
    pets.sort(key = lambda pet: pet.Hits)
    
    print("---------- - - - - ------------------")
    for pet in pets:
        print(f"Pet Name: { pet.Name } Health: { pet.Hits } / { pet.HitsMax } ")
    
    #for pet in pets:
    if len(pets) > 0:
        pet = pets[0]

        petCurrentHealthPercent = getHealthPercent(pet)
        if petCurrentHealthPercent < healthPercent or pet.Poisoned or pet.Hits == 0:
        #if petCurrentHealthPercent < healthPercent or pet.Poisoned or pet.IsGhost:
            #if runToPet and Player.DistanceTo(petID) > 2:
            #    pathFindToPet()
            if Player.DistanceTo(pet) <= 2 and not Player.BuffsExist('Veterinary'):
            
            
                if pet.Hits == 0:
                    Player.HeadMessage(88, "Rezzing {}".format(pet.Name))
                else:
                    Player.HeadMessage(88, "Bandaging {}".format(pet.Name))
            
                #moreTimeForRezzing = 0
                #canRezPet = False
                #if LAST_PET_REZZED is not None:
                #    if pet.Serial == LAST_PET_REZZED["serial"] and time.time() > LAST_PET_REZZED["ready"]:
                #        canRezPet = True
                #    elif pet.Serial != LAST_PET_REZZED["serial"]:
                #        canRezPet = True
                #        
                #if pet.Hits == 0 and canRezPet:
                #    Player.HeadMessage(88, "Rezzing {}".format(pet.Name))
                #    moreTimeForRezzing = rezDelayMs
                #    LAST_PET_REZZED = { "serial": pet.Serial, "ready": time.time() + 3000 }
                #elif not pet.IsGhost:
                #    Player.HeadMessage(88, "Bandaging {}".format(pet.Name, pet.IsGhost))
                #else:
                #    continue

                bandage = Items.FindByID(0x0E21, 0, containerSerial)
                #Items.UseItem(bandage, petSerial)
                Items.UseItem(bandage)
                Target.WaitForTarget(3000)
                Target.TargetExecute(pet)
                Misc.Pause(bandageDelayMs)
                
        # Heal with spell
        if petCurrentHealthPercent < 50 and healSpellName != None and not pet.Poisoned and pet.Hits > 0:
            Spells.Cast(healSpellName)
            Target.WaitForTarget(3000)
            Target.TargetExecute(pet)
                
                
                #return True
        #return False
    #return False
    
    if Timer.Check("vetLoopPetWarning") == False:
        if not atLeastOnePetFound:
            Player.HeadMessage(38, "Could not find any pets.")
        elif atLeastOnePetMissing:
            Player.HeadMessage(38, "At least one pet missing.")
        Timer.Create("vetLoopPetWarning", 3000)

# Returns a current HP percentage value. Works for pets, but does quite a bit of rounding for them, as
# pet max HP is always considered to be 25, and they decrease as fractions of that. (i.e., 23/25 is 92%)
# This method was completely hijacked from Smaptastic. All credit to them.
def getHealthPercent(mobForHP):
    if mobForHP:
        if mobForHP.HitsMax <= 0:
            return 0
        healthPercent = 100 * mobForHP.Hits / mobForHP.HitsMax
        return healthPercent
        
# Uses a pet leash on all deployed pets. Pet leash must be in backpack.
def leash_pets ():
    leash = find_first_in_container_by_ids(PET_LEASH_STATIC_IDS)
    if leash == None:
        Player.HeadMessage(38, "You do not have a leash in backpack.")
        return False
    
    for pet in get_pets():
        if Player.DistanceTo(pet) <= 5:
            Items.UseItem(leash)
            Target.WaitForTarget(3000)
            Player.HeadMessage( 88, "Leashing fluffy {}".format(pet.Name))
            Target.TargetExecute(pet)
            Misc.Pause(1000)

# This is the public API you should use when running a pet heal bot
# in the background. You will need to get your pet serials first. To do that
# use razor enhanced, go to scripts, and click the "Inspect" button at top right.
# Target your pet and it will display the serial. Done.
def run_vet_loop (
    
    # An array of serials for your pets. You must provide this.
    # To get the serials you can use razor and press "Inspect Entities",
    # but really all of these programs have this feature and most clients
    # to too.
    petSerials = [], 
    
    # Container where your bandages live. Defautls to player backpack. You can change
    # this to a different bag. Use Razor Enhanced and click "Inspect" to get your preferred
    # bags serial.
    containerSerial = Player.Backpack, 
    
    # Only bandage things when their health is below this percent.
    healthPercent = 95, 
    
    # Wait this long in between bandage attempts. This is a dumb
    # program, it doesnt know when fingers slip, or even whether
    # fingers can slip bandaging an aneemal.
    bandageDelayMs = 2000,
    
    # Wait this long after rezzing a pet before doing anythign else,
    # otherwise it may start bandaging something else (bandage time is faster than rez time?)
    rezDelayMs = 3000,
    
    # Optionally provide a heal spell name if you really want to get serious
    # Currently will only use this if pet is < 50% health. Can have things like
    # "Greater Heal" or "Close Wounds".
    healSpellName = None):
        
    # This is just a head message to let us know the application is running.
    Timer.Create("vetLoopTimer", 1000)

    # Always enable on start
    Misc.SetSharedValue("core_loops_enabled", 1)
    
    while True:
        while not Player.IsGhost:
            
            if Misc.ReadSharedValue("core_loops_enabled") != 1:
                Misc.Pause(500)
                Player.HeadMessage( 88, 'Vet Loop Paused...' )
                Timer.Create( 'vetLoopTimer', 1000 )
                continue            
            
            if Timer.Check("vetLoopTimer") == False:
                Player.HeadMessage(88, "Vet Loop Running")
                Timer.Create("vetLoopTimer", 3000)

            vet_pets(healthPercent, petSerials, containerSerial, bandageDelayMs, rezDelayMs, healSpellName)
            Misc.Pause(500)
            continue

        # If youre a ghost, the script just pauses for a second then checks again on whether youre a ghost.
        Misc.Pause(1000)
        continue