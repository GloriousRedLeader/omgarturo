def get_corpses(range=2):
    filter = Items.Filter()
    filter.OnGround = True
    filter.RangeMax = range
    filter.IsCorpse = True
    return Items.ApplyFilter(filter)
filter = Items.Filter()
while Player.GetSkillValue('Forensic Evaluation') < 55:
    corpses = get_corpses(1)
    for corpse in corpses:
        Player.UseSkill('Forensics')
        Target.WaitForTarget(10000, False)
        Target.TargetExecute(corpse.Serial)
        Misc.Pause(1000)
while Player.GetSkillValue('Forensic Evaluation') < Player.GetSkillCap('Forensic Evaluation'):
    Player.UseSkill('Forensics')
    Target.WaitForTarget(10000, False)
    Target.TargetExecute(1090963549)
    Misc.Pause(1000)
