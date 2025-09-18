using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text.RegularExpressions;
using System.Threading;
using RazorEnhanced;

namespace fooIUO.Basher
{
    public class fooIUOBasher
    {
        /// <summary>
        /// This determines whether or not the script shall attempt to cast "helper spells" whenever 
        /// enemies are near. Both can be set by using the setup gump, but the initial setting can
        /// - and should - be set here so you don't have to use the gump every time you start the
        /// script.
        /// </summary>
        public bool UseConsecrateWeapon { get; set; } = false;
        public bool UseDivineFury { get; set; } = false;
        public bool UseEnemyOfOne { get; set; } = true;

        /// <summary>
        /// Defines whether or not the script shall attempt to automatically bank gold via a bag of sending.
        /// </summary>
        public bool AutoBankGold { get; set; } = true;        
        
        /// <summary>
        /// Sets the numeric limit for gold and the weight percentage limit to be reached before the AutoBanking
        /// function fires. The more loot you accumulate - besides gold -, the heavier the character gets. Since
        /// you will not be able to carry around 50000 gold pieces when your inventory already has 250 stones of 
        /// other loot, an additional weight limit is needed.
        /// Both properties will usually be slightly overshot because they represent thresholds.
        /// </summary>
        public int GoldLimit { get; private set; } = 50000;
        public int WeightPercentageLimit { get; private set; } = 90;

        /// <summary>
        /// Defines whether or not you are running Lootmaster - the only Lootscript that matters by the man
        /// himself, DORANA. The Automatic Banking does not always play nice with Lootmaster, so if this is
        /// set to true, the script will attempt to STOP Lootmaster before the banking process and START it
        /// again when the banking has finished.
        /// </summary>
        public bool UseLootmaster { get; set; } = true;

        /// <summary>
        /// Defines the maximum aggression distance in tiles. The script will identify viable mobiles as targets
        /// if they are within range of the number of tiles this property is set to. If this distance is longer
        /// than 10 tiles, Shield Bash may run out before the mobile reaches the player. Dependant on the playstyle,
        /// this could probably use some adjustment.
        /// </summary>
        public int MaxAggroRange { get; private set; } = 10;

        /// <summary>
        /// The serial (!) of the anti-paralyze crate. Leave at 0 if you have none, but you should really have one.
        /// Serial can be given as decimal or hexadecimal integer.
        /// </summary>
        public int AntiParalyzeCrate { get; private set; } = 0;

        /// <summary>
        /// Sets whether or not the script shall attempt to automatically cure the Blood Oath curse whenever it
        /// detects it. If the script finds enchanted apples in the player's inventory, it will use these. If there
        /// are no enchanted apples to be found, the script will attempt to cure via the Remove Curse spell. It will
        /// stop attacking during that time, but the UO autoattack will still work.
        /// Set this to false if you wish to skip this.
        /// </summary>
        public bool AutoCureBloodOath { get; set; } = true; 

        /// <summary>
        /// The time delay to elapse until the script starts the next cycle. On slower computers this can be raised
        /// but should probably not exceed 250 milliseconds. Raising this will also raise the frequency of target
        /// aquisition which can make the whole experience less "smooth".
        /// Should not be below 25 ms for the time being.
        /// </summary>
        public int ParseDelay { get; private set; } = 25;

        /// <summary>
        /// Sets the targeting mode. false is the default and targets only neutral and evil mobiles - grey and red
        /// stuff. If this is set to true, blue mobiles are added to the potential targets. Useful for hunting
        /// Cu Sidhes or Unicorns. Even if this is set to true, the standard filter will still apply.
        /// </summary>
        public bool TargetBlues { get; private set; } = false;

        /// <summary>
        /// Sets the filtering mode. If set to true, the _doNotTarget field defined below will exempt certain
        /// targets from being attacked by the script. If it is set to false instead, absolutely every mobile
        /// will be attacked.
        /// </summary>
        public bool FilterTargets { get; set; } = true;
        
        /// <summary>
        /// Internal storage for the current target. Do not modify.
        /// </summary>
        public Mobile CurrentTarget { get; set; }


        /// <summary>
        /// The script will check the properties of each target against this list. If it finds any substring from this list
        /// in the target's properties, the target will be deemed as invalid and be exempt from attacking. Use lowercase
        /// when adding entries, since the properties from each Mobile will transformed to lowercase as well.
        /// </summary>
        private static readonly List<string> _doNotTarget = new List<string>
        {
            "healer", "priest of mondain",
            "a dog", "a cat", "a horse", "a sheep", "a crane", "a sheep", "a cow", "a bull", "a chicken", "a pig", "a boar",
            "a dolphin", "a cu sidhe", "bravehorn", "satyr",
            "a pack horse", "a pack llama", "(summoned)", "bonded", "Loyalty"
        };


