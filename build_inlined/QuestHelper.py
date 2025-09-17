# ===============================================
# Imports
# ===============================================
from System import Byte, Int32
from System.Collections.Generic import List
from System.Threading import EventWaitHandle, EventResetMode, Thread
from math import ceil
import atexit
import sys
import threading
import time

# ===============================================
# Auto-generated inlined code. Do not edit
# ===============================================

# ===== Inlined block from core_items.py =====
# ---- RARE_SERPENT_EGG_STATIC_ID (binding from core_items.py)
RARE_SERPENT_EGG_STATIC_ID = 0x41BF

# ===== Inlined block from core_items.py =====
# ---- SERPENT_NEST_STATIC_ID (binding from core_items.py)
SERPENT_NEST_STATIC_ID = 0x2233

# ===== Inlined block from core_items.py =====
# ---- SNAKE_CHARMER_FLUTE_STATIC_ID (binding from core_items.py)
SNAKE_CHARMER_FLUTE_STATIC_ID = 0x2805

# ===== Inlined block from core_items.py =====
# ---- CARRONADE_GRAPHIC_ID (binding from core_items.py)
CARRONADE_GRAPHIC_ID = 0x421D

# ===== Inlined block from core_items.py =====
# ---- CANNON_GRAPHIC_IDS (binding from core_items.py)
CANNON_GRAPHIC_IDS = [CARRONADE_GRAPHIC_ID]

# ===== Inlined block from core_items.py =====
# ---- RAMROD_STATIC_ID (binding from core_items.py)
RAMROD_STATIC_ID = 0x4246

# ===== Inlined block from core_mobiles.py =====
# ---- SILVER_SERPENT_MOBILE_ID (binding from core_mobiles.py)
SILVER_SERPENT_MOBILE_ID = 0x005C

# ===== Inlined block from core_mobiles.py =====
# ---- GIANT_SERPENT_MOBILE_ID (binding from core_mobiles.py)
GIANT_SERPENT_MOBILE_ID = 0x0015

# ===== Inlined block from core_items.py =====
# ---- PAINTS_AND_A_BRUSH_STATIC_ID (binding from core_items.py)
PAINTS_AND_A_BRUSH_STATIC_ID = 0x0FC1

# ===== Inlined block from core_items.py =====
# ---- BOW_GRAPHIC_ID (binding from core_items.py)
BOW_GRAPHIC_ID = 0x13B2

# ===== Inlined block from core_items.py =====
# ---- HUNTING_PERMIT_GRAPHIC_ID (binding from core_items.py)
HUNTING_PERMIT_GRAPHIC_ID = 0x14F0

# ===== Inlined block from core_items.py =====
# ---- DRYDOCK_SHIP_GRAPHIC_ID (binding from core_items.py)
DRYDOCK_SHIP_GRAPHIC_ID = 0x14F4

# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-09-04
# Use at your own risk. 


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
                    
# 3. Just a nice helper for taking out beacons, ships. Just fires a cannon
# over and over.
def fire_nearest_cannon_loop(stop, interval):
    while not stop.WaitOne(interval) and not Player.IsGhost:       
        CANNON_GUMP_ID = 0x40e8c348
        LOAD_TIME_MS = 10000
        FIRE_TIME_MS = 5000

        # We could make the loop stop when the beacon is no longer visible,
        # But I might want to use this for taking out ships as well.
        #PLUNDER_BEACON_GRAPHIC_ID = 0x4724

        filter = Items.Filter()
        filter.Graphics = List[Int32](CANNON_GRAPHIC_IDS) 
        filter.OnGround = True
        filter.RangeMax = 2
        items = Items.ApplyFilter(filter)

        if len(items) > 0:
            # Gets the cannon gump. Side effect opens cannon container.
            Items.UseItem(items[0])
            Gumps.WaitForGump(CANNON_GUMP_ID,3000)
            
            state = Gumps.LastGumpGetLine(1)
            print(state)
            if state == "Not Charged":
                Misc.SendMessage("Loading Cannon", 123)
                Gumps.SendAction(CANNON_GUMP_ID, 1)
                Misc.Pause(LOAD_TIME_MS)
            elif state == "UNLOAD":
                Misc.SendMessage("Firing Cannon", 123)
                Gumps.SendAction(CANNON_GUMP_ID, 6)
                Misc.Pause(FIRE_TIME_MS)
            else:
                Misc.Pause(1000)    
                
