from cm2certantydataimport import dataimportcm2
import os
import pandas as pd

source = os.fsencode(r'C:\Users\joach\Desktop\Wordstuff\Uddannelse\Univeristetet\3semester\fagprojekt\Data\shx')
filesJ1 = []
filesJ2 = []
i = 0
j = 0
for root, dirs, filenames in os.walk(source):
    for file in filenames:
        file = file.decode('utf-8')
        print(file)
        if "gbJ1" in file:
            i += 1
            dataimportcm2(file,"J1({}).csv".format(i))
            filesJ1.append("J1({}).csv".format(i))
        if "gbJ2" in file:
            j += 1
            dataimportcm2(file,"J2({}).csv".format(j))
            filesJ2.append("J2({}).csv".format(i))

#combined_csvJ1 = pd.concat( [ pd.read_csv(f) for f in filesJ1 ] )
#combined_csvJ1.to_csv( "combined_csvJ1.csv", index=False )
#combined_csv = pd.concat( [ pd.read_csv(f) for f in filesJ2 ] )
#combined_csv.to_csv( "combined_csvJ2.csv", index=False )
#print(files)
