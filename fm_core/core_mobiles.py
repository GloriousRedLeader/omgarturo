# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2024-03-26
# Use at your own risk. 

from System.Collections.Generic import List
from System import Byte, Int32
#from builtins import Mobile

FIRE_BEETLE_MOBILE_ID = 0x00A9
BLUE_BEETLE_MOBILE_ID = 0x0317
SILVER_SERPENT_MOBILE_ID = 0x005C
GIANT_SERPENT_MOBILE_ID = 0x0015

ANIMATE_DEAD_MOBILE_NAMES = [
    "a gore fiend",
    "a lich",
    "a flesh golem",
    "a mummy",
    "a skeletal dragon",
    "a lich lord",
    "a skeletal knight",
    "a bone knight",
    "a skeletal mage",
    "a bone mage",
    "a patchwork skeleton",
    "a mound of maggots",
    "a wailing banshee",
    "a wraith",
    "a hellsteed",
    "a skeletal steed",
    "an Undead Gargoyle",
    "a skeletal drake",
    "a putrid undead gargoyle",
    "a blade spirit",
    "an energy vortex"
]

# This was taken from the lumberjack script written by Credzba
# https://razorenhanced.net/dokuwiki/doku.php?id=resourcegatheringscripts
def range_mobile( mobile ):
    dist = math.sqrt( ((Player.Position.X - mobile.Position.X)**2) + ((Player.Position.Y - mobile.Position.Y)**2) )
    return dist
    
# This is the most inefficient thing known to man. But it does 
# kind of work. If you feed to select a list of mobiles and exclude
# some of them based on a list of serials, this will do it.
# Noterieties:  blue = 1, green = 2, gray = 3, gray crim = 4, orange = 5, red = 6, yellow = 7
#def get_mobs_exclude_serials (range, checkLineOfSight = False, serialsToExclude = [], namesToExclude = []):
#    fil = Mobiles.Filter()
#    fil.Enabled = True
#    fil.RangeMax = range
#    fil.Notorieties = List[Byte](bytes([3,4,5,6]))
#    fil.IsGhost = False
#    fil.Friend = False
#    fil.CheckLineOfSight = checkLineOfSight
#    mobs = Mobiles.ApplyFilter(fil)
    
    #namesToExclude = ["omg arthur"]
#    listValid = [m.Serial for m in mobs if m.Serial not in serialsToExclude and m.Name not in namesToExclude]
    #listValid = [m.Serial for m in mobs if m.Serial not in serialsToExclude]

#    if len(listValid) == 0:
#        return []

#    fil = Mobiles.Filter()
#    fil.Enabled = True
#    for l in listValid:
#        fil.Serials.Add(l)
#    fil.RangeMax = range
#    fil.Notorieties = List[Byte](bytes([3,4,5,6]))
#    fil.IsGhost = False
#    fil.Friend = False
#    fil.CheckLineOfSight = checkLineOfSight

#    mobs = Mobiles.ApplyFilter(fil)

#   return mobs
    
# Find a vendor NPC by name and highlight. 
# The vendor name IS case sensitive, so a search for "john" will not match "John"
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
    
# Returns mobiles for pets or friends. Just provide names.
# Noterieties:  blue = 1, green = 2, gray = 3, gray crim = 4, orange = 5, red = 6, yellow = 7
def get_friends_by_names (friendNames = [], range = 8):
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = range
    fil.Notorieties = List[Byte](bytes([1, 2]))
    fil.IsGhost = False
    fil.Friend = False
    fil.CheckLineOfSight = True
    mobs = Mobiles.ApplyFilter(fil)

    #listValid = [m.Serial for m in mobs if m.Name in friendNames]

    if len(mobs) > 0:
        mobsList = List[type(mobs[0])]([mob for mob in mobs if mob.Name in friendNames])
        return mobsList    
    
    
    #if len(listValid) == 0:
    #    return []

    #fil = Mobiles.Filter()
    #fil.Enabled = True
    #for l in listValid:
    #    fil.Serials.Add(l)
    #fil.RangeMax = range
    #fil.Notorieties = List[Byte](bytes([1, 2]))
    #fil.IsGhost = False
    #fil.Friend = False
    #fil.CheckLineOfSight = True

    mobs = Mobiles.ApplyFilter(fil)

    return mobs

