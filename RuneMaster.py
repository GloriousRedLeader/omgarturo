# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-09-04
# Use at your own risk. 

import clr
clr.AddReference ('System.Windows.Forms')
clr.AddReference('System.Drawing')
import re
from System.Drawing import Color, Font, FontStyle, FontFamily
from System.Drawing import Point
from System.Windows.Forms import TextBox, Keys, KeyPressEventHandler, DataGridView, DataGridViewHeaderBorderStyle
from System.Windows.Forms import DataGridViewCellBorderStyle, ColumnStyle, SizeType, RowStyle, GroupBox
from System.Windows import Forms
from System.Collections.Generic import List

from math import ceil
import sys

# Permanent Atlas Gump with juicy buttons

RUNIC_ATLAS_SERIAL = 0x4064F6A5
RUNIC_ATLAS_GUMP_ID = 0x1f2


RUNEBOOK_GUMP_ID =  0x59

OUR_GUMP_ID = 1239862390


class Book:
    def __init__(self, serial, graphic, hue, name):
        self.serial = serial
        self.graphic = graphic
        self.hue = hue
        self.name = name
        #self.runes = []
        self.left = []
        self.right = []
        
    def getRuneCountForColumn(self):
        return len(self.left)
        
    #def getXYCoordsForRuneEntry(self, runeEntry):
    #    return False
    
        
class Rune:
    #def __init__(self, buttonid, name, globalindex, localindex, type, bookSerial):
    #def __init__(self, runeIndex, buttonid, name, bookSerial, bookGraphic, bookHue):
    def __init__(self, runebookButtonId, name, book):
        self.runebookButtonId = runebookButtonId
        self.name = name
        self.book = book
    
        
        
    #def getPage(self):
    #    return ceil(self.localindex / 8)
RUNIC_ATLAS_GRAPHIC_ID = 0x9C16
RUNEBOOK_GRAPHIC_ID = 0x22C5

def get_runes():
    runes = []
    allRunes = []
    allBooks = []
    
    magerySkill = Player.GetSkillValue("Magery")
    chivalrySkill = Player.GetSkillValue("Chivalry")
    
    books = Items.FindAllByID(RUNIC_ATLAS_GRAPHIC_ID, -1, Player.Backpack.Serial, 0)
    for book in books:
    #book = Items.FindBySerial(bookSerial)
    
        Items.UseItem(book.Serial)
        Gumps.WaitForGump(RUNIC_ATLAS_GUMP_ID, 3000)

        data = Gumps.GetGumpData(RUNIC_ATLAS_GUMP_ID).gumpData[1:]
        #data = [gd  for gd in data if "center" not in gd and gd != "Empty"]
        #for gd in data:
        #    print("OFFICIAL 1: ", gd)
            
        Gumps.SendAction(RUNIC_ATLAS_GUMP_ID, 1150)
        Gumps.WaitForGump(RUNIC_ATLAS_GUMP_ID, 3000)
        data.AddRange(Gumps.GetGumpData(RUNIC_ATLAS_GUMP_ID).gumpData[1:])

        Gumps.SendAction(RUNIC_ATLAS_GUMP_ID, 1150)
        Gumps.WaitForGump(RUNIC_ATLAS_GUMP_ID, 3000)
        data.AddRange(Gumps.GetGumpData(RUNIC_ATLAS_GUMP_ID).gumpData[1:])

        runicAtlas = Book( book.Serial, book.Graphics, book.Hue, "fucker")
        
        data = [gd  for gd in data if "center" not in gd and gd != "Empty"]  
        
        i = 0
        for gd in data:
            rune =  Rune(100 + i, gd, runicAtlas)
            allRunes.append(rune)
            if i + 1 > ceil(len(data) / 2):
                runicAtlas.right.append(rune)
            else:
                runicAtlas.left.append(rune)
            i = i + 1
            
        allBooks.append(runicAtlas)
 
            
        Gumps.CloseGump(RUNIC_ATLAS_GUMP_ID)        
            
    books = Items.FindAllByID(RUNEBOOK_GRAPHIC_ID, -1, Player.Backpack.Serial, 0)
    for book in books:
        print(book.Serial)
        print("Runebook")
        Items.UseItem(book)
        Gumps.WaitForGump(RUNEBOOK_GUMP_ID,3300)
        #gumpData = Gumps.GetGumpData(RUNEBOOK_GUMP_ID).text[2:]
        data = Gumps.GetGumpData(RUNEBOOK_GUMP_ID).gumpData[4:20]
        
        data = [gd  for gd in data if "center" not in gd and gd != "Empty"]  
        
        runeBook = Book( book.Serial, book.Graphics, book.Hue, "regularcrane")
        allBooks.append(runeBook)
        i = 0
        for gd in data:
            # Magery Rune 1 = 50
            # Magery Rune 2 = 51
            # Chivalry Rune 1 = 75
            # Chivalry Rune 2 = 76
            # Defaults to magery if both magery and chivalry are 0 (pure necro)
            buttonId = 75 + i if chivalrySkill > magerySkill else 50 + i        
            
            rune = Rune(buttonId, gd, runeBook)
            allRunes.append(rune)
            if i + 1 > ceil(len(data) / 2):
                runeBook.right.append(rune)
            else:
                runeBook.left.append(rune)
            i = i + 1

        Gumps.CloseGump(RUNEBOOK_GUMP_ID)
    return allRunes, allBooks
    
    
