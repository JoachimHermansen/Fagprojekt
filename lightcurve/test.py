import matplotlib    
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.mlab as mlab
Scw = "004500300010"
koords = "83.6315,  22.0141"
Scwthere = 0
Scwthere = 0
with open("gbJ1_A_4_E03.reg.txt") as f:
    lines = f.readlines()
for i in range(len(lines)):
   
        
    if "BegiN {}".format(Scw) in lines[i]:
        start = i
        Scwthere = 1
    if "EnD {}".format(Scw) in lines[i]:
        end = i
if Scwthere == 0:
    print("{} not found".format(Scw))
else:
    for i in range(start+1,end):
        print(lines[i])
        if "fk5;point( {})".format(koords) in lines[i]:
            print("found it")
