import numpy as np
import pandas as pd
import re
import os

N = 500000  # amount of lines

search = ["fk5;point", "EnD", "flux"]
fluxColumns = ["File", "SCW", "coordinate1", "coordinate2",
               "Name", "flux"]  # units in [], s = seconds, D = days

directory = "0reg/"  # Chosen Directory (E03 or E04)


def fluxExtract(directory):

    for filename in os.listdir("FluxFiles/"+directory):
        if filename.endswith(".txt"):
            with open(os.path.join("FluxFiles/"+directory, filename), 'r', errors='ignore') as fin:  # Open file and read the lines
                lines = fin.readlines()

            m = 0
            n = 0
            x = 0

            fluxdf = pd.DataFrame(np.zeros((N, len(fluxColumns))), columns=fluxColumns)

            ''' Goes through the lines of the text file data '''
            for i in range(len(lines)):
                if x < N:
                    if search[0] in lines[i]: # Leder efter fk5;point i linjerne
                        coordinates = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", lines[i])
                        info = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", lines[i + 1])

                        # Display which file the source is found in
                        fluxdf.iloc[n, 0] = filename

                        # Tildeler koordinaterne til deres plads i DF
                        fluxdf.iloc[n, 2] = float(coordinates[1])
                        fluxdf.iloc[n, 3] = float(coordinates[2])

                        # Tildeler yderligere info til deres plads i DF
                        fluxdf.iloc[n, 5] = float(info[7])  # flux
                        n += 1

                        # Finds the SCW of the source
                        for j in range(i, len(lines)):
                            if search[1] in lines[j]:
                                scw = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", lines[j])
                                fluxdf.iloc[m, 1] = int(scw[0])
                                break

                        for j in range(i, len(lines)):  # Finds Name of Source
                            if "text={}" in lines[j]:
                                break
                            elif "text=" in lines[j]:
                                s = lines[j]
                                fluxdf.iloc[m, 4] = s[s.find("{")+1:s.find("}")]
                                break
                            else:
                                pass

                        m += 1
                        x += 1

            print("Thinking slowly")

            ''' Sorts data (Removes zero rows) '''
            fluxdf = fluxdf[(fluxdf.T != 0).any()]

            fluxdf.to_csv("FluxFiles/" + filename + ".csv", sep=',', encoding="utf-8", index=False)

    print("Done!")


fluxExtract(directory)

