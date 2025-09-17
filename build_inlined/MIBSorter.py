# ===============================================
# Imports
# ===============================================
import re

# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2024-03-26
# Use at your own risk. 


# Organizes scrolls for mibs into containers based on x, y coordinates.
# Set one container for east and another for west. 

#SOURCE_CONTAINER_ID = 0x40DB059B # Blue bag
#SOURCE_CONTAINER_ID = 0x408A916E # Brown bag

SOURCE_CONTAINER_ID = Target.PromptTarget("Pick source container", 38)

WEST_CONTAINER_ID = 0x4010BA53
CENTRAL_CONTAINER_ID = 0x401F082C
EAST_CONTAINER_ID = 0x40801537
SCROLL_ITEM_ID = 0x14EE
MIB_ITEM_ID = 0x099F

mibs = Items.FindAllByID(MIB_ITEM_ID, -1, SOURCE_CONTAINER_ID, 1)
for mib in mibs:
    Items.UseItem(mib)
    Misc.Pause(250)

scrolls = Items.FindAllByID(SCROLL_ITEM_ID, -1, SOURCE_CONTAINER_ID, 1)
for scroll in scrolls:
    for prop in scroll.Properties:
        match = re.match(r"(.*){1}\:\s\((\d+){1}, (\d+){1}\)", prop.ToString())
        if match is not None:
            facet = match.group(1)
            x = int(match.group(2))
            y = int(match.group(3))
            if facet == "Felucca":
                # West
                if x < 1500:
                    print(facet, x, y, "Moving to west")
                    Items.Move(scroll, WEST_CONTAINER_ID, scroll.Amount)
                # Central
                elif x < 3500:
                    print(facet, x, y, "Moving to central")
                    Items.Move(scroll, CENTRAL_CONTAINER_ID, scroll.Amount)
                # East
                else: 
                    print(facet, x, y, "Moving to east")
                    Items.Move(scroll, EAST_CONTAINER_ID, scroll.Amount)
                Misc.Pause(650)            