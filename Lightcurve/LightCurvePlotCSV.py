from LightCurveData import *

directory = "CoorExtract/"
#filename = "BurstFound EXO 1745-248 (Tz 5)f" + ".csv"
filename = "BurstFound Aql X-1.csv"

df = pd.read_csv(os.path.join("BurstCSV/" + directory, filename))

for i in range(len(df.iloc[:, 0])):
    filename = 'E03/' + df.iloc[i, 0]

    if "J1" in filename:
        sat = "J1"
    else:
        sat = "J2"

    scw = int(df.iloc[i, 1])
    chwidth = df.iloc[i, 6]
    cm2 = df.iloc[i, 5]
    xCoor = df.iloc[i, 2]
    yCoor = df.iloc[i, 3]
    print(scw)

    xPlot = lightcurve(scw, chwidth, xCoor, yCoor, filename)[0]
    yPlot = lightcurve(scw, chwidth, xCoor, yCoor, filename)[1]
    chmax = lightcurve(scw, chwidth, xCoor, yCoor, filename)[2]

    if scw == int(df.iloc[i-1, 1]):
        print("Already plotted")
    else:
        if len(xPlot) == 0:
            print("No imgpoly that fit chmax")

        elif len(chmax) == 1:
            ''' Creating a plot '''
            plt.plot(xPlot, yPlot, linestyle="-", color="b")
            plt.grid(True)
            plt.title(sat + " SCW " + str(scw) + ": " + "chmax " + str(chmax[0]) + " cm2 " + str(cm2),
                      fontsize=16)
            plt.xlabel("Seconds [s]", fontsize=18)
            plt.ylabel("Standard Deviation", fontsize=18)
            plt.show()
        else:
            for j in range(len(chmax)):
                ''' Creating a plot '''
                plt.plot(xPlot[j], yPlot[j], linestyle="-", color="b")
                plt.grid(True)
                plt.title(sat + " scw " + str(scw) + ": " + "chmax " + str(chmax[j]) + " cm2" + str(cm2),
                          fontsize=16)
                plt.xlabel("Seconds [s]", fontsize=18)
                plt.ylabel("Standard Deviation", fontsize=18)
                plt.show()

# Jeg skal finde toppunktets x-koordinat. Herefter skal jeg kigge på det x-koordinat i samtlige
# imgpoly. Jeg summer for punktet, plus -1 og +1 i forhold til koordinaten.
# Herefter sammenligner jeg og ser hvilket punkt har den højeste vægtede sum.

