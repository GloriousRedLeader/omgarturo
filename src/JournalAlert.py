# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2024-10-26
# Use at your own risk. 

# This is a standalone script that will monitor exciting entries in the journal.
# If you are looking for a rare pet, just plug the name in here.
# If you are waiting for a boss to spawn during some event (e.g. SoTW on InsaneUO, 
# add the strings here.)

# Number of times to beep and flash a message
HOW_MANY_TIMES_TO_BEEP = 5

# If you want a pulse just to let you know this script is running
# this is the number of milliseconds to remind you it is running.
# Set to a really high number if you do not want to deal with it.
HOW_OFTEN_TO_PING_MS = 5000

# Anything matching these strings will alert
STRINGS_TO_LOOK_FOR = [
    "The Master of the Hunt has",
    "You sense a dark presence",
    "Headless Horseman",
    "Coil",
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