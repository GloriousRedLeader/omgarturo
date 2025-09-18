from System import Byte, Int32
from System.Collections.Generic import List
import sys

# Constants
DEPLOYED_LOBSTER_TRAP_STATIC_ID = 17611
FISH_STATIC_IDS = [17154, 17155, 17158, 17159, 2508, 2509, 2510, 2511, 17603, 17604, 17605, 17606, 17617, 17618, 17619, 17620]
LOBSTER_TRAP_STATIC_IDS = [17615]

# Functions
def move_item_to_container(item, destinationSerial):
    Items.Move(item, destinationSerial, item.Amount)
    Misc.Pause(800)
def run_crab_fishing_loop(numLoops=1, moveTiles=0, maxTraps=19, trapDelayMs=65000, fishToKeep=None):
    for i in range(1, numLoops + 1):
        Player.HeadMessage(28, 'Running crab fishing loop {} / {}'.format(i, numLoops))
        traps = []
        trapItems = find_all_in_container_by_ids(LOBSTER_TRAP_STATIC_IDS)
        for trapItem in trapItems:
            if trapItem.Name == 'empty lobster trap':
                traps.append(trapItem)
        actualTraps = len(traps)
        Player.HeadMessage(28, 'Stand in middle of cargo hold')
        Misc.Pause(500)
        Player.HeadMessage(28, 'You have {}/{} lobster traps'.format(actualTraps, maxTraps))
        trapNum = 1
        for trap in traps:
            Target.Cancel()
            if trap.Name != 'empty lobster trap':
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
            Target.TargetExecute(x, y, z)
            Misc.Pause(650)
            trapNum = trapNum + 1
            if trapNum > maxTraps or trapNum > actualTraps:
                Player.HeadMessage(28, 'all traps out')
                break
        Player.HeadMessage(28, 'All traps deployed, now we wait')
        Misc.Pause(trapDelayMs)
        Player.HeadMessage(28, 'Time to collect traps')
        filter = Items.Filter()
        filter.Graphics = List[Int32](DEPLOYED_LOBSTER_TRAP_STATIC_ID)
        filter.Movable = 0
        filter.OnGround = True
        filter.RangeMax = 7
        items = Items.ApplyFilter(filter)
        for item in items:
            if item.ItemID == DEPLOYED_LOBSTER_TRAP_STATIC_ID:
                Items.UseItem(item)
                print('Clicking item {}'.format(item.Name))
                Misc.Pause(650)
        Player.HeadMessage(28, 'Time to let the crabs out of the traps')
        Misc.Pause(2000)
        trapItems = find_all_in_container_by_ids(LOBSTER_TRAP_STATIC_IDS)
        for trapItem in trapItems:
            if trapItem.Name != 'empty lobster trap':
                Items.UseItem(trapItem)
                Misc.Pause(650)
                Target.Cancel()
        Player.HeadMessage(28, 'Move crabs to hold')
        Misc.Pause(2000)
        fishies = find_all_in_container_by_ids(FISH_STATIC_IDS)
        fil = Items.Filter()
        fil.Name = 'cargo hold'
        fil.RangeMax = 3
        hatches = Items.ApplyFilter(fil)
        if len(hatches) > 0:
            for fish in fishies:
                if fishToKeep is not None and fish.Name.lower().find(fishToKeep.lower()) > -1:
                    Player.HeadMessage(28, 'Keeping fish {} item id {}'.format(fish.Name, fish.ItemID))
                    continue
                print('Moving fish {} item id {}'.format(fish.Name, fish.ItemID))
                move_item_to_container(fish, hatches[0].Serial)
        if i == numLoops:
            return
        for i in range(0, moveTiles):
            Player.ChatSay('forward one')
            Misc.Pause(750)
def find_all_in_container_by_ids(itemIDs, containerSerial=Player.Backpack.Serial):
    items = []
    for itemID in itemIDs:
        items = items + Items.FindAllByID(itemID, -1, containerSerial, 1)
    return items

# Main code
run_crab_fishing_loop(numLoops=2, moveTiles=4, maxTraps=5, trapDelayMs=5000, fishToKeep='blue crab')
