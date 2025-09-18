while Player.GetSkillValue("Stealth") < 60: 

    if Player.Visible:
        Target.Cancel()        
        Player.UseSkill("Hiding")
        Misc.Pause(3000)

    while not Player.Visible:
        Player.Walk("North")
        Player.Walk("North")
        Player.Walk("East")
        Player.Walk("East")
        Player.Walk("East")
        Player.Walk("South")
        Player.Walk("South")
        Player.Walk("West")
        Player.Walk("West")
        Player.Walk("West")
        
    Misc.Pause(400)
    
sys.exit()
