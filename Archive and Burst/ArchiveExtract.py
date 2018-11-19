import numpy as np
import pandas as pd
import re
import os

N = 1000  # amount of lines

search = ["fk5;", "EnD", "Channel Width"]
archiveColumns = ["SCW", "coordinate1", "coordinate2", "Name",
                  "ObsTime[s]", "time chans start", "time chans stop",
                  "Significance", "IJDStart[D]", "IJDStop[D]", "ChannelWidth[s]",
                  "BurstStart[s]"]  # units in [], s = seconds, D = days

directory = "E03/" # Chosen Directory (E03 or E04)


def archiveExtract(directory):
    for filename in os.listdir("ArchiveFiles/"+directory):
        if filename.endswith(".txt"):
            with open(os.path.join("ArchiveFiles/"+directory, filename), 'r') as fin: # Open file and read the lines
                lines = fin.readlines()

            archivedf = pd.DataFrame(np.zeros((N, len(archiveColumns))), columns=archiveColumns)

            ''' Goes through the lines of the text file data '''
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
                        archivedf.iloc[n, 4] = float(info[3])  # obstime
                        archivedf.iloc[n, 5] = float(info[8])  # time chans start
                        archivedf.iloc[n, 6] = float(info[9])  # time chans stop
                        archivedf.iloc[n, 7] = float(info[7])  # Significance
                        archivedf.iloc[n, 8] = float(info[1])  # IJDStart
                        archivedf.iloc[n, 9] = float(info[2])  # IJDStop
                        n += 1

                        for j in range(i, len(lines)): # Finds SCW
                            if search[1] in lines[j]:
                                scw = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", lines[j])
                                archivedf.iloc[m, 0] = int(scw[0])
                                break

                        for j in range(i, len(lines)): # Finds Channel Width
                            if search[2] in lines[j]:
                                chanwid = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", lines[j])
                                archivedf.iloc[m, 10] = float(chanwid[2])
                                archivedf.iloc[m, 11] = float(chanwid[2])*archivedf.iloc[m, 5]
                                break

                        for j in range(i, len(lines)): # Finds Name of Source
                            if "text={}" in lines[j]:
                                break
                            elif "text=" in lines[j]:
                                s = lines[j]
                                archivedf.iloc[m, 3] = s[s.find("{")+1:s.find("}")]
                                break
                            else:
                                pass

                        m += 1
                        x += 1

            ''' Sorts data (Removes zero rows) '''
            archivedf = archivedf[(archivedf.T != 0).any()]

            archivedf.to_csv("ArchiveCSV/"+directory+filename+".csv", sep=',', encoding="utf-8" , index=False)
            print("Thinking slowly")
    print("Done!")


archiveExtract(directory)

