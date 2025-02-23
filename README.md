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
        ├── your_other_scripts.py          # Your normal collection of razor scripts
        └── ...
```

* *<root>* -> This is the stuff you'll use. Modify these. Configure them. Bind them to keys. Covers training skills and powerful loops for gathering, attacking, crafting, etc.
* *fm_core* -> This is framework stuff I've written (for the most part). These don't do anything on their own.

**Note**: You do NOT need to add **fm_core** scripts into Razor Enhanced. They just need to be present. You can use the command "git pull" inside the **omgarturo** folder to get the latest changes. 

### Usage

Useful things you'll find:

A highly configurable **Dexer Attack Loop** that supports some chiv, necro and shield bash stuff. More to come later, I just don't really play other builds.

A rather inefficient **Caster Attack Loop**. Good for mage tamer and InsaneUO specific focused necro caster.

A couple of **resource gathering** scripts. Use with caution. Don't break any rules. Includes fishing on a boat (also crab fishing), lumberjacking, and mining.

**Restocker** is InsaneUO specific. It moves items from resource boxes (miner's storage box, reagent box, etc.) to a real container. No more clicking a million times and letting resources pile up at your feet. Useful in conjunction with bod builder. 

**BOD Builder** script to automate crafting and filling small and large bods. Seriously, this does 100% of the work for you. Highly configurable. Current support for
* Alchemy
* Tailoring
* Inscription
* Blacksmithy
* Tinkering

**Move Items** scripts to put things in various containers. Lots of different flavors and uses. They all present with a target reticle so no need for hard coding anything. Different flavors include:
* Move x number of items from one container to another (type number of items in chat, target source container, target destination container)
* Move all items of a type from their current container to another container (target item, target destination container)
* Move all items of a type **and color** from their current container to another container, you can use this turn in bods (target item, target destination container)
* Move all items from container to another container (target source container, target destination container)

**Automated character movement** script that uses the rails framework. Several default routes already established. You can easily add your own, it's just a list of x, y coordinates. Use this in conjunction with dexer / caster loops for maximum farming. For the love of all that is holy, use while you're at your machine supervising. You will get banned.

A script that **scans journal entries and alerts** with obnoxious sounds and overhead text. Useful for holiday bosses so you don't miss the message. Also good for hunting down specific NPCs like when doing the honesty virtue.

**Shadowguard** script from Dorana. Just keeping a copy. This thing is amazing. Dear god.

**Lootmaster** script from Dorana. Just keeping a copy for posterity.

A script that **opens Messages in a bottle and sorts them** into 3 chests, one for each section of the map (west, central, east). This makes fishing MiBs much more efficient since you aren't hunting all over the map, just 1/3 of it with more condensed spots. I usually take about 100 of them with me.

An **IDOC Scanner** script. This thing is awesome. Written by someone else (can't track down author). Just storing for safe keeping. 

**Character Stats** is a standalone tool that will have some details on character stats from item properties. Just bind it to a key and run it when you want to see all your properties like resists, HCI, SDI, etc. Note that it does get a little wonkie sometimes and you'll have to close and re-open your paperdoll. This script will tell you when it needs to be done (has something to do with item caching in the client / razor).

### Credits

I wrote some of this stuff. Others I am just storing for safekeeping. These were acquired via discord or github. All credit goes to original authors.

#### Warning

There are some powerful features here. Use with care. Don't be a jackass.
