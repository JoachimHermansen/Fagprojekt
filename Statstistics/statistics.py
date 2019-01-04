import pandas as pd
import numpy as np
file="SCW Check - BurstFound 4U 1323-62.csv"
convertfile="scwtosec.csv"
df=pd.read_csv(file)
N=len(df)

#len(df)
df.iloc[:,7]=0
converter=pd.read_csv(convertfile)
for j in range(N):
    for i in range(len(converter)):
        if int(converter.iloc[i,1]) == int(df.iloc[j,1]):
            df.iloc[j,7]=converter.iloc[i,2]

if df.empty:
    print("No data")
else:
    df.to_csv("withsec"+file, sep=',', encoding="utf-8" , index=False)



#2000130010
#23701060010
#2390011001
#23900120010
#100400140010
           