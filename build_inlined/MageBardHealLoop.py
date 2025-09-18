# ===============================================
# Imports
# ===============================================
import sys

# ===============================================
# Auto-generated inlined code. Do not edit
# ===============================================

# ===== Inlined block from core_attack.py =====
# ===== Inlined block from core_mobiles.py =====
# ---- get_mobile_percent_hp (from core_mobiles.py)
def get_mobile_percent_hp(mobile):
    if mobile is not None and mobile.Hits is not None and mobile.Hits > 0 and mobile.HitsMax is not None and mobile.HitsMax > 0:
        return mobile.Hits / mobile.HitsMax
    else:
        return 0

# ===== Inlined block from core_rails.py =====
# ---- user32 (binding from core_rails.py)
user32 = ctypes.WinDLL('user32', use_last_error=True)

# ---- is_player_moving (from core_rails.py)
def is_player_moving():
    return user32.GetAsyncKeyState(0x02) & 0x8000

# ===== Inlined block from core_spells.py =====
# ---- SUMMON_FAMILIAR_DELAY (binding from core_spells.py)
SUMMON_FAMILIAR_DELAY = 2250

# ---- check_summon_familiar (from core_spells.py)
def check_summon_familiar(

    # Milliseonds of extra delay when computing cast time to account for internet fuzz. Fine tune this as needed.
    latencyMs = 200
):
    SUMMON_FAMILIAR_GUMP_ID = 0x2082496e
    
    if Timer.Check("checkSummonFamiliarTimer") == False:
        if not Gumps.HasGump(SUMMON_FAMILIAR_GUMP_ID):
            Spells.CastNecro("Summon Familiar")
            Gumps.WaitForGump(SUMMON_FAMILIAR_GUMP_ID, 1000)

        if Gumps.HasGump(SUMMON_FAMILIAR_GUMP_ID):
            petButtonMap = {}
            data = Gumps.GetGumpData(SUMMON_FAMILIAR_GUMP_ID)
            for piece in data.layoutPieces:
                match = re.match(r"button (?:\d+\s)*(\d+)", piece)
                if match is not None:
                    buttonId = int(match.group(1))
                    #print("buttonId! ", buttonId, type(buttonId))
                    if buttonId in [2, 102]:
                        petButtonMap["Shadow Wisp"] = buttonId
                    elif buttonId in [3, 103]:
                        petButtonMap["Dark Wolf"] = buttonId
                    elif buttonId in [4, 104]:
                        petButtonMap["Death Adder"] = buttonId
                    elif buttonId in [5, 105]:
                        petButtonMap["Vampire Bat"] = buttonId

            pets = get_pets(range = 15, checkLineOfSight = False)
            petNames = [pet.Name.replace(Player.Name + " ", "") for pet in pets]    
            goodPetCount = 0
            connectionTooTenuous = False # Rare error where we need to reset all pets completely, dunno
            for petName in petButtonMap:
                
                # Summon a pet
                if petButtonMap[petName] < 6:
                    Journal.Clear()
                    Gumps.SendAction(SUMMON_FAMILIAR_GUMP_ID, petButtonMap[petName])
                    Misc.Pause(get_fc_delay (baseDelayMs = SUMMON_FAMILIAR_DELAY, fcCap = FC_CAP_NECROMANCY, latencyMs = latencyMs))
                    Misc.Pause(250) # Extra pause for create to appear in world or we get stuck in an infinite loop

                    # Summon failed. Need to unsummon all pets (below)
                    if Journal.Search("Your connection to the netherworld") == True:
                        connectionTooTenuous = True
                        break
                    return True
                    
                # Unsummon pet if it is out of range
                elif petName not in petNames:
                    Gumps.SendAction(SUMMON_FAMILIAR_GUMP_ID, petButtonMap[petName])
                    Misc.Pause(250)    
                    
                # Dont do anything, we have this pet and it is in range
                else:
                    goodPetCount = goodPetCount + 1
                    
                # We have all 4 pets and they are nearby. Dont call again
                # for this many seconds                    
                if goodPetCount == 4:
                    Timer.Create("checkSummonFamiliarTimer", 3000)

            # Special case where we got an error that says our connection is too tenous.
            # So, unsummon all existing pets. The thing above that unsummons just does it on
            # a per pet basis if they are out of range.
            if connectionTooTenuous:
                for petName in petButtonMap:
                    if petButtonMap[petName] > 6:
                        if not Gumps.HasGump(SUMMON_FAMILIAR_GUMP_ID):
                            Spells.CastNecro("Summon Familiar")
                            Gumps.WaitForGump(SUMMON_FAMILIAR_GUMP_ID, 1000)                        
                        Gumps.SendAction(SUMMON_FAMILIAR_GUMP_ID, petButtonMap[petName])
                        Misc.Pause(250)    
                        
    return False