runes, books = get_runes()

def render_gump(runes, books):
    LINE_HEIGHT = 25
    PAGE_WIDTH = 165
    TITLE_PADDING_TOP = 15
    LINE_TOP_PADDING = 15
    LINE_LEFT_PADDING = 15
    BOOK_PADDING = 25
    
    atlasGump = Gumps.CreateGump(True, True, True, False)
    atlasGump.buttonid = -1
    atlasGump.gumpId   = OUR_GUMP_ID
    atlasGump.serial   = Player.Serial
    atlasGump.x        = 600
    atlasGump.y        = 100
    
    gumpWidth = (PAGE_WIDTH * 2) + 10
    gumpHeight = TITLE_PADDING_TOP + 10
    for book in books:
        gumpHeight = gumpHeight + (book.getRuneCountForColumn() * LINE_HEIGHT) +  (BOOK_PADDING * 2)
    
    y = TITLE_PADDING_TOP
    Gumps.AddBackground(atlasGump, 0, 0, gumpWidth, gumpHeight, 3500)
    Gumps.AddLabel(atlasGump, 120, y, 1258, "Runemaster 5000")      

    i = 1
    y = y + BOOK_PADDING 
    for book in books:
        print("iterating book", book.serial)
        print("Runes left: ", len(book.left))
        print("Runes right: ", len(book.right))
        
        Gumps.AddLabel(atlasGump, 55, y, 1258, book.name)  
        Gumps.AddItem( atlasGump, 10, y - 3, book.graphic, book.hue)
        
        y = y + BOOK_PADDING 
        for index, rune in enumerate(book.left):
            x = LINE_LEFT_PADDING
            Gumps.AddButton(atlasGump, x, y + (LINE_HEIGHT * index), 0x4BA, 0x4B9, i, 1, 1)
            Gumps.AddLabel(atlasGump, x + 25, y + (LINE_HEIGHT * index), 77, rune.name[:20])
            print("x =", x, " y =", y + (LINE_HEIGHT * index), "gd =", rune.name, "buttonid =", i)
            i = i + 1
        for index, rune in enumerate(book.right):
            x = LINE_LEFT_PADDING + PAGE_WIDTH
            Gumps.AddButton(atlasGump, x, y + (LINE_HEIGHT * index), 0x4BA, 0x4B9, i, 1, 1)
            Gumps.AddLabel(atlasGump, x + 25, y + (LINE_HEIGHT * index), 77, rune.name[:20])
            print("x =", x, " y =", y + (LINE_HEIGHT * index), "gd =", rune.name, "buttonid =", i)
            i = i + 1
        
        y = y + (book.getRuneCountForColumn() * LINE_HEIGHT) + 15
        

          
    Gumps.CloseGump(OUR_GUMP_ID)
    Gumps.SendGump(atlasGump, 0, 0)

