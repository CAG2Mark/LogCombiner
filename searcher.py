import gzip
from os import walk
import os.path as path
import shutil

p_mcpath = "mcpath.txt"

if (path.exists(p_mcpath)):
    mc_path = open("mcpath.txt", "r").read()
    mc_path += "\\logs"
else:
    print("Please create a file called \"mcpath.txt\" with your Minecraft directory.")
    exit()

keywords = []
x = ""
while x != "confirm":
    if (len(x) > 2):
        keywords.append(x)
    x = input()

cutoff = int(input())
i = 0

found = {}
for k in keywords:
    found[k] = []

for (p, folder, files) in walk(mc_path, True):
    for file in reversed(files):
        # extract read then check
        if file[-3:] != ".gz": continue
        
        with gzip.open(path.join(p, file)) as f_out:
            with open("temp.txt", "wb") as f_in:
                shutil.copyfileobj(f_out, f_in)
            with open("temp.txt", "r") as f_read:
                s = f_read.read()
            
            out = ""
            for k in keywords:
                k_ = k.lower()
                for l in s.split("\n"):
                    l_ = l.lower()
                    indexes = []
                    ind = 0
                    while k_ in l_[ind:]:
                        ind = l_.index(k_, ind)
                        indexes.append(ind)
                        ind += len(k)

                    if len(indexes) == 0: continue

                    for i in indexes:
                        found[k].append((l + "\n" + " "*i + "^"*len(k) + "\n", file))
        
        i += 1
        if i == cutoff: break

for k in found.keys():
    print(k + ":")
    if len(found[k]) == 0: print("    None found\n")
    for t in found[k]:
        print("    [Found from: {}]".format(t[1]))
        print("    " + t[0].replace("\n", "\n    "))