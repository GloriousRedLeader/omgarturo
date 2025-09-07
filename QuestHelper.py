# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-09-04
# Use at your own risk. 

from System.Collections.Generic import List
from math import ceil
import sys
import threading, atexit
from System import Byte, Int32
import time
from System.Threading import EventWaitHandle, EventResetMode, Thread
from Scripts.omgarturo.fm_core.core_items import RARE_SERPENT_EGG_STATIC_ID
from Scripts.omgarturo.fm_core.core_items import SERPENT_NEST_STATIC_ID
from Scripts.omgarturo.fm_core.core_items import SNAKE_CHARMER_FLUTE_STATIC_ID
from Scripts.omgarturo.fm_core.core_mobiles import SILVER_SERPENT_MOBILE_ID
from Scripts.omgarturo.fm_core.core_mobiles import GIANT_SERPENT_MOBILE_ID
from Scripts.omgarturo.fm_core.core_items import PAINTS_AND_A_BRUSH_STATIC_ID
from Scripts.omgarturo.fm_core.core_mobiles import get_yellows_in_range
from Scripts.omgarturo.fm_core.core_mobiles import get_enemies

# Just a place to dump misc. scripts that aid in doing
# quests or particular tasks. Works as a gump where
# you toggle the functionality off / on.
# Each helper option is a function that runs as a background
# thread until triggered off. To make it fit in this framework
# follow the threading pattern below (check out existing implementations)

# 1. Medusa Egg Helper - Will use snake charming flute to lure
# snakes to egg nests. WIll pick up eggs.
def medusa_helper(stop, interval):
    while not stop.WaitOne(interval) and not Player.IsGhost:        
        #print("Meduca egg helper")
        #flute = Items.FindByID(SNAKE_CHARMER_FLUTE_STATIC_ID, -1, Player.Backpack.Serial, 1)
        flute = Items.FindByName("snake charmer flute", -1, Player.Backpack.Serial, 0)
        if flute is None:
            print("Unable to find snake charmer flute. Quitting.")
            break
        
        filter = Items.Filter()
        filter.Movable = 0
        filter.OnGround = True
        filter.RangeMax = 10
        filter.Graphics = List[Int32]([SERPENT_NEST_STATIC_ID]) 
        nests = Items.ApplyFilter(filter)
        nest = Items.Select(nests, "Nearest")
        
        if nest is not None:
            if Timer.Check("nestPingTimer") == False:
                Items.Message(nest, 68, "^ nest ^")
                Timer.Create("nestPingTimer", 3500)
            fil = Mobiles.Filter()
            fil.Enabled = True
            fil.RangeMax = 10
            fil.Notorieties = List[Byte](bytes([3, 4, 5, 6]))
            fil.IsGhost = False
            fil.Friend = False
            fil.CheckLineOfSight = True
            fil.Bodies = List[Int32]([SILVER_SERPENT_MOBILE_ID, GIANT_SERPENT_MOBILE_ID]) 
            mobiles = Mobiles.ApplyFilter(fil)
            closestMobile = None
            closestMobileDistance = None
            for mobile in mobiles:
                
                distance = Misc.Distance(nest.Position.X, nest.Position.Y, mobile.Position.X, mobile.Position.Y)
                if closestMobile == None or (closestMobileDistance > distance):
                    closestMobile = mobile
                    closestMobileDistance = distance
            
            if closestMobile is not None and Timer.Check("snakeCharmTimer") == False:
                Items.UseItem(flute)
                Target.WaitForTarget(1000)
                Target.TargetExecute(mobile)
                Target.WaitForTarget(1000)
                Target.TargetExecute(nest)
                Timer.Create("snakeCharmTimer", 6000)
                
        filter = Items.Filter()
        filter.Movable = 1
        filter.OnGround = True
        filter.RangeMax = 10
        filter.Graphics = List[Int32]([RARE_SERPENT_EGG_STATIC_ID]) 
        eggs = Items.ApplyFilter(filter)

        for egg in eggs:
            if Timer.Check("eggPingTimer") == False:
                Items.Message(egg, 38, "^ egg ^")
                Timer.Create("eggPingTimer", 3500)

            if Player.DistanceTo(egg) < 3:
                Items.Move(egg, Player.Backpack.Serial, 1)
                Misc.Pause(800)

