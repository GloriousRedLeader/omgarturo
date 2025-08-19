# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-08-19
# Use at your own risk. 

from Scripts.omgarturo.fm_core.core_attack import run_mage_loop

#   This one is configured for a Mage SpellWeaver Tamer Bard
#   It doesnt cast any AoE or damage spells. Purely focused
#   on healing, well with the exception of Discordance.

#   Can cast Necro, Magery, Spellweaving Spells - and some Bard stuff.
# 
#   Run different configurations:
#   1. Pure Necro 
#   2. Mage Tamer 
#   3. Bard SW Tamer
#   4. Healer Only
#   5. Big SW AoE 
#   6. Big Boom Boom Death Ray Mage
#
#   Read the options below and configure as needed. Highlights are just pick a single target nuke
#   and an AoE. Pick heals you want. Set friends. As an added bonus, this will also work with bag 
#   of sending and automatically bank gold.
run_mage_loop(

    # Give it a fun name in case you have different versions, e.g.
    # Mage AOE Loop or Mage Single Target Loop
    loopName = "Bard Mage (heal only)",

    # Applicable when heal spells are enabled (Greater Heal, etc.) which are configured
    # down below. This governs how you want to heal allies. By default your character is always healed.
    # 0 = Heal only names in friendNames array (below), 1 = heal any blue in range, 2 = my pets only
    friendSelectMethod = 0,
    
    # Names of pets or blue characters you want to heal / cure if they are in range.
    # Note that you still need to enable useCure / useGreaterHeal etc.
    friendNames = ["omg arturo", "omg arthur", "badhorsey", "omg art", "omg artus", "omg artie", "goodhorsey"],
    
    # Only look for mobs and pets/friends inside of this range. IF they are farther, then
    # dont heal them / dont attack them.
    range = 10,
    
    # Use Arcane Empowerment (spell weaving) 0 = disabled, 1 = enabled
    # Will cast every time buff expires automatically AND an enemy is in range.
    useArcaneEmpowerment = 1,
    
    # Main spammable nuke. Cast when only 1 - 2 mobs.
    # 0 = Disabled, no nuke.
    # 1 = Poison Strike (Necro)
    # 2 = Energy Bolt (Magery)
    # 3 = Flame Strike (Magery)
    mainNukeSpell = 0,
    
    # Delay between nuke casts. Timer starts when casting is finished.
    # By default there is only 100ms delay between casts.
    mainNukeDelayMs = 100,
    
    # Main spammable AoE. Note that wildfire has its own configuration since its a DoT type.
    # Cast when > 2 mobs.
    # 0 = Disabled, dont cast any aoe spells.
    # 1 = Wither (Necro)
    # 2 = Thunderstorm (Magery)
    # 3 = Chain Lightning (Magery)
    mainAoeSpell = 0,
    
    # Delay between AoE attacks. Timer starts when casting is finished.
    # By default there is hardly any delay, 100ms.
    mainAoeDelayMs = 100,
    
    # Threshold count of mobs within aoeRange. If found, will cast mainAoeSpell.
    aoeMinMobCount = 3,
    
    # Counts monsters within this range of tiles from player (inclusive).
    aoeMaxRange = 8,
    
    # Whether to use this spell 0 = disabled, 1 = enabled
    useStrangle = 0,
    
    # Change to an appropriate value for strangle spell, number of MS in between usages
    strangleDelayMs = 60000,
    
    # Whether to use this spell 0 = disabled, 1 = enabled
    useCorpseSkin = 0,
    
    # Change to an appropriate value, number of MS in between usages
    corpseSkinDelayMs = 60000,
    
    # Couple of different modes:
    # 0 = Disabled
    # 1 = Use before dots and curses (e.g. strangle and corpse skin)
    # 2 = Use based on the delay variable below
    useEvilOmen = 0,
    
    # Adding this option because it is wild on InsaneUO. It is a pretty cool dot.
    evilOmenDelayMs = 20000,
    
    # Cast blood oath necro spell
    useBloodOath = 0,
    
    # Time between blood oath casts in milliseconds
    bloodOathDelayMs = 30000,
    
    # Whether to use the magery curse spell, 0 = disabled, 1 = enabled
    useCurse = 0,
    
    # How often to cast this spell in millesconds
    curseDelayMs = 60000,
    
    # Whether to use the magery spell poison, will only cast if poison is not on target 0 = disabled, 1 = enabled
    usePoison = 0,
    
    # How often we can cast poison in milliseconds
    poisonDelayMs = 30000,
    
    # Magery poison field spell 0 = disabled, 1 = enabled. Will only cast if there is a nonpoisoned mob.
    usePoisonField = 0,
    
    # How often to cast this spell in milliseconds
    poisonFieldDelayMs = 10000,
    
    # Magery fire field spell 0 = disabled, 1 = enabled.
    useFireField = 0,
    
    # How often to cast this spell in milliseconds
    fireFieldDelayMs = 10000,
    
    # Toggles death ray. Requires magery mastery. There is no timer because this remains
    # active until you move or you are interrupted or the creature dies. It will attempt to
    # reapply immediately. 0 = disabled, 1 = enabled
    useDeathRay = 0,
    
    # Will use shadow word death on eligible targets until they die. This is more of a toggle.
    # 0 = disabled, 1 = enabled
    useWordOfDeath = 0,
    
    # Whether to use this spell 0 = disabled, 1 = enabled
    useWildfire = 0,
    
    # Use necromancy pain spike every 10 seconds. On some servers this might be good.
    usePainSpike = 0,
    
    # This is Insane UO Specific. That means there is no target reticle. Wont work
    # on other servers.
    useAnimateDead = 0,
    
    # Cast it this often
    animateDeadDelayMs = 60000,
    
    # InsaneUO specific. Keeps all 4 pets summoned when safe to cast.
    useSummonFamiliar = 0,
    
    # Make sure we are in wraith form when it is safe to cast.
    # 0 = Do not force any form.
    # 1 = Make sure we are in wraith form.
    # 2 = Make sure we are in vampire form.
    useForm = 0,
    
    # Whether to cure yourself or your pet
    useCure = 1,
    
    # Whether to heal yourself or your pet
    useGreaterHeal = 1,
    
    # Necro heal
    useSpiritSpeak = 0,
    
    # Necro mastery for aoe damage, looks for buff. If no buff, casts it.
    # 0 = Do not use
    # 1 = Cast only when buff is not present in buff bar (kind of unreliable)
    # 2 = Cast every conduitDelayMs milliseconds
    useConduit = 0,
    
    # Recast conduit after this many milliseconds. Only applicablewhen useConduit = 2.
    conduitDelayMs = 15000,
    
    # When standing still, no mobes in range, not bleeding, strangled, or poisoned, will start meditating.
    useMeditation = 1,
    
    # Only heal things that are below this percent HP
    healThreshold = 0.70,
    
    # InsaneUO specific. There is a cloak that grants immunity. Looks like 30 second cooldown.
    # Looks for item on Cloak layer and uses it. Timer for this is created in the main core_attack script.
    useCloakOfGraveMists = 0,
    
    # Spellweaving spell. Think its 2.5 min cooldown.
    # 0 = Do not use
    # 1 = Cast on yourself or anyone in friends list (uses timer to track cooldown so not very reliable on restart)
    useGiftOfRenewal = 0,
    
    # 0 = Do not use
    # 1 = Cast on yourself and pet (uses your buff to track, not pets, so not very reliable)
    useGiftOfLife = 0,
    
    # Use a bard ability.
    # 0 = Default, do nothing
    # 1 = Discord (Yes)
    # 2 = Peacemaking (notimplemented)
    # 3 = Provocation (notimplemented)
    useBardAbility = 1,
    
    # Wait this long in milliseconds between bard ability uses
    bardAbilityDelayMs = 10000,
    
    # EXPERIMENTAL: Does not work great. Would recommend not using this.
    # Whether to honor a nearby enemy to gain the perfection buff.
    # Will try to find an enemy at full health when the buff doesnt exist on player.
    useHonor = 0,
    
    # If greater than 0 will attempt to use bag of sending when this much gold is present. Default is 0, no bag of sending usage.
    minGold = 45000,
    
    # Milliseonds of extra delay when computing cast time to account for internet fuzz. Fine tune this as needed.
    latencyMs = 200
)