        /// <summary>
        /// If a mob's name is matched to any entry in this list, the script will attempt to cast EOO if that mobile is the
        /// only target in the area. If anything else spawns, the next cycle will automatically cancel EOO. Entries can be 
        /// added, make sure to include the COMMA.
        /// </summary>
        private static readonly List<string> _eooTargets = new List<string>
        {
            // common Champs
            "Neira", "Mephitis", "Rikktor", "Barracoon", "Semidar", "Lord Oaks", "Sylvani",

            // advanced Champs
            "Dragon Turtle", "Serado", "Yukio's Captor", "Meraktus", "Ilhenir", "Twaulo", "Abyssal Infernal", "Primeval Lich", "Khal Ankur",

            // Peerless
            "Medusa", "Stygian Dragon", "Dread Horn", "Lady Melisande", "Paroxysmus", "Shimmering Effusion", "Monstrous Interred Grizzle",
            "Travesty", 

            // Doom
            "Abyssmal Horror", "Fleshrenderer", "Darknight Creeper", "Impaler", "Shadow Knight", "Dark Father", "Bone Daemon",

            // Shadowguard
            "Anon", "Virtuebane", "Ozymandias", "Juo'nar",

            // general assholes
            "evil spellbook", "The Slasher of Veils", "Putrefier", "Harrower",
        };


        /// <summary>
        /// UO hues for internal messaging. Can be customized to personal preferences.
        /// </summary>
        private int _red = 138;
        private int _yellow = 53;
        private int _green = 78;
        private int _blue = 188;





        //------------------------------------------//
        // DO NOT CHANGE ANYTHING BELOW THIS POINT! //
        //------------------------------------------//

        private readonly string _version = "0.9.5 BETA";

        private BasherShield _shield;

        
        /// <summary>
        /// Taken from ServUO code, used in cast delay calculations. Do not modify.
        /// </summary>
        public static readonly double HighFrequency = 1000.0 / Stopwatch.Frequency;
        public static double Ticks { get { return Stopwatch.GetTimestamp() * HighFrequency; } }


        /// <summary>
        /// Supported weapons, all have either Armor Ignore (AI) or Whirlwind (WW)
        /// </summary>
        private static List<BasherWeapon> weapons = new List<BasherWeapon>
        {
            // Swordsmanship
            new BasherWeapon(0x13FF, "katana", 2.5, 10, 14),
            new BasherWeapon(0x2D33, "radiant scimitar", 2.5, 10, 14),
            new BasherWeapon(0x0F5E, "broadsword", 3.25, 13, 17),
            new BasherWeapon(0x0F61, "longsword", 3.5, 14, 18),
            new BasherWeapon(0xA28B, "bladed whip", 3.25, 13, 17),

            // Fencing
            new BasherWeapon(0x1401, "kryss", 2.0, 10, 12),
            new BasherWeapon(0x2D22, "leafblade", 2.75, 11, 15),
            new BasherWeapon(0xA292, "spiked whip", 3.25, 13, 17),

            // Mace Fighting
            new BasherWeapon(0x13B0, "war axe", 3.0, 12, 16),
            new BasherWeapon(0x143D, "hammer pick", 3.25, 13, 17),
            new BasherWeapon(0xA289, "barbed whip", 3.25, 13, 17),

            // Throwing
            new BasherWeapon(0x090A, "soul glaive", 4.0, 16, 20),
            new BasherWeapon(0x0901, "cyclone", 3.25, 13, 17),
            new BasherWeapon(0x08FF, "boomerang", 2.75, 11, 15)
        };


        /// <summary>
        /// A mapping for the various slayer types with their respective properties strings
        /// taken from ServUO code.
        /// </summary>
        public static List<SlayerType> Slayers { get; private set; } = new List<SlayerType>
        {
            // Super Slayers
            new SlayerType(1060458, "Arachnid"),
            new SlayerType(1060461, "Demon"),
            new SlayerType(1060464, "Elemental"),
            new SlayerType(1060472, "Repond"),
            new SlayerType(1060473, "Reptile"),
            new SlayerType(1060479, "Undead"),
            new SlayerType(1070855, "Fey"),
            new SlayerType(1156126, "Eodon"),

            // Lesser Slayers


        };


        /// <summary>
        /// Imports the GetAsyncKeyState method from Windows' user32.dll.
        /// Used in the check of whether or not the player is moving.
        /// </summary>
        /// <param name="vKey">the hex id of the key in question, 0x02 for the right mouse button</param>
        /// <returns>the handle of GetAsyncKeyState</returns>
        [DllImport("user32.dll")]
        public static extern short GetAsyncKeyState(int vKey);


