# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2024-03-26
# Use at your own risk. 

# This is a standalone script to train musicianship. Praise be.

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