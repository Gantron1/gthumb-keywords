# TODO: 
# * Import existing tags from gthumb
# * Get back to image characters
# * Get rid of bodypos and just have fempos and malepos
# * Menus have titles, especially useful for fempos
# 
from subprocess import Popen, PIPE, STDOUT
import Tkinter as tk
import tkMessageBox
import sys
import StringIO

root = tk.Tk()
root.withdraw()

class category:
    # What user has selected
    sellist = []

    def __init__(self, name, prev, next, selnext = False):
        self.name = name
        self.prev = prev
        self.next = next   # Which menu is next
        self.selnext = selnext   #If True, then next menu is vtag, else go to next menu
        self.tags = []   # List of all tags in this category. Each item in self.tags is a pair (also a list): vtag and atag. "vtag" is what the user sees in the menu (v means visual), and "atag" is what actually gets output. The "tag" can include codes to trigger additional functions.
        self.onlyonce = False   # Set to true if the menu is to be accessed only once. 

#########################
# Set these parameters. #
#########################

# Folder with your category lists. (Must not have trailing /) Files must have .tag extension.
tagdir = "/home/kanon/Dropbox/gthumb-tagger"

# Names of your categories. Make a file with this name and .tag for the extension, and put in your keywords (tags). Format: one keyword per line. First thing on the line is the "vtag", meaning the tag that will appear in the menu. Follow it by a comma, and then put the "atag", which is the actual tag. If there is no comma and atag, then vtag will be used.
categories = {}

categories['media'] = category('media', 'common', 'imgchar')
categories['imgchar'] = category('imgchar', 'common', 'parts')
categories['parts'] = category('parts', 'imgchar', 'partchar')
categories['partchar'] = category('partchar', 'common', 'fempos_onlyonce')
categories['fempos_onlyonce'] = category('fempos_onlyonce', 'common', 'common')
categories['bodypos'] = category('bodypos', 'partchar', 'common', True)
categories['fempos'] = category('fempos', 'partchar', 'common')
categories['malepos'] = category('malepos', 'partchar', 'common')
categories['common'] = category('common', 'bodypos', 'common', True)
categories['scene'] = category('scene', 'common', 'common')
categories['sexpos'] = category('sexpos', 'common', 'common')
categories['var'] = category('var', 'common', 'common')
categories['1act'] = category('1act', 'common', 'common')
categories['2act'] = category('2act', 'common', 'common')
categories['actchar'] = category('actchar', 'common', 'common')

# Which category program begins with.
startcategory = 'media'

###############
# GLOBAL VARS #
###############

#sourcelist = []   # For holding all tags in a categoryDELME
#finalTags = ""    # DELMEsellist when done, converted to comma-delimited string
#sel = ""          # DELMEselection returned by dmenu

####################
# FUNCTION SECTION #
####################

# Read category files and fill (dictionary) categories with all category lists.
def fillcats():
    for cat in categories.values():
        with open('{0}/{1}.tag'.format(tagdir, cat.name), 'r') as f:
            for line in f:
                pline = line.rpartition(',')
                if (pline[0] == '' and pline[1] == ''):
                    atag = vtag = pline[2].strip()
                else: 
                    vtag = pline[0].strip()
                    atag = pline[2].strip()

                cat.tags.append([vtag, atag])
    return

# Paste selected tags string, and quit.
def pasteDone():
    finalTags = ", ".join(category.sellist)
    tkMessageBox.showwarning("Your title", "tags: "+finalTags)
    #dialog.info_dialog("Window information", "'%s'" % finalTags)
    exit(0)

def showMenu(catname):
    cat = categories[catname]
    commands = dict()
    tagdict = dict()

    # Remove already selected tags
    if(len(category.sellist) > 0):
        for already in category.sellist: 
            for tagpair in cat.tags:
                if (tagpair[0] == already):
                    cat.tags.remove(tagpair)

    # Construct \n delimited string of tags. Construct special commands.
    catstr = ''
    for tag in cat.tags:
        catstr += tag[0]+'\n'
        if (tag[1][:1] == '*'):   # If first char of atag is *, it's a special command
            commands[tag[0]] = tag[1]
        else:
            tagdict[tag[0]] = tag[1]   # Not a special command

    # Run dmenu and set sel to the result (will be nothing or one or more tags)
    pipe = Popen(["dmenu", "-a", "-c", "-y", "350"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    sel = pipe.communicate(input=catstr)[0]

    # Process dmenu's output 
    selarray = sel.split('\n')
    for sel in selarray:
        # If sel is a command execute it. Will skip tags if the command is in front of them, which would be a bug, but this should never happen.
        sel = sel.strip()
        if(sel in commands):
            if(commands[sel] == "*next"):
                return cat.next
            elif(commands[sel] == "*prev"):
                return cat.prev
            elif(commands[sel] == "*done"):
                pasteDone()
            elif(commands[sel][:6] == "*goto:"):
                return commands[sel][6:]
        else:
            if (sel == ""): exit(0)     # ESC = Abort.
            else: 
                category.sellist.append(tagdict[sel])        # Add the tag to the list
            return cat.next

    exit(0)   # Unreachable

#################
# THE MAIN CODE #
#################

fillcats()
menu = startcategory
while True:
    menu = showMenu(menu)

