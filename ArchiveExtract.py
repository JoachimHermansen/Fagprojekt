import numpy as np
import pandas as pd
import re

filename = "ArchiveFiles/gbJ1_A_4_E03.txt"
x = 0
N = 100 # Antal linjer

search = ["fk5;", "EnD"]
archivecolums = ["SCW", "coordinate1", "coordinate2", "Name",
            "ObsTime", "time chans start", "time chans stop", "Significance"]


with open(filename) as fin: #Åbner filen og indlæser linjerne
    lines = fin.readlines()

archivedf = pd.DataFrame(np.zeros((N, len(archivecolums))), columns=archivecolums)

''' Gennemgår linjerne for data '''

m = 0
n = 0

for i in range(len(lines)):
    if x < N:
        if search[0] in lines[i]: # Leder efter fk5 i linjerne
            coordinates = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", lines[i])
            info = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", lines[i + 1])

            # Tildeler koordinaterne til deres plads i DF
            archivedf.iloc[n, 1] = coordinates[1]
            archivedf.iloc[n, 2] = coordinates[2]

            # Tildeler yderligere info til deres plads i DF
            archivedf.iloc[n, 4] = info[3] # obstime
            archivedf.iloc[n, 5] = info[8] # time chans start
            archivedf.iloc[n, 6] = info[9] # time chans stop
            archivedf.iloc[n, 7] = info[7] # Significance
            n += 1

            j = i

            for j in range(i, len(lines)):
                if search[1] in lines[j]:
                    scw = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", lines[j])
                    archivedf.iloc[m, 0] = scw[0]
                    m += 1
                    break
            x += 1

''' Sorter data (fjerner nul rækker) '''
archivedf = archivedf[(archivedf.T != 0).any()]

archivedf.to_csv("ArchiveCSV/BurstArchive", sep='\t', encoding='utf-8', index=False)

m = 0
n = 0

burstdf = pd.DataFrame(np.zeros((N, len(archivecolums))), columns=archivecolums)

for i in range(len(archivedf.iloc[:, 0])-1):
    if (archivedf.iloc[i, 0] == archivedf.iloc[i+1, 0]) \
            or (int(archivedf.iloc[i, 0])-int(archivedf.iloc[i+1, 0]) == 1):
        if (float(archivedf.iloc[i, 1])-float(archivedf.iloc[i+1, 1]) <= 0.003) \
                or (float(archivedf.iloc[i, 1])-float(archivedf.iloc[i+1, 1]) <= -0.003):
            if (float(archivedf.iloc[i, 2])-float(archivedf.iloc[i+1, 2]) <= 0.003) \
                    or (float(archivedf.iloc[i, 2])-float(archivedf.iloc[i+1, 2]) <= -0.003):
                if (float(archivedf.iloc[i+1, 6]) < float(archivedf.iloc[i, 5])
                        or float(archivedf.iloc[i+1, 5]) > float(archivedf.iloc[i, 6])):
                    burstdf.iloc[i, :] = archivedf.iloc[i, :]
                    burstdf.iloc[i+1, :] = archivedf.iloc[i+1, :]

''' Sorter data (fjerner nul rækker) '''
burstdf = burstdf[(burstdf.T != 0).any()]

print(burstdf)

burstdf.to_csv("BurstCSV/gbJ1_A_4_E03", sep='\t', encoding='utf-8', index=False)