def recall_or_sacred_journey(runeButtonId, runes, books):
    rune = runes[runeButtonId - 1]
    Items.UseItem(rune.book.serial)
    if rune.book.graphic == RUNEBOOK_GRAPHIC_ID:
        Gumps.WaitForGump(RUNEBOOK_GUMP_ID, 3000)
        Gumps.SendAction(RUNEBOOK_GUMP_ID, rune.runebookButtonId)
    else:
        Gumps.WaitForGump(RUNIC_ATLAS_GUMP_ID, 3000)
        Gumps.SendAction(RUNIC_ATLAS_GUMP_ID, rune.runebookButtonId)
        Gumps.WaitForGump(RUNIC_ATLAS_GUMP_ID, 3000)
        Gumps.SendAction(RUNIC_ATLAS_GUMP_ID, 4)


render_gump(runes, books)

while True:
    

    gd = Gumps.GetGumpData(OUR_GUMP_ID)
    
    if gd is not None and gd.buttonid > 0:
        # First button is 100
        # Page 2 first button is 116
        # Recall is 4
        print("Recall to rune number: ", gd.buttonid)
        
        recall_or_sacred_journey(gd.buttonid,runes,books)
        
        # Sets button id back to -1 so we exit this nonsense
        render_gump(runes, books)
        
    elif gd is not None and gd.buttonid == 0:
        print("Exiting")
        # NO idea whatshappening here. After script exits
        # runebooks cant be dragged...
        #Gumps.CloseGump(RUNEBOOK_GUMP_ID)
        #Gumps.CloseGump(RUNIC_ATLAS_GUMP_ID)
        Gumps.SendAction(RUNEBOOK_GUMP_ID,0)
        Gumps.SendAction(RUNIC_ATLAS_GUMP_ID,0)
        break
    
    Misc.Pause(250)    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
sys.exit()

#OUR_GUMP_ID = 1239862391
Items.UseItem(RUNIC_ATLAS_SERIAL)
Gumps.WaitForGump(RUNIC_ATLAS_GUMP_ID, 3000)

data = Gumps.GetGumpData(RUNIC_ATLAS_GUMP_ID).gumpData[1:]
#data = [gd  for gd in data if "center" not in gd and gd != "Empty"]
#for gd in data:
#    print("OFFICIAL 1: ", gd)
    
Gumps.SendAction(RUNIC_ATLAS_GUMP_ID, 1150)
Gumps.WaitForGump(RUNIC_ATLAS_GUMP_ID, 3000)
data.AddRange(Gumps.GetGumpData(RUNIC_ATLAS_GUMP_ID).gumpData[1:])

Gumps.SendAction(RUNIC_ATLAS_GUMP_ID, 1150)
Gumps.WaitForGump(RUNIC_ATLAS_GUMP_ID, 3000)
data.AddRange(Gumps.GetGumpData(RUNIC_ATLAS_GUMP_ID).gumpData[1:])

data = [gd  for gd in data if "center" not in gd and gd != "Empty"]    
for gd in data:
    print("OFFICIAL: ", gd)
    
pageCount = ceil(len(gd) / 8)
sectionCount = ceil(pageCount / 2)
print("Pages, ", pageCount)
print("Sections: ", sectionCount)
    
Gumps.CloseGump(RUNIC_ATLAS_GUMP_ID)
    
#atlasGump = Gumps.CreateGump(True, True, True, False)

#atlasGump.buttonid = -1
#atlasGump.gumpId   = OUR_GUMP_ID
#atlasGump.serial   = Player.Serial
#atlasGump.x        = 600
#atlasGump.y        = 100

#Gumps.AddBackground(atlasGump, 0, 0, 450, 700, 3500)
#Gumps.AddLabel(atlasGump, 30, 15, 1258, "fooBasher Status Gump")

