from LightCurveData import *

filename = "E03/gbJ1_B_4_E03.txt"

xCoor = 287.8176
yCoor = 0.589

chwidth = 4.0
scw = "30900660010"

xPlot = lightcurve(scw, chwidth, xCoor, yCoor, filename)[0]
yPlot = lightcurve(scw, chwidth, xCoor, yCoor, filename)[1]
chmax = lightcurve(scw, chwidth, xCoor, yCoor,   filename)[2]


''' Creating a plot '''
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

