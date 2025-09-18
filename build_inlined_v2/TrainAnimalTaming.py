from System import Byte
from System import Int32
from System.Collections.Generic import List
'\nAuthor: Aga - original author of the uosteam script\nOther Contributors: TheWarDoctor95 - converted to Razor Enhanced script\nLast Contribution By: TheWarDoctor95 - March 19, 2019\n\nDescription: Tames nearby animals to train Animal Taming to GM\n'
renameTamedAnimalsTo = 'crane'
petsToIgnore = [renameTamedAnimalsTo, 'omg doggie', 'snuggle monster']
numberOfFollowersToKeep = 1
maximumTameAttempts = 0
minimumTamingDifficulty = 50
enableFollowAnimal = True
journalEntryDelayMilliseconds = 100
targetClearDelayMilliseconds = 100
class Animal:
    name = ''
    mobileID = 0
    color = 0
    minTamingSkill = -1
    maxTamingSkill = -1
    packType = None

    def __init__(self, name, mobileID, color, minTamingSkill, maxTamingSkill, packType):
        self.name = name
        self.mobileID = mobileID
        self.color = color
        self.minTamingSkill = minTamingSkill
        self.maxTamingSkill = maxTamingSkill
animals = {'dog': Animal('dog', 217, 0, 0, 10, ['canine']), 'gorilla': Animal('gorilla', 29, 0, 0, 10, None), 'parrot': Animal('parrot', 831, 0, 0, 10, None), 'rabbit (brown)': Animal('rabbit', 205, 0, 0, 10, None), 'rabbit (black)': Animal('rabbit', 205, 2318, 0, 10, None), 'jack rabbit': Animal('jack rabbit', 205, 443, 0, 10, None), 'skittering hopper': Animal('skittering hopper', 302, 0, 0, 10, None), 'squirrel': Animal('squirrel', 278, 0, 0, 10, None), 'mongbat': Animal('mongbat', 39, 0, 0, 20, None), 'chickadee': Animal('chickadee', 6, 2112, 10, 20, None), 'crossbill': Animal('crossbill', 6, 2106, 10, 20, None), 'crow': Animal('crow', 6, 2305, 10, 20, None), 'finch': Animal('finch', 6, 2101, 10, 20, None), 'hawk': Animal('hawk', 6, 2101, 10, 20, None), 'kingfisher': Animal('kingfisher', 6, 2111, 10, 20, None), 'lapwing': Animal('lapwing', 6, 2103, 10, 20, None), 'magpie': Animal('magpie', 6, 2305, 10, 20, None), 'nuthatch': Animal('nuthatch', 6, 2129, 10, 20, None), 'plover': Animal('plover', 6, 2119, 10, 20, None), 'raven': Animal('raven', 6, 2305, 10, 20, None), 'skylark': Animal('skylark', 6, 2108, 10, 20, None), 'starling': Animal('starling', 2110, 2117, 10, 20, None), 'swift': Animal('swift', 6, 2117, 10, 20, None), 'tern': Animal('tern', 6, 2119, 10, 20, None), 'towhee': Animal('towhee', 6, 2119, 10, 20, None), 'woodpecker': Animal('woodpecker', 6, 2129, 10, 20, None), 'wren': Animal('wren', 6, 2128, 10, 20, None), 'cat': Animal('cat', 201, 0, 10, 20, ['feline']), 'chicken': Animal('chicken', 208, 0, 10, 20, None), 'mountain goat': Animal('mountain goat', 88, 0, 10, 20, None), 'rat': Animal('rat', 238, 0, 10, 20, None), 'sewer rat': Animal('sewer rat', 238, 0, 10, 20, None), 'cow (brown)': Animal('cow', 231, 0, 20, 30, None), 'cow (black)': Animal('cow', 216, 0, 20, 30, None), 'goat': Animal('goat', 209, 0, 20, 30, None), 'pig': Animal('pig', 203, 0, 20, 30, None), 'sheep': Animal('sheep', 207, 0, 20, 30, None), 'giant beetle': Animal('giant beetle', 791, 0, 20, 50, None), 'slime': Animal('slime', 51, 0, 20, 50, None), 'eagle': Animal('eagle', 5, 0, 30, 40, None), 'bouraRuddy': None, 'boar': Animal('boar', 290, 0, 40, 50, None), 'bullfrog': Animal('bullfrog', 81, 0, 40, 50, None), 'lowland boura': None, 'ferret': Animal('ferret', 279, 0, 40, 50, None), 'giant rat': Animal('giant rat', 215, 0, 40, 50, None), 'hind': Animal('hind', 237, 0, 40, 50, None), 'horse': Animal('horse', 200, 0, 40, 50, None), 'horse2': Animal('horse', 226, 0, 40, 50, None), 'horse3': Animal('horse', 204, 0, 40, 50, None), 'horse4': Animal('horse', 228, 0, 40, 50, None), 'horsePack': Animal('pack horse', 291, 0, 40, 50, None), 'horsePalomino': None, 'horseWar': None, 'pack llama': Animal('pack llama', 292, 0, 40, 50, None), 'llamaRideable': None, 'ostard': Animal('desert ostard', 210, 0, 40, 50, ['ostard']), 'forest ostard (green)': Animal('forest ostard', 219, 34976, 40, 50, ['ostard']), 'forest ostard (red)': Animal('forest ostard', 219, 34973, 40, 50, ['ostard']), 'timber wolf': Animal('timber wolf', 225, 0, 40, 50, ['canine']), 'rideable wolf': Animal('rideable wolf', 277, 0, 40, 50, ['canine']), 'black bear': Animal('black bear', 211, 0, 50, 60, ['bear']), 'polar bear': Animal('polar bear', 213, 0, 50, 60, ['bear']), 'deathwatch beetle': None, 'llama': Animal('llama', 220, 0, 50, 60, None), 'walrus': Animal('walrus', 221, 0, 50, 60, None), 'alligator': Animal('alligator', 202, 0, 60, 70, None), 'brown bear': Animal('brown bear', 167, 0, 60, 70, ['bear']), 'high plains boura': None, 'cougar': Animal('cougar', 63, 0, 60, 70, ['feline']), 'paralithode': None, 'scorpion': Animal('scorpion', 48, 0, 60, 70, None), 'rideable polar bear': Animal('rideable polar bear', 213, 0, 70, 80, ['bear']), 'grizzly bear': Animal('grizzly bear', 212, 0, 70, 80, ['bear']), 'young dragon': Animal('young dragon', 60, 0, 70, 80, None), 'great hart': Animal('great hart', 234, 0, 70, 80, None), 'snow leopard': Animal('snow leopard', 64, 0, 70, 80, ['feline']), 'snow leopard2': Animal('snow leopard', 65, 0, 70, 80, ['feline']), 'panther': Animal('panther', 214, 0, 70, 80, ['feline']), 'snake': Animal('snake', 52, 0, 70, 80, None), 'giant spider': Animal('giant spider', 28, 0, 70, 80, None), 'grey wolf (light grey)': Animal('grey wolf', 25, 0, 70, 80, ['canine']), 'grey wolf (dark grey)': Animal('grey wolf', 27, 0, 70, 80, ['canine']), 'gaman': None, 'slithStone': None, 'white wolf (dark grey)': Animal('white wolf', 34, 0, 80, 90, ['canine']), 'white wolf (light grey)': Animal('white wolf', 37, 0, 80, 90, ['canine']), 'bull (solid, brown)': Animal('bull', 232, 0, 90, 100, ['bull']), 'bull (solid, black)': Animal('bull', 232, 2305, 90, 100, ['bull']), 'bull (spotted, brown)': Animal('bull', 233, 0, 90, 100, ['bull']), 'bull (spotted, black)': Animal('bull', 233, 2305, 90, 100, ['bull']), 'foxBlood': None, 'hellcat (small)': Animal('hellcat', 201, 1607, 90, 100, ['feline']), 'mongbatGreater': None, 'frenzied ostard': Animal('frenzied ostard', 218, 0, 90, 100, ['ostard']), 'osseinRam': None, 'frost spider': Animal('frost spider', 20, 0, 90, 100, None), 'giant toad': Animal('giant toad', 80, 0, 90, 100, None), 'unicorn': None, 'giant ice worm': Animal('giant ice worm', 80, 0, 90, 100, None), 'drake (brown)': Animal('drake', 60, 0, 100, 110, None), 'drake (red)': Animal('drake', 61, 0, 100, 110, None), 'drakeCrimson': None, 'drakePlatinum': None, 'drakeStygian': None, 'hellcat (large)': Animal('hellcat', 127, 0, 100, 110, ['feline']), 'hellhound': Animal('hellhound', 98, 0, 100, 110, ['canine']), 'imp': Animal('imp', 74, 0, 100, 110, ['daemon']), 'kitsuneBake': None, 'lava lizard': Animal('lava lizard', 206, 0, 100, 110, None), 'ridgeback': Animal('ridgeback', 187, 0, 100, 110, None), 'savage ridgeback': Animal('savage ridgeback', 188, 0, 100, 110, None), 'slith': None, 'dire wolf': Animal('dire wolf', 23, 0, 100, 110, ['canine']), 'beetleDeath': None, 'beetleFire': None, 'rune beetle': Animal('rune beetle', 244, 0, 110, 120, None), 'dragon': Animal('dragon', 59, 0, 110, 120, None), 'dragonSwamp': None, 'dragonWater': None, 'dragonDeepWater': None, 'drakeCold': None, 'hiryu': None, 'hiryuLesser': None, 'lion': None, 'kiRin': None, 'nightbear': None, 'nightdragon': None, 'nightfrenzy': None, 'nightmare': None, 'nightllama': None, 'nightridge': None, 'nightwolf': None, 'skree': None, 'dread spider': Animal('dread spider', 11, 0, 110, 120, None), 'unicorn': None, 'wolfTsuki': None, 'white wyrm': Animal('white wyrm', 180, 0, 110, 120, None), 'cuSidhe': None, 'dimetrosaur': None, 'dragonBane': None, 'dragonFrost': None, 'a greater dragon': None, 'dragonSerpentine': None, 'gallusaurus': None, 'steedFire': None, 'steedSkeletal': None, 'horseDreadWar': None, 'miteFrost': None, 'najasaurus': None, 'phoenix': None, 'raptor': None, 'reptalon': None, 'saurosurus': None, 'tigerWild': None, 'tigerSabreToothed': None, 'triceratops': None, 'turtleHatchlingDragon': None, 'wolfDragon': None, 'shadow wyrm': Animal('shadow wyrm', 106, 0, 120, 120, None)}
def GetAnimalIDsAtOrOverTamingDifficulty(minimumTamingDifficulty):
    """
    Looks through the list of tameables for animals at or over the minimum taming level
    """
    global animals
    animalList = List[Int32]()
    for animal in animals:
        if not animals[animal] == None and (not animalList.Contains(animals[animal].mobileID)) and (animals[animal].minTamingSkill >= minimumTamingDifficulty):
            animalList.Add(animals[animal].mobileID)
    return animalList
