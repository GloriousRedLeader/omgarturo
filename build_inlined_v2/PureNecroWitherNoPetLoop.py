from System import Byte, Int32
from System.Collections.Generic import List
from ctypes import wintypes
from pathlib import Path
import __main__
import ctypes
import inspect
import os
import re
import sys
import time

# Constants
WILDFIRE_DELAY = 2500
SHIELD_BASH_DELAY = 1000
DEATH_RAY_DELAY = 2250
SUMMON_FAMILIAR_DELAY = 2250
WITHER_DELAY = 2250
FC_CAP_SPELLWEAVING = 4
PROTECTION_DELAY = 750
THUNDERSTORM_DELAY = 1500
REMOVE_CURSE_DELAY = 1500
CLOSE_WOUNDS_DELAY = 1500
FC_CAP_CHIVALRY = 4
ENEMY_OF_ONE_DELAY = 500
CONDUIT_DELAY = 2250
ARCANE_EMPOWERMENT_DELAY = 3000
GREATER_HEAL_DELAY = 1750
GOLD_STATIC_IDS = [3821]
ANIMATE_DEAD_DELAY = 1750
EVIL_OMEN_DELAY = 1000
POISON_FIELD_DELAY = 2000
SPIRIT_SPEAK_DELAY = 999
FC_CAP_BARD_SONG = 4
ATTUNE_WEAPON_DELAY = 1000
GIFT_OF_LIFE_DELAY = 4000
VAMPIRIC_EMBRACE_DELAY = 2250
CURSE_DELAY = 1750
FC_CAP_NECROMANCY = 3 if Player.GetSkillValue('Necromancy') == 120 and Player.GetSkillValue('Necromancy') == 120 and (not any((Player.GetSkillValue(skill) > 30 for skill in ['Magery', 'Spellweaving', 'Parrying', 'Mysticism', 'Chivalry', 'Animal Taming', 'Animal Lore', 'Ninjitsu', 'Bushido', 'Focus', 'Imbuing', 'Evaluating Intelligence']))) else 2
ANIMATE_DEAD_MOBILE_NAMES = ['a gore fiend', 'a lich', 'a flesh golem', 'a mummy', 'a skeletal dragon', 'a lich lord', 'a skeletal knight', 'a bone knight', 'a skeletal mage', 'a bone mage', 'a patchwork skeleton', 'a mound of maggots', 'a wailing banshee', 'a wraith', 'a hellsteed', 'a skeletal steed', 'an Undead Gargoyle', 'a skeletal drake', 'a putrid undead gargoyle', 'a blade spirit', 'an energy vortex', 'a skeletal drake']
user32 = ctypes.WinDLL('user32', use_last_error=True)
BANDAGE_STATIC_ID = 3617
CURSE_WEAPON_DELAY = 1000
POISON_DELAY = 1500
BLOOD_OATH_DELAY = 1750
CORPSE_SKIN_DELAY = 1750
STRANGLE_DELAY = 2250 + 500
MEDITATION_DELAY = 1250
CHAIN_LIGHTNING_DELAY = 2000
WORD_OF_DEATH_DELAY = 3500
LAP_HARP_GRAPHIC_ID = 3762
POISON_STRIKE_DELAY = 2000
FC_CAP_SHIELD_BASH = 4
CONSECRATE_WEAPON_DELAY = 500
ARCH_CURE_DELAY = 1750
FLAME_STRIKE_DELAY = 2500
DIVINE_FURY_DELAY = 1000
FC_CAP_MAGERY = 2
PAIN_SPIKE_DELAY = 1250
WRAITH_FORM_DELAY = 2250
FIRE_FIELD_DELAY = 1750
BARD_SONG_DELAY = 2000
GIFT_OF_RENEWAL_DELAY = 3000
ENERGY_BOLT_DELAY = 2000
INSTRUMENT_STATIC_IDS = [3740, 10245, 3763, LAP_HARP_GRAPHIC_ID, 3761, 3742, 3741]

# Functions
def find_first_in_container_by_name(itemName, containerSerial=Player.Backpack.Serial):
    return Items.FindByName(itemName, -1, containerSerial, 1)
def use_skill(skillName, target=None, latencyMs=None):
    if skillName == 'Discordance':
        Journal.Clear()
    Player.UseSkill(skillName)
    if skillName == 'Meditation':
        Misc.Pause(MEDITATION_DELAY)
    elif skillName == 'Spirit Speak':
        Misc.Pause(SPIRIT_SPEAK_DELAY)
    elif skillName == 'Discordance':
        Target.WaitForTarget(latencyMs)
        if Journal.Search('What instrument shall you play?') or Journal.Search('No instruments found to Discord with!'):
            instrument = find_first_in_container_by_ids(INSTRUMENT_STATIC_IDS)
            if instrument is not None:
                Target.TargetExecute(instrument)
                Target.WaitForTarget(latencyMs)
            else:
                Misc.SendMessage('No instruments found to Discord with!')
        Target.TargetExecute(target)
        Misc.Pause(latencyMs)
    else:
        Misc.Pause(1000)
