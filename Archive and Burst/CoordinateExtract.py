import pandas as pd

cd = "ArchiveCSV/"

directory = "E03/"

file = "CombinedE03Combined.csv"



name = ["EXO 0748-676","GS 0836-429","4U 1323-62","4U 1608-522",
        "4U 1636-536","MXB 1658-298","4U 1705-44","XTE J1710-281",
        "4U 1735-44","2S 1742-294","EXO 1745-248 (Tz 5)f","4U 1746-37 (NGC 6641)f",
        "SAX J1747.0-2853","Aql X-1","Cyg X-2f"]
x = [117.140460,129.348300,201.651290,243.179200,250.231300,255.527250,
     257.226958,257.551300,264.742900,266.521667,267.021650,267.552750,
     266.760830,287.816880,326.171477]
y = [-67.752140,-42.900600,-62.136080,-52.423100,-53.751400,-29.945580,
     -44.102042,-28.131700,-44.450000,-29.514806,-24.779833,-37.052280,
     -28.883030,0.584940,38.321407]
n = 14

def CoorExtract(file,x,y):
    
    for i in range(n):
        
        df=pd.read_csv(cd+directory+file)    
    
        df=df.loc[df['coordinate1']<=x[i]+0.003]
        df=df.loc[df['coordinate1']>=x[i]-0.003]

        df=df.loc[df['coordinate2']<=y[i]+0.003]
        df=df.loc[df['coordinate2']>=y[i]-0.003]
  
        if df.empty:
            print("No data")
        else:
            df.to_csv(cd+directory+"BurstFoundArchive"+name[i]+".csv", sep=',', encoding="utf-8" , index=False)
    
    return df

print(CoorExtract(file,x,y))
