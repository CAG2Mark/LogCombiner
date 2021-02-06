import gzip
from os import walk
import os.path as path
import shutil

def bin_search(l, t):
    min = 0
    max = len(l) - 1
    while min <= max:
        m = (min + max) >> 1
        if l[m] == t: return m
        if t < l[m]: max = m - 1
        else: min = m + 1
    return

p_mcpath = "mcpath.txt"
p_added = "added.txt"
p_logs = "logs.log"

if (path.exists(p_mcpath)):
    mc_path = open("mcpath.txt", "r").read()
    mc_path += "\\logs"
else:
    print("Please create a file called \"mcpath.txt\" with your Minecraft directory.")
    exit()

f_added = open(p_added, "a")
f_logs = open(p_logs, "ab")

f_added_r = open(p_added,"r")
added = f_added_r.readlines()
added = [x.replace("\n", "").strip() for x in added]
f_added_r.close()

# sort
added.sort()

i = 0
d = []
# O(n log n)
for (p, folder, files) in walk(mc_path, True):
    for file in files:
        if ("debug" in file) or (".gz" not in file) or not bin_search(added, file.strip()) is None: continue
        #f_added.write(file + "\n")

        f_logs.write("[\"{}\"]\n".format(file).encode())
        # extract read then append
        with gzip.open(path.join(p, file)) as f_out:
            shutil.copyfileobj(f_out, f_logs)
        
        f_logs.write("\n\n".encode())
        i += 1

if i:
    print("Added {} new log file{} to logs.log!".format(i, "" if i == 1 else "s"))
else:
    print("No new log files found.")