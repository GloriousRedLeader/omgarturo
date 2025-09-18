# Main code
SET_TO_DECORATIVE = False
RANGE = 3
PLANT_GUMP = 2847473961
REPRODUCTION_GUMP = 1726216037
DECORATIVE_GUMP = 3715612036
filter = Items.Filter()
filter.Movable = -1
filter.OnGround = True
filter.RangeMax = RANGE
plants = Items.ApplyFilter(filter)
plants = [plant for plant in plants if 'a vibrant' in plant.Name]
for plant in plants:
    print('Harvesting ', plant.Name)
    Items.UseItem(plant)
    Gumps.WaitForGump(PLANT_GUMP, 3000)
    Gumps.SendAction(PLANT_GUMP, 1)
    Gumps.WaitForGump(REPRODUCTION_GUMP, 3000)
    Gumps.SendAction(REPRODUCTION_GUMP, 7)
    Gumps.WaitForGump(REPRODUCTION_GUMP, 3000)
    Gumps.SendAction(REPRODUCTION_GUMP, 8)
    Gumps.WaitForGump(REPRODUCTION_GUMP, 3000)
    if SET_TO_DECORATIVE:
        Gumps.SendAction(REPRODUCTION_GUMP, 2)
        Gumps.WaitForGump(DECORATIVE_GUMP, 3000)
        Gumps.SendAction(DECORATIVE_GUMP, 3)
        Misc.Pause(650)
    Gumps.CloseGump(PLANT_GUMP)
    Gumps.CloseGump(REPRODUCTION_GUMP)
    Gumps.CloseGump(DECORATIVE_GUMP)
    Misc.Pause(1000)