def find_in_container_by_id(itemID, containerSerial=Player.Backpack.Serial, color=-1, ignoreContainer=[], recursive=False):
    ignoreColor = False
    if color == -1:
        ignoreColor = True
    container = Items.FindBySerial(containerSerial)
    if isinstance(itemID, int):
        foundItem = next((item for item in container.Contains if item.ItemID == itemID and (ignoreColor or item.Hue == color)), None)
    elif isinstance(itemID, list):
        foundItem = next((item for item in container.Contains if item.ItemID in itemID and (ignoreColor or item.Hue == color)), None)
    else:
        raise ValueError('Unknown argument type for itemID passed to FindItem().', itemID, container)
    if foundItem != None:
        return foundItem
    elif recursive == True:
        for item in container.Contains:
            if item.IsContainer:
                foundItem = find_in_container_by_id(itemID, containerSerial=item.Serial, color=color, ignoreContainer=ignoreContainer, recursive=recursive)
                if foundItem != None:
                    return foundItem
def is_player_moving():
    return user32.GetAsyncKeyState(2) & 32768
def get_enemies(range=10, serialsToExclude=[]):
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = range
    fil.Notorieties = List[Byte](bytes([3, 4, 5, 6]))
    fil.IsGhost = False
    fil.Friend = False
    fil.CheckLineOfSight = True
    mobs = Mobiles.ApplyFilter(fil)
    if len(mobs) > 0:
        mobsList = List[type(mobs[0])]([mob for mob in mobs if not (mob.Name in ANIMATE_DEAD_MOBILE_NAMES and mob.Notoriety == 6) and mob.Serial not in serialsToExclude])
        return mobsList
    return mobs
def get_honor_target():
    for mob in get_enemies(10):
        if mob.Hits == mob.HitsMax:
            return mob
def get_fc_delay(baseDelayMs, fcCap, latencyMs=200):
    latency = 100
    fcOffset = 250 * (min(max(Player.FasterCasting - 2, 0), fcCap - 2) if Player.BuffsExist('Protection') else min(Player.FasterCasting, fcCap))
    delay = baseDelayMs - fcOffset
    if delay < 250:
        delay = 250
    return delay + latencyMs
def find_first_in_container_by_ids(itemIDs, containerSerial=Player.Backpack.Serial):
    for itemID in itemIDs:
        item = find_in_container_by_id(itemID, containerSerial)
        if item != None:
            return item
    return None
def get_blues_in_range(range=8):
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = range
    fil.Notorieties = List[Byte](bytes([1, 2]))
    fil.IsGhost = False
    fil.Friend = False
    fil.CheckLineOfSight = True
    mobs = Mobiles.ApplyFilter(fil)
    return mobs
def get_mobile_percent_hp(mobile):
    if mobile is not None and mobile.Hits is not None and (mobile.Hits > 0) and (mobile.HitsMax is not None) and (mobile.HitsMax > 0):
        return mobile.Hits / mobile.HitsMax
    else:
        return 0
