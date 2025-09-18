# Inlined dependencies (topologically sorted)
def move_all_items_from_container(sourceSerial, destinationSerial):
    for item in Items.FindBySerial(sourceSerial).Contains:
        Player.HeadMessage(455, 'Moving item {}'.format(item.Name))
        Items.Move(item, destinationSerial, item.Amount)
        Misc.Pause(800)

# Main code
sourceSerial = Target.PromptTarget('Pick source container')
destinationSerial = Target.PromptTarget('Pick target container')
Items.UseItem(sourceSerial)
Misc.Pause(650)
Items.UseItem(destinationSerial)
Misc.Pause(650)
move_all_items_from_container(sourceSerial, destinationSerial)
