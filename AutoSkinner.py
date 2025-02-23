# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/uo-razor-enhanced
#   2024-11-21
# Use at your own risk. 

from System.Collections.Generic import List
import sys
from System import Byte, Int32
from Scripts.omgarturo.fm_core.core_player import find_first_in_container_by_ids
from Scripts.omgarturo.fm_core.core_player import find_first_in_hands_by_id
from Scripts.omgarturo.fm_core.core_player import move_all_items_from_container
from Scripts.omgarturo.fm_core.core_player import move_item_to_container_by_id
from Scripts.omgarturo.fm_core.core_player import find_in_container_by_id
from Scripts.omgarturo.fm_core.core_player import find_first_in_container_by_name
from Scripts.omgarturo.fm_core.core_player import find_all_in_container_by_id
from Scripts.omgarturo.fm_core.core_player import move_item_to_container
from Scripts.omgarturo.fm_core.core_mobiles import get_friends_by_names
from Scripts.omgarturo.fm_core.core_rails import move
from Scripts.omgarturo.fm_core.core_rails import go_to_tile
from Scripts.omgarturo.fm_core.core_rails import get_tile_in_front
from Scripts.omgarturo.fm_core.core_items import AXE_STATIC_IDS
from Scripts.omgarturo.fm_core.core_items import LOG_STATIC_IDS
from Scripts.omgarturo.fm_core.core_items import TREE_STATIC_IDS
from Scripts.omgarturo.fm_core.core_items import DAGGER_STATIC_IDS
from Scripts.omgarturo.fm_core.core_items import BOARD_STATIC_IDS
from Scripts.omgarturo.fm_core.core_items import MINER_TOOLS_STATIC_IDS
from Scripts.omgarturo.fm_core.core_items import ORE_STATIC_IDS
from Scripts.omgarturo.fm_core.core_items import INGOT_STATIC_IDS
from Scripts.omgarturo.fm_core.core_items import STONE_STATIC_IDS
from Scripts.omgarturo.fm_core.core_items import SAND_STATIC_IDS

# Auto skinner
# Just storing this. Original author: https://razorenhanced.net/dokuwiki/doku.php?id=toolscripts
   
import sys
from System.Collections.Generic import List

self_pack = Player.Backpack.Serial
##Types
corpse = 0x2006
uncutleather = 0x1079
scalesType = 0x26B4
scissorsType = 0x0F9F

##lists
bladeList = [0x2D20, 0xf52, 0xec4, 0x13f6, 0xec3]
leathersList = List[Int32]((0x1081))
ignore = []

def scan():
    skin = Items.Filter()
    skin.Enabled = True
    
    skin.RangeMin = 0
    skin.RangeMax = 2
    skin.IsCorpse = True

    skins = Items.ApplyFilter(skin)
    for toskin in skins:
        if toskin:
            if not toskin.Serial in ignore:
                Misc.SendMessage( 'Corpse found', 20 )
                skinLoot(toskin)
                ignore.append(toskin.Serial)
                Misc.Pause(1100)
        
    else :
        Misc.SendMessage( 'No corpse', 20 )

    
    
    
    

# Helper Functions
###################################
def getByItemID(itemid, source):
    #find an item id in container serial
    for item in Items.FindBySerial(source).Contains:
        if item.ItemID == itemid:
            return item
        else:
            Misc.NoOperation()
###################################

def getBlade():
    for item in bladeList:
        blade = getByItemID(item, self_pack)
        if blade is not None:
            return blade
            
def getLeatherFromGround():
    leatherFilter = Items.Filter()
    leatherFilter.Enabled = True
    leatherFilter.OnGround = True
    leatherFilter.Movable = True
    leatherFilter.Graphics = leathersList
    leatherFilter.RangeMax = 2
    
    leathers = Items.ApplyFilter(leatherFilter)
    Misc.SendMessage
    for leather in leathers:
        Items.Move(leather.Serial, self_pack, 100)
        Misc.Pause(700)

def skinLoot(x):
    corpse = x
    if corpse:
        Items.UseItem(corpse)
        Misc.Pause(550)
        for item in bladeList:
            blade = getBlade()
        if blade is not None:
            Items.UseItem(blade)
            Target.WaitForTarget(3000, True)
            Target.TargetExecute(corpse)
            Misc.Pause(1000)
        else:
            Misc.SendMessage('No Blades Found')
            #sys.exit()
    else:
        Misc.SendMessage('cantfind corpse')
        #sys.exit()
        
    leather = getByItemID(uncutleather, corpse.Serial)
    scales = getByItemID(scalesType, corpse.Serial)
    
    if scales is not None:
        Items.Move(scales, self_pack, 0)
        Misc.Pause(550)
        
    if leather is not None:
        Misc.Pause(150)
        Items.MoveOnGround(leather, 0, Player.Position.X + 1, Player.Position.Y + 1, Player.Position.Z)
        Misc.Pause(550)
        scissors = getByItemID(scissorsType, self_pack)
        if scissors is not None:
            Items.UseItem(scissors)
            Target.WaitForTarget(3000, True)
            Target.TargetExecute(leather)
            Misc.Pause(700)
        else:
            Misc.SendMessage('No Scissors Found')
            #sys.exit()
            
        getLeatherFromGround()
        
   
while True:
    scan()
    Misc.Pause(3000)