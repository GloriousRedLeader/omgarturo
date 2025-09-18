from System import Byte, Int32
from System.Collections.Generic import List

# Inlined dependencies (topologically sorted)
def get_friends_by_names(friendNames=[], range=8):
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = range
    fil.Notorieties = List[Byte](bytes([1, 2]))
    fil.IsGhost = False
    fil.Friend = False
    fil.CheckLineOfSight = True
    mobs = Mobiles.ApplyFilter(fil)
    if len(mobs) > 0:
        mobsList = List[type(mobs[0])]([mob for mob in mobs if mob.Name in friendNames])
        return mobsList
    mobs = Mobiles.ApplyFilter(fil)
    return mobs

# Main code
RANGE = 15
NAMES_TO_SEARCH = ['Daedaulus', "Daedaulus'", 'Daedaulus`', 'Bamba']
while True:
    mobiles = get_friends_by_names(friendNames=NAMES_TO_SEARCH, range=RANGE)
    if len(mobiles) > 0:
        mobile = mobiles[0]
        for i in range(1, 10):
            Mobiles.Message(mobile, 78, '^ IM HERE ^', False)
            Mobiles.Message(mobile, 48, '^ IM HERE ^', False)
            Mobiles.Message(mobile, 28, '^ IM HERE ^', False)
            Misc.Pause(1500)
    else:
        Player.HeadMessage(28, 'Could not find that mobile')
    Misc.Pause(1000)
