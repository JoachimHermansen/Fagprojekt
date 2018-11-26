from LightCurveData import *

directory = "CoorExtract/"
filename = "BurstFound EXO 1745-248 (Tz 5)f" + ".csv"

df = pd.read_csv(os.path.join("BurstCSV/" + directory, filename))

for i in range(len(df.iloc[:, 0])):
    filename = "E03Combined.txt"

    scw = int(df.iloc[i, 0])
    chwidth = df.iloc[i, 10]
    xCoor = df.iloc[i, 1]
    yCoor = df.iloc[i, 2]
    print(scw)

    xPlot = lightcurve(scw, chwidth, xCoor, yCoor, filename)[0]
    yPlot = lightcurve(scw, chwidth, xCoor, yCoor, filename)[1]
    chmax = lightcurve(scw, chwidth, xCoor, yCoor, filename)[2]

    if scw == int(df.iloc[i-1, 0]):
        print("Already plotted")
    else:
        if len(xPlot) == 0:
            print("No imgpoly that fit chmax")

        elif len(chmax) == 1:
            ''' Creating a plot '''
            plt.plot(xPlot, yPlot, linestyle="-", color="b")
            plt.grid(True)
            plt.title("scw " + str(scw) + ": " + "chmax " + str(chmax[0]),
                      fontsize=16)
            plt.xlabel("Seconds [s]", fontsize=18)
            plt.ylabel("Standard Deviation", fontsize=18)
            plt.show()
        else:
            for j in range(len(chmax)):
                ''' Creating a plot '''
                plt.plot(xPlot[j], yPlot[j], linestyle="-", color="b")
                plt.grid(True)
                plt.title("scw " + str(scw) + ": " + "chmax " + str(chmax[j]),
                          fontsize=16)
                plt.xlabel("Seconds [s]", fontsize=18)
                plt.ylabel("Standard Deviation", fontsize=18)
                plt.show()

# Jeg skal finde toppunktets x-koordinat. Herefter skal jeg kigge på det x-koordinat i samtlige
# imgpoly. Jeg summer for punktet, plus -1 og +1 i forhold til koordinaten.
# Herefter sammenligner jeg og ser hvilket punkt har den højeste vægtede sum.

