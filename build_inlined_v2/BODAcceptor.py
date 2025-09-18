from System import Byte, Int32
from System.Collections.Generic import List
import sys

# Constants
BOD_BOOK_STATIC_ID = 8793
BOD_STATIC_ID = 8792

# Functions
def get_yellows_in_range(range=8):
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = range
    fil.Notorieties = List[Byte](bytes([7]))
    fil.IsGhost = False
    fil.Friend = False
    fil.CheckLineOfSight = False
    mobs = Mobiles.ApplyFilter(fil)
    return mobs

# Main code
placeInBodBook = False
NPC_BOD_GUMP_ID = 2611865322
BOD_BOOK_GUMP_ID = 1425364447
ALLOWED_SUFFIXES = ['scribe', 'alchemist', 'carpenter', 'bowyer', 'tinker', 'tailor', 'blacksmith', 'cook']
while True:
    Gumps.CloseGump(BOD_BOOK_GUMP_ID)
    Misc.Pause(500)
    npcs = get_yellows_in_range(4)
    for npc in npcs:
        for prop in npc.Properties:
            res = any((s in prop.ToString() for s in ALLOWED_SUFFIXES))
            if res == True:
                Misc.UseContextMenu(npc.Serial, 'Bulk Order Info', 3000)
                Misc.Pause(1000)
                gid = Gumps.CurrentGump()
                if gid is not None and gid != 0:
                    Gumps.SendAction(gid, 1)
                    print('gid {}'.format(gid))
                else:
                    print('No bods')
                if Gumps.HasGump(BOD_BOOK_GUMP_ID):
                    Gumps.CloseGump(BOD_BOOK_GUMP_ID)
                    Misc.Pause(500)
    if placeInBodBook:
        bods = Items.FindAllByID(itemid=BOD_STATIC_ID, color=-1, container=Player.Backpack.Serial, range=1)
        for bod in bods:
            bodBook = Items.FindByID(itemid=BOD_BOOK_STATIC_ID, color=bod.Hue, container=Player.Backpack.Serial, range=3)
            if bodBook is not None:
                Items.Move(bod.Serial, bodBook.Serial, 1)
                Misc.Pause(650)