        /// <summary>
        /// The unique Id necessary for the status gump.
        /// </summary>
        private readonly uint _gumpId = 1239862391;


        /// <summary>
        /// Checks the state of the right mouse button. If it is DOWN, the script assumes the player
        /// to be moving and thus pauses. The sleep timer represents the parsing interval, here the 
        /// CPU clock seems to be more trustworthy than whatever RE is doing with Misc.Pause().
        /// </summary>
        /// <returns>true if right mouse button is down, false if it is not</returns>
        private bool IsPlayerMoving()
        {
            Thread.Sleep(ParseDelay);   // dirty, but working - should not be lower than 25
            return (GetAsyncKeyState(0x02) & 0x8000) != 0;
        }


        /// <summary>
        /// Breaks paralysis by using the trapped box defined in the property AntiParalysisCrate.
        /// If no box is found, nothing happens.
        /// </summary>
        private void BreakParalysis()
        {
            if (Player.BuffsExist("Paralysis"))
            {
                Item crate = Player.Backpack.Contains.Where(x => x.Serial == AntiParalyzeCrate).FirstOrDefault();

                if (crate != null)
                {
                    Misc.SendMessage($"foo> Breaking paralysis ...", _yellow);
                    Items.UseItem(crate);
                    Misc.Pause(ParseDelay * 2);
                }
            }
        }


        private void RemoveCurseSelf()
        {
            while (Player.BuffsExist("Blood Oath (curse)"))
            {
                Spells.CastChivalry("Remove Curse");
                Target.WaitForTarget(1500, true);
                Target.Self();
                Misc.Pause(ParseDelay * 3);
            }

            Player.HeadMessage(_green, "BLOOD OATH CURED!");
        }





        /// <summary>
        /// Attempts to cure the Blood Oath curse - the only curse or debuff that needs INSTANT attention.
        /// If no enchanted apples are found in the player's inventory, the script will attempt to cure 
        /// Blood Oath via the Chivalry spell Remove Curse. During this attacking will cease.
        /// It is strongly recommend to always carry a number of enchanted apples, because eating those 
        /// will cure any debuff, costs no mana and cannot be interrupted.
        /// </summary>
        private void CureBloodOath()
        {
            Journal journal = new Journal();
            journal.Clear();


            if (!AutoCureBloodOath)
            {
                return;
            }

            Item enchantedApples = Player.Backpack.Contains.Where(x => x.ItemID == 0x2FD8 && x.Hue == 0x0488).FirstOrDefault();

            if (Player.BuffsExist("Blood Oath (curse)") && enchantedApples != null)
            {
                Player.HeadMessage(_red, "BLOOD OATH ACTIVE!");
                Items.UseItem(enchantedApples);
                Misc.Pause(ParseDelay);

                if (!journal.Search("another enchanted apple"))
                {
                    Misc.SendMessage($"foo> Enchanted apple eaten. Blood Oath cured!", _green);
                    Player.HeadMessage(_green, "BLOOD OATH CURED!");
                    UpdateGump();
                    Misc.Pause(ParseDelay);
                }
                else
                {
                    Misc.SendMessage($"foo> Enchanted apples on cooldown, attempting Remove Curse!", _red);
                    RemoveCurseSelf();
                }
            }
            else if (Player.BuffsExist("Blood Oath (curse)"))
            {
                Player.HeadMessage(_red, "BLOOD OATH ACTIVE!");
                Misc.SendMessage($"foo> No enchanted apples found, attempting Remove Curse!", _red);
                RemoveCurseSelf();
            }
        }


        /// <summary>
        /// Finds the bag of sending in the player's backpack.
        /// </summary>
        /// <returns>the first bag of sending found or null if there is none</returns>
        private Item GetBagOfSending()
        {
            return Player.Backpack.Contains.Where(x => x.Name == "a bag of sending").FirstOrDefault();
        }


        /// <summary>
        /// Reads the remaining charges on the bag of sending and returns those as an integer.
        /// Parsing is done from the item properties.
        /// </summary>
        /// <param name="bag">the bag of sending to check (as Item object)</param>
        /// <returns>the number of remaining charges</returns>
        private int GetCharges(Item bag)
        {
            if (bag == null)
            {
                return 0;
            }

            Property charges = bag.Properties.Last();
            string value = Regex.Match(charges.ToString(), @"\d+").Value;
            return Int32.Parse(value);
        }


