from ArchiveExtract import *

directory = "E03/"
filename = "E03Combined.csv"


def burstSearch(directory, filename):

    archiveCSV = pd.read_csv(os.path.join("ArchiveCSV/" + directory, filename))  # Loads data from ArchiveCSV
    archivedf = pd.DataFrame(archiveCSV)  # Creates a Dataframe

    burstdf = pd.DataFrame(np.zeros((N, len(archiveColumns))), columns=archiveColumns)

    for i in range(len(archivedf.iloc[:, 0])-1):
        if (83.6280 <= archivedf.iloc[i, 2] <= 83.6361) \
                    and (22.0151 <= archivedf.iloc[i, 3] <= 22.0199): # Removes Crab Nebula
            pass
        elif (((archivedf.iloc[i, 0] == archivedf.iloc[i+1, 0])
               or abs((archivedf.iloc[i, 1]%10e6 - archivedf.iloc[i+1, 1]%10e6) == 1))
              and (abs((archivedf.iloc[i, 2]-archivedf.iloc[i+1, 2])) <= 0.003)
              and (abs((archivedf.iloc[i, 3]-archivedf.iloc[i+1, 3])) <= 0.003)
              and (archivedf.iloc[i+1, 11] < archivedf.iloc[i, 10]
                   or archivedf.iloc[i+1, 10] > archivedf.iloc[i, 11])):
            burstdf.iloc[i, :] = archivedf.iloc[i, :]
            burstdf.iloc[i+1, :] = archivedf.iloc[i+1, :]
        else:
            pass

    ''' Sorter data (fjerner nul rækker) '''
    burstdf = burstdf[(burstdf.T != 0).any()]

    burstdf = burstdf.sort_values(by=['SCW', 'time chans start'])

    burstdf.to_csv("BurstCSV/" + directory + "E03CombinedBurst" + ".csv", sep=',', encoding='utf-8', index=False)

    print("Done!")


burstSearch(directory, filename)


