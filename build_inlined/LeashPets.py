# ===============================================
# Imports
# ===============================================
import time

# ===============================================
# Auto-generated inlined code. Do not edit
# ===============================================

# ===== Inlined block from core_pets.py =====
# ===== Inlined block from core_items.py =====
# ---- PET_LEASH_STATIC_IDS (binding from core_items.py)
PET_LEASH_STATIC_IDS = [0x1374]

# ---- leash_pets (from core_pets.py)
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

# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2024-03-26
# Use at your own risk. 


# Uses a pet leash on all deployed pets. Pet leash must be in backpack.
leash_pets()