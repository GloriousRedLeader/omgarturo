# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-01-11
# Use at your own risk. 

from Scripts.omgarturo.fm_core.core_attack import run_dex_loop

# Intended for Bashers and uses Secondary Ability

# Basic dexer loop that attacks nearby monsters using the abilities listed below.
# Can automatically use bag of sending if you enable it. 
# Works well in conjunction with the auto bandage feature in RE.
run_dex_loop (

    # Give it a fun name in case you have different versions, e.g.
    # DexLoop Single Targert, DexLoop AOE, etc.
    loopName = "Basher (secondary)",

    # This is my special convention. It represents abilities that are toggled and
    # activated by next auto attack. These are what the possible values are:
    # 0 - Disabled, dont do anything
    # 1 - Use primary ability whatever it may be
    # 2 - Use secondary ability whatever it may be
    # 3 - Use lightning strike (bushido)
    # 4 - Use focus attack (ninjitsu)
    # 5 - Momentum strike (bushido)
    specialAbilityType = 2,
    
    # This causes insane damage when combined with weapon specials.
    # Buff lasts for only a few seconds but at least there is a buff.
    useShieldBash = 1,
    
    # Flag that tells us to use the Chiv consecrate weapon ability. This is the default
    # value (0 = disabled, 1 = enabled)
    useConsecrateWeapon = 1,
    
    # Necro spell. Uses buff for recast tracking.
    useCurseWeapon = 0,
    
    # Flag with a value of 1 means to periodically cast divine fury, otherwise it is
    # disabled. This is the default value.
    useDivineFury = 0,
    
    # Checks for the buff, if it doesnt exist, casts it.
    useEnemyOfOne = 0,
    
    # Removes less troublesome things like Curse, Feeblemind, Mind Rot, etc. every 10 seconds.
    # Uses remove curse when blood oath is detected IMMEDIATELY.
    useRemoveCurse = 1,
    
    # Paladin spell for curing poisons, only works on self.
    useCleanseByFire = 0,
    
    # EXPERIMENTAL: Does not work great. Would recommend not using this.
    # Whether to honor a nearby enemy to gain the perfection buff.
    # Will try to find an enemy at full health when the buff doesnt exist on player.
    useHonor = 0,
    
    # how many tiles to look for enemies and attack them
    attackRange = 6,
    
    # Bandage self. Requires healing skill and bandages in top level of pack.
    # 0 = Disabled, 1 = Enabled
    useBandagesOnSelf = 1,
    
    # Only heal things that are below this percent HP
    healThreshold = 0.95,
    
    # If greater than 0 will attempt to use bag of sending when this much gold is present. Default is 0, no bag of sending usage.
    minGold = 35000,
    
    # Milliseonds of extra delay when computing cast time to account for internet fuzz. Fine tune this as needed.
    latencyMs = 200   
)