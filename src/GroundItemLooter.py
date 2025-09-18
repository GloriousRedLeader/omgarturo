# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2024-11-21
# Use at your own risk. 

from System.Collections.Generic import List
import sys
from System import Byte, Int32
from Scripts.omgarturo.src.fm_core.core_player import find_first_in_container_by_ids
from Scripts.omgarturo.src.fm_core.core_player import move_all_items_from_container
from Scripts.omgarturo.src.fm_core.core_player import move_item_to_container_by_id
from Scripts.omgarturo.src.fm_core.core_player import find_in_container_by_id
from Scripts.omgarturo.src.fm_core.core_player import find_first_in_container_by_name
from Scripts.omgarturo.src.fm_core.core_player import find_all_in_container_by_id
from Scripts.omgarturo.src.fm_core.core_player import move_item_to_container
from Scripts.omgarturo.src.fm_core.core_mobiles import get_friends_by_names
from Scripts.omgarturo.src.fm_core.core_mobiles import get_pets
from Scripts.omgarturo.src.fm_core.core_rails import move
from Scripts.omgarturo.src.fm_core.core_rails import go_to_tile
from Scripts.omgarturo.src.fm_core.core_rails import get_tile_in_front
from Scripts.omgarturo.src.fm_core.core_items import AXE_STATIC_IDS
from Scripts.omgarturo.src.fm_core.core_items import LOG_STATIC_IDS
from Scripts.omgarturo.src.fm_core.core_items import TREE_STATIC_IDS
from Scripts.omgarturo.src.fm_core.core_items import DAGGER_STATIC_IDS
from Scripts.omgarturo.src.fm_core.core_items import BOARD_STATIC_IDS
from Scripts.omgarturo.src.fm_core.core_items import MINER_TOOLS_STATIC_IDS
from Scripts.omgarturo.src.fm_core.core_items import ORE_STATIC_IDS
from Scripts.omgarturo.src.fm_core.core_items import INGOT_STATIC_IDS
from Scripts.omgarturo.src.fm_core.core_items import STONE_STATIC_IDS
from Scripts.omgarturo.src.fm_core.core_items import SAND_STATIC_IDS
from Scripts.omgarturo.src.fm_core.core_items import BLUE_BEETLE_ITEM_ID

# Will pick up items on the ground and stash them in inventory or giant beetles
# Will attempt to deploy giant beetles that are in inventory.
# You can use this for idocs. It isnt great though. Needs work.
# Basically it launches a bunch of beetles, looks for things on the ground
# and tries to stash as much crap as it finds in the beetles and your inventory.

deployGiantBeetle = True

Timer.Create( 'pingTimer', 1 )

numDeployedPets = len(Player.Pets)
if numDeployedPets < 5 and deployGiantBeetle:
    for blueBeetle in Items.FindAllByID(BLUE_BEETLE_ITEM_ID, -1, Player.Backpack.Serial, -1):
        Items.UseItem(blueBeetle)
        Misc.Pause(650)
        numDeployedPets = numDeployedPets + 1
        if numDeployedPets == 5:
            break

Player.ChatSay("All Follow Me")

while True:
    if Timer.Check( 'pingTimer' ) == False:
        Player.HeadMessage( 118, "Ground Looter Running...")
        Timer.Create( 'pingTimer', 3000)
        
    filter = Items.Filter()
    filter.Movable = 1
    filter.OnGround = True
    filter.RangeMax = 2
    items = Items.ApplyFilter(filter)

    packAnimals = get_pets()
    for packAnimal in packAnimals:
        Items.UseItem(packAnimal.Backpack.Serial)
        Misc.Pause(650)
        
    for item in items:
      
        if Player.Weight + item.Weight < Player.MaxWeight and ((not item.IsContainer and Player.Backpack.Contains.Count < 125) or (item.IsContainer and Player.Backpack.Contains.Count + item.Contains.Count < 125)):
            print("Moving item {}".format(item.Name))
            move_item_to_container(item, Player.Backpack.Serial)
        elif len(packAnimals) > 0:
            for packAnimal in packAnimals:
                Items.UseItem(packAnimal.Backpack.Serial)
                Misc.Pause(650)
                print("Animal: {}, Weight: {}, Items: {}".format(packAnimal.Name, packAnimal.Backpack.Weight, packAnimal.Backpack.Contains.Count))
                if packAnimal.Backpack.Weight + item.Weight < 1350:
                    if item.IsContainer:
                        if item.Contains.Count + packAnimal.Backpack.Contains.Count < 125:
                            print("Moving container {}".format(item.Name))
                            move_item_to_container(item, packAnimal.Backpack.Serial)
                            break
                        else:
                            print("Not moving container because there are too many items in the container")
                    else:
                        print("Moving container {}".format(item.Name))
                        move_item_to_container(item, packAnimal.Backpack.Serial)
                        break
                else:
                    print("Not moving item {} because it is too heavy".format(item.Name))
    Misc.Pause(650)                    