def cast_spell(spellName, target=None, latencyMs=200):
    Target.Cancel()
    if spellName == 'Wildfire':
        Spells.CastSpellweaving(spellName)
        Target.WaitForTarget(get_fc_delay(WILDFIRE_DELAY, FC_CAP_SPELLWEAVING, latencyMs))
    elif spellName == 'Attune Weapon':
        Spells.CastSpellweaving(spellName)
        Target.WaitForTarget(get_fc_delay(ATTUNE_WEAPON_DELAY, FC_CAP_SPELLWEAVING, latencyMs))
    elif spellName == 'Thunderstorm':
        Spells.CastSpellweaving(spellName)
        Misc.Pause(get_fc_delay(THUNDERSTORM_DELAY, FC_CAP_SPELLWEAVING, latencyMs))
    elif spellName == 'Word of Death':
        Spells.CastSpellweaving(spellName)
        Target.WaitForTarget(get_fc_delay(WORD_OF_DEATH_DELAY, FC_CAP_SPELLWEAVING, latencyMs))
    elif spellName == 'Arcane Empowerment':
        Spells.CastSpellweaving(spellName)
        Target.WaitForTarget(get_fc_delay(ARCANE_EMPOWERMENT_DELAY, FC_CAP_SPELLWEAVING, latencyMs))
    elif spellName == 'Gift of Life':
        Spells.CastSpellweaving(spellName)
        Target.WaitForTarget(get_fc_delay(GIFT_OF_LIFE_DELAY, FC_CAP_SPELLWEAVING, latencyMs))
    elif spellName == 'Gift of Renewal':
        Spells.CastSpellweaving(spellName)
        Target.WaitForTarget(get_fc_delay(GIFT_OF_RENEWAL_DELAY, FC_CAP_SPELLWEAVING, latencyMs))
    elif spellName == 'Wither':
        Spells.CastNecro(spellName)
        Misc.Pause(get_fc_delay(WITHER_DELAY, FC_CAP_NECROMANCY, latencyMs))
    elif spellName == 'Conduit':
        Spells.CastMastery(spellName)
        Target.WaitForTarget(get_fc_delay(CONDUIT_DELAY, FC_CAP_NECROMANCY, latencyMs))
    elif spellName == 'Corpse Skin':
        Spells.CastNecro(spellName)
        Target.WaitForTarget(get_fc_delay(CORPSE_SKIN_DELAY, FC_CAP_NECROMANCY, latencyMs))
    elif spellName == 'Pain Spike':
        Spells.CastNecro(spellName)
        Target.WaitForTarget(get_fc_delay(PAIN_SPIKE_DELAY, FC_CAP_NECROMANCY, latencyMs))
    elif spellName == 'Evil Omen':
        Spells.CastNecro(spellName)
        Target.WaitForTarget(get_fc_delay(EVIL_OMEN_DELAY, FC_CAP_NECROMANCY, latencyMs))
    elif spellName == 'Blood Oath':
        Spells.CastNecro(spellName)
        Target.WaitForTarget(get_fc_delay(BLOOD_OATH_DELAY, FC_CAP_NECROMANCY, latencyMs))
    elif spellName == 'Strangle':
        Spells.CastNecro(spellName)
        Target.WaitForTarget(get_fc_delay(STRANGLE_DELAY, FC_CAP_NECROMANCY, latencyMs))
    elif spellName == 'Poison Strike':
        Spells.CastNecro(spellName)
        Target.WaitForTarget(get_fc_delay(POISON_STRIKE_DELAY, FC_CAP_NECROMANCY, latencyMs))
    elif spellName == 'Curse Weapon':
        Spells.CastNecro(spellName)
        Misc.Pause(get_fc_delay(CURSE_WEAPON_DELAY, FC_CAP_NECROMANCY, latencyMs))
    elif spellName == 'Animate Dead':
        Spells.CastNecro(spellName)
        Misc.Pause(get_fc_delay(ANIMATE_DEAD_DELAY, FC_CAP_NECROMANCY, latencyMs))
    elif spellName == 'Wraith Form':
        Spells.CastNecro(spellName)
        Misc.Pause(get_fc_delay(WRAITH_FORM_DELAY, FC_CAP_NECROMANCY, latencyMs))
    elif spellName == 'Vampiric Embrace':
        Spells.CastNecro(spellName)
        Misc.Pause(get_fc_delay(VAMPIRIC_EMBRACE_DELAY, FC_CAP_NECROMANCY, latencyMs))
    elif spellName == 'Poison Field':
        Spells.CastMagery(spellName)
        Target.WaitForTarget(get_fc_delay(POISON_FIELD_DELAY, FC_CAP_MAGERY, latencyMs))
    elif spellName == 'Fire Field':
        Spells.CastMagery(spellName)
        Target.WaitForTarget(get_fc_delay(FIRE_FIELD_DELAY, FC_CAP_MAGERY, latencyMs))
    elif spellName == 'Poison':
        Spells.CastMagery(spellName)
        Target.WaitForTarget(get_fc_delay(POISON_DELAY, FC_CAP_MAGERY, latencyMs))
    elif spellName == 'Protection':
        Spells.CastMagery(spellName)
        Misc.Pause(get_fc_delay(PROTECTION_DELAY, FC_CAP_MAGERY, latencyMs))
    elif spellName == 'Energy Bolt':
        Spells.CastMagery(spellName)
        Target.WaitForTarget(get_fc_delay(ENERGY_BOLT_DELAY, FC_CAP_MAGERY, latencyMs))
    elif spellName == 'Flame Strike':
        Spells.CastMagery(spellName)
        Target.WaitForTarget(get_fc_delay(FLAME_STRIKE_DELAY, FC_CAP_MAGERY, latencyMs))
    elif spellName == 'Chain Lightning':
        Spells.CastMagery(spellName)
        Target.WaitForTarget(get_fc_delay(CHAIN_LIGHTNING_DELAY, FC_CAP_MAGERY, latencyMs))
    elif spellName == 'Death Ray':
        Spells.CastMastery(spellName)
        Target.WaitForTarget(get_fc_delay(DEATH_RAY_DELAY, FC_CAP_MAGERY, latencyMs))
    elif spellName == 'Curse':
        Spells.CastMagery(spellName)
        Target.WaitForTarget(get_fc_delay(CURSE_DELAY, FC_CAP_MAGERY, latencyMs))
        Target.TargetExecute(target)
    elif spellName == 'Arch Cure':
        Spells.CastMagery(spellName)
        Target.WaitForTarget(get_fc_delay(ARCH_CURE_DELAY, FC_CAP_MAGERY, latencyMs))
    elif spellName == 'Greater Heal':
        Spells.CastMagery(spellName)
        Target.WaitForTarget(get_fc_delay(GREATER_HEAL_DELAY, FC_CAP_MAGERY, latencyMs))
    elif spellName == 'Remove Curse':
        Spells.CastChivalry(spellName)
        Target.WaitForTarget(get_fc_delay(REMOVE_CURSE_DELAY, FC_CAP_CHIVALRY, latencyMs))
    elif spellName == 'Close Wounds':
        Spells.CastChivalry(spellName)
        Target.WaitForTarget(get_fc_delay(CLOSE_WOUNDS_DELAY, FC_CAP_CHIVALRY, latencyMs))
    elif spellName == 'Divine Fury':
        Spells.CastChivalry(spellName)
        Misc.Pause(get_fc_delay(DIVINE_FURY_DELAY, FC_CAP_CHIVALRY, latencyMs))
    elif spellName == 'Consecrate Weapon':
        Spells.CastChivalry(spellName)
        Misc.Pause(get_fc_delay(CONSECRATE_WEAPON_DELAY, FC_CAP_CHIVALRY, latencyMs))
    elif spellName == 'Enemy of One':
        Spells.CastChivalry(spellName)
        Misc.Pause(get_fc_delay(ENEMY_OF_ONE_DELAY, FC_CAP_CHIVALRY, latencyMs))
    elif spellName == 'Shield Bash':
        Spells.CastMastery(spellName)
        Misc.Pause(get_fc_delay(SHIELD_BASH_DELAY, FC_CAP_SHIELD_BASH, latencyMs))
    elif spellName == 'Inspire' or spellName == 'Invigorate' or spellName == 'Resilience' or (spellName == 'Perseverance'):
        Journal.Clear()
        Spells.CastMastery(spellName)
        Misc.Pause(get_fc_delay(BARD_SONG_DELAY, FC_CAP_BARD_SONG, latencyMs))
        if Journal.Search('What instrument shall you play?'):
            instrument = find_first_in_container_by_ids(INSTRUMENT_STATIC_IDS)
            if instrument is not None:
                Target.TargetExecute(instrument)
                Target.WaitForTarget(latencyMs)
            else:
                Misc.SendMessage('No instruments found to play bard songs!')
    else:
        Player.HeadMessage(28, 'That spell is not supported! Pausing.')
        Misc.Pause(1000)
    if target is not None:
        if type(target).__name__ == 'Point3D':
            Target.TargetExecute(target.X, target.Y, target.Z)
        else:
            Target.TargetExecute(target)
    Misc.Pause(get_fcr_delay(spellName, latencyMs))
