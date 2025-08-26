### Ultima Online Razor Enhanced Script Library

These are scripts I've either written, liberally modified, or just stored for safekeeping (these are the good ones written by others). They have been tested on a few free shards:

* UOAlive
* InsaneUO

They may or may not work on others. Requires razor enhanced 0.8.2.242

### Setup

Easy way is to clone this repo into your scripts directory.

```bash
cd <razor_install_dir>/Scripts
git clone https://github.com/GloriousRedLeader/omgarturo.git
```

That will create the **omgarturo** folder in your /Scripts folder and download all files from this repo into it. If you don't have git or don't care for it, you'll still need to create the directory structure *exactly* as it is below. All files in **omgarturo/fm_core** are required. The rest of the files you can just pick and choose what you want.

Also, if this file doesn't exist, create it: /Scripts/\_\_init\_\_.py. This is in the root /Scripts folder. It is an empty file. It just needs to be present. You might already have it.

```bash
└── RazorInstallDirectory
    └── Scripts
        └── omgarturo                      # This repo
        |   ├── fm_core                    # Core framework stuff, don't touch. You need all of these.
        |   |   ├── core_items.py
        |   |   ├── core_mobiles.py
        |   |   └── ...
        |   ├── CasterLoop.py              # Use, modify, bind to hotkeys
        |   ├── DexLoop.py
        |   ├── MiningLoop.py
        |   ├── BODBuilder.py
        |   ├── TrainMagery.py
        |   ├── TrainHiding.py
        |   └── ...
        ├── __init__.py                    # 100% needed. If this file doesn't exist, create it. It is empty. 2 underscores on either side.
        ├── your_other_scripts.py          # Your normal collection of razor scripts
        └── ...
```

* *omgarturo* -> The scripts directly in this root folder are what you'll use. Modify these. Configure them. Bind them to keys. Covers training skills and powerful loops for gathering, attacking, crafting, etc.
* *fm_core* -> This is framework stuff I've written. All the main business logic resides here. No need to touch unless you're insane.

**Note**: You do NOT need to add the scripts in **fm_core** into Razor Enhanced. They just need to be present in the directory structure outlined above. You can use the command "git pull" inside the **omgarturo** folder to get the latest changes. 

### Usage

Useful things you'll find:

Several combat scripts that are configurable for many uses. They are all based off two main archetypes: caster and dexer. It is recommended to customize these to meet your needs. You'd want to set some healing targets in the caster script if you want to heal your pet for example. 
Here are some pre-canned versions that are ready for your customization!
|Script|Single Target|AoE|Heals|Cures|Bard|Pets|Other|
|------|-------------|---|-----|-----|----|----|-----|
|[Basic Chiv Dexer](https://github.com/GloriousRedLeader/omgarturo/blob/master/BasicChivDexerLoop.py)|Primary Weapon Ability|None|None|None|None|None|Consecrate Weapon|
|[Shield Basher Primary Ability](https://github.com/GloriousRedLeader/omgarturo/blob/master/BasherPrimaryLoop.py)|Shield Bash + Armor Ignore|None|Bandages|Remove Curse; Bandages|None|None|Consecreate Weapon|
|[Shield Basher Secondary Ability](https://github.com/GloriousRedLeader/omgarturo/blob/master/BasherSecondaryLoop.py)|Shield Bash + Armor Ignore|None|Bandages|Remove Curse; Bandages|None|None|Consecreate Weapon|
|[Pure Necro - Conduit](https://github.com/GloriousRedLeader/omgarturo/blob/master/PureNecroConduitLoop.py)|Poison Strike + Pain Spike + Evil Omen + Strangle + Corpse Skin|Conduit|Spirit Speak|None|None|Summon Familiar + Animated Dead|Cloak of Grave Mists; Vampiric Embrace|
|[Pure Necro - Conduit (No Pet)](https://github.com/GloriousRedLeader/omgarturo/blob/master/PureNecroConduitNoPetLoop.py)|Poison Strike + Pain Spike + Evil Omen + Strangle + Corpse Skin|Conduit|Spirit Speak|None|None|None|Cloak of Grave Mists; Vampiric Embrace|
|[Pure Necro - Wither](https://github.com/GloriousRedLeader/omgarturo/blob/master/PureNecroWitherLoop.py)|Poison Strike|Wither|Spirit Speak|None|None|Summon Familiar + Animate Dead|Cloak of Grave Mists; Vampiric Embrace|
|[Pure Necro - Wither (No Pet)](https://github.com/GloriousRedLeader/omgarturo/blob/master/PureNecroWitherLoop.py)|Poison Strike|Wither|Spirit Speak|None|None|None|Cloak of Grave Mists; Vampiric Embrace|
|[Mage Bard Thunderstorm](https://github.com/GloriousRedLeader/omgarturo/blob/master/MageBardThunderstormLoop.py) |Word of Death|Thunderstorm + Wildfire|Greater Heal + Gift of Renewal|Arch Cure|Inspire + Invigorate + Discord|None|Gift of Life; Protection|
|[Mage Bard Wildfire](https://github.com/GloriousRedLeader/omgarturo/blob/master/MageBardWildfireLoop.py) |Word of Death|Wildfire|Greater Heal + Gift of Renewal|Arch Cure|Inspire + Invigorate + Discord|None|Gift of Life; Protection|
|[Mage Bard Heals](https://github.com/GloriousRedLeader/omgarturo/blob/master/MageHealLoop.py) |None|None|Greater Heal + Gift of Renewal|Arch Cure|Inspire + Invigorate + Discord|None|Gift of Life; Protection|

A couple of resource gathering scripts. Use with caution. Don't break any rules. Includes [fishing on a boat](https://github.com/GloriousRedLeader/omgarturo/blob/master/FishLoopBoat.py), [crab fishing](https://github.com/GloriousRedLeader/omgarturo/blob/master/FishLoopCrab.py), [lumberjacking](https://github.com/GloriousRedLeader/omgarturo/blob/master/LumberjackingLoop.py), and [mining](https://github.com/GloriousRedLeader/omgarturo/blob/master/MiningLoop.py).

[Restocker](https://github.com/GloriousRedLeader/omgarturo/blob/master/Restocker.py) is InsaneUO specific. It moves items from resource boxes (miner's storage box, reagent box, etc.) to a real container. No more clicking a million times and letting resources pile up at your feet. Useful in conjunction with bod builder. 

There are some quality of life scripts for simple things like [mounting](https://github.com/GloriousRedLeader/omgarturo/blob/master/PetMount.py) and [dismounting](https://github.com/GloriousRedLeader/omgarturo/blob/master/PetDismount.py) pets, [leashing](https://github.com/GloriousRedLeader/omgarturo/blob/master/LeashPets.py) pets, and [recalling / sacred journey](https://github.com/GloriousRedLeader/omgarturo/blob/master/RecallOrSacredJourneyRune1.py) from a rulebook.

[BOD Builder](https://github.com/GloriousRedLeader/omgarturo/blob/master/BODBuilder.py) script to automate crafting and filling small and large bods. Seriously, this does 100% of the work for you. Highly configurable. Current support for
* Alchemy
* Tailoring
* Inscription
* Blacksmithy
* Tinkering

A [CraftItems](https://github.com/GloriousRedLeader/omgarturo/blob/master/CraftItems.py) script. This might seem silly but I find it invaluable for min/maxing suits. This will craft a particular item (specified in script) repeatedly and discard any items that don't pass your filter requirements (also configured in script). For example, if you are an advanced crafter looking for a specific set of resists on leather leggings, e.g. 3 physical, 10 fire, 11 cold - then this script is for you. It will discard all the rubbish. Reforging is a painful process, and this helps make it easier by providing a large pool of potential items. But really, even if  you aren't reforging and just imbuing, it is still helpful. Makes life easier.

**Move Items** scripts to put things in various containers. Lots of different flavors and uses. They all present with a target reticle so no need for hard coding anything. Different flavors include:
* [Move number of items](https://github.com/GloriousRedLeader/omgarturo/blob/master/MoveNumberOfItems.py) from one container to another (type number of items in chat, target source container, target destination container)
* [Move all items by type](https://github.com/GloriousRedLeader/omgarturo/blob/master/MoveItemsByID.py) from their current container to another container (target item, target destination container)
* [Move all items by type and color](https://github.com/GloriousRedLeader/omgarturo/blob/master/MoveItemsByIDAndColor.py) from their current container to another container, you can use this turn in bods (target item, target destination container)
* [Move all items](https://github.com/GloriousRedLeader/omgarturo/blob/master/MoveAllItemsFromContainer.py) from one container to another container (target source container, target destination container)

[Automated character movement](https://github.com/GloriousRedLeader/omgarturo/blob/master/RailLoop.py) script that uses the rails framework. Several default routes already established. You can easily add your own, it's just a list of x, y coordinates. Use this in conjunction with dexer / caster loops for maximum farming. For the love of all that is holy, use while you're at your machine supervising. You will get banned.

A script that [scans journal entries and alerts](https://github.com/GloriousRedLeader/omgarturo/blob/master/JournalAlert.py) with obnoxious sounds and overhead text. Useful for holiday bosses so you don't miss the message. Also good for hunting down specific NPCs like when doing the honesty virtue.

[Shadowguard](https://github.com/GloriousRedLeader/omgarturo/blob/master/Shadowguard2.cs) script from Dorana. Just keeping a copy. This thing is amazing. Dear god.

[Lootmaster](https://github.com/GloriousRedLeader/omgarturo/blob/master/Lootmaster-1-8-0.cs) script from Dorana. Just keeping a copy for posterity.

A script that [opens Messages in a bottle and sorts them](https://github.com/GloriousRedLeader/omgarturo/blob/master/MIBSorter.py) into 3 chests, one for each section of the map (west, central, east). This makes fishing MiBs much more efficient since you aren't hunting all over the map, just 1/3 of it with more condensed spots. I usually take about 100 of them with me. The second part to this is a [script by foobarvar](https://github.com/GloriousRedLeader/omgarturo/blob/master/SOSCharter.cs) that will add the sos scrolls (also opens mibs) in your pack as coordinates on the map. This is truly amazing. You will of course need to manually remove the coordinates after you fish the location, but thats easy.

An [IDOC Scanner](https://github.com/GloriousRedLeader/omgarturo/blob/master/IDOCAlert.py) script. This thing is awesome. Written by someone else (can't track down author). Just storing for safe keeping. 

[Character Stats](https://github.com/GloriousRedLeader/omgarturo/blob/master/CharacterStats.py) is fairly worthless now. Just use [mystats in game. This WILL show you overcapped resists though which is nice. Note that it does get a little wonkie sometimes and you'll have to close and re-open your paperdoll. This script will tell you when it needs to be done (has something to do with item caching in the client / razor).

### Credits

I wrote some of this stuff. Others I am just storing for safekeeping. These were acquired via discord or github. All credit goes to original authors.

#### Warning

There are some powerful features here. Use with care. Don't be a jackass.
