from subprocess import Popen, PIPE, STDOUT
import Tkinter as tk
import tkMessageBox
import sys
import StringIO

root = tk.Tk()
root.withdraw()

#########################
# Set these parameters. #
#########################

# Folder with your category lists.
tagdir = "/home/kanon/Dropbox/gthumb-tagger"

# Program will look in tagdir folder for catlist items with the .tag extension. catlist holds your category lists.
catlist = [
    'media',
    'imgchar',
    'parts',
    'partchar',
    'bodypos',
    'fempos',
    'mascpos',
    'common',
    'scene',
    'sexpos',
    'var',
    '1act',
    '2act',
    'actchar'
]

# Menus (categories) to show only once, i.e. forward and back (& and *) skip them the second time around.
onlyonce = ['media', 'parts']

# Which category program begins with.
startcategory = 'media'

###############
# GLOBAL VARS #
###############

sellist = []      # What user has selected
#sourcelist = []   # For holding all tags in a categoryDELME
#finalTags = ""    # DELMEsellist when done, converted to comma-delimited string
#sel = ""          # DELMEselection returned by dmenu

####################
# FUNCTION SECTION #
####################

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
    if (category == 'bodypos') 
        alltags = "female\nmale\n&\n$\n"
    else
        alltags = "*\n" # Start list with a *
        f = open('{0}/{1}.tag'.format(, jcategory), 'r')
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

options[next]()

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