def get_friends_by_names(friendNames=[], range=8):
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = range
    fil.Notorieties = List[Byte](bytes([1, 2]))
    fil.IsGhost = False
    fil.Friend = False
    fil.CheckLineOfSight = True
    mobs = Mobiles.ApplyFilter(fil)
    if len(mobs) > 0:
        mobsList = List[type(mobs[0])]([mob for mob in mobs if mob.Name in friendNames])
        return mobsList
    mobs = Mobiles.ApplyFilter(fil)
    return mobs
def get_fcr_delay(spellName, latencyMs=200):
    fcr = int((6 - Player.FasterCastRecovery) / 4 * 1000)
    if fcr < 1:
        fcr = 1
    return fcr + latencyMs
def use_bag_of_sending(minGold=50000):
    bag = find_first_in_container_by_name('a bag of sending', containerSerial=Player.Backpack.Serial)
    if bag is not None:
        goldPiles = find_all_in_container_by_ids(GOLD_STATIC_IDS)
        for goldPile in goldPiles:
            if goldPile.Amount >= minGold:
                Items.UseItem(bag)
                Target.WaitForTarget(1000, False)
                Target.TargetExecute(goldPile)
    else:
        print('No bag of sending found!')
def heal_player_and_friends(friendSelectMethod=0, friendNames=[], range=8, healThreshold=0.7, useCure=0, useGreaterHeal=0, useCloseWounds=0, useCleanseByFire=0, useRemoveCurse=0, useSpiritSpeak=0, useCloakOfGraveMists=0, useGiftOfRenewal=0, useBandagesOnSelf=0, latencyMs=100):
    if useCure == 0 and useGreaterHeal == 0 and (useCloseWounds == 0) and (useCleanseByFire == 0) and (useRemoveCurse == 0) and (useSpiritSpeak == 0) and (useCloakOfGraveMists == 0) and (useGiftOfRenewal == 0) and (useBandagesOnSelf == 0):
        return False
    bandage = find_in_container_by_id(BANDAGE_STATIC_ID) if useBandagesOnSelf == 1 else None
    if useCloakOfGraveMists == 1 and Timer.Check('cloakOfGraveMistsTimer') == False and (Player.Hits / Player.HitsMax <= 0.25):
        cloak = Player.GetItemOnLayer('Cloak')
        Items.UseItem(cloak)
        Target.WaitForTarget(1000)
        Target.Cancel()
        Timer.Create('cloakOfGraveMistsTimer', 30000)
        Misc.Pause(100)
        return True
    elif useBandagesOnSelf == 1 and bandage is not None and (not Player.BuffsExist('Healing')) and (Player.Hits / Player.HitsMax < healThreshold or Player.Poisoned):
        Items.UseItem(bandage)
        Target.WaitForTarget(1500)
        Target.TargetExecute(Player.Serial)
    elif useGiftOfRenewal == 1 and Timer.Check('useGiftOfRenewalTimer') == False and (Player.Hits / Player.HitsMax < healThreshold):
        cast_spell('Gift of Renewal', Player.Serial, latencyMs)
        Timer.Create('useGiftOfRenewalTimer', 60 * 2500)
        return True
    elif useCure == 1 and Player.Poisoned:
        cast_spell('Arch Cure', Player.Serial)
        return True
    elif useGreaterHeal == 1 and (not Player.Poisoned) and (Player.Hits / Player.HitsMax < healThreshold) and (not Player.YellowHits) and (Player.Mana > 15):
        cast_spell('Greater Heal', Player.Serial, latencyMs)
        return True
    elif useCloseWounds == 1 and (not Player.Poisoned) and (Player.Hits / Player.HitsMax < healThreshold) and (not Player.YellowHits) and (Player.Mana > 15):
        cast_spell('Close Wounds', Player.Serial, latencyMs)
        return True
    elif useSpiritSpeak == 1 and (not Player.Poisoned) and (Player.Hits / Player.HitsMax < healThreshold) and (not Player.YellowHits) and (Player.Mana > 15):
        use_skill('Spirit Speak')
        return True
    elif useCleanseByFire == 1 and Player.Poisoned and (Player.Mana > 15):
        cast_spell('Cleanse by Fire', None, latencyMs)
        return False
    elif useRemoveCurse == 1 and (Player.BuffsExist('Curse') or Player.BuffsExist('Feeblemind') or Player.BuffsExist('Corpse Skin') or Player.BuffsExist('Clumsy') or Player.BuffsExist('Mind Rot') or Player.BuffsExist('Weaken')) and (Player.Mana > 15) and (Timer.Check('useRemoveCurseNonCriticalTimer') == False):
        cast_spell('Remove Curse', Player.Serial, latencyMs)
        Timer.Create('useRemoveCurseNonCriticalTimer', 10000)
        return False
    elif useRemoveCurse == 1 and Player.BuffsExist('Blood Oath (curse)') and (Player.Mana > 15):
        cast_spell('Remove Curse', Player.Serial, latencyMs)
        return False
    if friendSelectMethod == 0:
        friendMobiles = get_friends_by_names(friendNames, range)
    elif friendSelectMethod == 1:
        friendMobiles = get_blues_in_range(range)
    elif friendSelectMethod == 2:
        friendMobiles = get_pets()

    def sort_friends(x, y):
        if x is None or y is None:
            return False
        if x.HitsMax is None or x.HitsMax == 0 or y.HitsMax is None or (y.HitsMax == 0):
            return False
        return x.Hits / x.HitsMax > y.Hits / y.HitsMax
    if len(friendMobiles) > 0:
        friendMobiles.Sort(sort_friends)
        friendMobile = friendMobiles[0]
        if not (useCure == 1 and friendMobile.Poisoned) and (not ((useGreaterHeal == 1 or useGiftOfRenewal == 1) and (not friendMobile.Poisoned) and (friendMobile.HitsMax is not None) and (friendMobile.HitsMax > 0) and (friendMobile.Hits / friendMobile.HitsMax < healThreshold) and (not friendMobile.YellowHits) and (friendMobile.Hits > 0))) and (Player.Mana < 15):
            return False
        if useCure == 1 and friendMobile.Poisoned:
            cast_spell('Arch Cure', friendMobile, latencyMs)
            return True
        elif useGiftOfRenewal == 1 and Timer.Check('useGiftOfRenewalTimer') == False and (not friendMobile.Poisoned) and (friendMobile.HitsMax is not None) and (friendMobile.HitsMax > 0) and (friendMobile.Hits / friendMobile.HitsMax < healThreshold) and (not friendMobile.YellowHits) and (friendMobile.Hits > 0):
            cast_spell('Gift of Renewal', friendMobile, latencyMs)
            Timer.Create('useGiftOfRenewalTimer', 60 * 2500)
            return True
        elif useGreaterHeal == 1 and (not friendMobile.Poisoned) and (friendMobile.HitsMax is not None) and (friendMobile.HitsMax > 0) and (friendMobile.Hits / friendMobile.HitsMax < healThreshold) and (not friendMobile.YellowHits) and (friendMobile.Hits > 0):
            cast_spell('Greater Heal', friendMobile, latencyMs)
            return True
    return False