        /// <summary>
        /// Automatically banks gold via the bag of sending if the property AutoBankGold is set to true.
        /// If Lootmaster is detected, it will be stopped and restarted after the banking procedure.
        /// </summary>
        private void BankGold()
        {
            if (!AutoBankGold)
            {
                return;
            }

            Item goldStack = Player.Backpack.Contains.Where(x => x.ItemID == 0x0EED && x.Hue == 0x000).FirstOrDefault();
            Item bagOfSending = GetBagOfSending();

            if (bagOfSending == null) return;

            if (goldStack != null && bagOfSending != null && GetCharges(bagOfSending) > 0)
            {
                if (goldStack.Amount >= GoldLimit || Player.Weight >= (Player.MaxWeight * ((float)WeightPercentageLimit / 100)))
                {
                    if (UseLootmaster && Misc.ScriptStatus("Lootmaster.cs"))
                    {
                        Misc.ScriptStop("Lootmaster.cs");
                        Misc.Pause(ParseDelay);
                    }

                    Misc.SendMessage($"foo> Attempting to bank {goldStack.Amount} gold.", _blue);

                    Journal journal = new Journal();
                    journal.Clear();

                    Items.UseItem(bagOfSending);
                    Target.WaitForTarget(1000, true);
                    Target.TargetExecute(goldStack);
                    Misc.Pause(ParseDelay * 12);


                    if (UseLootmaster)
                    {
                        Misc.ScriptRun("Lootmaster.cs");
                    }

                    UpdateGump();
                }

            }
            else if (GetCharges(bagOfSending) == 0)
            {
                Misc.SendMessage($"foo> Your bag of sending has run out of charges.", _red);
            }
        }


        /// <summary>
        /// Adds all mobiles within the defined maximum range to a list and filters. Filters applied
        /// work by notoriety and excluding keywords in the properties of the mobile (i. e. "healer").
        /// Finally sorts the targets by distance to the player (ascending).
        /// </summary>
        /// <returns>a filtered and sorted list of targets</returns>
        private List<Mobile> GenerateTargetList()
        {
            List<byte> notorieties = new List<byte>();

            switch (TargetBlues)
            {
                // targets ALL viable Mobiles, including "good" ones
                case true:
                    notorieties.Add(1);
                    notorieties.Add(2);
                    notorieties.Add(3);
                    break;
                
                // targets only "neutral / grey" Mobiles
                case false:
                    notorieties.Add(3);
                    break;
            }

            // targets "evil" Mobiles
            notorieties.AddRange(new List<byte> { 4, 5, 6 });

            Mobiles.Filter targetFilter = new Mobiles.Filter
            {
                RangeMin = 0,
                RangeMax = MaxAggroRange,
                IsGhost = 0,
                Friend = 0,
                CheckLineOfSight = true,
                CheckIgnoreObject = true,
                Notorieties = notorieties
            };

            List<Mobile> targets = Mobiles.ApplyFilter(targetFilter);

            if (FilterTargets)
            {
                targets.RemoveAll(IsInvalidTarget);
            }
            
            targets.Sort((x, y) => Player.DistanceTo(x).CompareTo(Player.DistanceTo(y)));
            return targets;
        }

        
        /// <summary>
        /// Checks if the passed mobile has any properties which exempt it from being a target.
        /// Mobiles are checked against the _doNotTarget field.
        /// </summary>
        /// <param name="mobile">the mobile to check</param>
        /// <returns>true for exemption, false for valid target</returns>
        private static bool IsInvalidTarget(Mobile mobile)
        {
            string properties = String.Join(" ", mobile.Properties).ToLower();
            
            foreach (string keyword in _doNotTarget)
            {
                if (properties.Contains(keyword))
                {
                    return true;
                }

                if (properties.IndexOf(keyword, StringComparison.OrdinalIgnoreCase) >= 0)
                {
                    return true;
                }
            }

            return false;
        }


        /// <summary>
        /// Returns the number of targets which are in close proximity to the player - these targets
        /// allow the use of Whirlwind if there are at least 2. Detection range is 4 tiles.
        /// Used in the selection of the special attacks.
        /// </summary>
        /// <returns>the number of targets within 4 tiles of the player</returns>
        private int CountTargetsInProximity()
        {
            return GenerateTargetList().Where(t => (Player.DistanceTo(t) < 4)).ToList().Count;
        }


        /// <summary>
        /// Returns the player's LMC stat factorized as a double, used for mana calculations for special attacks.
        /// </summary>
        /// <returns>the LMC factor</returns>
        private double GetLMCFactor()
        {
            return (double)Player.LowerManaCost / 100;
        }


        /// <summary>
        /// Calculates the actual cast time for Shield Bash based on the characters FC stat.
        /// Base cast time of Shield Bash is 1 second. Maximum acceleration is reached
        /// with FC 3, minimum cast time will always be 250 milliseconds.
        /// </summary>
        /// <returns>adjusted cast delay in milliseconds</returns>
        private int GetShieldBashDelay()
        {
            return (1000 - (Math.Min(Player.FasterCasting, 3) * 250));
        }


