from ArchiveExtract import *

directory = "E03/"

def burstSearch(directory):

    for filename in os.listdir("ArchiveCSV/"+directory):
        if filename.endswith(".csv"):

            archivecsv = pd.read_csv(os.path.join("ArchiveCSV/"+directory, filename))  # indlæser data
            archivedf = pd.DataFrame(archivecsv)  # skaber et dataframe

            burstdf = pd.DataFrame(np.zeros((N, len(archiveColumns))), columns=archiveColumns)

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

            burstdf.to_csv("BurstCSV/"+filename, sep=',', encoding='utf-8', index=False)

burstSearch(directory)

