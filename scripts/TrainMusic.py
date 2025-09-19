# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-09-19
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

INSTRUMENT_STATIC_IDS = [ 
    0x0E9C, # drum
    0x2805, # flute
    0x0EB3, # lute
    0x0EB2, # lap harp
    0x0EB1, # standing harp
    0x0E9E, # tambourine
    0x0E9D, # tambourine (tassle)
]

Player.HeadMessage(38, "Training Musicianship")
Player.HeadMessage(38, "Make sure you have instruments in your backpack.")

while not Player.IsGhost and Player.GetSkillValue('Musicianship') < 110:
    instruments = Items.FindAllByID(INSTRUMENT_STATIC_IDS, -1, Player.Backpack.Serial, 0)
    for instrument in instruments:
        Items.UseItem(instrument)
        Misc.Pause(3000)
