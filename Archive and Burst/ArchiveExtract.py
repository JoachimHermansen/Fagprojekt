import numpy as np
import pandas as pd
import re
import os

N = 20000  # amount of lines

search = ["fk5;", "EnD", "Channel Width"]
archiveColumns = ["File", "SCW", "coordinate1", "coordinate2", "Name",
                  "cm2", "ChannelWidth[s]", "Significance",
                  "ObsTime[s]", "BurstStart[s]",
                  "time chans start", "time chans stop",
                  "IJDStart[D]", "IJDStop[D]"]  # units in [], s = seconds, D = days

directory = "E03/"  # Chosen Directory (E03 or E04)


def archiveExtract(directory):

    archivedf = pd.DataFrame(np.zeros((N, len(archiveColumns))), columns=archiveColumns)
    m = 0
    n = 0
    x = 0

    for filename in os.listdir("ArchiveFiles/"+directory):
        if filename.endswith(".txt"):
            with open(os.path.join("ArchiveFiles/"+directory, filename), 'r') as fin: # Open file and read the lines
                lines = fin.readlines()

            ''' Goes through the lines of the text file data '''

            for i in range(len(lines)):
                if x < N:
                    if search[0] in lines[i]: # Leder efter fk5 i linjerne
                        coordinates = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", lines[i])
                        info = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", lines[i + 1])

                        # Display which file the source is found in
                        archivedf.iloc[n, 0] = filename

                        # Tildeler koordinaterne til deres plads i DF
                        archivedf.iloc[n, 2] = float(coordinates[1])
                        archivedf.iloc[n, 3] = float(coordinates[2])

                        # Tildeler yderligere info til deres plads i DF
                        archivedf.iloc[n, 5] = float(info[5])  # cm2
                        archivedf.iloc[n, 7] = float(info[7])  # Significance
                        archivedf.iloc[n, 8] = float(info[3])  # obstime
                        archivedf.iloc[n, 10] = float(info[8])  # time chans start
                        archivedf.iloc[n, 11] = float(info[9])  # time chans stop
                        archivedf.iloc[n, 12] = float(info[1])  # IJDStart
                        archivedf.iloc[n, 13] = float(info[2])  # IJDStop
                        n += 1

                        # Finds the SCW of the source
                        for j in range(i, len(lines)):
                            if search[1] in lines[j]:
                                scw = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", lines[j])
                                archivedf.iloc[m, 1] = int(scw[0])
                                break

                        for j in range(i, len(lines)): # Finds Channel Width
                            if search[2] in lines[j]:
                                chanwid = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", lines[j])
                                archivedf.iloc[m, 6] = float(chanwid[2])  # Channel Width
                                archivedf.iloc[m, 9] = float(chanwid[2])*archivedf.iloc[m, 10]  # Burst start
                                break

                        for j in range(i, len(lines)): # Finds Name of Source
                            if "text={}" in lines[j]:
                                break
                            elif "text=" in lines[j]:
                                s = lines[j]
                                archivedf.iloc[m, 4] = s[s.find("{")+1:s.find("}")]
                                break
                            else:
                                pass

                        m += 1
                        x += 1

            print("Thinking slowly")

    ''' Sorts data (Removes zero rows) '''
    archivedf = archivedf[(archivedf.T != 0).any()]

    archivedf.to_csv("ArchiveCSV/" + directory + "E03Combined" + ".csv", sep=',', encoding="utf-8", index=False)

    print("Done!")


archiveExtract(directory)

