
# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/uo-razor-enhanced
#   2025-02-07
# Use at your own risk. 

from Scripts.omgarturo.fm_core.core_mobiles import get_enemies
from Scripts.omgarturo.fm_core.core_player import move_all_items_from_container
from Scripts.omgarturo.fm_core.core_items import AXE_STATIC_IDS, LOG_STATIC_IDS, TREE_STATIC_IDS
from Scripts.omgarturo.fm_core.core_player import find_in_container_by_id
from Scripts.omgarturo.fm_core.core_player import move_item_to_container
from Scripts.omgarturo.fm_core.core_spells import get_fc_delay
from Scripts.omgarturo.fm_core.core_rails import get_tile_in_front
from System.Collections.Generic import List
import sys
from System import Byte, Int32
import time

# Drops everything in the list below to the ground so it doesnt clutter your bags.
# Its like and inverse auto looter.

TRASH_NAMES = [
    "Helm of Swiftness",
    "Talon Bite",
    "Fey Leggings",
    "Soul Seeker",
    "Blade Dance",
    "Quiver of the Elements",
    "Quiver of Rage",
    "Flesh Ripper",
    "Aegis of Grace",
    "Pads of the Cu Sidhe",
    "Totem of the Void",
    "Bonesmasher",
    "Robe of the Equinox",
    "Robe of the Eclipse",
    "Righteous Anger",
    "Boomstick",
    "Bloodwood Spirit",
    "Windsong",
    "Wildfire Bow",
    "Raed's Glory",
    "Brightsight Lenses",
    "Burglar's Bandana",
    "Orcish Visage",
    "Gloves of the Pugilist",
    "Blaze of Death",
    "Arctic Death Dealer",
    "Staff of Power",
    "Violet Courage",
    "Gold Bricks",
    "Lord Blackthorn's Exemplar", # '
    "Wrath of the Dryad",
    "Jaana's Staff", #'
    "Sentinel's Guard", #'
    "a map of the known world",
    "10th Anniversary Sculpture",
    "Katrina's Crook", #'
    "Pixie Swatter",
    "Dragon's End", #'
    "Heart of the Lion",
    "Luna Lance",
    "Breastplate of Justice (Virtue Armor Set)",
    "Gorget of Honesty (Virtue Armor Set)",
    "Legs of Honor (Virtue Armor Set)",
    "Helm of Spirituality (Virtue Armor Set)",
    "Gwenno's Harp", #'
    "Sollerets of Sacrifice (Virtue Armor Set)",
    "Gauntlets of Valor (Virtue Armor Set)",
    "Arms of Compassion (Virtue Armor Set)",
    "Alchemist's Bauble", #'
    "Night's Kiss", #'
    "Bow of the Juka King",
]

Timer.Create( 'pingTimer', 1 )

while True:
    if Timer.Check( 'pingTimer' ) == False:
        Player.HeadMessage( 128, "Ground Dropper Running...")
        Timer.Create( 'pingTimer', 25000)   
        
    for trashName in TRASH_NAMES:
        item = Items.FindByName(trashName, -1, Player.Backpack.Serial, range = 0)
        if item is not None:
            print("Drop item {}".format(item.Name))
            x, y, z = get_tile_in_front(distance = 1)
            Items.MoveOnGround(item.Serial, item.Amount,x,y,z)
            Misc.Pause(750)

    Misc.Pause(1000)        