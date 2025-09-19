# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-02-04
# Use at your own risk. 

from Scripts.omgarturo.src.fm_core.core_crafting import CRAFTING_GUMP_ID
from Scripts.omgarturo.src.fm_core.core_crafting import CAT_TINKERING_TRAPS
from Scripts.omgarturo.src.fm_core.core_items import SMALL_CRATE_GRAPHIC_ID
from Scripts.omgarturo.src.fm_core.core_items import TINKERING_TOOL_STATIC_ID

# Will attempt to tracp a small crate.
# Requirements: 
#   1) 30 tinkering skill. This means low % chance to trap, 
#       but the traps do less dmg to players.
#   2) Lots of tinkering tools in your backpack.
#   3) Arrows and Iron Ingots in backpack.
#   4) Small crates in backpack. Grain alined north south 
#       (use a house tool to align)

gumpDelayMs = 750
gumpSet = False
countTrapped = 0
crates = Items.FindAllByID(SMALL_CRATE_GRAPHIC_ID, -1, Player.Backpack.Serial, 0)
for crate in crates:
    print("************************")
    print(crate.Name, crate.Color)
    #for p in crate.Properties:
        #print(p.ToString())
        
    # Were just setting a default here. It may very well be trapped.
    # But there is nothing wrong with trying to trap it again.
    # It will fail fast and tell us the crate is already trapped and move on.
    crateIsTrapped = False
    print("Current trapped boxes: ", countTrapped)
    while not crateIsTrapped:
        
        tools = Items.FindAllByID(TINKERING_TOOL_STATIC_ID, -1, Player.Backpack.Serial, 0)
        if len(tools) > 0:
            Items.UseItem(tools[0])
            Gumps.WaitForGump(CRAFTING_GUMP_ID, 10000)
            Misc.Pause(gumpDelayMs)#1000 before
            
            if not Gumps.HasGump(CRAFTING_GUMP_ID):
                print("Quitting: Might not have a tool")
                sys.exit()

            # One time initialization.
            if not gumpSet:
                print("Setting Special Material and Category (one time operation)")
                # Set category to traps
                Gumps.SendAction(CRAFTING_GUMP_ID, CAT_TINKERING_TRAPS)                    
                Gumps.WaitForGump(CRAFTING_GUMP_ID, 10000)
                Misc.Pause(gumpDelayMs)#1000 before
                if not Gumps.HasGump(CRAFTING_GUMP_ID):
                    print("Quitting: Could not set category to traps")
                    sys.exit()
                
                # Set material to iron just in case
                Gumps.SendAction(CRAFTING_GUMP_ID, 7)
                Gumps.WaitForGump(CRAFTING_GUMP_ID, 5000)
                Misc.Pause(gumpDelayMs)#1000 before
                if not Gumps.HasGump(CRAFTING_GUMP_ID):
                    print("Quitting: Could not set special material")
                    sys.exit()
                    
                # The actual special material button
                Gumps.SendAction(CRAFTING_GUMP_ID, 6)
                Gumps.WaitForGump(CRAFTING_GUMP_ID, 5000)
                Misc.Pause(gumpDelayMs)#1000 before
                gumpSet = True
        else:
            print("Quitting: no tools found")
            sys.exit()
        
        Gumps.SendAction(CRAFTING_GUMP_ID, 2)
        Target.WaitForTarget(3000)
        Target.TargetExecute(crate)
        
        Gumps.WaitForGump(CRAFTING_GUMP_ID, 5000)
        Misc.Pause(760)
        gumpData = Gumps.GetGumpData(CRAFTING_GUMP_ID).gumpText
        
        crateIsTrapped = next((True for gd in gumpData if "Trap is disabled until you lock the chest." == gd or "You can only place one trap on an object at a time." == gd), False)
        #print("crateIsTrapped ", crateIsTrapped)
        
        Misc.Pause(250)

    countTrapped = countTrapped + 1