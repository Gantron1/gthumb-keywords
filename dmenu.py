from subprocess import Popen, PIPE, STDOUT
import Tkinter as tk
import tkMessageBox
import sys
import StringIO

root = tk.Tk()
root.withdraw()

sourcelist = []   # For holding all tags in a category
sellist = []      # What user has selected
#finalTags = ""    # sellist when done, converted to comma-delimited string
#sel = ""          # selection returned by dmenu

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
    global sellist

    f = open('/home/kanon/Dropbox/gthumb-tagger/media.tag', 'r')
    alltags = f.read()
    if(len(sellist) > 0):
        for already in sellist: 
            #print("Removing "+already+" from "+alltags+"\n")
            alltags = alltags.replace(already+"\n", '')

    pipe = Popen(["dmenu", "-a", "-c", "-y", "350"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    sel = pipe.communicate(input=alltags)[0]

    if (sel == "$\n"): pasteDone()
    # Starthere: test if strip does \n. Add & and *.
    else: 
        sellist.append(sel.strip())
    return;

#################
# THE MAIN CODE #
#################

# Get media type. Then go on. Also accepts $ for done.
getMedia()

# Get Image characteristics. Repeats until *, &, or $.
selectedTags = subprocess.Popen(("cat "
    "~/Dropbox/gthumb-tagger/image-char.tag "
    "| dmenu -n -y 360"), 
    shell=True, 
    stdout=subprocess.PIPE).stdout.read()

if (selectedTags == "$\n"): pasteDone()
#elif selectedTags == "*\n" : 
else: 
    finalTags += selectedTags

# Get cr-delimited list of keywords
while (selectedTags != "$\n"):
    # Get cr-delimited list of keywords from dmenu (usually just one)
    selectedTags = subprocess.Popen(("cat "
        "~/Dropbox/gthumb-tagger/media.tag "
        "~/Dropbox/gthumb-tagger/image-char.tag " 
        "~/Dropbox/gthumb-tagger/part-char.tag "
        "~/Dropbox/gthumb-tagger/participants.tag "
        "~/Dropbox/gthumb-tagger/top.tag "
        "| dmenu -n -y 360"), 
        shell=True, 
        stdout=subprocess.PIPE).stdout.read()
        
    # If ESC was pressed finish also
    if (selectedTags == ""): selectedTags = "done\n"
    
    finalTags += selectedTags

# Clean up keyword list
finalTags = finalTags.replace("done\n", "")
finalTags = finalTags.replace("\n", ", ")

#dialog.info_dialog("Window information", "'%s'" % finalTags)
pasteDone()

