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

    def __init__(self, name, prev, next, autonext = 'next'):
        self.name = name
        self.prev = prev
        self.next = next   # Which menu is next
        self.autonext = autonext   #If 'sel' then next menu is vtag, else go to next menu
        self.tags = {}   # Dictionary. Format: vtag, atag. "vtag" is what the user sees in the menu (v means visual), and "atag" is what actually gets output. The "tag" can include codes to trigger additional functions.
        self.onlyonce = 0   # Set to true if the menu is to be accessed only once. 

#########################
# Set these parameters. #
#########################

# Folder with your category lists. (Must not have trailing /) Files must have .tag extension.
tagdir = "/home/kanon/Dropbox/gthumb-tagger"

# Names of your categories. Make a file with this name and .tag for the extension, and put in your keywords (tags). Format: one keyword per line. First thing on the line is the "vtag", meaning the tag that will appear in the menu. Follow it by a comma, and then put the "atag", which is the actual tag. If there is no comma and atag, then vtag will be used.
#catlist = [
#    'media',
#    'imgchar',
#    'parts',
#    'partchar',
#    'bodypos',
#    'fempos',
#    'malepos',
#    'common',
#    'scene',
#    'sexpos',
#    'var',
#    '1act',
#    '2act',
#    'actchar'
#]

categories = {}

categories['media'] = category('media', 'common', 'imgchar')
categories['imgchar'] = category('imgchar', 'common', 'parts')
categories['parts'] = category('parts', 'imgchar', 'partchar')
categories['partchar'] = category('partchar', 'common', 'fempos_onlyonce')
categories['fempos_onlyonce'] = category('fempos_onlyonce', 'common', 'bodypos')
categories['bodypos'] = category('bodypos', 'partchar', 'common', 'sel')
categories['fempos'] = category('fempos', 'partchar', 'common')
categories['malepos'] = category('malepos', 'partchar', 'common')
categories['common'] = category('common', 'bodypos', 'common', 'sel')
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
                    atag = vtag = pline[2]
                else: 
                    vtag = pline[0]
                    atag = pline[2]

                cat.tags[vtag] = atag
    return

# Paste selected tags string, and quit.
def pasteDone():
    finalTags = ", ".join(sellist)
    tkMessageBox.showwarning("Your title", "tags: "+finalTags)
    #dialog.info_dialog("Window information", "'%s'" % finalTags)
    exit(0)

# Show menu: Media
def getMedia():
    return