# 2. Collector quest - Will talk to NPCs and take photos of
# creatures.
def collector_quest(stop, interval):
    lastNpcTalkedToSerial = None
    paintedMobCache = []
    paintedMobCacheTime = time.time()
    while not stop.WaitOne(interval) and not Player.IsGhost:
        #print("Running Collector Quest")

        # 1) Finds nearest yellow npc and opens the talk contextual menu.
        # Use this for doing quests if you cant be bothered to click on an NPC.
        TALK_CONTEXT = 0x00001500
        npcs = get_yellows_in_range(range = 1)
        if len(npcs) > 0 and lastNpcTalkedToSerial != npcs[0].Serial:
            lastNpcTalkedToSerial = npcs[0].Serial
            print("Talking to ", npcs[0].Name)
            Misc.UseContextMenu(npcs[0].Serial,"Talk",3000)
            
        # 2) Takes picutres of things
        MONSTER_NAMES = [
            "a betrayer", 
            "a bogling",
            "a bog thing",
            "a juggernaut",
            "a juka mage",
            "a juka warrior",
            "a lich",
            "a meer mage",
            "a meer warrior",
            "a mongbat",
            "a mummy",
            "a plague beast",
            "a sand vortex",
            "a stone gargoyle",
            "a swamp dragon",
            "a wisp"
        ]
        
        paints = Items.FindByName("paints and brush", -1,  Player.Backpack.Serial, 0)
        if paints is not None:
            if time.time() - paintedMobCacheTime > 60:
                paintedMobCache = []
                paintedMobCacheTime = time.time()
                print("Clear painted mob cache")

            # blue = 1, green = 2, gray = 3, gray crim = 4, orange = 5, red = 6, yellow = 7
            fil = Mobiles.Filter()
            fil.RangeMax = 8
            fil.Notorieties = List[Byte](bytes([1,3,4,5,6]))
            fil.CheckLineOfSight = True
            mobs = Mobiles.ApplyFilter(fil)

            if len(mobs) > 0:
                mobs = List[type(mobs[0])]([mob for mob in mobs if mob.Name in MONSTER_NAMES ])
            for mob in mobs:
                if mob.Name not in paintedMobCache:
                    paintedMobCacheTime = time.time()
                    paintedMobCache.append(mob.Name)
                    print("Refreshing painted mob cache for 60 seconds with new mob ", mob.Name)
                    Items.UseItem(paints)
                    Target.WaitForTarget(2500)
                    Target.TargetExecute(mob)

# Register each helper here
BUTTONS = [
    [ 1, 0x41BF, "Medusa Egg Helper", "Uses snake charming flute to lure snakes to egg nests.\nPicks up eggs from ground.", medusa_helper],
    [ 2, 0x0FC1, "Collector Quest", "Will talk to NPCs and take photos of creatures.", collector_quest   ],
]

# Should not need to edit anything below this line    
OUR_GUMP_ID = 0xBADF00D2
Gumps.CloseGump(OUR_GUMP_ID)

# Absolutely do not try to make sense of this.
# I wrote it and I have no idea what it does.
def render_gump(buttonid):
    
    WIDTH = 450
    LINE_HEIGHT = 25
    PADDING = 15
    STYLE = 3500
    
    atlasGump = Gumps.CreateGump(True, True, True, False)
    atlasGump.buttonid = -1
    atlasGump.gumpId   = OUR_GUMP_ID
    atlasGump.serial   = Player.Serial
    atlasGump.x        = 600
    atlasGump.y        = 100
    
    height = PADDING + (2 * PADDING) + LINE_HEIGHT
    for button in BUTTONS:
        numDescLines = button[3].count('\n') + 1
        height = height + PADDING + LINE_HEIGHT + (LINE_HEIGHT * numDescLines)
    
    y = PADDING
    Gumps.AddBackground(atlasGump, 0, 0, WIDTH, height, STYLE)
    Gumps.AddLabel(atlasGump, 120, y, 1258, "Questmaster 5000")      
    
    HUE_INACTIVE = 0
    HUE_ACTIVE = 1258
    
    y = y + PADDING + LINE_HEIGHT
    for button in BUTTONS:
        hueTitle = 1258 if buttonid == button[0] else 10
        hueDesc = 77 if buttonid == button[0] else 0
        numDescLines = button[3].count('\n') + 1
        titleText = (button[2] + " - Running") if buttonid == button[0] else button[2]
        
        Gumps.AddItem( atlasGump, 10, y - 3, button[1])
        Gumps.AddLabel(atlasGump, 55, y, hueTitle, titleText)  
        y = y + LINE_HEIGHT
        Gumps.AddButton(atlasGump, 25, y , 0x4BA, 0x4B9, button[0], 1, 1)
        Gumps.AddLabel(atlasGump, 55, y, hueDesc, button[3])
        y = y + PADDING + (LINE_HEIGHT * numDescLines)
    
    Gumps.CloseGump(OUR_GUMP_ID)
    Gumps.SendGump(atlasGump, 0, 0)

STOP_EVENT_NAME = r"Local\RazorEnhanced.OMGArthur.Stop"

def _get_stop_handle():
    return EventWaitHandle(False, EventResetMode.ManualReset, STOP_EVENT_NAME)

def start_worker(func):
    print("Starting Worker")
    h = _get_stop_handle()
    h.Set()
    Thread.Sleep(300)
    h.Reset()
    
    _worker = threading.Thread(target=func, args=(h, 1000), name="OMGWorker")
    _worker.daemon = True
    
    _worker.start()

def stop_worker():
    _get_stop_handle().Set()

render_gump(-1)

activeFunc = None

stop_worker()

while True:
    gd = Gumps.GetGumpData(OUR_GUMP_ID)
    
    if gd is not None and gd.buttonid > 0:
        print("User pressed button, lets see what were dealing with here: ", gd.buttonid)
        stop_worker()
        tempActiveFunc = next((button[4] for button in BUTTONS if button[0] == gd.buttonid), None)
        if tempActiveFunc == activeFunc:
            activeFunc = None
            gd.buttonid = -1
        else:
            activeFunc = tempActiveFunc
            start_worker(activeFunc)

        render_gump(gd.buttonid)

    elif gd is not None and gd.buttonid == 0:
        print("Exiting")
        stop_worker()
        Gumps.CloseGump(OUR_GUMP_ID)
        break

    
    Misc.Pause(250)    
    