# Returns mobiles for pets or friends. Just provide names.
# Noterieties:  blue = 1, green = 2, gray = 3, gray crim = 4, orange = 5, red = 6, yellow = 7
def get_blues_in_range(range = 8):
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = range
    fil.Notorieties = List[Byte](bytes([1, 2]))
    fil.IsGhost = False
    fil.Friend = False
    fil.CheckLineOfSight = True
    mobs = Mobiles.ApplyFilter(fil)

    return mobs
    
# Good for getting town npcs like crafters.
# Noterieties:  blue = 1, green = 2, gray = 3, gray crim = 4, orange = 5, red = 6, yellow = 7
def get_yellows_in_range(range = 8):
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = range
    fil.Notorieties = List[Byte](bytes([7]))
    fil.IsGhost = False
    fil.Friend = False
    fil.CheckLineOfSight = False
    mobs = Mobiles.ApplyFilter(fil)

    return mobs
    
# Gets attackable things.
# Noterieties:  blue = 1, green = 2, gray = 3, gray crim = 4, orange = 5, red = 6, yellow = 7
def get_enemies(range = 10, serialsToExclude = []):
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = range
    fil.Notorieties = List[Byte](bytes([3,4,5,6]))
    fil.IsGhost = False
    fil.Friend = False
    fil.CheckLineOfSight = True
    mobs = Mobiles.ApplyFilter(fil)
    
    # need to remove Animate dead summons. There are a handfull of MobileIDs that match
    # the regular mobs, however these are red from animate dead when they are normally gray.
    if len(mobs) > 0:
        #for mob in mobs:
            #print(mob.Name, mob.Name not in ANIMATE_DEAD_MOBILE_NAMES and mob.Notoriety != 6 and mob.Serial not in serialsToExclude)
            #print("is in animate dead", mob.Name not in ANIMATE_DEAD_MOBILE_NAMES)
            
        mobsList = List[type(mobs[0])]([mob for mob in mobs if not (mob.Name in ANIMATE_DEAD_MOBILE_NAMES and mob.Notoriety == 6) and mob.Serial not in serialsToExclude])
#        if len(mobsList) == 0:
#            print("No mobs found")
        return mobsList

    return mobs

# Gets an enemy at full health within 10 paces of tile and is within line of sight.    
def get_honor_target():
    for mob in get_enemies(10):
        if mob.Hits == mob.HitsMax:
            return mob

# Gets your pets as mobiles    
def get_pets(range = 10, checkLineOfSight = True, mobileId = None):
    pets = []
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = range
    fil.Notorieties = List[Byte](bytes([1, 2]))
    fil.IsGhost = False
    fil.Friend = False
    fil.CheckLineOfSight = checkLineOfSight
    
    if mobileId is not None:
        fil.Bodies = List[Int32]([mobileId])
    
    blues = Mobiles.ApplyFilter(fil)    
    for blue in blues:
        if blue.CanRename:
            pets.append(blue)
    return pets
    
# Returns the decimal representation of mobile hp, e.g. 0.30 is 30% health
def get_mobile_percent_hp(mobile):
    if mobile is not None and mobile.Hits is not None and mobile.Hits > 0 and mobile.HitsMax is not None and mobile.HitsMax > 0:
        return mobile.Hits / mobile.HitsMax
    else:
        return 0
        
# Returns the decimal representation of mobile hp, e.g. 0.30 is 30% health
#def get_player_percent_mana():
#    if Player.Mana is not None and Player.Mana > 0 and Player.ManaMax is not None and Player.ManaMax > 0:
#        return Player.Mana / Player.ManaMax
#    else:
#        return 0