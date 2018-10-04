import re
import numpy as np
import pandas
import os
#savename = "cm2koordinatorall.csv"
def dataimportcm2(filename,savename):
    #with open(savename,'a') as fd:
    
    n = 0
    N = 10
  #  findlist = ["x/y/r:","Effective Flux Collection Area"]
    data = np.zeros(4)
    with open(filename) as f:
        lines = f.readlines()
    for i in range(len(lines)):
        if n < N:
            if "PID(scw)" in lines[i]:
                m = i
                SCW = [None] * N
                M = 0
                while len(lines[m]) > 1:
                    if  "x/y/r:"  in lines[m]:
                        temp = np.zeros(4)
                        xynumbs = re.findall(r"-?\d+\.?\d*", lines[m])
                        temp[0] = xynumbs[0]
                        temp[1] = xynumbs[1]
                            
                    if  "Effective Flux Collection Area"  in lines[m]:
                        #print(lines[m])
                        xynumbs2 = re.findall(r"-?\d+\.?\d*", lines[m])
                        temp[2] = xynumbs2[len(xynumbs2)-2]
                        temp[3] = xynumbs2[len(xynumbs2)-1]
                        data = np.vstack((data,temp))
                    m += 1
                M += 1
               # n=n+1
    #fd.write(data[1:,:])
    np.savetxt(savename, data[1:,:], delimiter=",")

#print(data)
#print(SCW)