        /// <summary>
        /// Calculates the required spell delay based on the player's FCR stat.
        /// Taken from ServUO directly, might be refactored in later versions.
        /// </summary>
        /// <returns>adjusted spell delay in milliseconds</returns>
        private int GetSpellDelay()
        {
            int crBase = 6;         // Base Cast Recovery (units)
            int crPerSecond = 4;    // Recovered per second

            int fcr = Player.FasterCastRecovery;
            int fcrDelay = -(1 * fcr);
            int spellDelay = Math.Max(crBase + fcrDelay, 0);

            return (int)TimeSpan.FromSeconds((double)spellDelay / crPerSecond).TotalMilliseconds;
        }



        /// <summary>
        /// Calculates the weapon swing time based on the equipped weapon, the player's stamina and
        /// the player's Swing Speed Increase (SSI). Formula taken from knuckleheads.dk
        /// </summary>
        /// <returns>the current swing time in milliseconds</returns>
        private int GetSwingTime()
        {
            Item equipped = Player.GetItemOnLayer("RightHand");

            if (equipped != null)
            {
                BasherWeapon weapon = weapons.Where(w => w.ItemId == equipped.ItemID).FirstOrDefault();

                double weaponTicks = weapon.Speed * 4;
                double staminaTicks = Math.Floor((double)Player.Stam / 30);

                double result = (Math.Floor((weaponTicks - staminaTicks) * (100.0 / (100 + Player.SwingSpeedIncrease))) * 1000);
                
                return Math.Max((int) (result / 4), 1250);
            }

            return 1250;
        }


        /// <summary>
        /// Checks if the target mobile of the player's last attack is still a valid Mobile or if 
        /// it has either died or vanished - in both cases it is time to select a new victim.
        /// </summary>
        /// <returns>true if valid Mobile is found, false if not</returns>
        private bool HasActiveTarget()
        {
            int targetSerial = Target.GetLastAttack();
            Mobile target = Mobiles.FindBySerial(targetSerial);

            return target != null;
        }

        /// <summary>
        /// Decides on what attack to used based on the currently equipped weapon. Only the registered
        /// weapons are considered so far, adding new ones is easy enough but questionable. Two handed
        /// weapons will never be considered because a shield needs to be equipped anyway.
        /// </summary>
        /// <param name="target">the target to attack</param>
        private void AttackTarget(Mobile target)
        {
            Player.Attack(target);
            Item weapon = Player.GetItemOnLayer("RightHand");

            if (weapon == null)
            {
                Misc.Pause(ParseDelay);
                return;
            }

            switch (weapon.ItemID)
            {
                /* single target weapons with Armor Ignore as PRIMARY special ability */
                case 0x13B0:    // war axe
                case 0x090A:    // soul glaive
                case 0x0F61:    // longsword
                    UseArmorIgnore(true);
                    break;

                /* single target weapons with Armor Ignore as SECONDARY special ability */
                case 0x13FF:    // katana (all)
                case 0x0F5E:    // broadsword
                case 0x2D22:    // leaf blade
                    UseArmorIgnore(false);
                    break;

                /* multi target weapons with Whirlwind as PRIMARY special ability  */
                case 0x2D33:    // radiant scimitar
                    UseWhirlwind(true);
                    break;

                /* multi target weapons with Whirlwind as SECONDARY special ability  */
                case 0xA28B:    // bladed whip
                case 0xA292:    // spiked whip
                case 0xA289:    // barbed whip
                    UseWhirlwind(false);
                    break;

                default:
                    Misc.NoOperation();
                    break;
            }
        }


        /// <summary>
        /// Fires the Armor Ignore special ability; based on current player mana this will
        /// be either a combination of Shield Bash + AI (70 mana * LMC factor), Solo Shield
        /// Bash (40 mana * LMC factor) or Solo AI (30 mana * LMC factor). If not even the 
        /// lowest threshold is met, a standard weapon attack is performed.
        /// </summary>
        /// <param name="primary">true if AI is the primary weapon SA, false if it is the secondary</param>
        private void UseArmorIgnore(bool primary)
        {
            UpdateGump();

            if (Player.Mana >=  Convert.ToInt32(Math.Ceiling(70 * GetLMCFactor())))
            {
                Spells.CastMastery("Shield Bash");
                Misc.Pause(GetShieldBashDelay());

                if (primary)
                {
                    Player.WeaponPrimarySA();
                }
                else
                {
                    Player.WeaponSecondarySA();
                }

                Misc.Pause(GetSwingTime() - GetSpellDelay() - 200);
            }
            else if (Player.Mana >= Convert.ToInt32(Math.Ceiling(41 * GetLMCFactor())))
            {
                Spells.CastMastery("Shield Bash");
                Misc.Pause(GetSwingTime() - GetShieldBashDelay());
            }
            else if (Player.Mana >= Convert.ToInt32(Math.Ceiling(30 * GetLMCFactor())))
            {
                if (primary)
                {
                    Player.WeaponPrimarySA();
                }
                else
                {
                    Player.WeaponSecondarySA();
                }

                Misc.Pause(GetSwingTime() - GetSpellDelay() - 200);
            }
            else
            {
                //Misc.SendMessage($"foo> Player Mana: {Player.Mana} -> Basic Attack!", _red);
                Misc.Pause(GetSwingTime());
            }


        }