def run_mage_loop(loopName='Mage Loop', friendSelectMethod=0, friendNames=[], range=8, useArcaneEmpowerment=0, mainNukeSpell=0, mainNukeDelayMs=100, mainAoeSpell=0, mainAoeDelayMs=100, aoeMinMobCount=3, aoeMaxRange=7, useStrangle=0, strangleDelayMs=60000, useCorpseSkin=0, corpseSkinDelayMs=60000, useEvilOmen=0, evilOmenDelayMs=20000, useBloodOath=0, bloodOathDelayMs=30000, useCurse=0, curseDelayMs=60000, usePoison=0, poisonDelayMs=30000, usePoisonField=0, poisonFieldDelayMs=10000, useFireField=0, fireFieldDelayMs=10000, useDeathRay=0, useWordOfDeath=0, useWildfire=0, wildfireDelayMs=9000, usePainSpike=0, useAnimateDead=0, animateDeadDelayMs=60000, useSummonFamiliar=0, useForm=0, useCure=0, useGreaterHeal=0, useSpiritSpeak=0, useConduit=0, conduitDelayMs=15000, useMeditation=0, healThreshold=0.7, useCloakOfGraveMists=0, useGiftOfRenewal=0, useGiftOfLife=0, useAttuneWeapon=0, useBardAbility=0, bardAbilityDelayMs=10000, useBardSongs=0, useProtection=0, useHonor=0, minGold=0, latencyMs=200):
    Timer.Create('animateDeadTimer', animateDeadDelayMs)
    if Player.Visible:
        Player.ChatSay('All Guard Me')
        Misc.Pause(250)
    while not Player.IsGhost:
        if Timer.Check('magePingTimer') == False:
            Player.HeadMessage(78, '{} Running...'.format(loopName))
            Timer.Create('magePingTimer', 10000)
        if not Player.Visible:
            Misc.Pause(500)
            continue
        if minGold > 0 and Player.Gold >= minGold:
            use_bag_of_sending(minGold)
        if is_player_moving():
            Misc.Pause(250)
            continue
        if heal_player_and_friends(friendSelectMethod=friendSelectMethod, friendNames=friendNames, range=range, healThreshold=healThreshold, useCure=useCure, useGreaterHeal=useGreaterHeal, useSpiritSpeak=useSpiritSpeak, useCloakOfGraveMists=useCloakOfGraveMists, useGiftOfRenewal=useGiftOfRenewal) == True:
            if useArcaneEmpowerment == 1 and (not Player.BuffsExist('Arcane Empowerment')) and (Player.Mana > 90) and (Player.Hits > 50):
                cast_spell('Arcane Empowerment', None, latencyMs)
            continue
        if Player.BuffsExist('Meditation') and Player.Mana / Player.ManaMax < 0.65:
            Misc.Pause(250)
            continue
        if Player.Mana > 30 and Player.Hits / Player.HitsMax > 0.9:
            if useForm == 1 and Player.Mana > 30 and (not Player.BuffsExist('Wraith Form')) and (Timer.Remaining('cloakOfGraveMistsTimer') < 20000):
                cast_spell('Wraith Form', None, latencyMs)
                continue
            elif useForm == 2 and Player.Mana > 30 and (not Player.BuffsExist('Vampiric Embrace')) and (Timer.Remaining('cloakOfGraveMistsTimer') < 20000):
                cast_spell('Vampiric Embrace', None, latencyMs)
                continue
            elif useBardSongs == 2 and Player.Mana > 50 and (not Player.BuffsExist('Invigorate')):
                cast_spell('Invigorate', None, latencyMs)
                continue
            elif useBardSongs == 2 and Player.Mana > 50 and (not Player.BuffsExist('Inspire')):
                cast_spell('Inspire', None, latencyMs)
                continue
            elif useBardSongs == 1 and Player.Mana > 50 and (not Player.BuffsExist('Resilience')):
                cast_spell('Resilience', None, latencyMs)
                continue
            elif useBardSongs == 1 and Player.Mana > 50 and (not Player.BuffsExist('Perseverance')):
                cast_spell('Perseverance', None, latencyMs)
                continue
            elif useProtection == 1 and Player.Mana > 25 and (not Player.BuffsExist('Protection')):
                cast_spell('Protection', None, latencyMs)
                continue
            elif useGiftOfLife == 1 and Player.Mana > 125 and (not Player.BuffsExist('Gift of Life')):
                pets = get_pets()
                if len(pets) > 0:
                    cast_spell('Gift of Life', pets[0], latencyMs)
                cast_spell('Gift of Life', Player.Serial, latencyMs)
                continue
            elif useAttuneWeapon == 1 and Player.Mana > 50 and (not Player.BuffsExist('Attune Weapon')) and (Timer.Check('attuneWeaponTimer') == False):
                cast_spell('Attune Weapon', None, latencyMs)
                Timer.Create('attuneWeaponTimer', 4 * 60 * 1000)
                continue
            if useSummonFamiliar == 1 and Player.Mana > 40:
                if check_summon_familiar(latencyMs):
                    continue
        eligible = get_enemies(range)
        if len(eligible) > 0:
            nearestMob = Mobiles.Select(eligible, 'Nearest')
            nonPoisonedMob = next((mob for mob in eligible if not mob.Poisoned and get_mobile_percent_hp(mob) > 0.5), None)
            countMobsInAoeRange = sum((1 for mob in eligible if Player.DistanceTo(mob) < aoeMaxRange))
            honorMob = get_honor_target() if useHonor == 1 and (not Player.BuffsExist('Perfection')) else None
            if honorMob is not None:
                Player.InvokeVirtue('Honor')
                Target.WaitForTarget(1000, False)
                Target.TargetExecute(honorMob)
            elif useBardAbility == 3 and Timer.Check('discordTimer') == False:
                use_skill('Discordance', nearestMob, latencyMs)
                Timer.Create('discordTimer', bardAbilityDelayMs)
            elif useArcaneEmpowerment == 1 and (not Player.BuffsExist('Arcane Empowerment')) and (Player.Mana > 90) and (Player.Hits > 50):
                cast_spell('Arcane Empowerment', None, latencyMs)
            elif useConduit == 1 and (not Player.BuffsExist('Conduit')) and (len(eligible) > 2) and (Player.DistanceTo(nearestMob) > 0):
                cast_spell('Conduit', nearestMob.Position, latencyMs)
            elif useConduit == 2 and Timer.Check('conduitTimer') == False and (len(eligible) > 2) and (Player.DistanceTo(nearestMob) > 0):
                cast_spell('Conduit', nearestMob, latencyMs)
                Timer.Create('conduitTimer', conduitDelayMs)
            elif useWordOfDeath == 1 and get_mobile_percent_hp(nearestMob) < 0.3 and (len(eligible) <= 3):
                cast_spell('Word of Death', nearestMob, latencyMs)
            elif useDeathRay == 1 and (not Player.BuffsExist('Death Ray')) and Player.BuffsExist('Arcane Empowerment') and (not Player.BuffsExist('Poison') and (not Player.BuffsExist('Strangle'))) and (Player.Mana > 125):
                cast_spell('Death Ray', nearestMob, latencyMs)
            elif usePainSpike == 1 and Timer.Check('painSpikeTimer') == False and (not Player.BuffsExist('Conduit')):
                cast_spell('Pain Spike', nearestMob, latencyMs)
                Timer.Create('painSpikeTimer', 10500)
            elif useEvilOmen == 2 and Timer.Check('evilOmenTimer') == False:
                cast_spell('Evil Omen', nearestMob, latencyMs)
                Timer.Create('evilOmenTimer', evilOmenDelayMs)
            elif useCorpseSkin == 1 and Timer.Check('corpseSkinTimer') == False and (get_mobile_percent_hp(nearestMob) > 0.5):
                if useEvilOmen == 1:
                    cast_spell('Evil Omen', nearestMob, latencyMs)
                cast_spell('Corpse Skin', nearestMob, latencyMs)
                Timer.Create('corpseSkinTimer', corpseSkinDelayMs)
            elif useStrangle == 1 and Timer.Check('strangleTimer') == False and (get_mobile_percent_hp(nearestMob) > 0.5):
                if useEvilOmen == 1:
                    cast_spell('Evil Omen', nearestMob, latencyMs)
                cast_spell('Strangle', nearestMob, latencyMs)
                Timer.Create('strangleTimer', strangleDelayMs)
            elif usePoison == 1 and Timer.Check('poisonTimer') == False and (nonPoisonedMob is not None):
                if useEvilOmen == 1:
                    cast_spell('Evil Omen', nonPoisonedMob, latencyMs)
                cast_spell('Poison', nonPoisonedMob, latencyMs)
                Timer.Create('poisonTimer', poisonDelayMs)
            elif useBloodOath == 1 and Timer.Check('bloodOathTimer') == False:
                cast_spell('Blood Oath', nearestMob, latencyMs)
                Timer.Create('bloodOathTimer', bloodOathDelayMs)
            elif useCurse == 1 and Timer.Check('curseTimer') == False and (get_mobile_percent_hp(nearestMob) > 0.75):
                if useEvilOmen == 1:
                    cast_spell('Evil Omen', nearestMob, latencyMs)
                cast_spell('Curse', nearestMob, latencyMs)
                Timer.Create('curseTimer', curseDelayMs)
            elif useAnimateDead == 1 and Timer.Check('animateDeadTimer') == False and (Player.Hits / Player.HitsMax > 0.9):
                cast_spell('Animate Dead', None, latencyMs)
                Timer.Create('animateDeadTimer', animateDeadDelayMs)
            elif useWildfire == 1 and Timer.Check('wildfireTimer') == False:
                cast_spell('Wildfire', nearestMob.Position, latencyMs)
                Timer.Create('wildfireTimer', wildfireDelayMs)
            elif usePoisonField == 1 and Timer.Check('poisonFieldTimer') == False and (nonPoisonedMob is not None):
                cast_spell('Poison Field', nonPoisonedMob, latencyMs)
                Timer.Create('poisonFieldTimer', poisonFieldDelayMs)
            elif useFireField == 1 and Timer.Check('fireFieldTimer') == False:
                cast_spell('Fire Field', nearestMob, latencyMs)
                Timer.Create('fireFieldTimer', fireFieldDelayMs)
            elif mainNukeSpell == 1 and Timer.Check('mainNukeTimer') == False and (countMobsInAoeRange < aoeMinMobCount or mainAoeSpell == 0):
                cast_spell('Poison Strike', nearestMob, latencyMs)
                Timer.Create('mainNukeTimer', mainNukeDelayMs)
            elif mainNukeSpell == 2 and Timer.Check('mainNukeTimer') == False and (countMobsInAoeRange < aoeMinMobCount or mainAoeSpell == 0):
                cast_spell('Energy Bolt', nearestMob, latencyMs)
                Timer.Create('mainNukeTimer', mainNukeDelayMs)
            elif mainNukeSpell == 3 and Timer.Check('mainNukeTimer') == False and (countMobsInAoeRange < aoeMinMobCount or mainAoeSpell == 0):
                cast_spell('Flame Strike', nearestMob, latencyMs)
                Timer.Create('mainNukeTimer', mainNukeDelayMs)
            elif mainAoeSpell == 1 and Timer.Check('mainAoeTimer') == False and (countMobsInAoeRange >= aoeMinMobCount) and (Player.Mana > 30):
                cast_spell('Wither', None, latencyMs)
                Timer.Create('mainAoeTimer', mainAoeDelayMs)
            elif mainAoeSpell == 2 and Timer.Check('mainAoeTimer') == False and (countMobsInAoeRange >= aoeMinMobCount) and (Player.Mana > 30):
                cast_spell('Thunderstorm', None, latencyMs)
                Timer.Create('mainAoeTimer', mainAoeDelayMs)
            elif mainAoeSpell == 3 and Timer.Check('mainAoeTimer') == False and (countMobsInAoeRange >= aoeMinMobCount) and (Player.Mana > 30):
                cast_spell('Chain Lightning', nearestMob, latencyMs)
                Timer.Create('mainAoeTimer', mainAoeDelayMs)
            elif useMeditation == 1 and Player.Mana / Player.ManaMax < 0.35 and (not Player.Poisoned) and (not Player.BuffsExist('Bleeding')) and (not Player.BuffsExist('Strangle')) and (Timer.Check('meditationTimer') == False):
                Player.HeadMessage(58, 'Stand still - going to meditate!')
                Misc.Pause(500)
                use_skill('Meditation')
                Player.HeadMessage(58, 'Meditating!')
                Timer.Create('meditationTimer', 10000)
        elif Player.Hits / Player.HitsMax < 0.95 and Player.Mana > 20 and (useGreaterHeal == 1 or useSpiritSpeak == 1 or useCure == 1) and (not Player.BuffsExist('Invigorate')) and (not Player.BuffsExist('Gift of Renewal')):
            heal_player_and_friends(friendSelectMethod=0, friendNames=[], range=range, healThreshold=0.95, useCure=useCure, useGreaterHeal=useGreaterHeal, useSpiritSpeak=useSpiritSpeak, useCloakOfGraveMists=0)
        elif useMeditation == 1 and Player.Mana / Player.ManaMax < 0.83 and (not Player.Poisoned) and (not Player.BuffsExist('Bleeding')) and (not Player.BuffsExist('Strangle')) and (Timer.Check('meditationTimer') == False):
            Player.HeadMessage(58, 'Stand still - going to meditate!')
            Misc.Pause(500)
            use_skill('Meditation')
            Player.HeadMessage(58, 'Meditating!')
            Timer.Create('meditationTimer', 10000)
        Misc.Pause(100)
