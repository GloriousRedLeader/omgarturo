# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-01-11
# Use at your own risk. 

from Scripts.omgarturo.fm_core.core_attack import run_mage_loop

# Can cast spellweaving, magery, necro spells. Can heal player, friends, pets, etc.
# Set the values you need and go. I run a few different versions of this:
#
#   1. Mage Tamer AoE = This will heal me, my pet and cast wildfire every 10 seconds.
#   2. Mage Tamer Heal Only = This heals me, my pet and a select few friends (no offense)
#   3. Focused Necro AoE = This will heal with spirit speak and spam whither
#   4. Focused Necro Single Target = Heals with spirit speak and uses evil omen, corpse skin, 
#       strangle every 30 seconds, and spams poison strike in between
#
# There is currently no logic that switches between AOE and single taret attacks. Instead,
# there is just a basic spell cast order. Some spells have a cast delay configured below
# (things like wildfire, strangle), while other spells just get spammed. Note that heals always get
# prioritized. As an added bonus, this will also work with bag of sending and automatically bank gold.
def run_mage_loop(

    # Give it a fun name in case you have different versions, e.g.
    # Mage AOE Loop or Mage Single Target Loop
    loopName = "Mage Loop",

    # Applicable when heal spells are enabled (Greater Heal, etc.) which are configured
    # down below. This governs how you want to heal allies. By default your character is always healed.
    # 0 = Heal only names in friendNames array (below), 1 = heal any blue in range, 2 = my pets only
    friendSelectMethod = 0,
    
    # Names of pets or blue characters you want to heal / cure if they are in range.
    # Note that you still need to enable useCure / useGreaterHeal etc.
    friendNames = [],
    
    # Only look for mobs and pets/friends inside of this range. IF they are farther, then
    # dont heal them / dont attack them.
    range = 8,
    
    # Use Arcane Empowerment (spell weaving) 0 = disabled, 1 = enabled
    useArcaneEmpowerment = 0,

    # Whether to use this spell 0 = disabled, 1 = enabled
    usePoisonStrike = 0,
    
    # Lower number like 10 means to spam repeatadly, number of MS in between usages
    poisonStrikeDelayMs = 8000,
    
    # Whether to use this spell 0 = disabled, 1 = enabled
    useStrangle = 0,
    
    # Change to an appropriate value for strangle spell, number of MS in between usages
    strangleDelayMs = 60000,
    
    # Whether to use this spell 0 = disabled, 1 = enabled
    useCorpseSkin = 0,
    
    # Change to an appropriate value, number of MS in between usages
    corpseSkinDelayMs = 60000,
    
    # Whether to use this spell before applying each dot and curse 0 = disabled, 1 = enabled
    useEvilOmenBeforeDotsAndCurses = 0,
    
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
    
    # Toggles death ray. Requires magery mastery. There is no timer because this remains
    # active until you move or you are interrupted or the creature dies. It will attempt to
    # reapply immediately. 0 = disabled, 1 = enabled
    useDeathRay = 0,
    
    # Will use shadow word death on eligible targets until they die. This is more of a toggle.
    # 0 = disabled, 1 = enabled
    useWordOfDeath = 0,
    
    # Whether to use this spell 0 = disabled, 1 = enabled
    useWildfire = 0,
    
    # Lower number like 10 means to spam repeatadly, number of MS in between usages
    wildfireDelayMs = 9000,
    
    # Whether to use the thunderstorm spellweaving spell. There is no delay here. Just spam.
    useThunderstorm = 0,
    
    # Whether to use this spell 0 = disabled, 1 = enabled. There is no delay here. Just spam.
    useWither = 0,
    
    # This is Insane UO Specific. That means there is no target reticle. Wont work
    # on other servers.
    useAnimateDead = 0,
    
    # Cast it this often
    animateDeadDelayMs = 60000,
    
    # InsaneUO specific. Keeps all 4 pets summoned when safe to cast.
    useSummonFamiliar = 0,
    
    # Make sure we are in wraith form when it is safe to cast.
    useWraithForm = 0,
    
    # Whether to cure yourself or your pet
    useCure = 0,
    
    # Whether to heal yourself or your pet
    useGreaterHeal = 0,
    
    # Necro heal
    useSpiritSpeak = 0,
    
    # Necro mastery for aoe damage, looks for buff. If no buff, casts it.
    useConduit = 0,
    
    # When standing still, no mobes in range, not bleeding, strangled, or poisoned, will start meditating.
    useMeditation = 0,
    
    # Only heal things that are below this percent HP
    healThreshold = 0.70,
    
    # InsaneUO specific. There is a cloak that grants immunity. Looks like 30 second cooldown.
    # Looks for item on Cloak layer and uses it. Timer for this is created in the main core_attack script.
    useCloakOfGraveMists = 0,
    
    # If greater than 0 will attempt to use bag of sending when this much gold is present. Default is 0, no bag of sending usage.
    minGold = 0,
    
    # Milliseonds of extra delay when computing cast time to account for internet fuzz. Fine tune this as needed.
    latencyMs = 200
)