#Gumps.AddButton(gd,x,y,normalID,pressedID,buttonID,type,param)
#Gumps.AddLabel(gd,x,y,hue,text)
#i = 1
#for gd in data:
#    x = 10
#    y = 30 * i
#    Gumps.AddButton(atlasGump, x, y, 0x4BA, 0x4B9, i, 1, 1)
#    Gumps.AddLabel(atlasGump, x + 25, y, 77, gd)
#    i = i + 1

#Gumps.AddButton(atlasGump, 360, 46, 0x4BA, 0x4B9, 3, 1, 1)
#Gumps.AddLabel(atlasGump, 380, 45, 77, "Blues?")
#Gumps.AddButton(atlasGump, 15, 15, normalID,pressedID,buttonID,type,param)



#print(atlasGump)
Gumps.CloseGump(OUR_GUMP_ID)
#Gumps.SendGump(atlasGump, 0, 0)


# Uses recall or sacred journey depending on skill
def recall_or_sacred_journey(runeButtonId):
    magerySkill = Player.GetSkillValue("Magery")
    chivalrySkill = Player.GetSkillValue("Chivalry")
    buttonid = 7 if chivalrySkill > magerySkill else 4
    
    Items.UseItem(RUNIC_ATLAS_SERIAL)
    Gumps.WaitForGump(RUNIC_ATLAS_GUMP_ID, 3000)
    Gumps.SendAction(RUNIC_ATLAS_GUMP_ID, runeButtonId)
    Gumps.WaitForGump(RUNIC_ATLAS_GUMP_ID, 3000)
    Gumps.SendAction(RUNIC_ATLAS_GUMP_ID, buttonid)

def render_gump():
    
    LINE_HEIGHT = 25
    PAGE_WIDTH = 165
    
    TITLE_PADDING_BOTTOM = 15
    
    LINE_TOP_PADDING = 15
    LINE_LEFT_PADDING = 15
    
    atlasGump = Gumps.CreateGump(True, True, True, False)
    atlasGump.buttonid = -1
    atlasGump.gumpId   = OUR_GUMP_ID
    atlasGump.serial   = Player.Serial
    atlasGump.x        = 600
    atlasGump.y        = 100
    
    gumpWidth = (PAGE_WIDTH * 2) + 10
    gumpHeight = (LINE_HEIGHT * 8 * sectionCount) + TITLE_PADDING_BOTTOM + 50

    
    Gumps.AddBackground(atlasGump, 0, 0, gumpWidth, gumpHeight, 3500)
    Gumps.AddLabel(atlasGump, 120, 10, 1258, "Runemaster 5000")    

    i = 1
    for gd in data:
        
        page = ceil(i / 8)
        section = ceil(i / 16)
        
        x = LINE_LEFT_PADDING if page % 2 != 0 else PAGE_WIDTH + LINE_LEFT_PADDING
        #y = i * LINE_HEIGHT
        #y = (i * LINE_HEIGHT) - (section * LINE_HEIGHT) if page % 2 != 0 else (i * LINE_HEIGHT)
        y = (i * LINE_HEIGHT) - (section * 8 * LINE_HEIGHT) + TITLE_PADDING_BOTTOM if page % 2 == 0 else (i * LINE_HEIGHT) + TITLE_PADDING_BOTTOM
        print("x =", x, " y =", y, "page =", page, " section =", section, "gd =", gd)
        
        
        Gumps.AddButton(atlasGump, x, y, 0x4BA, 0x4B9, i, 1, 1)
        Gumps.AddLabel(atlasGump, x + 25, y, 77, gd)
        i = i + 1

    Gumps.CloseGump(OUR_GUMP_ID)
    Gumps.SendGump(atlasGump, 0, 0)



render_gump()
while True:
    

    gd = Gumps.GetGumpData(OUR_GUMP_ID)
    
    if gd is not None and gd.buttonid > 0:
        # First button is 100
        # Page 2 first button is 116
        
        # Recall is 4
        print("Recall to rune number: ", gd.buttonid)
        
        recall_or_sacred_journey(gd.buttonid)
        
        # Sets button id back to -1 so we exit this nonsense
        render_gump()
        
    elif gd is not None and gd.buttonid == 0:
        print("Exiting")
        break
    
    Misc.Pause(250)



