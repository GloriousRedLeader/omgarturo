from pathlib import Path
import __main__
import inspect
import os
import re
script_name = getattr(__main__, '__file__', None) or sys.argv[0]
LAP_HARP_GRAPHIC_ID = 3762
CHAIN_LIGHTNING_DELAY = 2000
STRANGLE_DELAY = 2250 + 500
PROTECTION_DELAY = 750
hasWraith = Player.BuffsExist('Wraith Form')
EVIL_OMEN_DELAY = 1000
fcr = 1
FC_CAP_SPELLWEAVING = 4
BLOOD_OATH_DELAY = 1750
chivalrySkill = Player.GetSkillValue('Chivalry')
FC_CAP_MAGERY = 2
GIFT_OF_LIFE_DELAY = 4000
ATTUNE_WEAPON_DELAY = 1000
container = Items.FindBySerial(containerSerial)
ENEMY_OF_ONE_DELAY = 500
FC_CAP_NECROMANCY = 3 if Player.GetSkillValue('Necromancy') == 120 and Player.GetSkillValue('Necromancy') == 120 and (not any((Player.GetSkillValue(skill) > 30 for skill in ['Magery', 'Spellweaving', 'Parrying', 'Mysticism', 'Chivalry', 'Animal Taming', 'Animal Lore', 'Ninjitsu', 'Bushido', 'Focus', 'Imbuing', 'Evaluating Intelligence']))) else 2
WRAITH_FORM_DELAY = 2250
CONDUIT_DELAY = 2250
RUNEBOOK = 8901
match = re.match('button (?:\\d+\\s)*(\\d+)', piece)
VAMPIRIC_EMBRACE_DELAY = 2250
item = find_in_container_by_id(itemID, sourceSerial, color=color, ignoreContainer=[])
CONSECRATE_WEAPON_DELAY = 500
ARCH_CURE_DELAY = 1750
POISON_FIELD_DELAY = 2000
FC_CAP_SHIELD_BASH = 4
foundItem = find_in_container_by_id(itemID, containerSerial=item.Serial, color=color, ignoreContainer=ignoreContainer, recursive=recursive)
buttonId = int(match.group(1))
def cast_recall_or_sacred_journey(shapeshiftDelayMs=3000):
    RUNEBOOK_GUMP_ID = 89
    script_name = getattr(__main__, '__file__', None) or sys.argv[0]
    rune = int(re.search('RecallOrSacredJourneyRune(\\d+)\\.py', script_name).group(1))
    magerySkill = Player.GetSkillValue('Magery')
    chivalrySkill = Player.GetSkillValue('Chivalry')
    necroSkill = Player.GetSkillValue('Necromancy')
    hasWraith = Player.BuffsExist('Wraith Form')
    hasVampire = Player.BuffsExist('Vampiric Embrace')
    buttonId = 74 + rune if chivalrySkill > magerySkill else 49 + rune
    if magerySkill < 50 and chivalrySkill < 50 and (necroSkill > 80):
        while not Player.BuffsExist('Wraith Form'):
            cast_spell('Wraith Form', None, 650)
    runebook = Items.FindByID(RUNEBOOK, -1, Player.Backpack.Serial, 0)
    if runebook is None:
        Misc.SendMessage('No runebook found. Must be in backpack.', 38)
        sys.exit()
    print(runebook)
    print(script_name)
    print(f'Magery Skill {magerySkill}')
    print(f'Chivalry Skill {chivalrySkill}')
    print(f'Necromancy Skill {necroSkill}')
    print(f'Rune {rune}')
    print(f'Button ID {buttonId}')
    Items.UseItem(runebook)
    Gumps.WaitForGump(RUNEBOOK_GUMP_ID, 10000)
    Gumps.SendAction(RUNEBOOK_GUMP_ID, buttonId)
    Misc.Pause(3000)
    if hasVampire and Player.BuffsExist('Wraith Form'):
        Spells.CastNecro('Vampiric Embrace')
    if not hasVampire and (not hasWraith) and Player.BuffsExist('Wraith Form'):
        Spells.CastNecro('Wraith Form')
instrument = find_first_in_container_by_ids(INSTRUMENT_STATIC_IDS)
SHIELD_BASH_DELAY = 1000
FIRE_FIELD_DELAY = 1750
FLAME_STRIKE_DELAY = 2500
WORD_OF_DEATH_DELAY = 3500
GREATER_HEAL_DELAY = 1750
DIVINE_FURY_DELAY = 1000
ignoreColor = True
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
GIFT_OF_RENEWAL_DELAY = 3000
REMOVE_CURSE_DELAY = 1500
necroSkill = Player.GetSkillValue('Necromancy')
CORPSE_SKIN_DELAY = 1750
runebook = Items.FindByID(RUNEBOOK, -1, Player.Backpack.Serial, 0)
ANIMATE_DEAD_DELAY = 1750
WITHER_DELAY = 2250
delay = 250
RUNEBOOK_GUMP_ID = 89
def get_fcr_delay(spellName, latencyMs=200):
    fcr = int((6 - Player.FasterCastRecovery) / 4 * 1000)
    if fcr < 1:
        fcr = 1
    return fcr + latencyMs
POISON_STRIKE_DELAY = 2000
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
CURSE_DELAY = 1750
INSTRUMENT_STATIC_IDS = [3740, 10245, 3763, LAP_HARP_GRAPHIC_ID, 3761, 3742, 3741]
FC_CAP_CHIVALRY = 4
def find_first_in_container_by_ids(itemIDs, containerSerial=Player.Backpack.Serial):
    for itemID in itemIDs:
        item = find_in_container_by_id(itemID, containerSerial)
        if item != None:
            return item
    return None
DEATH_RAY_DELAY = 2250
ARCANE_EMPOWERMENT_DELAY = 3000
def get_fc_delay(baseDelayMs, fcCap, latencyMs=200):
    latency = 100
    fcOffset = 250 * (min(max(Player.FasterCasting - 2, 0), fcCap - 2) if Player.BuffsExist('Protection') else min(Player.FasterCasting, fcCap))
    delay = baseDelayMs - fcOffset
    if delay < 250:
        delay = 250
    return delay + latencyMs
ENERGY_BOLT_DELAY = 2000
hasVampire = Player.BuffsExist('Vampiric Embrace')
magerySkill = Player.GetSkillValue('Magery')
POISON_DELAY = 1500
PAIN_SPIKE_DELAY = 1250
rune = int(re.search('RecallOrSacredJourneyRune(\\d+)\\.py', script_name).group(1))
BARD_SONG_DELAY = 2000
fcOffset = 250 * (min(max(Player.FasterCasting - 2, 0), fcCap - 2) if Player.BuffsExist('Protection') else min(Player.FasterCasting, fcCap))
WILDFIRE_DELAY = 2500
THUNDERSTORM_DELAY = 1500
FC_CAP_BARD_SONG = 4
CLOSE_WOUNDS_DELAY = 1500
CURSE_WEAPON_DELAY = 1000
cast_recall_or_sacred_journey()
