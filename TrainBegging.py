# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/uo-razor-enhanced
#   2024-03-26
# Use at your own risk. 

# Find an npc and go for it.

MSG = "Pick an NPC to beg from"
Player.HeadMessage(128, MSG)
npc = Mobiles.FindBySerial(Target.PromptTarget(MSG))

while Player.GetSkillValue('Begging') < Player.GetSkillCap('Begging'):
    Player.UseSkill("Begging")
    Target.WaitForTarget(10000, False)
    Target.TargetExecute(npc)
    Misc.Pause(3000)
