import pandas as pd
import numpy as np
 
#os.chdir("C:/Folder")
data = np.array([0,0,0,0])
for i in range(1,28):
    filename = "J1({}).csv".format(i)
    datain = pd.read_csv(filename) 
    tempdata =np.copy(datain)
    data = np.vstack((data,tempdata))

np.savetxt("J1data.csv", data[1:,:], delimiter=",")
