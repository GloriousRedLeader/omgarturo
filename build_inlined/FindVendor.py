# ===============================================
# Imports
# ===============================================
from System import Byte, Int32
from System.Collections.Generic import List

# ===============================================
# Auto-generated inlined code. Do not edit
# ===============================================

# ===== Inlined block from core_mobiles.py =====
# ---- find_vendor_by_name (from core_mobiles.py)
def find_vendor_by_name (vendorName, vendorRange = 10):
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

# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2024-03-26
# Use at your own risk. 

# This is an example of how to find a vendor in a sea of vendors.
# If the vendor is on your screen and within range it should be able to find
# it. Just provide the vendor name.
# When it finds the vendor text will appear above its head so you can find it.

# Just replace this with your vendors name and walk around mashing this script. 
VENDOR_NAME = "Luthien"

# Search within this many tiles
VENDOR_RANGE = 15

vendor = find_vendor_by_name(vendorName = VENDOR_NAME, vendorRange = VENDOR_RANGE)

if vendor != None:
    for i in range(1, 10):
        Mobiles.Message(vendor,78,"^ IM HERE ^",False)
        Mobiles.Message(vendor,48,"^ IM HERE ^",False)
        Mobiles.Message(vendor,28,"^ IM HERE ^",False)
        Misc.Pause(1500)
else:
    Player.HeadMessage(28, "Could not find that vendor")