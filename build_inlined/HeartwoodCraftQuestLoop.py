# ===============================================
# Imports
# ===============================================
import re
import sys

# ===============================================
# Auto-generated inlined code. Do not edit
# ===============================================

# ===== Inlined block from core_items.py =====
# ---- HEATER_SHIELD_GRAPHIC_ID (binding from core_items.py)
HEATER_SHIELD_GRAPHIC_ID = 0x1B76

# ===== Inlined block from core_items.py =====
# ---- BASCINET_GRAPHIC_ID (binding from core_items.py)
BASCINET_GRAPHIC_ID = 0x140C

# ===== Inlined block from core_items.py =====
# ---- BROADSWORD_GRAPHIC_ID (binding from core_items.py)
BROADSWORD_GRAPHIC_ID = 0x0F5E

# ===== Inlined block from core_items.py =====
# ---- KILT_GRAPHIC_ID (binding from core_items.py)
KILT_GRAPHIC_ID = 0x1537

# ===== Inlined block from core_items.py =====
# ---- FANCY_SHIRT_GRAPHIC_ID (binding from core_items.py)
FANCY_SHIRT_GRAPHIC_ID = 0x1EFD

# ===== Inlined block from core_items.py =====
# ---- FLOWER_GARLAND_GRAPHIC_ID (binding from core_items.py)
FLOWER_GARLAND_GRAPHIC_ID =  0x2306

# ===== Inlined block from core_items.py =====
# ---- STUDDED_BUSTIER_GRAPHIC_ID (binding from core_items.py)
STUDDED_BUSTIER_GRAPHIC_ID = 0x1C0C

# ===== Inlined block from core_items.py =====
# ---- SPYGLASS_GRAPHIC_ID (binding from core_items.py)
SPYGLASS_GRAPHIC_ID = 0x14F5

# ===== Inlined block from core_items.py =====
# ---- FOOT_STOOL_GRAPHIC_ID (binding from core_items.py)
FOOT_STOOL_GRAPHIC_ID = 0x0B5E

# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-08-26
# Use at your own risk. 


# Does the heartwood quests. 
# You need a pack animal that contains all of your tools and resources.
# You can configure the quests you want to do / skip below.
# Just stand near an npc and hit play. This will craft things in your backpack.
# Make sure you dont have any valuable items that may have the same graphic id
# as the items you are crafting, e.g. spellbooks. Would hate to see one of those
# get turned in as a quest item.

pets = get_pets()
if len(pets) == 0:
    print("Terminating: You need a pack animal with all your tools and resources")
    sys.exit()

# Where crafting happens. Has to be different than the final "Keep" container
# otherwise my shit script gets confused.
CRAFT_CONTAINER_SERIAL = 0x406766F0

# Can set to any sub container. I just use backpack.
KEEP_CONTAINER_SERIAL = Player.Backpack.Serial

# You shouldnt change this. But if you really wanted to,
# you could have another pouch for  your stuff. 
RESOURCE_CONTAINER_SERIAL = pets[0].Backpack.Serial
TOOL_CONTAINER_SERIAL = pets[0].Backpack.Serial

# Configure quests you want to do. All quests in this list will be accepted.
QUESTS = [
    # Metal Weaver
    [ "Cuts Both Ways", "broadsword", BROADSWORD_GRAPHIC_ID ],
    [ "The Bulwark", "heater shield", HEATER_SHIELD_GRAPHIC_ID ],
    [ "Nothing Fancy", "bascinet", BASCINET_GRAPHIC_ID ],
    
    # Cloth Weaver
    [ "The King of Clothing", "kilt", KILT_GRAPHIC_ID ],
    [ "The Puffy Shirt", "fancy shirt", FANCY_SHIRT_GRAPHIC_ID ],
    [ "Hâute Couture", "flower garland", FLOWER_GARLAND_GRAPHIC_ID ],
    
    # Bark Weaver
    [ "Stop Harping on Me", "lap harp", LAP_HARP_GRAPHIC_ID ],
    
    # Trinket weaver
    [ "From the Gaultier Collection", "studded bustier", STUDDED_BUSTIER_GRAPHIC_ID ],
    [ "The Far Eye", "spyglass", SPYGLASS_GRAPHIC_ID ],
    [ "Arch Support", "foot stool", FOOT_STOOL_GRAPHIC_ID ]
]

# Shouldnt have to touch this. This is crap like "Bob the builder" so
# the script knows which NPCs have heartwood quests.
ALLOWED_SUFFIXES = ["metal weaver", "cloth weaver", "bark weaver", "trinket weaver"]

QUEST_GUMP_ID = 0x4c4c6db0

QUEST_ITEM_HUE = 0x04EA

# Checks if suffix is in the npcs props
def is_quest_giver(npc):
    for prop in npc.Properties:
        if any(s in prop.ToString() for s in ALLOWED_SUFFIXES):
            return True
    return False
    
# Looks up the quest by our approved list of quest names and returns
# a throuple: questName, questItemName, questItemGraphic
def get_quest_details(gumpText):
    for quest in QUESTS:
        if quest[0] in gumpText:
            return quest[0], quest[1], quest[2]
    return None, None, None
    
# Extra parsing needed for the quantity of items to craft
def get_quest_amount(gumpText):
    pattern = rf"(\d+)\s+{re.escape(questItemName)}s"
    match = re.search(pattern, gumpText)
    if match:
        return int(match.groups()[0])

