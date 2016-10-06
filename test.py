badlist = ["rape\n", "kill\n"]
string = "love\nrape\nfuck\nkill\neat"
for bad in badlist: string=string.replace(bad, "")
print string
