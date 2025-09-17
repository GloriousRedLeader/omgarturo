# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2024-11-27
# Use at your own risk. 


# Trains Forensic Eval

# 0 - 30 from trainer
# 30 - 55 corpses
# 55+ chests?

while Player.GetSkillValue('Forensic Evaluation') < 55:
    corpses = get_corpses(1)
    for corpse in corpses:
        Player.UseSkill("Forensics")
        Target.WaitForTarget(10000, False)
        Target.TargetExecute(corpse.Serial)
        Misc.Pause(1000)

# Just plugging in a chest serial for now.        
while Player.GetSkillValue('Forensic Evaluation') < Player.GetSkillCap('Forensic Evaluation'):
    Player.UseSkill("Forensics")
    Target.WaitForTarget(10000, False)
    Target.TargetExecute(0x4106C85D)
    Misc.Pause(1000)