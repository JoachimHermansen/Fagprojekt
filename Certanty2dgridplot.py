import pandas as pd
import numpy as np
import matplotlib as mp
from plot2dgrid import plot2dgrid
#filenavn : J1data.csv,J2data.csv
#gridplot("J1data.csv",100,"E03","1")
def gridplot(filename,N,plot,plotoption):
   # filename = filename.format(i)
    datain = pd.read_csv(filename) 
    data =np.copy(datain)
    
    #Grid dimention
    N=int(N/2)
    
    data[:,0] = (data[:,0]*N)/(225)
    data[:,1] = (data[:,1]*N)/(225)
    data[:,0] = np.around(data[:,0])
    data[:,1] = np.around(data[:,1])
    
    datalist = []
    
    
    
    for i in range(-N,N+1):
        listtemp = []
        for j in range(-N,N+1):
             temp = data[(data[:,0] == i) & (data[:,1] == j)][:,2:4]
             #print(temp)
             #matrix for data
             listtemp.append(temp)
             #add extra info like, amount of measurments, avg for each energy, unsertanty
        datalist.append(listtemp)
             
    
    nvals = np.zeros((2*N+1,2*N+1))
    for i in range(0,2*N+1):
        for j in range(0,2*N+1):
            nvals[i,j] = (len(datalist[i][j][:,0]))
    
    cm2avgE03vals = np.zeros((2*N+1,2*N+1))
    for i in range(0,2*N+1):
        for j in range(0,2*N+1):
            cm2avgE03vals[i,j] = np.sum(datalist[i][j][:,0])/(len(datalist[i][j][:,0]))
    
    cm2avgE04vals = np.zeros((2*N+1,2*N+1))
    for i in range(0,2*N+1):
        for j in range(0,2*N+1):
            cm2avgE04vals[i,j] = np.sum(datalist[i][j][:,1])/(len(datalist[i][j][:,1]))
    
    cm2stdE03vals = np.zeros((2*N+1,2*N+1))
    for i in range(0,2*N+1):
        for j in range(0,2*N+1):
            cm2stdE03vals[i,j] = np.std(datalist[i][j][:,0])
    cm2stdE04vals = np.zeros((2*N+1,2*N+1))
    for i in range(0,2*N+1):
        for j in range(0,2*N+1):
            cm2stdE04vals[i,j] = np.std(datalist[i][j][:,1])
    
    if plot == "n":
        plot2dgrid(nvals,plotoption)
    if plot == "E03":
        plot2dgrid(cm2avgE03vals,plotoption)
    if plot == "E04":
        plot2dgrid(cm2avgE04vals,plotoption)
    if plot == "stdE03":
        plot2dgrid(cm2stdE03vals,plotoption)
    if plot == "stdE04":
        plot2dgrid(cm2stdE04vals,plotoption)
