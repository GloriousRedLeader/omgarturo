# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2024-03-26
# Use at your own risk. 

# This is an example of how to find a vendor in a sea of vendors.
# If the vendor is on your screen and within range it should be able to find
# it. Just provide the vendor name.
# When it finds the vendor text will appear above its head so you can find it.
from Scripts.omgarturo.fm_core.core_mobiles import get_friends_by_names

# Search within this many tiles
RANGE = 15

NAMES_TO_SEARCH = ["Daedaulus", "Daedaulus'", "Daedaulus`", "Bamba"]

while True:
    mobiles = get_friends_by_names(friendNames = NAMES_TO_SEARCH, range = RANGE)
    if len(mobiles) > 0:
        mobile = mobiles[0]
        for i in range(1, 10):
            Mobiles.Message(mobile,78,"^ IM HERE ^",False)
            Mobiles.Message(mobile,48,"^ IM HERE ^",False)
            Mobiles.Message(mobile,28,"^ IM HERE ^",False)
            Misc.Pause(1500)
    else:
        Player.HeadMessage(28, "Could not find that mobile")
    Misc.Pause(1000)