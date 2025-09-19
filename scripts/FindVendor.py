# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-09-19
# Use at your own risk.

# ##########################################################
# #                                                        #
# #              INLINED DEPENDENCIES                      #
# #                                                        #
# #  DO NOT EDIT THIS SECTION - AUTO-GENERATED CODE        #
# #                                                        #
# #  These are dependencies from fm_core that have been    #
# #  automatically inlined. For user-editable code,        #
# #  scroll down to the bottom of this file.               #
# #                                                        #
# ##########################################################

from System import Byte, Int32
from System.Collections.Generic import List

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

# ##########################################################
# #                                                        #
# #                 USER EDITABLE CODE                      #
# #                                                        #
# #  This is the original script code that you can         #
# #  modify and customize. Edit the parameters, logic,     #
# #  and function calls below as needed for your setup.    #
# #                                                        #
# #  The dependencies above have been automatically        #
# #  inlined and should not be modified.                   #
# ##########################################################

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
