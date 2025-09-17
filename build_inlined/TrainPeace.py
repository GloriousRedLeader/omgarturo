# ===============================================
# Imports
# ===============================================
from System.Collections.Generic import List

# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2024-03-26
# Use at your own risk. 


# I DID NOT WRITE THIS SCRIPT! I did make it worse though.
# Credit goes to wherever this came from. 
# Im hosting for safekeeping.
# Also, it may or may not work. I forget. Good luck.


'''
Author: TheWarDoctor95
Other Contributors:
Last Contribution By: TheWarDoctor95 - March 23, 2019

Description: Uses the Peacemaking skill on the player to train Peacemaking to GM
'''

Player.HeadMessage(38, "Training Peacemaking")

peacemakingTimerMilliseconds = 10200
journalEntryDelayMilliseconds = 200
targetClearDelayMilliseconds = 200

def TrainPeacemaking():
    '''
    Trains Peacemaking to GM
    '''
    # Script variables
    global peacemakingTimerMilliseconds
    peacemakingHandled = False

    if Player.GetRealSkillValue( 'Peacemaking' ) == Player.GetSkillCap( 'Peacemaking' ):
        Misc.SendMessage( 'You\'ve already maxed out Peacemaking!', 65 )
        return

    # Initialize skill timers
    Timer.Create( 'peacemakingTimer', 1 )

    # Initialize the journal and ignore object list
    Journal.Clear()
    Misc.ClearIgnore()

    while not Player.IsGhost and Player.GetRealSkillValue( 'Peacemaking' ) < Player.GetSkillCap( 'Peacemaking' ):
        if not Timer.Check( 'peacemakingTimer' ):
            # Clear any previously selected target and the target queue
            Target.ClearLastandQueue()

            # Wait for the target to finish clearing
            Misc.Pause(targetClearDelayMilliseconds )

            #Player.UseSkill( 'Peacemaking' )

            # Wait for the journal entry to come up
            #Misc.Pause( journalEntryDelayMilliseconds )

            # Handle the Journal response
            #if Journal.SearchByType( 'What instrument shall you play?', 'Regular' ):
            instrument = find_first_in_container_by_ids(INSTRUMENT_STATIC_IDS, Player.Backpack)
                ##instrument = FindInstrument( Player.Backpack )
            if instrument == None:
                Misc.Message( 'No instrument to peacemake with.', 1100 )
                return
             #Target.WaitForTarget( 2000, True )
            
            Items.UseItem(instrument)
            Misc.Pause(1000)
             
            Player.UseSkill( 'Peacemaking' )
             
            #Target.TargetExecute( instrument )

            Target.WaitForTarget( 2000, True )
            Target.TargetExecute( Player.Serial )

            # Wait for the journal entry to come up
            Misc.Pause( journalEntryDelayMilliseconds )

            if ( Journal.SearchByType( 'You play hypnotic music, calming your target.', 'Regular' ) or
                    Journal.SearchByType( 'You play your hypnotic music, stopping the battle.', 'Regular' ) or
                    Journal.SearchByType( 'You attempt to calm everyone, but fail.', 'Regular' ) or
                    Journal.SearchByType( 'You play hypnotic music, but there is nothing in range for you to calm.', 'Regular' ) or
                    Journal.SearchByType( 'You attempt to calm your target, but fail.', 'Regular' ) ):
                # Skill was used successfully, even if the enemy was not successfully put to peace
                Timer.Create( 'peacemakingTimer', peacemakingTimerMilliseconds )
            elif Journal.SearchByType( 'You have no chance of calming that creature', 'Regular' ):
                # We werent able to use the skill, indicate as such by not waiting for the typical cooldown
                Timer.Create( 'peacemakingTimer', 1 )
            else:
                # We werent able to use the skill, indicate as such by not waiting for the typical cooldown
                Timer.Create( 'peacemakingTimer', 1 )

            Journal.Clear()

        # Wait a little bit so that the while loop doesn't consume as much CPU
        Misc.Pause( 50 )

# Start Peacemaking training
TrainPeacemaking()