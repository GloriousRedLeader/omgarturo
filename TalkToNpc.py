# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-09-03
# Use at your own risk. 

from Scripts.omgarturo.fm_core.core_mobiles import get_yellows_in_range

# Finds nearest yellow npc and opens the talk contextual menu.
# Use this for doing quests if you cant be bothered to click on an NPC.

TALK_CONTEXT = 0x00001500

npcs = get_yellows_in_range(range = 1)
if len(npcs) > 0:
    print(npcs[0].Name)
    Misc.UseContextMenu(npcs[0].Serial,"Talk",3000)
    Misc.Pause(1000)

#Misc.WaitForContext(TALK_CONTEXT, 10000)
#Misc.ContextReply(TALK_CONTEXT, 1)