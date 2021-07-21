import math
import sys
try:
    ogfile = sys.argv[1]
except IndexError:
    finished = input("No file dropped! Please drop the save file you want to update the checksum of\nPress enter to close")
    sys.exit()
decfile = []
cnsfile = []
with open(ogfile,"r+b") as file:
    while True:
        fileread = file.read(1)
        if len(fileread) < 1:
            break
        decdata = int.from_bytes(fileread, byteorder='little', signed=False)
        decfile.append(decdata)
    header = decfile[0:8]
    if header[0] == 9:
        header[0] = 1
    for a in range(0,8):
        decfile.pop(0)
    for a in range(0,math.trunc(len(decfile)/34)):
        cnsfile.append(decfile[0:34])
        del decfile[0:34]
    for a in range(0,len(cnsfile)):
        del cnsfile[a][15:31]
        del cnsfile[a][2]
        del cnsfile[a][0]
        if cnsfile[a][0] == 5:
            cnsfile[a][0] = 4
        elif cnsfile[a][0] == 4:
            cnsfile[a][0] = 3
    newformat = header
    for a in range(0,len(cnsfile)):
        newformat += cnsfile[a]
with open(ogfile+".conv","w+b") as file:
    file.write(bytearray(newformat))
finished = input(".cns file has been converted\nPress enter to close")
sys.exit()
