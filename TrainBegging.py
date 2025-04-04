# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2024-03-26
# Use at your own risk. 

# Find an npc and go for it.
# This may or may not work. I think you may need high karma. 
# Never got around to raising this skill.

MSG = "Pick an NPC to beg from"
Player.HeadMessage(128, MSG)
npc = Mobiles.FindBySerial(Target.PromptTarget(MSG))

while Player.GetSkillValue('Begging') < Player.GetSkillCap('Begging'):
    Player.UseSkill("Begging")
    Target.WaitForTarget(10000, False)
    Target.TargetExecute(npc)
    Misc.Pause(3000)
