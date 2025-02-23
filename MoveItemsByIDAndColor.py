# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/uo-razor-enhanced
#   2024-03-26
# Use at your own risk. 

# Prompts for an item type and destination container. Transfers 
# all items matching that item id AND color to another container.
# You can use this to turn in bods. Hit the hotkey, target the 
# bod, and then target the npc. Thats it.

from Scripts.omgarturo.fm_core.core_player import move_item_to_container_by_id

# Prompts for an item type
# Source is that items container
# Destination is prompt
# Moves all items with that ItemID and Color

itemSerial = Target.PromptTarget("Which item type? Click one.")
destinationSerial = Target.PromptTarget("Pick target container")

Items.UseItem(destinationSerial)
Misc.Pause(650)

item = Items.FindBySerial(itemSerial)
if item is not None:
    sourceSerial = Items.FindBySerial(item.Container).Serial
    move_item_to_container_by_id(item.ItemID, sourceSerial, destinationSerial, item.Color)