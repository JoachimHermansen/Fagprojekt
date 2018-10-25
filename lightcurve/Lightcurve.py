#Light curve
#I made this...
import numpy as np
import pandas as pd
import re

filename = "ArchiveFiles/gbJ1_A_4_E03.reg.txt"
x = 0
N = 10 # Antal linjer

search = ["fk5;", "EnD"]
dfcolums = ["SCW", "coordinate1", "coordinate2", "Name",
            "ObsTime", "time chans start", "time chans stop", "Significance"]


with open(filename) as fin: #Åbner filen og indlæser linjerne
    lines = fin.readlines()

df = pd.DataFrame(np.zeros((N, len(dfcolums))), columns=dfcolums)

''' Gennemgår linjerne for data '''

m = 0
n = 0

for i in range(len(lines)):
    if x < N:
        if search[0] in lines[i]: # Leder efter fk5 i linjerne
            coordinates = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", lines[i])
            info = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", lines[i + 1])

            # Tildeler koordinaterne til deres plads i DF
            df.iloc[n, 1] = coordinates[1]
            df.iloc[n, 2] = coordinates[2]

            # Tildeler yderligere info til deres plads i DF
            df.iloc[n, 4] = info[3] # obstime
            df.iloc[n, 5] = info[8] # time chans start
            df.iloc[n, 6] = info[9] # time chans stop
            df.iloc[n, 7] = info[7] # Significance
            n += 1

            j = i

            for j in range(i, len(lines)):
                if search[1] in lines[j]:
                    scw = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", lines[j])
                    df.iloc[m, 0] = scw[0]
                    m += 1
                    break
            x += 1


''' Sorter data (fjerner nul rækker) '''
df = df[(df.T != 0).any()]
lol =df.values.tolist()

newstuff = [40 , 60 , 20 , 10]

lol[0].append(newstuff)
#df.to_csv("ArchiveCSV/BurstArchive", sep='\t', encoding='utf-8', index=False)