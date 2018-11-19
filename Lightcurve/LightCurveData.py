import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import re

directory = "E03/"
filename = "gbJ1_B_4_E03.txt"

chwidth = 4.0
scw = "030900660010"  # Remember to include the first zero
interval = np.array([])
imgpoly = np.array([])
chmax = np.array([])


with open(os.path.join("ArchiveFiles/" + directory, filename), 'r') as fin:  # Open file and read the lines
    lines = fin.readlines()

for i in range(len(lines)):  # Finds interval of SCW
    if "BegiN " + scw in lines[i]:
        interval = np.append(interval, int(i))
    elif "EnD " + scw in lines[i]:
        interval = np.append(interval, int(i))
        break
    else:
        pass

x = 0
for i in range(int(interval[0]), int(interval[1])):  # Finds all relevant plot points
    if ("IMAGE;polygon" in lines[i]) and x >= 1:
        imgpoly = np.append(imgpoly, i)
        x += 1
    elif ("IMAGE;polygon" in lines[i]) and x >= 0:
        x += 1

for i in range(int(interval[0]), int(interval[1])):
    if "chmax:" in lines[i]:
        s = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", lines[i])
        chmax = np.append(chmax, int(s[10]))


for i in range(len(chmax)):
    top = round(((chmax[i]*4)/chwidth))
    weighted = np.array([])

    for j in range(len(imgpoly)):
        poly = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*?\d*(?:[eE][-+]?\d+)?", lines[int(imgpoly[j])])
        offset = 256 - ((int(poly[-2]) - int(poly[0]))/2)
        xSpot = round(top + offset)  # x-coordinate
        xPlot = np.asarray(poly[::2]).astype(int)  # All even positions
        yPlot = np.asarray(poly[1::2]).astype(int)  # uneven positions

        for k in range(len(xPlot)):
            if xPlot[k] == xSpot:
                weighted = np.append(weighted, yPlot[k-1]+yPlot[k]+yPlot[k+1]-(3*yPlot[0]))
                break

    n = np.argmax(weighted)  # Position of highest value of weighted (The best imgpoly fit)
    poly = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*?\d*(?:[eE][-+]?\d+)?", lines[int(imgpoly[n])])

    xPlot = np.asarray(poly[::2]).astype(int)  # All even positions
    yPlot = np.asarray(poly[1::2]).astype(int)

    plt.plot(xPlot, yPlot, linestyle="-", color="b")
    plt.axhline(y=yPlot[0], linestyle="-", color="r")
    plt.grid(True)
    plt.title("scw " + str(scw) + ": " + "chmax " + str(chmax[i]) + " , best imgpoly " + str(n),
              fontsize=16)
    plt.xlabel("x-akse", fontsize=18)
    plt.ylabel("y-akse", fontsize=18)
    plt.show()

    # Jeg skal finde toppunktets x-koordinat. Herefter skal jeg kigge på det x-koordinat i samtlige
    # imgpoly. Jeg summer for punktet, plus -1 og +1 i forhold til koordinaten.
    # Herefter sammenligner jeg og ser hvilket punkt har den højeste vægtede sum.




