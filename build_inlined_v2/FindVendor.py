from System import Byte, Int32
from System.Collections.Generic import List
def find_vendor_by_name(vendorName, vendorRange=10):
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = vendorRange
    fil.Notorieties = List[Byte](bytes([7]))
    fil.IsGhost = False
    fil.Friend = False
    fil.CheckLineOfSight = False
    mobs = Mobiles.ApplyFilter(fil)
    for m in mobs:
        if m.Name == vendorName:
            return m
    return None
fil = Mobiles.Filter()
mobs = Mobiles.ApplyFilter(fil)
VENDOR_NAME = 'Luthien'
VENDOR_RANGE = 15
vendor = find_vendor_by_name(vendorName=VENDOR_NAME, vendorRange=VENDOR_RANGE)
if vendor != None:
    for i in range(1, 10):
        Mobiles.Message(vendor, 78, '^ IM HERE ^', False)
        Mobiles.Message(vendor, 48, '^ IM HERE ^', False)
        Mobiles.Message(vendor, 28, '^ IM HERE ^', False)
        Misc.Pause(1500)
else:
    Player.HeadMessage(28, 'Could not find that vendor')