def find_all_in_container_by_ids(itemIDs, containerSerial=Player.Backpack.Serial):
    items = []
    for itemID in itemIDs:
        items = items + Items.FindAllByID(itemID, -1, containerSerial, 1)
    return items
def check_summon_familiar(latencyMs=200):
    SUMMON_FAMILIAR_GUMP_ID = 545409390
    if Timer.Check('checkSummonFamiliarTimer') == False:
        if not Gumps.HasGump(SUMMON_FAMILIAR_GUMP_ID):
            Spells.CastNecro('Summon Familiar')
            Gumps.WaitForGump(SUMMON_FAMILIAR_GUMP_ID, 1000)
        if Gumps.HasGump(SUMMON_FAMILIAR_GUMP_ID):
            petButtonMap = {}
            data = Gumps.GetGumpData(SUMMON_FAMILIAR_GUMP_ID)
            for piece in data.layoutPieces:
                match = re.match('button (?:\\d+\\s)*(\\d+)', piece)
                if match is not None:
                    buttonId = int(match.group(1))
                    if buttonId in [2, 102]:
                        petButtonMap['Shadow Wisp'] = buttonId
                    elif buttonId in [3, 103]:
                        petButtonMap['Dark Wolf'] = buttonId
                    elif buttonId in [4, 104]:
                        petButtonMap['Death Adder'] = buttonId
                    elif buttonId in [5, 105]:
                        petButtonMap['Vampire Bat'] = buttonId
            pets = get_pets(range=15, checkLineOfSight=False)
            petNames = [pet.Name.replace(Player.Name + ' ', '') for pet in pets]
            goodPetCount = 0
            connectionTooTenuous = False
            for petName in petButtonMap:
                if petButtonMap[petName] < 6:
                    Journal.Clear()
                    Gumps.SendAction(SUMMON_FAMILIAR_GUMP_ID, petButtonMap[petName])
                    Misc.Pause(get_fc_delay(baseDelayMs=SUMMON_FAMILIAR_DELAY, fcCap=FC_CAP_NECROMANCY, latencyMs=latencyMs))
                    Misc.Pause(250)
                    if Journal.Search('Your connection to the netherworld') == True:
                        connectionTooTenuous = True
                        break
                    return True
                elif petName not in petNames:
                    Gumps.SendAction(SUMMON_FAMILIAR_GUMP_ID, petButtonMap[petName])
                    Misc.Pause(250)
                else:
                    goodPetCount = goodPetCount + 1
                if goodPetCount == 4:
                    Timer.Create('checkSummonFamiliarTimer', 3000)
            if connectionTooTenuous:
                for petName in petButtonMap:
                    if petButtonMap[petName] > 6:
                        if not Gumps.HasGump(SUMMON_FAMILIAR_GUMP_ID):
                            Spells.CastNecro('Summon Familiar')
                            Gumps.WaitForGump(SUMMON_FAMILIAR_GUMP_ID, 1000)
                        Gumps.SendAction(SUMMON_FAMILIAR_GUMP_ID, petButtonMap[petName])
                        Misc.Pause(250)
    return False
