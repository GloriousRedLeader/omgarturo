# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-09-19
# Use at your own risk.

# ##########################################################
# #                                                        #
# #              INLINED DEPENDENCIES                      #
# #                                                        #
# #  DO NOT EDIT THIS SECTION - AUTO-GENERATED CODE        #
# #                                                        #
# #  These are dependencies from fm_core that have been    #
# #  automatically inlined. For user-editable code,        #
# #  scroll down to the bottom of this file.               #
# #                                                        #
# ##########################################################

from System import Byte, Int32
from System.Collections.Generic import List

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

# Trick or treat event. Targets nearest yellow npc and does the needful.
# Iterates through NPCs and does the trick or treat stuff.
    
fil = Mobiles.Filter()
fil.Enabled = True
fil.RangeMax = 3
fil.Notorieties = List[Byte](bytes([7]))
fil.IsGhost = False
fil.Friend = False
fil.CheckLineOfSight = False
mobs = Mobiles.ApplyFilter(fil)

mob = Mobiles.Select(mobs,"Nearest")

if mob is not None:
    #Player.HeadMessage(38, "Targeting {}".format(mob.Name))
    Player.ChatSay("trick or treat")
    Target.WaitForTarget(4000, False)
    Target.TargetExecute(mob)