def showMenu(category):
    global sellist

    # Construct alltags, a string containing all tags in this category, except ones already in sellist
    if (category == 'bodypos') :
        alltags = "female\nmale\n&\n$\n"
    else:
        alltags = "*\n" # Start list with a *
        #f = open('{0}/{1}.tag'.format(, jcategory), 'r')
        alltags += f.read()
        if(len(sellist) > 0):
            for already in sellist: 
                #print("Removing "+already+" from "+alltags+"\n")
                alltags = alltags.replace(already+"\n", '')
        alltags += "&\n$\n"   # Append the & and $

    # Run dmenu and set sel to the result (will be nothing or one or more tags)
    pipe = Popen(["dmenu", "-a", "-c", "-y", "350"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    sel = pipe.communicate(input=alltags)[0]

    # Set next and previous
    if (category == "media"): next = "imgchar"; prev = "common"
    if (category == "imgchar"): next = "parts"; prev = "common"
    if (category == "parts"): next = "partchar"; prev = "imgchar"
    if (category == "partchar"): next = "bodypos"; prev = "imgchar"
    if (category == ""): next = ""; prev = ""
    if (category == ""): next = ""; prev = ""
    if (category == ""): next = ""; prev = ""
    if (category == ""): next = ""; prev = ""
    if (category == ""): next = ""; prev = ""
    if (category == ""): next = ""; prev = ""
    if (category == ""): next = ""; prev = ""
    if (category == ""): next = ""; prev = ""

    # Process dmenu's output 
    if (sel == "$\n"): pasteDone()         # $ = We're done. 
    elif (sel == "&\n") : getCommon()      # & = Go back
    elif (sel == "*\n") : getImageChar()   # * = Go forward
    elif (sel == ""): exit(0)     # ESC = Abort.
    else: 
        # Starthere: test if strip does \n.
        sellist.append(sel.strip())        # Add the tag to the list
    return

# Show menu: Image Characteristics
def getImageChar():
    global sellist

    # Construct alltags, a string containing all tags in this category
    alltags = "*\n" # Start list with a *
    f = open('/home/kanon/Dropbox/gthumb-tagger/image-char.tag', 'r')
    alltags += f.read()
    if(len(sellist) > 0):
        for already in sellist: 
            #print("Removing "+already+" from "+alltags+"\n")
            alltags = alltags.replace(already+"\n", '')
    alltags += "&\n*\n"   # Append the & and *

    # Run dmenu and set sel to the result (will be nothing or one or more tags)
    pipe = Popen(["dmenu", "-a", "-c", "-y", "350"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    sel = pipe.communicate(input=alltags)[0]

    # Process dmenu's output 
    if (sel == "$\n"): pasteDone()         # $ = We're done. 
    elif (sel == "&\n") : getCommon()      # & = Go back
    elif (sel == "*\n") : getImageChar()   # * = Go forward
    elif (sel == ""): exit(0)     # ESC = Abort.
    else: 
        # Starthere: test if strip does \n.
        sellist.append(sel.strip())        # Add the tag to the list
    return

# Show menu: Participants
def getParts():
    global sellist

    # Construct alltags, a string containing all tags in this category
    alltags = "*\n" # Start list with a *
    f = open('/home/kanon/Dropbox/gthumb-tagger/media.tag', 'r')
    alltags += f.read()
    if(len(sellist) > 0):
        for already in sellist: 
            #print("Removing "+already+" from "+alltags+"\n")
            alltags = alltags.replace(already+"\n", '')
    alltags += "&\n*\n"   # Append the & and *

    # Run dmenu and set sel to the result (will be nothing or one or more tags)
    pipe = Popen(["dmenu", "-a", "-c", "-y", "350"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    sel = pipe.communicate(input=alltags)[0]

    # Process dmenu's output 
    if (sel == "$\n"): pasteDone()         # $ = We're done. 
    elif (sel == "&\n") : getCommon()      # & = Go back
    elif (sel == "*\n") : getImageChar()   # * = Go forward
    elif (sel == ""): exit(0)     # ESC = Abort.
    else: 
        # Starthere: test if strip does \n.
        sellist.append(sel.strip())        # Add the tag to the list
    return

# Show menu: Participant Characteristics
def getPartChar():
    global sellist

    # Construct alltags, a string containing all tags in this category
    alltags = "*\n" # Start list with a *
    f = open('/home/kanon/Dropbox/gthumb-tagger/media.tag', 'r')
    alltags += f.read()
    if(len(sellist) > 0):
        for already in sellist: 
            #print("Removing "+already+" from "+alltags+"\n")
            alltags = alltags.replace(already+"\n", '')
    alltags += "&\n*\n"   # Append the & and *

    # Run dmenu and set sel to the result (will be nothing or one or more tags)
    pipe = Popen(["dmenu", "-a", "-c", "-y", "350"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    sel = pipe.communicate(input=alltags)[0]

    # Process dmenu's output 
    if (sel == "$\n"): pasteDone()         # $ = We're done. 
    elif (sel == "&\n") : getCommon()      # & = Go back
    elif (sel == "*\n") : getImageChar()   # * = Go forward
    elif (sel == ""): exit(0)     # ESC = Abort.
    else: 
        # Starthere: test if strip does \n.
        sellist.append(sel.strip())        # Add the tag to the list
    return

# Show menu: Body Position
def getBodyPos():
    global sellist

    # Construct alltags, a string containing all tags in this category
    alltags = "*\n" # Start list with a *
    f = open('/home/kanon/Dropbox/gthumb-tagger/media.tag', 'r')
    alltags += f.read()
    if(len(sellist) > 0):
        for already in sellist: 
            #print("Removing "+already+" from "+alltags+"\n")
            alltags = alltags.replace(already+"\n", '')
    alltags += "&\n*\n"   # Append the & and *

    # Run dmenu and set sel to the result (will be nothing or one or more tags)
    pipe = Popen(["dmenu", "-a", "-c", "-y", "350"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    sel = pipe.communicate(input=alltags)[0]

    # Process dmenu's output 
    if (sel == "$\n"): pasteDone()         # $ = We're done. 
    elif (sel == "&\n") : getCommon()      # & = Go back
    elif (sel == "*\n") : getImageChar()   # * = Go forward
    elif (sel == ""): exit(0)     # ESC = Abort.
    else: 
        # Starthere: test if strip does \n.
        sellist.append(sel.strip())        # Add the tag to the list
    return

# Show menu: Most common tags (amalgam of all menus)
def getCommon():
    global sellist

    # Construct alltags, a string containing all tags in this category
    alltags = "*\n" # Start list with a *
    f = open('/home/kanon/Dropbox/gthumb-tagger/media.tag', 'r')
    alltags += f.read()
    if(len(sellist) > 0):
        for already in sellist: 
            #print("Removing "+already+" from "+alltags+"\n")
            alltags = alltags.replace(already+"\n", '')
    alltags += "&\n*\n"   # Append the & and *

    # Run dmenu and set sel to the result (will be nothing or one or more tags)
    pipe = Popen(["dmenu", "-a", "-c", "-y", "350"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    sel = pipe.communicate(input=alltags)[0]

    # Process dmenu's output 
    if (sel == "$\n"): pasteDone()         # $ = We're done. 
    elif (sel == "&\n") : getCommon()      # & = Go back
    elif (sel == "*\n") : getImageChar()   # * = Go forward
    elif (sel == ""): exit(0)     # ESC = Abort.
    else: 
        # Starthere: test if strip does \n.
        sellist.append(sel.strip())        # Add the tag to the list
    return

# Still to do:
def getFemPos():
    return
def getMascPos():
    return
def getScene():
    return
def getSexPos():
    return
def getVar():
    return
def get1act():
    return
def get2act():
    return
def getActChar():
    return

#################
# THE MAIN CODE #
#################

fillcats()
print categories
exit

# Keep serving up menus until done.
options = {
    'media' : getMedia,
    'imgchar' : getImageChar,
    'parts' : getParts,
    'partchar' : getPartChar,
    'bodypos' : getBodyPos,
    'fempos' : getFemPos,
    'mascpos' : getMascPos,
    'common' : getCommon,
    'scene' : getScene,
    'sexpos' : getSexPos,
    'var' : getVar,
    '1act' : get1act,
    '2act' : get2act,
    'actchar' : getActChar
}

#options[next]()

getMedia()

# Get Image characteristics. Repeats until *, &, or $.
sel = subprocess.Popen(("cat "
    "~/Dropbox/gthumb-tagger/image-char.tag "
    "| dmenu -n -y 360"), 
    shell=True, 
    stdout=subprocess.PIPE).stdout.read()

if (sel == "$\n"): pasteDone()
#elif sel == "*\n" : 
else: 
    finalTags += sel

# Get cr-delimited list of keywords
while (sel != "$\n"):
    # Get cr-delimited list of keywords from dmenu (usually just one)
    sel = subprocess.Popen(("cat "
        "~/Dropbox/gthumb-tagger/media.tag "
        "~/Dropbox/gthumb-tagger/image-char.tag " 
        "~/Dropbox/gthumb-tagger/part-char.tag "
        "~/Dropbox/gthumb-tagger/participants.tag "
        "~/Dropbox/gthumb-tagger/top.tag "
        "| dmenu -n -y 360"), 
        shell=True, 
        stdout=subprocess.PIPE).stdout.read()
        
    # If ESC was pressed finish also (change this to abort instead)
    if (sel == ""): sel = "done\n"
    
    finalTags += sel

# Clean up keyword list
finalTags = finalTags.replace("done\n", "")
finalTags = finalTags.replace("\n", ", ")

#dialog.info_dialog("Window information", "'%s'" % finalTags)
pasteDone()

