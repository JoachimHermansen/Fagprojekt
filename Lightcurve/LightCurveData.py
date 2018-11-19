import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import re

directory = "E03/"
filename = "gbJ1_B_4_E03.txt"

chwidth = 4.0
scw = "030900660010"  # Remember to include the first zero


def lightcurve(scw, chwidth, filename, directory):
    interval = np.array([])  # Array of the interval of a SCW
    imgpoly = np.array([])  # Array of IMAGE;polygon line numbers
    chmax = np.array([])  # Array of chmax values
    x = 0  # integer counting the number of IMAGE;polygon instances

    # Open file and read the lines
    with open(os.path.join("ArchiveFiles/" + directory, filename), 'r') as fin:
        lines = fin.readlines()

    for i in range(len(lines)):  # Finds interval of the entire SCW
        if "BegiN " + scw in lines[i]:
            interval = np.append(interval, int(i))
        elif "EnD " + scw in lines[i]:
            interval = np.append(interval, int(i))
            break

    ''' Loops through the SCW and find all instances of IMAGE;polygon 
    and append the line numbers '''
    for i in range(int(interval[0]), int(interval[1])):
        if ("IMAGE;polygon" in lines[i]) and x >= 1:  # Only append from the second instance and after
            imgpoly = np.append(imgpoly, i)
            x += 1
        elif ("IMAGE;polygon" in lines[i]) and x >= 0:
            x += 1

    ''' Loops through the SCW and find all chmax values and append them'''
    for i in range(int(interval[0]), int(interval[1])):
        if "chmax:" in lines[i]:
            s = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", lines[i])
            chmax = np.append(chmax, int(s[10]))

    ''' Looking through each chmax value in the chmax-array '''
    for i in range(len(chmax)):
        top = round(((chmax[i]*4)/chwidth))
        weighted = np.array([])  # Array for all the weighted averages

        ''' Looking through each relevant line with IMAGE;polygon '''
        for j in range(len(imgpoly)):
            poly = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*?\d*(?:[eE][-+]?\d+)?", lines[int(imgpoly[j])])
            offset = 256 - ((int(poly[-2]) - int(poly[0]))/2)
            xSpot = round(top + offset)  # x-coordinate
            xPlot = np.asarray(poly[::2]).astype(int)  # All even positions
            yPlot = np.asarray(poly[1::2]).astype(int)  # uneven positions

            ''' Finding the weighted average of the curve data at the xSpot coordinate '''
            for k in range(len(xPlot)):
                if xPlot[k] == xSpot:  # If the x-value is equal to the calculated x-spot
                    # Append the weighted average
                    weighted = np.append(weighted, yPlot[k-1]+yPlot[k]+yPlot[k+1]-(3*yPlot[0]))
                    break

        n = np.argmax(weighted)  # Position of highest value of weighted (The best imgpoly fit)
        poly = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*?\d*(?:[eE][-+]?\d+)?", lines[int(imgpoly[n])])

        xPlot = np.asarray(poly[::2]).astype(int)  # All even positions as integers
        yPlot = np.asarray(poly[1::2]).astype(int)  # All uneven positions as integers

        ''' Creating a plot '''
        plt.plot(xPlot, yPlot, linestyle="-", color="b")
        plt.axhline(y=yPlot[0], linestyle="-", color="r")
        plt.grid(True)
        plt.title("scw " + str(scw) + ": " + "chmax " + str(chmax[i]) + " , best imgpoly " + str(n),
                  fontsize=16)
        plt.xlabel("x-axis", fontsize=18)
        plt.ylabel("y-axis", fontsize=18)
        plt.show()

    # Jeg skal finde toppunktets x-koordinat. Herefter skal jeg kigge på det x-koordinat i samtlige
    # imgpoly. Jeg summer for punktet, plus -1 og +1 i forhold til koordinaten.
    # Herefter sammenligner jeg og ser hvilket punkt har den højeste vægtede sum.


lightcurve(scw, chwidth, filename, directory)



