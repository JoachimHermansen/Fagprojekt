import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import re


def lightcurve(scw, chwidth, xCoor, yCoor, filename):
    interval = np.array([])  # Array of the interval of a SCW
    imgpoly = np.array([])  # Array of IMAGE;polygon line numbers
    chmax = np.array([])  # Array of chmax values
    xTotal = np.array([])
    yTotal = np.array([])
    x = 0  # integer counting the number of IMAGE;polygon instances

    # Open file and read the lines
    with open(os.path.join("ArchiveFiles/", filename), 'r') as fin:
        lines = fin.readlines()

    for i in range(len(lines)):  # Finds interval of the entire SCW
        if "BegiN " in lines[i] and str(scw) in lines[i]:
            interval = np.append(interval, int(i))
        elif "EnD " in lines[i] and str(scw) in lines[i]:
            interval = np.append(interval, int(i))
            break

    ''' Loops through the SCW and find all instances of IMAGE;polygon 
    and append the line numbers '''
    for i in range(int(interval[0]), int(interval[1])):
        if ("IMAGE;polygon" in lines[i]) and x >= 1:  # Only append from the second instance and after
            imgpoly = np.append(imgpoly, i)
            x += 1
        elif ("IMAGE;polygon" in lines[i]) and x == 0:
            x += 1

    ''' Loops through the SCW and find all chmax values and append them'''
    for i in range(int(interval[0]), int(interval[1])):
        if str(xCoor) in lines[i] and str(yCoor) in lines[i]:
            s = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", lines[i+1])
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

        if len(weighted) == 0:
            pass
        else:
            n = np.argmax(weighted)  # Position of highest value of weighted (The best imgpoly fit)
            poly = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*?\d*(?:[eE][-+]?\d+)?", lines[int(imgpoly[n])])

            xPlot = np.asarray(poly[::2]).astype(int)  # All even positions as integers
            yPlot = np.asarray(poly[1::2]).astype(int)  # All uneven positions as integers

            xPlot = [x * chwidth for x in xPlot]  # Changing channels to seconds
            yPlot = [(y - yPlot[0])/20 for y in yPlot]  # Changing y-values to standard deviation

            if len(xTotal) == 0:
                xTotal = np.append(xTotal, xPlot)
                yTotal = np.append(yTotal, yPlot)
            else:
                xTotal = np.vstack((xTotal, xPlot))
                yTotal = np.vstack((yTotal, yPlot))

    return xTotal, yTotal, chmax



