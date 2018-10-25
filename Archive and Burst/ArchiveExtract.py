import numpy as np
import pandas as pd
import re
import os

N = 1000 # Antal linjer

search = ["fk5;", "EnD"]
archiveColumns = ["SCW", "coordinate1", "coordinate2", "Name",
                  "ObsTime", "time chans start", "time chans stop",
                  "Significance", "IJDStart", "IJDStop"]

# filename = "ArchiveFiles/gbJ1_A_4_E03.txt"
directory = "E03/"


def archiveExtract(directory):
    for filename in os.listdir("ArchiveFiles/"+directory):
        if filename.endswith(".txt"):
            with open(os.path.join("ArchiveFiles/"+directory, filename), 'r') as fin: #Åbner filen og indlæser linjerne
                lines = fin.readlines()

            archivedf = pd.DataFrame(np.zeros((N, len(archiveColumns))), columns=archiveColumns)

            ''' Gennemgår linjerne for data '''
            m = 0
            n = 0
            x = 0

            for i in range(len(lines)):
                if x < N:
                    if search[0] in lines[i]: # Leder efter fk5 i linjerne
                        coordinates = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", lines[i])
                        info = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", lines[i + 1])

                        # Tildeler koordinaterne til deres plads i DF
                        archivedf.iloc[n, 1] = float(coordinates[1])
                        archivedf.iloc[n, 2] = float(coordinates[2])

                        # Tildeler yderligere info til deres plads i DF
                        archivedf.iloc[n, 4] = float(info[3]) # obstime
                        archivedf.iloc[n, 5] = float(info[8]) # time chans start
                        archivedf.iloc[n, 6] = float(info[9]) # time chans stop
                        archivedf.iloc[n, 7] = float(info[7]) # Significance
                        archivedf.iloc[n, 8] = float(info[1]) # IJDStart
                        archivedf.iloc[n, 9] = float(info[2]) # IJDStop
                        n += 1

                        for j in range(i, len(lines)):
                            if search[1] in lines[j]:
                                scw = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", lines[j])
                                archivedf.iloc[m, 0] = int(scw[0])
                                m += 1
                                break
                        x += 1

            ''' Sorter data (fjerner nul rækker) '''
            archivedf = archivedf[(archivedf.T != 0).any()]

            archivedf.to_csv("ArchiveCSV/"+directory+filename+".csv", sep=',', encoding="utf-8" , index=False)
            print("Keep going")
    print("Done!")

archiveExtract(directory)
