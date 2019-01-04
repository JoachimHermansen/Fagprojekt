import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#number of boxes for single
ns =100
#number of boxes for multi
nm =50
#filename
file="SCW Check - BurstFound 2S 1742-294.csv"

directory="burststatistics/"
df=pd.read_csv(directory+file)

burst = np.array(df.loc[:,["Antal burst"]].values)
time = np.array(df.loc[:,["Dato"]].values)
#når den bliver overført på docs kommer der en factor 10 i csv til excel formateringen.
time = time / 10
Ns=0
Nm=0
singletid=np.array([])
multi=np.array([])
multitid=np.array([])
#np.append(array, time90)
for i in range(len(burst)):
    if burst[i] == 1:
        Ns += 1
        singletid=np.append(singletid, time[i])
    if burst[i] > 1:
        Nm += 1
        multitid=np.append(multitid, time[i])
        multi=np.append(multi, burst[i])
        
difsingletid = np.array([])
difmultitid = np.array([])
for i in range(Ns-1):
    if (singletid[i+1]-singletid[i]) != 0:
        difsingletid=np.append(difsingletid,singletid[i+1]-singletid[i])
        
for i in range(Nm-1):
    if (singletid[i+1]-singletid[i]) != 0:
        difmultitid=np.append(difmultitid,multitid[i+1]-multitid[i])
#convert to days
difsingletid=difsingletid/(60*60*24)
difmultitid=difmultitid/(60*60*24)
#singleburstplot
plt.figure()
n, bins, patches = plt.hist(difsingletid, ns)
plt.xlabel('days')
plt.ylabel('counts')
plt.title('Singleburst for 2S 1742-294')
#plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
#plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()
#multiburstplot
plt.figure()
n, bins, patches = plt.hist(difmultitid, nm)
plt.xlabel('days')
plt.ylabel('counts')
plt.title('multiburst for 2S 1742-294')
#plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
#plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()