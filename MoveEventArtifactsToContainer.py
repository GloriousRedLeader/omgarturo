# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2024-11-21
# Use at your own risk. 

from System.Collections.Generic import List
import sys
from System import Byte, Int32

# Scans backpack for "of the three", "of wildfire", etc. 
# and moves to a container. This is just a dumper script.
# I like to turn in my arties on just one char, so my other
# chars use this to offload. Too lazy to click and drag
# or even use taz uo alt + click.

SUFFIXES = [
    "of the archlich"
]

PAUSE_DELAY = 750

# Prompt for container
# destContainerSerial = Target.PromptTarget("Pick destination container", 17)

# Hard coded container (easier, no clicking)
destContainerSerial = 0x40CBB649

for item in Items.FindBySerial(Player.Backpack.Serial).Contains:
    print(item.Name)
    for s in SUFFIXES:
        if item.Name is not None and s.lower() in item.Name.lower():
            Misc.SendMessage("Moving ", item.Name)
            Items.Move(item, destContainerSerial, 1);
            Misc.Pause(PAUSE_DELAY)
            break
