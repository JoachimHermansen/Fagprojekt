from LightCurveData import *

directory = "CoorExtract/"
filename = "BurstFound 2S 1742-294" + ".csv"

df = pd.read_csv(os.path.join("BurstCSV/" + directory, filename))

df = df.sort_values(by=['SCW'])

df = df.drop_duplicates(subset=['File', 'SCW'], keep='first')

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

    if i != len(df.iloc[:, 0])-1:
        filename2 = 'E03/' + df.iloc[i+1, 0]

        if "J1" in filename:
            sat2 = "J1"
        else:
            sat2 = "J2"

        scw2 = int(df.iloc[i+1, 1])
        chwidth2 = df.iloc[i+1, 6]
        cm22 = df.iloc[i+1, 5]
        xCoor2 = df.iloc[i+1, 2]
        yCoor2 = df.iloc[i+1, 3]

        xPlot2 = lightcurve(scw2, chwidth2, xCoor2, yCoor2, filename2)[0]
        yPlot2 = lightcurve(scw2, chwidth2, xCoor2, yCoor2, filename2)[1]
        chmax2 = lightcurve(scw2, chwidth2, xCoor2, yCoor2, filename2)[2]

    if len(df.iloc[:, 0]) > 1 and scw == int(df.iloc[i-1, 1]):
        print("Already plotted")

    else:
        if scw == scw2 and len(chmax) == 1 and len(chmax2) == 1:
            ''' Creating a plot '''
            plt.plot(xPlot, yPlot, linestyle="-", color="b", label='JEM-X 1')
            plt.plot(xPlot2, yPlot2, linestyle="--", color="r", label='JEM-X 2')
            plt.grid(True)
            plt.title("2S 1742-294 - " + "Scw " + str(scw),
                      fontsize=16)
            #plt.title("J1/J2" + " SCW " + str(scw) + ": " + " cm2 " + str(cm2) + "/" + str(cm22),
                      #fontsize=16)
            plt.xlim(800, 1200)
            plt.xlabel("Time [s]", fontsize=14)
            plt.ylabel("Standard Deviation", fontsize=14)
            plt.legend()
            plt.show()

        elif scw == scw2 and len(chmax) > 1 and len(chmax2) == 1:
            for j in range(len(chmax)):
                plt.plot(xPlot[j], yPlot[j], linestyle="-", color="b", label='JEM-X 1')
                plt.plot(xPlot2, yPlot2, linestyle="--", color="r", label='JEM-X 2')
                plt.grid(True)
                plt.title("2S 1742-294 - " + "Scw " + str(scw),
                          fontsize=16)
                #plt.title("J1/J2" + " SCW " + str(scw) + ": " + " cm2 " + str(cm2) + "/" + str(cm22),
                          #fontsize=16)
                plt.xlim(800, 1200)
                plt.xlabel("Time [s]", fontsize=14)
                plt.ylabel("Standard Deviation", fontsize=14)
                plt.legend()
                plt.show()

        elif scw == scw2 and len(chmax) == 1 and len(chmax2) > 1:
            for j in range(len(chmax2)):
                plt.plot(xPlot, yPlot, linestyle="-", color="b", label='JEM-X 1')
                plt.plot(xPlot2[j], yPlot2[j], linestyle="--", color="r", label='JEM-X 2')
                plt.grid(True)
                plt.title("2S 1742-294 - " + "Scw " + str(scw),
                          fontsize=16)
                #plt.title("J1/J2" + " SCW " + str(scw) + ": " + " cm2 " + str(cm2) + "/" + str(cm22),
                          #fontsize=16)
                plt.xlim(800, 1200)
                plt.xlabel("Time [s]", fontsize=14)
                plt.ylabel("Standard Deviation", fontsize=14)
                plt.legend()
                plt.show()

        elif scw == scw2 and len(chmax) > 1 and len(chmax2) > 1:
            for k in range(len(chmax)):
                for j in range(len(chmax2)):
                    plt.plot(xPlot[k], yPlot[k], linestyle="-", color="b", label='JEM-X 1')
                    plt.plot(xPlot2[j], yPlot2[j], linestyle="--", color="r", label='JEM-X 2')
                    plt.grid(True)
                    plt.title("2S 1742-294 - " + "Scw " + str(scw),
                              fontsize=16)
                    plt.xlim(800, 1200)
                    plt.xlabel("Time [s]", fontsize=14)
                    plt.ylabel("Standard Deviation", fontsize=14)
                    plt.legend()
                    plt.show()

        elif len(xPlot) == 0:
            print("No imgpoly that fit chmax")

        elif len(chmax) == 1:
            ''' Creating a plot '''
            plt.plot(xPlot, yPlot, linestyle="-", color="b")
            plt.grid(True)
            plt.title("2S 1742-294 - " + "Scw " + str(scw),
                      fontsize=16)
            #plt.title(sat + " SCW " + str(scw) + ": " + "chmax " + str(chmax[0]) + " cm2 " + str(cm2),
                      #fontsize=16)
            plt.xlim(800, 1200)
            plt.xlabel("Time [s]", fontsize=14)
            plt.ylabel("Standard Deviation", fontsize=14)
            plt.show()
        else:
            for j in range(len(chmax)):
                ''' Creating a plot '''
                plt.plot(xPlot[j], yPlot[j], linestyle="-", color="b")
                plt.grid(True)
                plt.title(sat + " scw " + str(scw) + ": " + "chmax " + str(chmax[j]) + " cm2" + str(cm2),
                          fontsize=16)
                plt.xlabel("Time [s]", fontsize=14)
                plt.ylabel("Standard Deviation", fontsize=14)
                plt.show()
                plt.figure()

# Jeg skal finde toppunktets x-koordinat. Herefter skal jeg kigge på det x-koordinat i samtlige
# imgpoly. Jeg summer for punktet, plus -1 og +1 i forhold til koordinaten.
# Herefter sammenligner jeg og ser hvilket punkt har den højeste vægtede sum.