        /// <summary>
        /// Fires the Whirlwind special ability, analogue to the AI method above.
        /// </summary>
        /// <param name="primary">true for primary SA, false for secondary</param>
        private void UseWhirlwind(bool primary)
        {
            if (Player.Mana >= Convert.ToInt32(55 * GetLMCFactor()))
            {
                Spells.CastMastery("Shield Bash");
                Misc.Pause(GetShieldBashDelay());

                // if there are enough targets for Whirlwind
                if (CountTargetsInProximity() >= 2)
                {
                    if (primary)
                    {
                        Player.WeaponPrimarySA();
                    }
                    else
                    {
                        Player.WeaponSecondarySA();
                    }
                    Misc.Pause(GetSwingTime() - GetSpellDelay() - 200);
                }
                else
                {
                    Misc.Pause(GetSwingTime() - GetShieldBashDelay());
                }
            }
            else if (Player.Mana >= Convert.ToInt32(40 * GetLMCFactor()))
            {
                Spells.CastMastery("Shield Bash");
                Misc.Pause(GetSwingTime() - GetShieldBashDelay());
            }
            else if (Player.Mana >= Convert.ToInt32(15 * GetLMCFactor()))
            {
                // if there are enough targets for Whirlwind
                if (CountTargetsInProximity() >= 2)
                {
                    if (primary)
                    {
                        Player.WeaponPrimarySA();
                    }
                    else
                    {
                        Player.WeaponSecondarySA();
                    }
                    Misc.Pause(GetSwingTime() - GetSpellDelay() - 200);
                }
                else
                {
                    Misc.Pause(GetSwingTime() - GetShieldBashDelay());
                }
            }
            else
            {
                Misc.Pause(GetSwingTime());
            }

            UpdateGump();
        }


        /// <summary>
        /// Displays the greeting and some status checks.
        /// </summary>
        private void StartUp()
        {
            Misc.SendMessage($"foo> Welcome to fooBasher!", _green);
            Misc.SendMessage($"foo> Current version: {_version}", _green);
            Misc.SendMessage("---------------------------", _green);
            Misc.Pause(150);
            Misc.SendMessage($"foo> Player FC is  {Player.FasterCasting}", _blue);
            Misc.SendMessage($"foo> Ergo: Shield Bash cast time is {GetShieldBashDelay()} ms.", _yellow);
            Misc.SendMessage("---------------------------", _blue);
            Misc.Pause(150);
            Misc.SendMessage($"foo> Player FCR is {Player.FasterCastRecovery}", _blue);
            Misc.SendMessage($"foo> Ergo: Spell Delay is {GetSpellDelay()} ms.", _yellow);
            Misc.SendMessage("---------------------------", _blue);
            Misc.Pause(150);

            Item equipped = Player.GetItemOnLayer("RightHand");
            if (equipped != null)
            {
                BasherWeapon weapon = weapons.Where(w => w.ItemId == equipped.ItemID).FirstOrDefault();
            
                Misc.SendMessage($"foo> Equipped weapon is a {weapon.Name}", _blue);
                Misc.SendMessage($"foo> Ergo: Basic weapon speed is {weapon.Speed} s.", _yellow);
                Misc.SendMessage("---------------------------", _blue);
            }

            Misc.SendMessage($"foo> Parsing shield data ...", _blue);
            _shield = GetShieldData();
            Misc.SendMessage("---------------------------", _blue);

            Misc.SendMessage($"foo> Player SSI is {Player.SwingSpeedIncrease}", _blue);
            Misc.SendMessage($"foo> Player Stamina is {Player.Stam}", _blue);

            double seconds = (double) GetSwingTime() / 1000;

            Misc.SendMessage($"foo> Ergo: Current Swing Speed is {seconds} s.", _yellow);
            Misc.SendMessage("---------------------------", _blue);
            Misc.SendMessage($"foo> LMC factor is {GetLMCFactor()}", _blue);
        }



        private int GetshieldDurabilityHue()
        {
            if (_shield.Durability >= _shield.MaxDurability * 0.6)
            {
                return _green;
            }

            if (_shield.Durability >= _shield.MaxDurability * 0.2)
            {
                return _yellow;
            }

            if (_shield.Durability <= _shield.MaxDurability * 0.2)
            {
                return _red;
            }

            return 0;
        }