# ---- run_mage_loop (from core_attack.py)
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
    # Will cast every time buff expires automatically AND an enemy is in range.
    useArcaneEmpowerment = 0,
    
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
    aoeMaxRange = 7,
    
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
    
    # Lower number like 10 means to spam repeatadly, number of MS in between usages
    wildfireDelayMs = 9000,
    
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
    useCure = 0,
    
    # Whether to heal yourself or your pet
    useGreaterHeal = 0,
    
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
    useMeditation = 0,
    
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
    
    # Attune weapon has a cooldown. Stratics says 2 minues. On IUO it is longer. It might have
    # something to do with Focus skill. I dont know. So, Im setting this to about 4 minutes.
    # 0 = Do not use
    # 1 = Cast on self.
    useAttuneWeapon = 0,
    
    # Use a bard ability.
    # 0 = Default, do nothing
    # 1 = Peacemaking (notimplemented)
    # 2 = Provocation (notimplemented)
    # 3 = Discord (Yes)
    useBardAbility = 0,
    
    # Wait this long in milliseconds between bard ability uses
    bardAbilityDelayMs = 10000,
    
    # List the bard songs you wish to use. 
    # 0 = Default, do nothing
    # 1 = Peacemaking (Resilience, Perseverance)
    # 2 = Provocation (Inspire, Invigorate)
    # 3 = Discord (does nothing)
    useBardSongs = 0,
    
    # Use the Magery Protection spell. Casts when no nearby enemies.
    useProtection = 0,
    
    # EXPERIMENTAL: Does not work great. Would recommend not using this.
    # Whether to honor a nearby enemy to gain the perfection buff.
    # Will try to find an enemy at full health when the buff doesnt exist on player.
    useHonor = 0,
    
    # If greater than 0 will attempt to use bag of sending when this much gold is present. Default is 0, no bag of sending usage.
    minGold = 0,
    
    # Milliseonds of extra delay when computing cast time to account for internet fuzz. Fine tune this as needed.
    latencyMs = 200
):
    Timer.Create( 'animateDeadTimer', animateDeadDelayMs )

    if Player.Visible:
        Player.ChatSay("All Guard Me")
        Misc.Pause(250)
    
    while not Player.IsGhost:
        #Target.Cancel()
        
        if Timer.Check( 'magePingTimer' ) == False:
            Player.HeadMessage( 78, "{} Running...".format(loopName) )
            Timer.Create( 'magePingTimer', 10000 )

        if not Player.Visible:
            Misc.Pause(500)
            continue  
            
        if minGold > 0 and Player.Gold >= minGold:
            use_bag_of_sending(minGold)            
            
        if is_player_moving():
            Misc.Pause(250)
            continue

        # Continue loop before doing harmul actions, focus on healing/curing.
        if heal_player_and_friends(friendSelectMethod = friendSelectMethod, friendNames = friendNames, range = range, healThreshold = healThreshold, useCure = useCure, useGreaterHeal = useGreaterHeal, useSpiritSpeak = useSpiritSpeak, useCloakOfGraveMists = useCloakOfGraveMists, useGiftOfRenewal = useGiftOfRenewal) == True:
            if useArcaneEmpowerment == 1 and not Player.BuffsExist("Arcane Empowerment") and Player.Mana > 90 and Player.Hits > 50:
                cast_spell("Arcane Empowerment", None, latencyMs)
            continue
            
        if Player.BuffsExist("Meditation") and Player.Mana / Player.ManaMax < 0.65:
            Misc.Pause(250)
            continue
            
        # Buffs / Forms
        if Player.Mana > 30 and Player.Hits / Player.HitsMax > 0.90:
            if useForm == 1 and Player.Mana > 30 and not Player.BuffsExist("Wraith Form") and Timer.Remaining("cloakOfGraveMistsTimer") < 20000:
                cast_spell("Wraith Form", None, latencyMs)
                continue
            elif useForm == 2 and Player.Mana > 30 and not Player.BuffsExist("Vampiric Embrace") and Timer.Remaining("cloakOfGraveMistsTimer") < 20000:
                cast_spell("Vampiric Embrace", None, latencyMs)
                continue
            elif useBardSongs == 2 and Player.Mana > 50 and not Player.BuffsExist("Invigorate"):
                cast_spell("Invigorate", None, latencyMs)
                continue
            elif useBardSongs == 2 and Player.Mana > 50 and not Player.BuffsExist("Inspire"):
                cast_spell("Inspire", None, latencyMs)
                continue
            elif useBardSongs == 1 and Player.Mana > 50 and not Player.BuffsExist("Resilience"):
                cast_spell("Resilience", None, latencyMs)
                continue
            elif useBardSongs == 1 and Player.Mana > 50 and not Player.BuffsExist("Perseverance"):
                cast_spell("Perseverance", None, latencyMs) 
                continue
            elif useProtection == 1 and Player.Mana > 25 and not Player.BuffsExist("Protection"):
                cast_spell("Protection", None, latencyMs)
                continue
            elif useGiftOfLife == 1 and Player.Mana > 125 and not Player.BuffsExist("Gift of Life"):
                # This is a not so great way of doing this. When player loses debuff, we
                # re-apply to Pet and Player. Pet may not need it. And there may be times
                # when we dont need  it but pet does.
                pets = get_pets()
                if len(pets) > 0:
                    # Just cast on first pet, this spell is expensive.
                    cast_spell("Gift of Life", pets[0], latencyMs)
                # Cast on self
                cast_spell("Gift of Life", Player.Serial, latencyMs)
                continue
            elif useAttuneWeapon == 1 and Player.Mana > 50 and not Player.BuffsExist("Attune Weapon") and Timer.Check("attuneWeaponTimer") == False:
                cast_spell("Attune Weapon", None, latencyMs)
                Timer.Create("attuneWeaponTimer", 4 * 60 * 1000)
                continue
                
            if useSummonFamiliar == 1 and Player.Mana > 40:
                if check_summon_familiar(latencyMs):
                    #Misc.Pause(250)
                    continue

        eligible = get_enemies(range)
        if len(eligible) > 0:  
            nearestMob = Mobiles.Select(eligible, 'Nearest')
            nonPoisonedMob = next((mob for mob in eligible if not mob.Poisoned and get_mobile_percent_hp(mob) > 0.5), None)
            countMobsInAoeRange = sum(1 for mob in eligible if Player.DistanceTo(mob) < aoeMaxRange)
            
            # Experimental
            honorMob = get_honor_target() if useHonor == 1 and not Player.BuffsExist("Perfection") else None
            if honorMob is not None:
                Player.InvokeVirtue("Honor")
                Target.WaitForTarget(1000, False)
                Target.TargetExecute(honorMob)
            elif useBardAbility == 3 and Timer.Check("discordTimer") == False:
                use_skill("Discordance", nearestMob, latencyMs)
                Timer.Create("discordTimer", bardAbilityDelayMs)
            elif useArcaneEmpowerment == 1 and not Player.BuffsExist("Arcane Empowerment") and Player.Mana > 90 and Player.Hits > 50:
                cast_spell("Arcane Empowerment", None, latencyMs)            
            elif useConduit == 1 and not Player.BuffsExist("Conduit") and len(eligible) > 2 and Player.DistanceTo(nearestMob) > 0:
                cast_spell("Conduit", nearestMob.Position, latencyMs)
            elif useConduit == 2 and  Timer.Check( 'conduitTimer' ) == False and len(eligible) > 2 and Player.DistanceTo(nearestMob) > 0:
                cast_spell("Conduit", nearestMob, latencyMs)
                Timer.Create( 'conduitTimer', conduitDelayMs ) 
            elif useWordOfDeath == 1 and get_mobile_percent_hp(nearestMob) < 0.3 and len(eligible) <= 3:
                cast_spell("Word of Death", nearestMob, latencyMs)   
            elif useDeathRay == 1 and not Player.BuffsExist("Death Ray") and Player.BuffsExist("Arcane Empowerment") and (not Player.BuffsExist("Poison") and not Player.BuffsExist("Strangle")) and Player.Mana > 125:
                cast_spell("Death Ray", nearestMob, latencyMs)                                
                         
            elif usePainSpike == 1  and Timer.Check( 'painSpikeTimer' ) == False and not Player.BuffsExist("Conduit"):
                cast_spell("Pain Spike", nearestMob, latencyMs)
                Timer.Create( 'painSpikeTimer', 10500 )
            elif useEvilOmen == 2 and Timer.Check( 'evilOmenTimer' ) == False:
                cast_spell("Evil Omen", nearestMob, latencyMs)
                Timer.Create( 'evilOmenTimer', evilOmenDelayMs )
            elif useCorpseSkin == 1 and Timer.Check( 'corpseSkinTimer' ) == False and get_mobile_percent_hp(nearestMob) > 0.5:
                if useEvilOmen == 1:
                    cast_spell("Evil Omen", nearestMob, latencyMs)
                cast_spell("Corpse Skin", nearestMob, latencyMs)
                Timer.Create( 'corpseSkinTimer', corpseSkinDelayMs )
            elif useStrangle == 1 and Timer.Check( 'strangleTimer' ) == False and get_mobile_percent_hp(nearestMob) > 0.5:
                if useEvilOmen == 1:
                    cast_spell("Evil Omen", nearestMob, latencyMs)
                cast_spell("Strangle", nearestMob, latencyMs)
                Timer.Create( 'strangleTimer', strangleDelayMs ) 
            elif usePoison == 1 and Timer.Check( 'poisonTimer' ) == False and nonPoisonedMob is not None:
                if useEvilOmen == 1:
                    cast_spell("Evil Omen", nonPoisonedMob, latencyMs)
                cast_spell("Poison", nonPoisonedMob, latencyMs)
                Timer.Create( 'poisonTimer', poisonDelayMs) 
            elif useBloodOath == 1 and Timer.Check( 'bloodOathTimer' ) == False:
                cast_spell("Blood Oath", nearestMob, latencyMs)
                Timer.Create( 'bloodOathTimer', bloodOathDelayMs )
            elif useCurse == 1 and Timer.Check( 'curseTimer' ) == False and get_mobile_percent_hp(nearestMob) > 0.75:
                if useEvilOmen == 1:
                    cast_spell("Evil Omen", nearestMob, latencyMs)
                cast_spell("Curse", nearestMob, latencyMs)
                Timer.Create( 'curseTimer', curseDelayMs) 
            elif useAnimateDead == 1 and Timer.Check( 'animateDeadTimer' ) == False and Player.Hits / Player.HitsMax > 0.90:
                cast_spell("Animate Dead", None, latencyMs)
                Timer.Create( 'animateDeadTimer', animateDeadDelayMs)
            elif useWildfire == 1 and Timer.Check( 'wildfireTimer' ) == False:
                #cast_spell("Wildfire", nearestMob, latencyMs)
                cast_spell("Wildfire", nearestMob.Position, latencyMs)
                Timer.Create( 'wildfireTimer', wildfireDelayMs )
            elif usePoisonField == 1 and Timer.Check( 'poisonFieldTimer' ) == False and nonPoisonedMob is not None:
                cast_spell("Poison Field", nonPoisonedMob, latencyMs)
                Timer.Create( 'poisonFieldTimer', poisonFieldDelayMs)                 
            elif useFireField == 1 and Timer.Check( 'fireFieldTimer' ) == False:
                cast_spell("Fire Field", nearestMob, latencyMs)
                Timer.Create( 'fireFieldTimer', fireFieldDelayMs)                 
            elif mainNukeSpell == 1  and Timer.Check( 'mainNukeTimer' ) == False and (countMobsInAoeRange < aoeMinMobCount or mainAoeSpell == 0):
                cast_spell("Poison Strike", nearestMob, latencyMs)
                Timer.Create( 'mainNukeTimer', mainNukeDelayMs )
            elif mainNukeSpell == 2  and Timer.Check( 'mainNukeTimer' ) == False and (countMobsInAoeRange < aoeMinMobCount or mainAoeSpell == 0):
                cast_spell("Energy Bolt", nearestMob, latencyMs)
                Timer.Create( 'mainNukeTimer', mainNukeDelayMs ) 
            elif mainNukeSpell == 3  and Timer.Check( 'mainNukeTimer' ) == False and (countMobsInAoeRange < aoeMinMobCount or mainAoeSpell == 0):
                cast_spell("Flame Strike", nearestMob, latencyMs)
                Timer.Create( 'mainNukeTimer', mainNukeDelayMs ) 
            elif mainAoeSpell == 1 and Timer.Check( 'mainAoeTimer' ) == False and countMobsInAoeRange >= aoeMinMobCount and Player.Mana > 30:
                cast_spell("Wither", None, latencyMs)
                Timer.Create( 'mainAoeTimer', mainAoeDelayMs ) 
            elif mainAoeSpell == 2 and Timer.Check( 'mainAoeTimer' ) == False and countMobsInAoeRange >= aoeMinMobCount and Player.Mana > 30:
                cast_spell("Thunderstorm", None, latencyMs)
                Timer.Create( 'mainAoeTimer', mainAoeDelayMs ) 
            elif mainAoeSpell == 3  and Timer.Check( 'mainAoeTimer' ) == False and countMobsInAoeRange >= aoeMinMobCount and Player.Mana > 30:
                cast_spell("Chain Lightning", nearestMob, latencyMs)
                Timer.Create( 'mainAoeTimer', mainAoeDelayMs )
            elif useMeditation == 1 and Player.Mana / Player.ManaMax < 0.35 and not Player.Poisoned and not Player.BuffsExist("Bleeding") and not Player.BuffsExist("Strangle") and Timer.Check( 'meditationTimer' ) == False:
                Player.HeadMessage(58, "Stand still - going to meditate!")
                Misc.Pause(500)
                use_skill("Meditation")
                Player.HeadMessage(58, "Meditating!")
                Timer.Create( 'meditationTimer', 10000)    
            
        elif Player.Hits / Player.HitsMax < 0.95 and Player.Mana > 20 and (useGreaterHeal == 1 or useSpiritSpeak == 1 or useCure == 1) and not Player.BuffsExist("Invigorate") and not Player.BuffsExist("Gift of Renewal"):
            # Top player off if no one is around and its safe (and only if player doesnt have any Heal over time)
            heal_player_and_friends(friendSelectMethod = 0, friendNames = [], range = range, healThreshold = 0.95, useCure = useCure, useGreaterHeal = useGreaterHeal, useSpiritSpeak = useSpiritSpeak, useCloakOfGraveMists = 0)
            
        elif useMeditation == 1 and Player.Mana / Player.ManaMax < 0.83 and not Player.Poisoned and not Player.BuffsExist("Bleeding") and not Player.BuffsExist("Strangle") and Timer.Check( 'meditationTimer' ) == False:
            Player.HeadMessage(58, "Stand still - going to meditate!")
            Misc.Pause(500)
            use_skill("Meditation")
            Player.HeadMessage(58, "Meditating!")
            Timer.Create( 'meditationTimer', 10000) 
                
        Misc.Pause(100)

# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-08-19
# Use at your own risk. 


#   This one is configured for a Mage SpellWeaver Tamer Bard
#   It doesnt cast any AoE or damage spells. Purely focused
#   on healing.
#   Uses the Provo Bard songs.


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
    loopName = "Mage Bard Heal",

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
    useGiftOfRenewal = 1,
    
    # 0 = Do not use
    # 1 = Cast on yourself and pet (uses your buff to track, not pets, so not very reliable)
    useGiftOfLife = 1,
    
    # Attune weapon has a cooldown. Stratics says 2 minues. On IUO it is longer. It might have
    # something to do with Focus skill. I dont know. So, Im setting this to about 4 minutes.
    # 0 = Do not use
    # 1 = Cast on self.
    useAttuneWeapon = 1,
    
    # Use a bard ability.
    # 0 = Default, do nothing
    # 1 = Peacemaking (notimplemented)
    # 2 = Provocation (notimplemented)
    # 3 = Discord (Yes)
    useBardAbility = 0,
    
    # Wait this long in milliseconds between bard ability uses
    bardAbilityDelayMs = 8000,
    
    # List the bard songs you wish to use. 
    # 0 = Default, do nothing
    # 1 = Peacemaking (Resilience, Perseverance)
    # 2 = Provocation (Inspire, Invigorate)
    # 3 = Discord (does nothing)
    useBardSongs = 2,
    
    # Use the Magery Protection spell. Casts when no nearby enemies.
    useProtection = 0,
    
    # EXPERIMENTAL: Does not work great. Would recommend not using this.
    # Whether to honor a nearby enemy to gain the perfection buff.
    # Will try to find an enemy at full health when the buff doesnt exist on player.
    useHonor = 0,
    
    # If greater than 0 will attempt to use bag of sending when this much gold is present. Default is 0, no bag of sending usage.
    minGold = 45000,
    
    # Milliseonds of extra delay when computing cast time to account for internet fuzz. Fine tune this as needed.
    latencyMs = 200
)