from System import Byte, Int32
from System.Collections.Generic import List
from pathlib import Path
import __main__
import inspect
import os
import re
import sys

# Constants
MEDITATION_DELAY = 1250
CONSECRATE_WEAPON_DELAY = 500
EVIL_OMEN_DELAY = 1000
ATTUNE_WEAPON_DELAY = 1000
FC_CAP_MAGERY = 2
ANIMATE_DEAD_DELAY = 1750
BANDAGE_STATIC_ID = 3617
VAMPIRIC_EMBRACE_DELAY = 2250
GREATER_HEAL_DELAY = 1750
FC_CAP_NECROMANCY = 3 if Player.GetSkillValue('Necromancy') == 120 and Player.GetSkillValue('Necromancy') == 120 and (not any((Player.GetSkillValue(skill) > 30 for skill in ['Magery', 'Spellweaving', 'Parrying', 'Mysticism', 'Chivalry', 'Animal Taming', 'Animal Lore', 'Ninjitsu', 'Bushido', 'Focus', 'Imbuing', 'Evaluating Intelligence']))) else 2
GOLD_STATIC_IDS = [3821]
GIFT_OF_LIFE_DELAY = 4000
ARCANE_EMPOWERMENT_DELAY = 3000
FC_CAP_SPELLWEAVING = 4
WORD_OF_DEATH_DELAY = 3500
GIFT_OF_RENEWAL_DELAY = 3000
DEATH_RAY_DELAY = 2250
CONDUIT_DELAY = 2250
POISON_FIELD_DELAY = 2000
PROTECTION_DELAY = 750
BARD_SONG_DELAY = 2000
BLOOD_OATH_DELAY = 1750
ARCH_CURE_DELAY = 1750
DIVINE_FURY_DELAY = 1000
WITHER_DELAY = 2250
ANIMATE_DEAD_MOBILE_NAMES = ['a gore fiend', 'a lich', 'a flesh golem', 'a mummy', 'a skeletal dragon', 'a lich lord', 'a skeletal knight', 'a bone knight', 'a skeletal mage', 'a bone mage', 'a patchwork skeleton', 'a mound of maggots', 'a wailing banshee', 'a wraith', 'a hellsteed', 'a skeletal steed', 'an Undead Gargoyle', 'a skeletal drake', 'a putrid undead gargoyle', 'a blade spirit', 'an energy vortex', 'a skeletal drake']
LAP_HARP_GRAPHIC_ID = 3762
INSTRUMENT_STATIC_IDS = [3740, 10245, 3763, LAP_HARP_GRAPHIC_ID, 3761, 3742, 3741]
WRAITH_FORM_DELAY = 2250
ENEMY_OF_ONE_DELAY = 500
WILDFIRE_DELAY = 2500
FIRE_FIELD_DELAY = 1750
FC_CAP_CHIVALRY = 4
STRANGLE_DELAY = 2250 + 500
CURSE_WEAPON_DELAY = 1000
FC_CAP_BARD_SONG = 4
POISON_DELAY = 1500
FC_CAP_SHIELD_BASH = 4
POISON_STRIKE_DELAY = 2000
SHIELD_BASH_DELAY = 1000
THUNDERSTORM_DELAY = 1500
CURSE_DELAY = 1750
CORPSE_SKIN_DELAY = 1750
REMOVE_CURSE_DELAY = 1500
CHAIN_LIGHTNING_DELAY = 2000
SPIRIT_SPEAK_DELAY = 999
CLOSE_WOUNDS_DELAY = 1500
PAIN_SPIKE_DELAY = 1250
FLAME_STRIKE_DELAY = 2500
ENERGY_BOLT_DELAY = 2000

# Functions
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
def find_first_in_container_by_name(itemName, containerSerial=Player.Backpack.Serial):
    return Items.FindByName(itemName, -1, containerSerial, 1)
def get_fc_delay(baseDelayMs, fcCap, latencyMs=200):
    latency = 100
    fcOffset = 250 * (min(max(Player.FasterCasting - 2, 0), fcCap - 2) if Player.BuffsExist('Protection') else min(Player.FasterCasting, fcCap))
    delay = baseDelayMs - fcOffset
    if delay < 250:
        delay = 250
    return delay + latencyMs
def get_fcr_delay(spellName, latencyMs=200):
    fcr = int((6 - Player.FasterCastRecovery) / 4 * 1000)
    if fcr < 1:
        fcr = 1
    return fcr + latencyMs