        private int GetBagOfSendingChargesHue()
        {
            if (GetCharges(GetBagOfSending()) >= 50)
            {
                return _green;
            }

            if (GetCharges(GetBagOfSending()) >= 10)
            {
                return _yellow;
            }

            if (GetCharges(GetBagOfSending()) <= 10)
            {
                return _red;
            }

            return 0;
        }


        private int GetEnchantedApplesCountHue()
        {
            int count = CountEnchantedApples();

            if (count >= 25)
            {
                return _green;
            }

            if (count >= 15)
            {
                return _yellow;
            }

            if (count <= 15)
            {
                return _red;
            }

            return 0;
        }


        private int CountEnchantedApples()
        {
            Item apples = Player.Backpack.Contains.Where(x => x.ItemID == 0x2FD8 && x.Hue == 0x0488).FirstOrDefault();

            if (apples != null)
            {
                return apples.Amount;
            }
            return 0;
        }


        /// <summary>
        /// (Re-)renders the status gump. Gets fired from various places.
        /// </summary>
        private void UpdateGump()
        {
            Gumps.GumpData basherGump = Gumps.CreateGump(true, true, true, false);

            basherGump.buttonid = -1;
            basherGump.gumpId = _gumpId;
            basherGump.serial = Convert.ToUInt32(Player.Serial);
            basherGump.x = 600;
            basherGump.y = 100;

            Gumps.AddBackground(ref basherGump, 0, 0, 450, 100, 3500);
            Gumps.AddLabel(ref basherGump, 30, 15, 1258, "fooBasher Status Gump");

            // Shield durability monitor
            _shield = GetShieldData();
            Gumps.AddItem(ref basherGump, 30, 45, _shield.ItemId, _shield.Hue);
            Gumps.AddLabel(ref basherGump, 85, 45, 0, "Durability:");
            Gumps.AddLabel(ref basherGump, 85, 65, GetshieldDurabilityHue(), _shield.Durability.ToString());
            Gumps.AddLabel(ref basherGump, 107, 65, 0, " / " + _shield.MaxDurability.ToString());

            // Bag of Sending monitor
            Gumps.AddItem(ref basherGump, 160, 45, 0x0E76, 0x08a5);
            Gumps.AddLabel(ref basherGump, 195, 45, 0, "Charges: ");
            Gumps.AddLabel(ref basherGump, 250, 45, GetBagOfSendingChargesHue(), GetCharges(GetBagOfSending()).ToString());

            // Enchanted apples monitor
            Gumps.AddItem(ref basherGump, 160, 68, 0x2FD8, 0x0488);
            Gumps.AddLabel(ref basherGump, 195, 65, 0, "Apples: ");
            Gumps.AddLabel(ref basherGump, 250, 65, GetEnchantedApplesCountHue(), CountEnchantedApples().ToString());

            // Switches
            Gumps.AddButton(ref basherGump, 300, 46, 0x4BA, 0x4B9, 1, 1, 1);
            Gumps.AddLabel(ref basherGump, 320, 45, GetStatusHue("CW"), "CW");
            Gumps.AddButton(ref basherGump, 300, 66, 0x4BA, 0x4B9, 2, 1, 1);
            Gumps.AddLabel(ref basherGump, 320, 65, GetStatusHue("DF"), "DF");

            Gumps.AddButton(ref basherGump, 360, 46, 0x4BA, 0x4B9, 3, 1, 1);
            Gumps.AddLabel(ref basherGump, 380, 45, GetStatusHue("Blues?"), "Blues?");
            Gumps.AddButton(ref basherGump, 360, 66, 0x4BA, 0x4B9, 4, 1, 1);
            Gumps.AddLabel(ref basherGump, 380, 65, GetStatusHue("EOO"), "EOO");


            Gumps.CloseGump(_gumpId);
            Gumps.SendGump(basherGump, 0, 0);
        }


        /// <summary>
        /// Reads the data from the equipped shield and displays the durability. The icon displayed in the gump
        /// will match the shield actually equipped, including the hue.
        /// </summary>
        /// <returns>BasherShield object (see below)</returns>
        private BasherShield GetShieldData()
        {
            BasherShield basherShield = new BasherShield();
            Item shield = Player.GetItemOnLayer("LeftHand");

            if (shield != null)
            {
                basherShield.ItemId = shield.ItemID;
                basherShield.Name = shield.Name;
                basherShield.Hue = shield.Hue;

                string[] durability = shield.Properties.Where(x => x.Number == 1060639).First().ToString().Split(' ', '/');
                basherShield.Durability = Convert.ToInt32(durability[1]);
                basherShield.MaxDurability = Convert.ToInt32(durability[4]);
            }

            return basherShield;
        }


