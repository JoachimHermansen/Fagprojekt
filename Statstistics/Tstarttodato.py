import numpy as np
import pandas as pd
import datetime
import re
#import os

#zeropoint of time first measurement
t0 = datetime.datetime(2002, 12, 12, 9, 13, 36)
f = open('scwstartT.txt', 'r')
rawlines = f.readlines()
f.close()
#
N=len(rawlines)
Columns = ["Scw", "Date"]
df = pd.DataFrame(np.zeros((N, len(Columns))), columns=Columns)
for i in range(N):
    Y = rawlines[i].split(' ')
    Z = re.split('-|T|:',Y[1])
    seconds = abs((t0-datetime.datetime(int(Z[0]), int(Z[1]), int(Z[2]), int(Z[3]), int(Z[4]), int(Z[5]))).total_seconds())
    df.iloc[i,0]=int(Y[0])
    df.iloc[i,1]=seconds

df.to_csv("scwtosec.csv", sep=',')