def get_honor_target():
    for mob in get_enemies(10):
        if mob.Hits == mob.HitsMax:
            return mob
def run_dex_loop(loopName='Dex Loop', specialAbilityType=0, useShieldBash=0, useConsecrateWeapon=0, useCurseWeapon=0, useDivineFury=0, useEnemyOfOne=0, useRemoveCurse=0, useCleanseByFire=0, useHonor=0, attackRange=6, useBandagesOnSelf=0, healThreshold=0.95, minGold=0, latencyMs=200):
    Timer.Create('dexPingTimer', 5000)
    while not Player.IsGhost:
        if Timer.Check('dexPingTimer') == False:
            Player.HeadMessage(78, '{} Running...'.format(loopName))
            Timer.Create('dexPingTimer', 10000)
        if minGold > 0 and Player.Gold >= minGold:
            use_bag_of_sending(minGold)
        if not Player.Visible:
            Misc.Pause(500)
            continue
        if heal_player_and_friends(useCleanseByFire=useCleanseByFire, useRemoveCurse=useRemoveCurse, useBandagesOnSelf=useBandagesOnSelf, healThreshold=healThreshold) == True:
            continue
        eligible = get_enemies(attackRange)
        if len(eligible) > 0:
            nearestMob = Mobiles.Select(eligible, 'Nearest')
            honorMob = get_honor_target() if useHonor == 1 and (not Player.BuffsExist('Perfection')) else None
            if honorMob is not None:
                Player.InvokeVirtue('Honor')
                Target.WaitForTarget(1000, False)
                Target.TargetExecute(honorMob)
            elif useEnemyOfOne == 1 and (not Player.BuffsExist('Enemy Of One')) and (Player.Mana > 20):
                cast_spell('Enemy of One', None, latencyMs)
            elif useConsecrateWeapon == 1 and (not Player.BuffsExist('Consecrate Weapon')) and (Player.Mana > 12):
                cast_spell('Consecrate Weapon', None, latencyMs)
            elif useDivineFury == 1 and (not Player.BuffsExist('Divine Fury')) and (Player.Mana > 20):
                cast_spell('Divine Fury', None, latencyMs)
            elif useCurseWeapon == 1 and (not Player.BuffsExist('Curse Weapon')) and (Player.Mana > 20):
                cast_spell('Curse Weapon', None, latencyMs)
            if useShieldBash == 1 and (not Player.BuffsExist('Shield Bash')) and (Player.Mana > 35):
                cast_spell('Shield Bash', None, latencyMs)
            if (useShieldBash == 0 or (useShieldBash == 1 and Player.BuffsExist('Shield Bash'))) and Player.Mana > 20:
                if specialAbilityType == 1:
                    if not Player.HasPrimarySpecial:
                        Player.WeaponPrimarySA()
                elif specialAbilityType == 2:
                    if not Player.HasSecondarySpecial:
                        Player.WeaponSecondarySA()
                elif specialAbilityType == 3:
                    if not Player.BuffsExist('Lightning Strike'):
                        Spells.CastBushido('Lightning Strike', True)
                elif specialAbilityType == 4:
                    print('This needs work, there is no buff for focus attack. TODO')
                    if not Player.BuffsExist('Focus Attack'):
                        Spells.CastNinjitsu('Focus Attack', True)
                elif specialAbilityType == 5:
                    print('This needs work, there is no buff for momentum strike. TODO')
                    if not Player.BuffsExist('Momentum Strike'):
                        Spells.CastBushido('Momentum Strike', True)
            Player.Attack(nearestMob)
        Misc.Pause(100)
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
def find_first_in_container_by_ids(itemIDs, containerSerial=Player.Backpack.Serial):
    for itemID in itemIDs:
        item = find_in_container_by_id(itemID, containerSerial)
        if item != None:
            return item
    return None
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
def find_all_in_container_by_ids(itemIDs, containerSerial=Player.Backpack.Serial):
    items = []
    for itemID in itemIDs:
        items = items + Items.FindAllByID(itemID, -1, containerSerial, 1)
    return items
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

# Main code
run_dex_loop(loopName='Basher (primary)', specialAbilityType=1, useShieldBash=1, useConsecrateWeapon=1, useCurseWeapon=0, useDivineFury=0, useEnemyOfOne=0, useRemoveCurse=1, useCleanseByFire=0, useHonor=0, attackRange=6, useBandagesOnSelf=1, healThreshold=0.95, minGold=35000, latencyMs=200)
