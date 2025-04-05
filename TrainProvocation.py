# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2024-03-26
# Use at your own risk. 

# I DID NOT WRITE THIS SCRIPT!
# Credit goes to wherever this came from. 
# Im hosting for safekeeping.
# Also, it may or may not work. I forget. Good luck.

'''
Author: TheWarDoctor95
Other Contributors:
Last Contribution By: TheWarDoctor95 - March 23, 2019

Description: Uses the instruments from the player's backpack and the selected or
    auto-selected target to train Provocation to its cap
'''


from Scripts.omgarturo.fm_core.core_items import INSTRUMENT_STATIC_IDS
from Scripts.omgarturo.fm_core.core_player import find_first_in_container_by_ids
from System import Byte
from System.Collections.Generic import List

Player.HeadMessage(38, "Training Provocation")

autoSelectTarget = False
provocationTimerMilliseconds = 10200
journalEntryDelayMilliseconds = 200
targetClearDelayMilliseconds = 200

colors = {
    'green': 65,
    'cyan': 90,
    'orange': 43,
    'red': 1100,
    'yellow': 52
}

#from Scripts import config
#from Scripts.glossary.items.instruments import FindInstrument
#from Scripts.glossary.colors import colors
#from Scripts.glossary.enemies import GetEnemies

def GetEnemies( Mobiles, minRange = 0, maxRange = 12, IgnorePartyMembers = False ):
    '''
    Returns a list of the nearby enemies with the specified notorieties
    '''
    
    notorieties = [Byte(3), Byte(4), Byte(5), Byte(6)]

    if Mobiles == None:
        raise ValueError( 'Mobiles was not passed to GetEnemies' )

    enemyFilter = Mobiles.Filter()
    enemyFilter.Enabled = True
    enemyFilter.RangeMin = minRange
    enemyFilter.RangeMax = maxRange
    enemyFilter.Notorieties = notorieties
    enemyFilter.CheckIgnoreObject = True
    enemyFilter.Friend = False
    enemies = Mobiles.ApplyFilter( enemyFilter )

    if IgnorePartyMembers:
        partyMembers = [ enemy for enemy in enemies if enemy.InParty ]
        for partyMember in partyMembers:
            enemies.Remove( partyMember )

    return enemies

def TrainProvocation():
    '''
    Trains Musicianship by using the instruments in the player's bag
    Transitions to a new instrument if the one being used runs out of uses
    '''
    global autoSelectTarget
    global provocationTimerMilliseconds

    Timer.Create( 'provocationTimer', 1 )

    #instrument = FindInstrument( Player.Backpack )
    instrument = find_first_in_container_by_ids(INSTRUMENT_STATIC_IDS, Player.Backpack)
    if instrument == None:
        Misc.SendMessage( 'No instruments to train with', colors[ 'red' ] )
        return
    
    provocationTarget = None
    while instrument != None and Player.GetSkillValue( 'Provocation' ) < 100 and not Player.IsGhost:
        if provocationTarget == None:
            if autoSelectTarget:
                enemies = GetEnemies( Mobiles, 0, 8 )
                provocationTarget = Mobiles.Select( enemies, 'Nearest' )
            else:
                provocationTarget = Target.PromptTarget( 'Select target to train provo on' )
                provocationTarget = Mobiles.FindBySerial( provocationTarget )
            
            if provocationTarget != None:
                Mobiles.Message( provocationTarget, colors[ 'cyan' ], 'Selected for provocation training' )
        else:
            provocationTarget = Mobiles.FindBySerial( provocationTarget.Serial )
            
        if autoSelectTarget and provocationTarget == None:
            Misc.Pause( 100 )
            continue

        if not Timer.Check( 'provocationTimer' ):
            Journal.Clear()
            Player.UseSkill( 'Provocation' )
            Misc.Pause( journalEntryDelayMilliseconds )
            if Journal.Search( 'What instrument shall you play?' ):
                # Instrument either broke or hasn't been selected
                instrument = FindInstrument( Player.Backpack )
                if instrument == None:
                    # No more instruments, stop the provo attempt
                    Target.Cancel()

                    Misc.SendMessage( 'Ran out of instruments to train with', colors[ 'red' ] )
                    return
                else:
                    Target.WaitForTarget( 2000, True )
                    Target.TargetExecute( instrument.Serial )

            Target.WaitForTarget( 2000, True )
            Target.TargetExecute( provocationTarget )
            Target.WaitForTarget( 2000, True )
            Target.TargetExecute( Player.Serial )
            Target.SetLast( provocationTarget )

            Timer.Create( 'provocationTimer', provocationTimerMilliseconds )

        # Wait a little bit so that the while loop doesn't consume as much CPU
        Misc.Pause( 50 )

# Start Training
TrainProvocation()