noAnimalsToTrainTimerMilliseconds = 10000
playerStuckTimerMilliseconds = 5000
catchUpToAnimalTimerMilliseconds = 20000
animalTamingTimerMilliseconds = 13000
def FindAnimalToTame():
    """
    Finds the nearest tameable animal nearby
    """
    global renameTamedAnimalsTo
    global minimumTamingDifficulty
    animalFilter = Mobiles.Filter()
    animalFilter.Enabled = True
    animalFilter.Bodies = GetAnimalIDsAtOrOverTamingDifficulty(minimumTamingDifficulty)
    animalFilter.RangeMin = 0
    animalFilter.RangeMax = 12
    animalFilter.IsHuman = 0
    animalFilter.IsGhost = 0
    animalFilter.CheckIgnoreObject = True
    tameableMobiles = Mobiles.ApplyFilter(animalFilter)
    tameableMobilesTemp = tameableMobiles[:]
    for tameableMobile in tameableMobiles:
        if tameableMobile.Name in petsToIgnore:
            tameableMobilesTemp.Remove(tameableMobile)
    tameableMobiles = tameableMobilesTemp
    if len(tameableMobiles) == 0:
        return None
    elif len(tameableMobiles) == 1:
        return tameableMobiles[0]
    else:
        return Mobiles.Select(tameableMobiles, 'Nearest')