while True:
    npcs = get_yellows_in_range(range = 8)
    npc = Mobiles.Select(npcs, "Nearest")

    if npc is not None and is_quest_giver(npc):
        Mobiles.UseMobile(npc)
        Gumps.WaitForGump(QUEST_GUMP_ID,3000)
        
        if Gumps.LastGumpTextExist("Quest Offer"):
            # Quest is available. Lets check it out. If its good, well begin crafting
            # and go all the way until were done. Otherwise refuse it and try again.

            gumpText = "".join(Gumps.GetGumpText(QUEST_GUMP_ID))
            questName, questItemName, questItemGraphic = get_quest_details(gumpText)
            
            print("QuestItemName: ", questItemName)
            if questItemName is not None:
                Gumps.SendAction(QUEST_GUMP_ID, 7)
                Gumps.WaitForGump(QUEST_GUMP_ID, 3000)
                Misc.Pause(3000)
                
                
                gumpText2 = "".join([str for str in Gumps.GetGumpData(QUEST_GUMP_ID).stringList if str is not None])
                amountNeeded = get_quest_amount(gumpText2)

                if amountNeeded is not None:
                    #print(match.groups())
                    print("Quest: ", questName)
                    print("Item: ", questItemName)
                    #amountToMake = int(match.groups()[0])
                    print("Amount: ", amountNeeded)
                    Gumps.SendAction(QUEST_GUMP_ID, 4)
                    
                    Misc.Pause(3000)
                    
                    craftedItems = Items.FindAllByID(questItemGraphic, 0, KEEP_CONTAINER_SERIAL, 0)
                    amountToMake = amountNeeded - len(craftedItems) + 1
                    print("Amount we already have in backpack: ", len(craftedItems))
                    print("Net amount needed: ", amountToMake)
                    if amountToMake > 0:
                        run_craft_loop(
                            recipeName = questItemName,
                            craftContainer = CRAFT_CONTAINER_SERIAL,
                            toolContainer = TOOL_CONTAINER_SERIAL, # Bag inside beetle
                            resourceContainer = RESOURCE_CONTAINER_SERIAL, 
                            keepContainers = [KEEP_CONTAINER_SERIAL],
                            trashContainer = None,
                            maxItemsToCraft = amountToMake, 
                            specialMaterialHue = None,
                            itemMoveDelayMs = 750,
                            gumpDelayMs = 750,
                            minPhysicalResist = None,
                            maxPhysicalResist = None,
                            minFireResist = None,
                            maxFireResist = None,
                            minColdResist = None,
                            maxColdResist = None,
                            minPoisonResist = None,
                            maxPoisonResist = None,
                            minEnergyResist = None,
                            maxEnergyResist = None
                        )
                    

                    print("Toggling quest items")
                    Misc.WaitForContext(0x000E0EDD, 10000)
                    Misc.ContextReply(0x000E0EDD, 7)
                    craftedItems = Items.FindAllByID(questItemGraphic, 0, KEEP_CONTAINER_SERIAL, 0)
                    for craftedItem in craftedItems:
                        Target.WaitForTarget(10000, False)
                        Target.TargetExecute(craftedItem.Serial)
                        Misc.Pause(250)
                    Target.Cancel()
                    
                    craftedItems = Items.FindAllByID(questItemGraphic, QUEST_ITEM_HUE, KEEP_CONTAINER_SERIAL, 0)
                    if len(craftedItems) < amountNeeded:
                        print("We only have ", len(craftedItems), " but we need ", amountNeeded)
                        sys.exit()
                    
                    print("Turning in quest")                
                    Misc.Pause(3000)
                    Mobiles.UseMobile(npc)
                    Gumps.WaitForGump(QUEST_GUMP_ID, 3000)
                    
                    Gumps.SendAction(QUEST_GUMP_ID, 8)
                    Gumps.WaitForGump(QUEST_GUMP_ID, 3000)
                    Gumps.SendAction(QUEST_GUMP_ID, 5)
                    Misc.Pause(1500)
                        
            else:
                print("Not taking this quest.")
                Gumps.SendAction(QUEST_GUMP_ID, 2)
                Gumps.WaitForGump(QUEST_GUMP_ID, 3000)
                Gumps.SendAction(QUEST_GUMP_ID, 0)
                Misc.Pause(3000)
                
                
        elif Gumps.LastGumpTextExist("Enjoy my thanks for your service"):
            # I think this is a rare case where someone may already be on a quest
            # AND have their items toggled as quest items.
          
            Gumps.SendAction(QUEST_GUMP_ID, 8)
            Gumps.WaitForGump(QUEST_GUMP_ID, 3000)
            Gumps.SendAction(QUEST_GUMP_ID, 5)
            Misc.Pause(3000)
            
        elif Gumps.LastGumpTextExist("I will be in your debt"):
            # Person is on a quest and in the middle of it. Need to abandon
            # and restart script. Kind of crappy, but I dont know how to get
            # current amount of items crafted from the quest if they are already
            # on it. I could parse chat logs and such, but too fat.
            print("You are already on a quest for this npc and need to abandon it and restart this script.")
            print("Quest: ", Gumps.GetGumpText(QUEST_GUMP_ID)[1])
            
            gumpText2 = "".join([str for str in Gumps.GetGumpText(QUEST_GUMP_ID) if str is not None])

            pattern = r"I will be in your debt if you bring me (.+)s"
            match = re.search(pattern, gumpText2)
            if match:
                print("Objective: Craft ", match.groups()[0])
                
            sys.exit()
            
        elif Gumps.LastGumpTextExist("Quest Conversation"):
            print("Something bad happened")
            sys.exit()
            
            
        Misc.Pause(1500)