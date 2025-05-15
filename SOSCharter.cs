using RazorEnhanced;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace fooScript
{
    public class SOSDataSet
    {
        public int XCoordinate;
        public int YCoordinate;
        public int Facet;
        public string FacetName;

        public SOSDataSet(List<Property> properties)
        {
            Property location = properties.Last();

            string source = location.ToString();
            string[] delimiters = new string[] { ": (", ", ", ")" };
            string[] result = source.Split(delimiters, StringSplitOptions.None);

            FacetName = result[0];

            switch (result[0])
            {
                case "Felucca":
                    Facet = 0;
                    break;

                case "Trammel":
                    Facet = 1;
                    break;

                case "Ilshenar":
                    Facet = 2;
                    break;

                case "Malas":
                    Facet = 3;
                    break;

                case "Tokuno":
                    Facet = 4;
                    break;

                case "Ter Mur":
                    Facet = 5;
                    break;
            }

            XCoordinate = Int32.Parse(result[1]);
            YCoordinate = Int32.Parse(result[2]);
        }
    }

    public class SOSCharter
    {
        // UO Dyeing hues
        protected int MessageColorGreen = 468;
        protected int MessageColorRed = 438;
        protected int MessageColorBlue = 490;
        protected int AncientSOSHue = 0x0481;

        // UO Item Ids
        protected int SOSBottle = 0x099F;
        protected int SOSScroll = 0x14EE;

        // The container serial for the SOS items
        protected int SOSContainer = 0x40DB059B;

        // List for writing data to file
        public List<SOSDataSet> Coordinates = new List<SOSDataSet>();

        // Path data for the map file
        //protected string FilePath = "M:\\Games\\UO\\TazUO\\Data\\Client\\userMarkers.usr";
        protected string FilePath = "F:\\games\\TazUO\\TazUO\\Data\\Client\\userMarkers.usr";
        


        public SOSDataSet ExtractCoordinates(int serial)
        {
            Item item = Items.FindBySerial(serial);
            List<Property> properties = item.Properties;
            
            SOSDataSet data = new SOSDataSet(properties);
            return data;
        }

        protected List<int> GetItemsById(int id, int source)
        {
            List<int> items = new List<int>();

            foreach (Item item in Items.FindBySerial(source).Contains)
            {
                if (item.ItemID == id && !items.Contains(item.Serial))
                {
                    items.Add(item.Serial);
                }
            }

            return items;
        }

        private void ParseSOSScrolls()
        {
            Misc.SendMessage("Scanning SOS container ...", MessageColorBlue);
            Items.WaitForContents(SOSContainer, 3000);

            List<int> bottles = GetItemsById(SOSBottle, SOSContainer);
            Misc.SendMessage($"{bottles.Count} SOS bottles found.", MessageColorBlue);
            Misc.SendMessage("Opening bottles ...", MessageColorBlue);

            foreach (int bottle in bottles)
            {
                Items.UseItem(bottle);
                Misc.Pause(100);
            }

            List<int> scrolls = GetItemsById(SOSScroll, SOSContainer);
            Misc.SendMessage($"{scrolls.Count} SOS scrolls found.", MessageColorBlue);
            Misc.SendMessage("Extracting coordinates from item properties ...", MessageColorBlue);

            List<SOSDataSet> coords = new List<SOSDataSet>();

            foreach (int scroll in scrolls)
            {
                coords.Add(ExtractCoordinates(scroll));
                Misc.Pause(100);
            }

            Misc.SendMessage($"{coords.Count} coordinate sets have been extracted.", MessageColorGreen);

            Coordinates = coords.OrderBy(s => s.Facet).ThenBy(s => s.XCoordinate).ThenBy(s => s.YCoordinate).ToList();
        }


        private void WriteCoordinates()
        {
            Misc.SendMessage("Checking marker file ...", MessageColorBlue);

            if (IsFileEmpty(FilePath))
            {
                Misc.SendMessage("Marker file is empty.", MessageColorGreen);
            }
            else
            {
                Misc.SendMessage("Marker file contains entries, overwriting ...", MessageColorRed);
            }

            string[] fileContents = File.ReadAllLines(FilePath);
            Misc.SendMessage($"Marker file contains {fileContents.Length} entries.", MessageColorBlue);

            using (StreamWriter sw = new StreamWriter(FilePath, append: true))
            {
                int written = 0;
                int duplicates = 0;

                foreach (SOSDataSet dataset in Coordinates)
                {
                    string data = $"{dataset.XCoordinate},{dataset.YCoordinate},{dataset.Facet},SOS ({dataset.FacetName} {dataset.XCoordinate} {dataset.YCoordinate}),,green,3";

                    if (!fileContents.Contains(data))
                    {
                        sw.WriteLine(data);
                        written++;
                    }
                    else
                    {
                        duplicates++;
                    }
                }

                Misc.SendMessage($"{written} entries written to map file, {duplicates} duplicates skipped.", MessageColorBlue);
            }
        }


        private static bool IsFileEmpty(string filename)
        {
            FileInfo info = new FileInfo(filename);

            if (info.Exists && info.Length < 6)
            {
                return true;
            }

            return false;
        }

        public void Run()
        {
            ParseSOSScrolls();
            WriteCoordinates();
        }
    }
}