def PlayerWalk(direction):
    """
    Moves the player in the specified direction
    """
    playerPosition = Player.Position
    if Player.Direction == direction:
        Player.Walk(direction)
    else:
        Player.Walk(direction)
        Player.Walk(direction)
    return
def FollowMobile(mobile, maxDistanceToMobile=2, startPlayerStuckTimer=False):
    """
    Uses the X and Y coordinates of the animal and player to follow the animal around the map
    Returns True if player is not stuck, False if player is stuck
    """
    if not Timer.Check('catchUpToAnimalTimer'):
        return False
    mobilePosition = mobile.Position
    playerPosition = Player.Position
    directionToWalk = ''
    if mobilePosition.X > playerPosition.X and mobilePosition.Y > playerPosition.Y:
        directionToWalk = 'Down'
    if mobilePosition.X < playerPosition.X and mobilePosition.Y > playerPosition.Y:
        directionToWalk = 'Left'
    if mobilePosition.X > playerPosition.X and mobilePosition.Y < playerPosition.Y:
        directionToWalk = 'Right'
    if mobilePosition.X < playerPosition.X and mobilePosition.Y < playerPosition.Y:
        directionToWalk = 'Up'
    if mobilePosition.X > playerPosition.X and mobilePosition.Y == playerPosition.Y:
        directionToWalk = 'East'
    if mobilePosition.X < playerPosition.X and mobilePosition.Y == playerPosition.Y:
        directionToWalk = 'West'
    if mobilePosition.X == playerPosition.X and mobilePosition.Y > playerPosition.Y:
        directionToWalk = 'South'
    if mobilePosition.X == playerPosition.X and mobilePosition.Y < playerPosition.Y:
        directionToWalk = 'North'
    if startPlayerStuckTimer:
        Timer.Create('playerStuckTimer', playerStuckTimerMilliseconds)
    playerPosition = Player.Position
    PlayerWalk(directionToWalk)
    newPlayerPosition = Player.Position
    if playerPosition == newPlayerPosition and (not Timer.Check('playerStuckTimer')):
        if Player.Direction == 'Up':
            for i in range(5):
                Player.Walk('Down')
        elif Player.Direction == 'Down':
            for i in range(5):
                Player.Walk('Up')
        elif Player.Direction == 'Right':
            for i in range(5):
                Player.Walk('Left')
        elif Player.Direction == 'Left':
            for i in range(5):
                Player.Walk('Right')
        Timer.Create('playerStuckTimer', playerStuckTimerMilliseconds)
    elif playerPosition != newPlayerPosition:
        Timer.Create('playerStuckTimer', playerStuckTimerMilliseconds)
    if Player.DistanceTo(mobile) > maxDistanceToMobile:
        Misc.Pause(100)
        FollowMobile(mobile, maxDistanceToMobile)
    return True
