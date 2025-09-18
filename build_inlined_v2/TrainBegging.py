# Main code
MSG = 'Pick an NPC to beg from'
Player.HeadMessage(128, MSG)
npc = Mobiles.FindBySerial(Target.PromptTarget(MSG))
while Player.GetSkillValue('Begging') < Player.GetSkillCap('Begging'):
    Player.UseSkill('Begging')
    Target.WaitForTarget(10000, False)
    Target.TargetExecute(npc)
    Misc.Pause(3000)
