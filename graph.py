__author__ = 'ed'
import random
import matplotlib
import matplotlib.pyplot as plt
import csv
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')


def graph():
    with open('monteCarlo.csv','r') as montecarlo:
        datas = csv.reader(montecarlo, delimiter=',')

        for eachLine in datas:
            percentROI = float(eachLine[0])
            wagerSizePercent = float(eachLine[1])
            wagerCount = float(eachLine[2])
            pcolor = eachLine[3]

            ax.scatter(wagerSizePercent,wagerCount,percentROI,color=pcolor)

            ax.set_xlabel('wager percent size')
            ax.set_ylabel('wager count')
            ax.set_zlabel('Percent ROI')



    plt.show()


graph()




def rollDice():
    roll = random.randint(1,100)

    if roll <= 50:
        return False
    elif roll >= 51:
        return True



def multiple_bettor2(funds, initial_wager, wager_count, multiple):
    global ROI
    global multiple_busts
    global multiple_profits

    value = funds
    wager = initial_wager
    wX = []
    vY = []
    currentWager = 1
    previousWager = 'win'
    previousWagerAmount = initial_wager

    while currentWager <= wager_count:
        if previousWager == 'win':
            if rollDice():
                value += wager
                wX.append(currentWager)
                vY.append(value)
            else:
                value -= wager
                previousWager = 'loss'
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value <= 0:
                    multiple_busts += 1
                    break
        elif previousWager == 'loss':
            if rollDice():
                wager = previousWagerAmount * multiple
                if (value - wager) <= 0:
                    wager = value

                value += wager
                wager = initial_wager
                previousWager = 'win'
                wX.append(currentWager)
                vY.append(value)
            else:
                wager = previousWagerAmount * multiple
                if (value - wager) <= 0:
                    wager = value
                value -= wager
                previousWager = 'loss'
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)

                if value <= 0:
                    multiple_busts += 1
                    break


        currentWager += 1
    #print 'ending Value:',value
    ROI += value

    #plt.plot(wX,vY)

    if value > funds:
        multiple_profits+=1




#lower_bust = 19.00
#higher_profit = 69.00


sampleSize = 1000
startingFunds = 100000

while True:




    #wagerSize = 100
    #wagerCount = 100

    wagerSize = random.uniform(1.0, 100.00)
    wagerCount = random.uniform(10.0, 10000)
    Ret = 0.0
    da_profits = 0.0
    da_busts = 0.0
    daSampleSize = 10000





    multipleSampSize = 1000000
    #multiple_busts = 0.0
    #multiple_profits = 0.0
    ROI = Ret - (daSampleSize+startingFunds)


    counter = 1


    while counter <= daSampleSize:
        multiple_bettor2(startingFunds,wagerSize,wagerCount,1.75)
        counter += 1
    ROI = Ret - (sampleSize*startingFunds)
    totalInvested = daSampleSize*startingFunds

    percentROI = (ROI/totalInvested)*100.00

    wagerSizePercent = (wagerSize/startingFunds)*100.00



    if percentROI > 1:

        print('__________________________________________________')
        print('Total Amount Invested:', daSampleSize * startingFunds)
        print('Total Return:',ROI)
        print('Difference:',ROI-(daSampleSize * startingFunds))
        print('Percent ROI:', percentROI)
        print('Bust Rate:',(multiple_busts/daSampleSize)*100.00)
        print('Profit Rate:',(multiple_profits/daSampleSize)*100.00)
        print('wager size:', wagerSize)
        print('wager count: ', wagerCount)
        print('wager size percent: ', wagerSizePercent)

        saveFile = open('monteCarlo.csv', 'a')
        saveLine = '\n' + str(percentROI) + ','+str(wagerSizePercent)+','+',g '
        saveFile.write(saveLine)
        saveFile.close()

    elif percentROI < -1:

        print('__________________________________________________')
        print('Total Amount Invested:', daSampleSize * startingFunds)
        print('Total Return:',ROI)
        print('Difference:',ROI-(daSampleSize * startingFunds))
        print('Percent ROI:', percentROI)
        print('Bust Rate:',(multiple_busts/daSampleSize)*100.00)
        print('Profit Rate:',(multiple_profits/daSampleSize)*100.00)
        print('wager size:', wagerSize)
        print('wager count: ', wagerCount)
        print('wager size percent: ', wagerSizePercent)

        saveFile = open('monteCarlo.csv', 'a')
        saveLine = '\n' + str(percentROI) + ','+str(wagerSizePercent)+','+',g '
        saveFile.write(saveLine)
        saveFile.close()