def TrainAnimalTaming():
    """
    Trains Animal Taming to GM
    """
    global renameTamedAnimalsTo
    global numberOfFollowersToKeep
    global maximumTameAttempts
    global enablePeacemaking
    global enableFollowAnimal
    global journalEntryDelayMilliseconds
    global targetClearDelayMilliseconds
    global noAnimalsToTrainTimerMilliseconds
    global playerStuckTimerMilliseconds
    global catchUpToAnimalTimerMilliseconds
    global animalTamingTimerMilliseconds
    global peacemakingTimerMilliseconds
    global bandageTimerMilliseconds
    if Player.GetRealSkillValue('Animal Taming') == Player.GetSkillCap('Animal Taming'):
        Misc.SendMessage("You've already maxed out Animal Taming!", 65)
        return
    animalBeingTamed = None
    tameHandled = False
    tameOngoing = False
    timesTried = 0
    Timer.Create('animalTamingTimer', 1)
    Journal.Clear()
    Misc.ClearIgnore()
    Player.SetWarMode(True)
    Player.SetWarMode(False)
    while not Player.IsGhost and Player.GetRealSkillValue('Animal Taming') < Player.GetSkillCap('Animal Taming'):
        if animalBeingTamed != None and Mobiles.FindBySerial(animalBeingTamed.Serial) == None:
            Misc.SendMessage('Animal was killed or disappeared')
            animalBeingTamed = None
        if not maximumTameAttempts == 0 and timesTried > maximumTameAttempts:
            Mobiles.Message(animalBeingTamed, 1100, 'Tried more than %i times to tame. Ignoring animal' % maximumTameAttempts)
            Mobiles.IgnoreObject(animalBeingTamed)
            animalBeingTamed = None
            timesTried = 0
        if animalBeingTamed == None:
            animalBeingTamed = FindAnimalToTame()
            if animalBeingTamed == None:
                Misc.Pause(1000)
                continue
            else:
                Mobiles.Message(animalBeingTamed, 90, 'Found animal to tame')
        maxDistanceToTarget = 5
        if not tameOngoing:
            maxDistanceToTarget = 2
        if Player.DistanceTo(animalBeingTamed) > 30:
            Misc.SendMessage('Animal moved too far away, ignoring for now', 1100)
            animalBeingTamed = None
            continue
        elif animalBeingTamed != None and Player.DistanceTo(animalBeingTamed) > maxDistanceToTarget:
            if enableFollowAnimal:
                Timer.Create('catchUpToAnimalTimer', catchUpToAnimalTimerMilliseconds)
                playerStuck = not FollowMobile(animalBeingTamed, maxDistanceToTarget, True)
                if playerStuck:
                    Player.HeadMessage(1100, 'Player stuck!')
                    return
            else:
                Mobiles.Message(animalBeingTamed, 34, 'Not close enough!')
        if not tameOngoing and (not Timer.Check('animalTamingTimer')):
            Target.ClearLastandQueue()
            Misc.Pause(targetClearDelayMilliseconds)
            Player.UseSkill('Animal Taming')
            Target.WaitForTarget(2000, True)
            Target.TargetExecute(animalBeingTamed)
            if Journal.SearchByType('Tame which animal?', 'System'):
                timesTried += 1
                Player.HeadMessage(68, 'STARTING STARTING')
                Player.HeadMessage(68, 'STARTING STARTING')
                Player.HeadMessage(68, 'STARTING STARTING')
                Timer.Create('animalTamingTimer', animalTamingTimerMilliseconds)
                tameOngoing = True
            else:
                continue
        if tameOngoing:
            if Journal.SearchByName('It seems to accept you as master.', animalBeingTamed.Name) or Journal.SearchByType("That wasn't even challenging.", 'Regular'):
                if animalBeingTamed.Name != renameTamedAnimalsTo:
                    Misc.PetRename(animalBeingTamed, renameTamedAnimalsTo)
                if Player.Followers > numberOfFollowersToKeep:
                    Player.HeadMessage(58, 'RELEASING SHITTER')
                    Misc.WaitForContext(animalBeingTamed.Serial, 2000)
                    Misc.ContextReply(animalBeingTamed.Serial, 9)
                    Gumps.WaitForGump(2426193729, 10000)
                    Gumps.SendAction(2426193729, 2)
                Misc.IgnoreObject(animalBeingTamed)
                animalBeingTamed = None
                timesTried = 0
                tameHandled = True
            elif Journal.SearchByName('You fail to tame the creature.', animalBeingTamed.Name) or Journal.SearchByType('You must wait a few moments to use another skill.', 'Regular'):
                tameHandled = True
            elif Journal.SearchByType('That is too far away.', 'Regular') or Journal.SearchByName('You are too far away to continue taming.', animalBeingTamed.Name) or Journal.SearchByName('Someone else is already taming this', animalBeingTamed.Name):
                animalBeingTamed = None
                timesTried = 0
                Timer.Create('animalTamingTimer', 1)
                tameHandled = True
            elif Journal.SearchByName('You have no chance of taming this creature', animalBeingTamed.Name) or Journal.SearchByType('Target cannot be seen', 'Regular') or Journal.SearchByName('This animal has had too many owners and is too upset for you to tame.', animalBeingTamed.Name) or Journal.SearchByName('That animal looks tame already.', animalBeingTamed.Name) or Journal.SearchByName('You do not have a clear path to the animal you are taming, and must cease your attempt.', 'System'):
                Misc.IgnoreObject(animalBeingTamed)
                animalBeingTamed = None
                timesTried = 0
                Timer.Create('animalTamingTimer', 1)
                tameHandled = True
            if tameHandled:
                Journal.Clear()
                tameHandled = False
                tameOngoing = False
        Misc.Pause(50)
TrainAnimalTaming()
