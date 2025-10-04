# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-10-04
# Use at your own risk.

# ##########################################################
# #                                                        #
# #                 USER EDITABLE CODE                      #
# #                                                        #
# #  This is the original script code that you can         #
# #  modify and customize. Edit the parameters, logic,     #
# #  and function calls below as needed for your setup.    #
# #                                                        #
# #  The dependencies above have been automatically        #
# #  inlined and should not be modified.                   #
# ##########################################################

HOW_MANY_TIMES_TO_BEEP = 5

# If you want a pulse just to let you know this script is running
# this is the number of milliseconds to remind you it is running.
# Set to a really high number if you do not want to deal with it.
HOW_OFTEN_TO_PING_MS = 5000

# Anything matching these strings will alert
STRINGS_TO_LOOK_FOR = [
    "The Master of the Hunt has",
    "You sense a dark presence",
    #"a putrid steed",
    #"a venom steed",
    #"an inferno steed",
    #"a blazing steed",
    #"a maelstrom steed", 
    #"a void steed",
    #"a glacial steed",
    #"an ice steed"
    
    
    
    
    
]

Timer.Create( 'journalAlertPingTimer', 1 )

Journal.Clear()
while True:
    
    if Timer.Check( 'journalAlertPingTimer' ) == False:
        Player.HeadMessage( 58, "Journal Alert Running...")
        Timer.Create( 'journalAlertPingTimer', HOW_OFTEN_TO_PING_MS )
    
    for search in STRINGS_TO_LOOK_FOR:
        if Journal.Search(search):
            found = Journal.GetLineText(search,False)
            Journal.Clear()
            #Player.ChatSay("[ohshit")
            for i in range(0, HOW_MANY_TIMES_TO_BEEP):
                Misc.Beep()
                Player.HeadMessage( 28, "^^ Journal Alert: {} ^^".format(found) )
                Player.HeadMessage( 48, "^^ Journal Alert: {} ^^".format(found) )
                Misc.Pause(1000) 
            #sys.exit()
            

    Misc.Pause(1000)      
