# Main code
HOW_MANY_TIMES_TO_BEEP = 5
HOW_OFTEN_TO_PING_MS = 5000
STRINGS_TO_LOOK_FOR = ['The Master of the Hunt has', 'You sense a dark presence', 'a putrid steed', 'a venom steed', 'an inferno steed', 'a blazing steed', 'a maelstrom steed', 'a void steed', 'a glacial steed', 'an ice steed']
Timer.Create('journalAlertPingTimer', 1)
Journal.Clear()
while True:
    if Timer.Check('journalAlertPingTimer') == False:
        Player.HeadMessage(58, 'Journal Alert Running...')
        Timer.Create('journalAlertPingTimer', HOW_OFTEN_TO_PING_MS)
    for search in STRINGS_TO_LOOK_FOR:
        if Journal.Search(search):
            found = Journal.GetLineText(search, False)
            Journal.Clear()
            for i in range(0, HOW_MANY_TIMES_TO_BEEP):
                Misc.Beep()
                Player.HeadMessage(28, '^^ Journal Alert: {} ^^'.format(found))
                Player.HeadMessage(48, '^^ Journal Alert: {} ^^'.format(found))
                Misc.Pause(1000)
    Misc.Pause(1000)