def get_pets(range=10, checkLineOfSight=True, mobileId=None):
    pets = []
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = range
    fil.Notorieties = List[Byte](bytes([1, 2]))
    fil.IsGhost = False
    fil.Friend = False
    fil.CheckLineOfSight = checkLineOfSight
    if mobileId is not None:
        fil.Bodies = List[Int32]([mobileId])
    blues = Mobiles.ApplyFilter(fil)
    for blue in blues:
        if blue.CanRename:
            pets.append(blue)
    return pets

# Main code
run_mage_loop(loopName='Wither Necro (no pet)', friendSelectMethod=0, friendNames=[], range=1, useArcaneEmpowerment=0, mainNukeSpell=1, mainNukeDelayMs=100, mainAoeSpell=1, mainAoeDelayMs=100, aoeMinMobCount=3, aoeMaxRange=9, useStrangle=0, strangleDelayMs=25000, useCorpseSkin=0, corpseSkinDelayMs=30000, useEvilOmen=0, evilOmenDelayMs=20000, useBloodOath=0, bloodOathDelayMs=30000, useCurse=0, curseDelayMs=60000, usePoison=0, poisonDelayMs=30000, usePoisonField=0, poisonFieldDelayMs=10000, useFireField=0, fireFieldDelayMs=10000, useDeathRay=0, useWordOfDeath=0, useWildfire=0, usePainSpike=0, useAnimateDead=0, animateDeadDelayMs=25000, useSummonFamiliar=1, useForm=2, useCure=0, useGreaterHeal=0, useSpiritSpeak=1, useConduit=0, conduitDelayMs=15000, useMeditation=0, healThreshold=0.7, useCloakOfGraveMists=1, useGiftOfRenewal=0, useGiftOfLife=0, useAttuneWeapon=0, useBardAbility=0, bardAbilityDelayMs=10000, useProtection=0, useHonor=0, minGold=45000, latencyMs=200)
