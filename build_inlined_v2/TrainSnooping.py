backpackSerial = Target.PromptTarget('Pick a bagpack to snoop, should be another player in guild')
while Player.GetSkillValue('Snooping') < Player.GetSkillCap('Snooping'):
    Items.UseItem(backpackSerial)
    Misc.Pause(1000)
