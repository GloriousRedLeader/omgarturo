from System import Byte, Int32
from System.Collections.Generic import List

# Inlined dependencies (topologically sorted)
def get_pets(range=10, checkLineOfSight=True, mobileId=None):
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

# Main code
pets = get_pets()
for pet in pets:
    Items.UseItem(1075577407)
    Target.WaitForTarget(3000)
    Target.TargetExecute(pet)
    Gumps.WaitForGump(1246209771, 3000)
    Gumps.SendAction(1246209771, 1)
    Misc.Pause(1000)
