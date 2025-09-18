# ===============================================
# Imports
# ===============================================
from System import Byte, Int32
from System.Collections.Generic import List
import sys

# ===============================================
# Auto-generated inlined code. Do not edit
# ===============================================

# ===== Inlined block from core_gathering.py =====
# ===== Inlined block from core_items.py =====
# ---- DEPLOYED_LOBSTER_TRAP_STATIC_ID (binding from core_items.py)
DEPLOYED_LOBSTER_TRAP_STATIC_ID = 0x44CB

# ===== Inlined block from core_items.py =====
# ---- LOBSTER_TRAP_STATIC_IDS (binding from core_items.py)
LOBSTER_TRAP_STATIC_IDS = [0x44CF]

# ---- run_crab_fishing_loop (from core_gathering.py)
def run_crab_fishing_loop(

    # Number of times to run the crab loop. Default is 1 then it stops.
    numLoops = 1,
    
    # If on a boat, tells the tiller to move forward this many times.
    moveTiles = 0, 
    
    # Number of traps to use. If you dont have this many, will use only what you have.
    maxTraps = 19,
    
    # How long to pause between casts
    trapDelayMs = 65000,
    
    # Will not do any fishHandling operations on this fish. Leaves it in backpack. Useful for fishing quests.
    fishToKeep = None
):

    for i in range(1, numLoops + 1):
        Player.HeadMessage(28, "Running crab fishing loop {} / {}".format(i, numLoops))
        traps = []
        trapItems = find_all_in_container_by_ids(LOBSTER_TRAP_STATIC_IDS)
        for trapItem in trapItems:
            if trapItem.Name == "empty lobster trap":
                traps.append(trapItem)
        actualTraps = len(traps)

        Player.HeadMessage(28, "Stand in middle of cargo hold")
        Misc.Pause(500)
        Player.HeadMessage(28, "You have {}/{} lobster traps". format(actualTraps, maxTraps))

        trapNum = 1
        for trap in traps:
            Target.Cancel()
            if trap.Name != "empty lobster trap":
                continue

            Items.UseItem(trap)
            Target.WaitForTarget(2000)
            if trapNum == 1:
                x = Player.Position.X + 6
                y = Player.Position.Y - 6
                z = Player.Position.Z
            elif trapNum == 2:
                x = Player.Position.X + 6
                y = Player.Position.Y - 4
                z = Player.Position.Z
            elif trapNum == 3:
                x = Player.Position.X + 6
                y = Player.Position.Y - 2
                z = Player.Position.Z        
            elif trapNum == 4:
                x = Player.Position.X + 6
                y = Player.Position.Y
                z = Player.Position.Z
            elif trapNum == 5:
                x = Player.Position.X + 6
                y = Player.Position.Y + 2
                z = Player.Position.Z    
            elif trapNum == 6:
                x = Player.Position.X + 6
                y = Player.Position.Y + 4
                z = Player.Position.Z        
            elif trapNum == 7:
                x = Player.Position.X + 6
                y = Player.Position.Y + 6
                z = Player.Position.Z                
            elif trapNum == 8:
                x = Player.Position.X + 4
                y = Player.Position.Y + 6
                z = Player.Position.Z   
            elif trapNum == 9:
                x = Player.Position.X + 2
                y = Player.Position.Y + 6
                z = Player.Position.Z    
            elif trapNum == 10:
                x = Player.Position.X + 0
                y = Player.Position.Y + 6
                z = Player.Position.Z    
            elif trapNum == 11:
                x = Player.Position.X - 2
                y = Player.Position.Y + 6
                z = Player.Position.Z    
            elif trapNum == 12:
                x = Player.Position.X - 4
                y = Player.Position.Y + 6
                z = Player.Position.Z    
            elif trapNum == 13:
                x = Player.Position.X - 6
                y = Player.Position.Y + 6
                z = Player.Position.Z    
            elif trapNum == 14:
                x = Player.Position.X - 6
                y = Player.Position.Y + 4
                z = Player.Position.Z          
            elif trapNum == 15:
                x = Player.Position.X - 6
                y = Player.Position.Y + 2
                z = Player.Position.Z    
            elif trapNum == 16:
                x = Player.Position.X - 6
                y = Player.Position.Y
                z = Player.Position.Z
            elif trapNum == 17:
                x = Player.Position.X - 6
                y = Player.Position.Y - 2
                z = Player.Position.Z  
            elif trapNum == 18:
                x = Player.Position.X - 6
                y = Player.Position.Y - 4
                z = Player.Position.Z   
            elif trapNum == 19:
                x = Player.Position.X - 6
                y = Player.Position.Y - 6
                z = Player.Position.Z            
            else:
                break

            Target.TargetExecute(x,y,z)
            Misc.Pause(650)
            
            trapNum = trapNum + 1
            if trapNum > maxTraps or trapNum > actualTraps:
                Player.HeadMessage(28, "all traps out")
                break

        Player.HeadMessage(28, "All traps deployed, now we wait")
        Misc.Pause(trapDelayMs)

        Player.HeadMessage(28, "Time to collect traps")
        filter = Items.Filter()
        #filter.Graphics = List[Int32]((DEPLOYED_LOBSTER_TRAP_STATIC_ID)) # This filter doesnt work
        # That filter didnt work because we were creating a list of a certain size (probalby way too big)
        # Instead, try the below:
        filter.Graphics = List[Int32](DEPLOYED_LOBSTER_TRAP_STATIC_ID) # 2025-08-24 Untested
        filter.Movable = 0
        filter.OnGround = True
        filter.RangeMax = 7
        items = Items.ApplyFilter(filter)

        for item in items:
            if item.ItemID == DEPLOYED_LOBSTER_TRAP_STATIC_ID:
                Items.UseItem(item)
                print("Clicking item {}".format(item.Name))
                Misc.Pause(650)

        Player.HeadMessage(28, "Time to let the crabs out of the traps")
        Misc.Pause(2000)

        trapItems = find_all_in_container_by_ids(LOBSTER_TRAP_STATIC_IDS)
        for trapItem in trapItems:
            if trapItem.Name != "empty lobster trap":
                Items.UseItem(trapItem)
                Misc.Pause(650)
                Target.Cancel()
                
        Player.HeadMessage(28, "Move crabs to hold")
        Misc.Pause(2000)

        fishies = find_all_in_container_by_ids(FISH_STATIC_IDS)
        fil = Items.Filter()
        fil.Name = "cargo hold"
        fil.RangeMax = 3
        hatches = Items.ApplyFilter(fil)
        if len(hatches) > 0:
            for fish in fishies:
                if fishToKeep is not None and fish.Name.lower().find(fishToKeep.lower()) > -1:
                    Player.HeadMessage(28, "Keeping fish {} item id {}".format(fish.Name, fish.ItemID))
                    continue
                print("Moving fish {} item id {}".format(fish.Name, fish.ItemID))                        
                move_item_to_container(fish, hatches[0].Serial)
            
        if i == numLoops:
            return
            
        for i in range(0, moveTiles):
            Player.ChatSay("forward one")
            Misc.Pause(750)

# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-01-11
# Use at your own risk. 


# Deploys traps. Collects traps after trapDelayMs. Loots the traps. Moves crabs to hold.
# You need lobster traps in your bag. You need to stand near the cargo hold on your ship.
run_crab_fishing_loop(

    # Number of times to run the crab loop. Default is 1 then it stops.
    numLoops = 2,
    
    # If on a boat, tells the tiller to move forward this many times.
    moveTiles = 4, 
    
    # Number of traps to use. If you dont have this many, will use only what you have.
    maxTraps = 5,
    
    # How long to pause between casts
    trapDelayMs = 5000,
    
    # Will not do any fishHandling operations on this fish. Leaves it in backpack. Useful for fishing quests.
    fishToKeep = "blue crab"
)