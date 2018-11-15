import matplotlib    
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import re
from scipy.signal import argrelextrema
#def lightplot(koords,Scw,filename):
#lightplot("83.6315,  22.0141","004500300010","gbJ1_A_4_E03.reg.txt")
#017200790010 266.4929, -29.5171  266.4721, -30.1561 ?
koords="258.5824, -34.0465"
Scw="017200840010"
filename="gbJ1_A_4_E03.reg.txt"

Scwthere = 0
number = -1
with open(filename) as f:
    lines = f.readlines()
for i in range(len(lines)):
       
            
    if "BegiN {}".format(Scw) in lines[i]:
        start = i
        Scwthere = 1
    if "EnD {}".format(Scw) in lines[i]:
        end = i
if Scwthere == 0:
    print("{} not found".format(Scw))
else:
    tempn = 0
        #finder hvilken fk5; hvor lyskurven skal plottes
        #note: Tager kun den sidste lyskurve der opfylder kravene
       #  or ("fk5;point( {})".format(koords)) or ("fk5;point(  {})".format(koords)
    nrfk5=0
    tops=[]
    for i in range(start+1,end):
        
        if ("fk5;point({})".format(koords) in lines[i]) or ("fk5;point( {})".format(koords) in lines[i]) or ("fk5;point(  {})".format(koords) in lines[i]):
            
            nrfk5 += 1
            tops.append(nrfk5)
            #divideddata = lines[i].split(" ")
            #print(lines[i])
            templist = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", lines[i+1])
            
            tops.append(templist[10])
            
                    
        if "Channel Width:" in lines[i]:
            templist2 = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", lines[i])
            channelWidth=templist2[len(templist2)-1]
        nrplygon = 0
        if "IMAGE;polygon" in lines[i]:
            nrplygon += 1
            data =[]
            data.insert(tempm,re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", lines[i]))
            intlist =[int(i) for i in data[0]]
            y = np.asarray(intlist)[1::2]
            x = np.asarray(intlist)[::2]
            xofset = int(round(256-(x[len(y)-1]-x[0])/2))
            topsplot = np.zeros(len(tops))
            #print(((float(tops[0])*4/float(channelWidth))+xofset))
            for i in range(len(tops)):
                #beregning af hvor toppunkterne burde ligge.
                topsplot[i] = int(round((float(tops[i])*4/float(channelWidth))+xofset))
                #regner summen af punkterne omkring beregnet peak
                burstsign = y[int(topsplot[i]-x[0])]+y[int(topsplot[i]-x[0])-1]+y[int(topsplot[i]-x[0])+1]
            
            #burstcoords=x[np.r_[True, y[1:] < y[:-1]] & np.r_[y[:-1] < y[1:], True]]
            #bursthight1=[j-i for i, j in zip(y[:-1], y[1:])]
            #bursthight=[j-i for i, j in zip(bursthight1[:-1], bursthight1[1:])]
            #print(min(bursthight))
            #    print("2")
             #   number = tempn       
        #finder lyskurven til den fk5; vi vil have
        
        if number != -1:
            #print(3)
            tempm = 0      
            for i in range(start+1,end):
                if "IMAGE;polygon" in lines[i]:
                    tempm += 1
                    if tempm == number:
                      #  print(4)
                        #divideddata = lines[i].split(" ")
                        data = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", lines[i])
                        intlist =[int(i) for i in data]
                        array = np.asarray(intlist)
                        #print(array)
                        y = array[1::2]
                        x = array[::2]
                        import matplotlib.pyplot as plt
                        plt.plot(y, 'r')
                        plt.axis([0, max(x)*1.02, 0, max(y)*1.05])
                        plt.show()
            """
            
            