        private int GetStatusHue(string spell)
        {
            switch (spell)
            {
                case "CW":
                    return (UseConsecrateWeapon) ? _green : _red;

                case "DF":
                    return (UseDivineFury) ? _green : _red;

                case "Blues?":
                    return (TargetBlues) ? _green : _red;

                case "EOO":
                    return (UseEnemyOfOne) ? _green : _red;

                default:
                    return 0;
            }
        }



        private bool IsEOOTarget(Mobile target)
        {
            List<string> eooList = _eooTargets.ConvertAll(x => x.ToLower());

            return (eooList.Contains(target.Name.ToLower())) ? true : false;
        }




        /// <summary>
        /// The main entry point.
        /// </summary>
        public void Run()
        {
            StartUp();
            Player.WeaponClearSA();
            Journal journal = new Journal();

            UpdateGump();

            while (true)
            {
                if (!IsPlayerMoving())
                {
                    BreakParalysis();
                    CureBloodOath();
                    BankGold();

                    Gumps.GumpData reply = Gumps.GetGumpData(_gumpId);

                    switch (reply.buttonid)
                    {
                        case 1:
                            UseConsecrateWeapon ^= true;
                            UpdateGump();
                            Misc.Pause(ParseDelay);
                            continue;

                        case 2:
                            UseDivineFury ^= true;
                            UpdateGump();
                            Misc.Pause(ParseDelay);
                            continue;

                        case 3:
                            TargetBlues ^= true;
                            UpdateGump();
                            Misc.Pause(ParseDelay);
                            continue;

                        case 4:
                            UseEnemyOfOne ^= true;
                            UpdateGump();
                            Misc.Pause(ParseDelay);
                            continue;

                    }

                    Mobile target = GenerateTargetList().FirstOrDefault();
                    if (target != null)
                    {
                        if (UseConsecrateWeapon && Player.Mana >=  Convert.ToInt32(Math.Ceiling(10 * GetLMCFactor())))
                        {
                            if (!Player.BuffsExist("Consecrate Weapon"))
                            {
                                Spells.CastChivalry("Consecrate Weapon");
                                Misc.Pause(GetSpellDelay());
                            }
                        }

                        if (UseDivineFury && Player.Mana >=  Convert.ToInt32(Math.Ceiling(15 * GetLMCFactor())))
                        {
                            if (!Player.BuffsExist("Divine Fury"))
                            {
                                Spells.CastChivalry("Divine Fury");
                                Misc.Pause(GetSpellDelay());
                            }
                        }

                        if (UseEnemyOfOne && GenerateTargetList().Count == 1 && IsEOOTarget(target) && !Player.BuffsExist("Enemy Of One"))
                        {
                            Spells.CastChivalry("Enemy Of One");
                            Misc.Pause(GetSpellDelay());
                        }

                        if (UseEnemyOfOne && GenerateTargetList().Count > 1 && IsEOOTarget(target) && Player.BuffsExist("Enemy Of One"))
                        {
                            Spells.CastChivalry("Enemy Of One");
                            Misc.Pause(GetSpellDelay());
                        }

                        AttackTarget(target);
                    }

                    if (journal.Search("Repairing"))
                    {
                        journal.Clear();
                        UpdateGump();
                    }
                    
                    Misc.Pause(ParseDelay);
                }
            }
        }
    }


    public class BasherWeapon
    {
        public int ItemId { get; set; }
        public string Name { get; set; }
        public double Speed { get; set; }
        public int MinDamage { get; set; }
        public int MaxDamage { get; set; }

        public BasherWeapon(int itemId, string name, double speed, int minDamage, int maxDamage)
        {
            ItemId = itemId;
            Name = name;
            Speed = speed;
            MinDamage = minDamage;
            MaxDamage = maxDamage;
        }
    }


    public class BasherShield
    {
        public int ItemId { get; set; }
        public string Name { get; set; }
        public int Hue { get; set; }
        public int Durability { get; set; }
        public int MaxDurability { get; set; }

        public BasherShield(int itemId, string name, int hue, int durability, int maxDurability)
        {
            ItemId = itemId;
            Name = name;
            Hue = hue;
            Durability = durability;
            MaxDurability = maxDurability;
        }

        public BasherShield() {}
    }


    public class SlayerType
    {
        public int ServUOId { get; set; }
        public string Name { get; set; }

        public SlayerType(int servUOId, string name)
        {
            ServUOId = servUOId;
            Name = name;
        }
    }

    public class PriorityTarget
    {
        public string Name { get; set; }
        public List<SlayerType> SlayerType { get; set; }

        public PriorityTarget(string name, List<SlayerType> slayer)
        {
            Name = name;
            SlayerType = slayer;
        }
    }
}