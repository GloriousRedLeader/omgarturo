from System import Byte, Int32
from System import Int32
from System.Collections.Generic import List

# Main code
class IDOCScanner(object):
    global signs
    ignore = []
    fil = None
    signs = List[Int32]((3026, 2966, 2980, 2982, 2984, 2986, 2988, 2990, 2992, 2996, 2998, 3000, 3002, 3004, 3006, 3008, 3010, 3012, 3014, 3016, 3018, 3020, 3022, 3024, 3026, 3028, 3030, 3032, 3034, 3036, 3038, 3040, 3042, 3044, 3046, 3048, 3050, 3052, 3054, 3056, 3058, 3060, 3062, 3064, 3066, 3068, 3070, 3072, 3074, 3076, 3078, 3080, 3082, 3084, 3086, 3087, 2994))

    def __init__(self):
        self.fil = Items.Filter()
        self.fil.Enabled = True
        self.fil.OnGround = True
        self.fil.Movable = True
        self.fil.Graphics = signs
        self.fil.RangeMax = 30

    def Main(self):
        while True:
            Misc.Pause(100)
            items = Items.ApplyFilter(self.fil)
            for item in items:
                if item.Serial in self.ignore:
                    continue
                Items.WaitForProps(item, 3000)
                props = Items.GetPropStringList(item)
                if len(props) > 4:
                    condition = props[4].ToLower()
                    if 'danger' in condition:
                        Misc.SendMessage('[House : IDOC found.]', 38)
                        Misc.SendMessage('[House : IDOC found.]', 38)
                        Misc.SendMessage('[House : IDOC found.]', 38)
                        Player.HeadMessage(38, 'IDOC')
                        Player.HeadMessage(38, 'IDOC')
                        Player.HeadMessage(38, 'IDOC')
                        self.ignore.append(item.Serial)
                    elif 'greatly' in condition:
                        Misc.SendMessage('[House : Greatly found.]', 38)
                        self.ignore.append(item.Serial)
                    elif 'fairly' in condition:
                        self.ignore.append(item.Serial)
                    elif 'somewhat' in condition:
                        self.ignore.append(item.Serial)
                    elif 'slightly' in condition:
                        self.ignore.append(item.Serial)
                    elif 'new' in condition:
                        self.ignore.append(item.Serial)
                    else:
                        Misc.NoOperation()
                else:
                    self.ignore.append(item.Serial)
                    Misc.SendMessage(f'Item {item.Serial} skipped due to insufficient properties.', 55)
Misc.SendMessage('Starting IDOC Scanner...', 88)
IS = IDOCScanner()
IS.Main()