# 4. Huntsman stuff in skara brae
def huntsman(stop, interval):
    GAME_ANIMALS = [
        "an alligator",
        "an allosaurus",
        "an anchisaur",
        "a bake kitsune",
        "a boar",
        "a bull",
        "a cougar",
        "a desert ostard",
        "a dimetrosaur",
        "an eagle",
        "a high plains boura",
        "a frenzie ostard",
        "a gaman",
        "a giant toad",
        "a gorilla",
        "a grey wolf",
        "a grizzly bear",
        "a hiryu",
        "a kraken",
        "a lion",
        "a myrmidex drone",
        "a myrmidex larvae",
        "a najasaurus",
        "a platinum drake",
        "a polar bear",
        "a raptor",
        "saber-toothed tiger",
        "a saurosaurus",
        "a scorpion",
        "a sea serpent",
        "a triceratops",
        "a turkey",
        "a tyrannosaurus rex",
        "a walrus",
        "a wild tiger",
        "a tiger"
    ]
    
    corpseScannerCache = []
    permitTurninCache = []
    while not stop.WaitOne(interval) and not Player.IsGhost:  
        permits = Items.FindAllByID(HUNTING_PERMIT_GRAPHIC_ID, 0, Player.Backpack.Serial, 0)
        permits = [permit for permit in permits if permit.Name.lower() == "hunting permit" and permit.Serial not in permitTurninCache ]
        needsPermit = next((False for permit in permits if len(permit.Properties) < 3), True)
        
        if needsPermit:
            npcs = get_yellows_in_range(range=2)
            npc = next((npc for npc in npcs if npc.Name.lower() == "aiko"), None)
            if npc is not None:
                Misc.SendMessage("Getting new Permit...", 38)
                Misc.UseContextMenu(npc.Serial,"Get Hunting Permit",3000)
        
        for permit in permits:
            if permit is not None and len(permit.Properties) < 4:
                if Timer.Check("hunstmansPulseTimer") == False:
                    mobs = get_enemies(range = 15)
                    if len(mobs) > 0:
                        mobs = List[type(mobs[0])]([mob for mob in mobs if mob.Name.lower() in GAME_ANIMALS ])
                        for mob in mobs:
                            Mobiles.Message(mob, 68, "^ Kill Me ^")
                            
                    Timer.Create("hunstmansPulseTimer", 3000)
                
                items = get_corpses(range = 5)
                corpses = [item for item in items if " ".join(item.Name.split()[1:-1]) in GAME_ANIMALS and item.Serial not in corpseScannerCache]

                for corpse in corpses:
                    Misc.SendMessage("Using Permit...", 38)
                    Items.UseItem(permit)
                    Target.WaitForTarget(3000)
                    Target.TargetExecute(corpse)
                    if len(corpseScannerCache) >= 30:
                        corpseScannerCache.pop(0)
                        #print("cacheLooted popping one off {}".format(len(corpseScannerCache)))
                    corpseScannerCache.append(corpse.Serial)
                    break
        
            else:
                npcs = get_yellows_in_range(range=2)
                npc = next((npc for npc in npcs if npc.Name.lower() == "aiko"), None)
                if npc is not None:
                    permitTurninCache.append(permit.Serial)
                    Misc.SendMessage("Turning in Permit...", 38)
                    Items.Move(permit, npc, 1)
           
        Misc.Pause(1000)

# Register each helper here
BUTTONS = [
    [ 1, RARE_SERPENT_EGG_STATIC_ID, "Medusa Egg Helper", "Uses snake charming flute to lure snakes to egg nests.\nPicks up eggs from ground.", medusa_helper ],
    [ 2, PAINTS_AND_A_BRUSH_STATIC_ID, "Collector Quest", "Will talk to NPCs and take photos of creatures when you\nget to that part.", collector_quest ],
    [ 3, DRYDOCK_SHIP_GRAPHIC_ID, "Fire Cannon!", "Fires nearest cannon on a loop. Hopefully while you are on\na ship. Just stand near it. BOOM BOOM BOOM.", fire_nearest_cannon_loop ],
    [ 4, HUNTING_PERMIT_GRAPHIC_ID, "Huntsman Stuff", "Alerts when relevant animals appear on screen.\nUses permit on corpses.\nTurns in permits and gets new permits.", huntsman ],
]

# Should not need to edit anything below this line    
OUR_GUMP_ID = 0xBADF00D2
Gumps.CloseGump(OUR_GUMP_ID)

# Absolutely do not try to make sense of this.
# I wrote it and I have no idea what it does.
def render_gump(buttonid):
    
    WIDTH = 450
    LINE_HEIGHT = 17
    PADDING = 25
    STYLE = 3500
    
    atlasGump = Gumps.CreateGump(True, True, True, False)
    atlasGump.buttonid = -1
    atlasGump.gumpId   = OUR_GUMP_ID
    atlasGump.serial   = Player.Serial
    atlasGump.x        = 600
    atlasGump.y        = 100
    
    #height = PADDING + (2 * PADDING) + LINE_HEIGHT
    height = PADDING + LINE_HEIGHT
    for button in BUTTONS:
        numDescLines = button[3].count('\n') + 1
        height = height + PADDING + LINE_HEIGHT + (LINE_HEIGHT * numDescLines)
    
    y = 10
    Gumps.AddBackground(atlasGump, 0, 0, WIDTH, height, STYLE)
    Gumps.AddLabel(atlasGump, 120, y, 1258, "Questmaster 5000")      
    
    HUE_INACTIVE = 0
    HUE_ACTIVE = 1258
    
    y = y + PADDING
    
    for button in BUTTONS:
        hueTitle = 1258 if buttonid == button[0] else 10
        hueDesc = 77 if buttonid == button[0] else 0
        numDescLines = button[3].count('\n') + 1
        titleText = (button[2] + " - Running") if buttonid == button[0] else button[2]
        
        
        Gumps.AddButton(atlasGump, 25, y , 0x4BA, 0x4B9, button[0], 1, 1)
        Gumps.AddLabel(atlasGump, 58, y, hueTitle, titleText)  
        y = y + LINE_HEIGHT
        Gumps.AddItem( atlasGump, 10, y, button[1])
        Gumps.AddLabel(atlasGump, 58, y, hueDesc, button[3])
        
        
        
        y = y + PADDING + (LINE_HEIGHT * numDescLines)    
            
        
        #Gumps.AddItem( atlasGump, 10, y - 10, button[1])
        #Gumps.AddLabel(atlasGump, 55, y, hueTitle, titleText)  
        #y = y + LINE_HEIGHT
        #Gumps.AddButton(atlasGump, 25, y , 0x4BA, 0x4B9, button[0], 1, 1)
        #Gumps.AddLabel(atlasGump, 55, y, hueDesc, button[3])
        #y = y + PADDING + (LINE_HEIGHT * numDescLines)
    
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
    
