# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/uo-razor-enhanced
#   2025-01-11
# Use at your own risk. 

from Scripts.omgarturo.fm_core.core_attack import run_dex_loop

run_dex_loop(

    # Give it a fun name in case you have different versions, e.g.
    # DexLoop Single Targert, DexLoop AOE, etc.
    loopName = "Dex Loop",

    # This is my special convention. It represents abilities that are toggled and
    # activated by next auto attack. These are what the possible values are:
    # 0 - Disabled, dont do anything
    # 1 - Use primary ability whatever it may be
    # 2 - Use secondary ability whatever it may be
    # 3 - Use lightning strike (bushido)
    # 4 - Use focus attack (ninjitsu)
    # 5 - Momentum strike (bushido)
    specialAbilityType = 0,
    
    # This causes insane damage when combined with weapon specials.
    # Buff lasts for only a few seconds but at least there is a buff.
    useShieldBash = 0,

    # Flag that tells us to use the Chiv consecrate weapon ability. This is the default
    # value (0 = disabled, 1 = enabled)
    useConsecrateWeapon = 0,
    
    # Necro spell. Uses buff for recast tracking.
    useCurseWeapon = 0,

    # Flag with a value of 1 means to periodically cast divine fury, otherwise it is
    # disabled. This is the default value.
    useDivineFury = 0,
    
    # Checks for the buff, if it doesnt exist, casts it.
    useEnemyOfOne = 0,
    
    # Chiv spell
    useRemoveCurse = 0,
    
    # Paladin spell for curing poisons, only works on self.
    useCleanseByFire = 0,
   
    # how many tiles to look for enemies and attack them
    attackRange = 6,
    
    # If greater than 0 will attempt to use bag of sending when this much gold is present. Default is 0, no bag of sending usage.
    minGold = 0,
    
    # Milliseonds of extra delay when computing cast time to account for internet fuzz. Fine tune this as needed.
    latencyMs = 200,    
)