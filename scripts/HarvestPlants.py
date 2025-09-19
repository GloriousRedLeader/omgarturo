# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-09-19
# Use at your own risk.

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

SET_TO_DECORATIVE = False

# planting has huge range, but harvesting has pretty limited range
# its 3 tiles in any direction (diagonal included)
RANGE = 3

PLANT_GUMP =  0xa9b90129
REPRODUCTION_GUMP = 0x66e3f765
DECORATIVE_GUMP =  0xdd77bd84

filter = Items.Filter()
filter.Movable = -1
filter.OnGround = True
filter.RangeMax = RANGE
plants = Items.ApplyFilter(filter)
plants = [plant for plant in plants if "a vibrant" in plant.Name]
    
for plant in plants:
    print("Harvesting ", plant.Name)
    
    Items.UseItem(plant)
    Gumps.WaitForGump(PLANT_GUMP, 3000)

    # Takes you to reproduction bump
    Gumps.SendAction(PLANT_GUMP, 1) 
    Gumps.WaitForGump(REPRODUCTION_GUMP, 3000)
    
    # Harvest resources / petals
    Gumps.SendAction(REPRODUCTION_GUMP, 7) 
    Gumps.WaitForGump(REPRODUCTION_GUMP, 3000)
    
    # Get seeds
    Gumps.SendAction(REPRODUCTION_GUMP, 8) 
    Gumps.WaitForGump(REPRODUCTION_GUMP, 3000)
    
    if SET_TO_DECORATIVE:
        Gumps.SendAction(REPRODUCTION_GUMP, 2) 
        Gumps.WaitForGump(DECORATIVE_GUMP, 3000)
        
        # Confirmation yes
        Gumps.SendAction(DECORATIVE_GUMP, 3) 
        Misc.Pause(650)
    
    # Close gump
    Gumps.CloseGump(PLANT_GUMP)
    Gumps.CloseGump(REPRODUCTION_GUMP) 
    Gumps.CloseGump(DECORATIVE_GUMP) 
            
    Misc.Pause(1000)
