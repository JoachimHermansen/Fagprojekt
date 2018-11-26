from LightCurveData import *

directory = "CoorExtract/"
filename = "BurstFound Aql X-1.csv"

df = pd.read_csv(os.path.join("BurstCSV/" + directory, filename))

for i in range(len(df.iloc[:, 0])):
    filename = "E03Combined.txt"

    scw = int(df.iloc[i, 0])
    chwidth = df.iloc[i, 10]
    print(scw)

    xTotal = lightcurve(scw, chwidth, filename)[0]
    yTotal = lightcurve(scw, chwidth, filename)[1]
    chmax = lightcurve(scw, chwidth, filename)[3]
    n = lightcurve(scw, chwidth, filename)[4]

    ''' Creating a plot '''
    if len(xTotal) > 50:
        plt.plot(xTotal, yTotal, linestyle="-", color="b")
        plt.grid(True)
        plt.title("scw " + str(scw) + ": " + "chmax " + str(chmax) + " , best imgpoly " + str(n),
                  fontsize=16)
        plt.xlabel("Seconds [s]", fontsize=18)
        plt.ylabel("Standard Deviation", fontsize=18)
        plt.show()
    else:
        for j in range(len(xTotal)):
            plt.plot(xTotal[j], yTotal[j], linestyle="-", color="b")
            plt.grid(True)
            plt.title("scw " + str(scw) + ": " + "chmax " + str(chmax[j]) + " , best imgpoly " + str(n[j]),
                      fontsize=16)
            plt.xlabel("Seconds [s]", fontsize=18)
            plt.ylabel("Standard Deviation", fontsize=18)
            plt.show()

# Jeg skal finde toppunktets x-koordinat. Herefter skal jeg kigge på det x-koordinat i samtlige
# imgpoly. Jeg summer for punktet, plus -1 og +1 i forhold til koordinaten.
# Herefter sammenligner jeg og ser hvilket punkt har den højeste vægtede sum.

