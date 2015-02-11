__author__ = 'ed'
import random
import matplotlib
import matplotlib.pyplot as plt
import time



lower_bust = 31.235
higher_profit = 63.208


sampleSize = 100

startingFunds = 10000
wagerSize = 100
wagerCount = 1000
da_profits = 0




def rollDice():
    roll = random.randint(1,100)

    if roll == 100:
        return Falseprint("we won, current value: " value)
    elif roll <= 50:
        return False
    elif 100 > roll >= 50:
        return True


def dAlembert(funds, initial_wager, wager_count):
    global da_busts
    global da_profits

    value = funds
    wager = initial_wager
    currentWager = 1
    previousWager = 'win'
    previousWagerAmount = initial_wager

    while currentWager <= wager_count:
        if previousWager == 'win':
            if wager == initial_wager:
                pass
            else:
                wager -= initial_wager
            print(currentWager, wager, value)
            if rollDice():
                value += wager
                print("we won, current value: ", value)
                previousWagerAmount = wager
            else:
                value -= wager
                previousWager = 'loss'
                print("we won, current value: ", value)
                previousWagerAmount = wager
            if value <= 0:
                da_busts += 1
                break

            elif previousWager == 'loss':
                wager = previousWagerAmount + initial_wager
                if (value - wager) <= 0:
                    wager = value
                print('lost the last wager, current wager: ', wager, value)

                if rollDice():
                    value += wager
                    previousWagerAmount = wager
                    print('we wont current value', value)
                    previousWager = 'win'

                else:
                    value -= wager
                    previousWagerAmount = wager
                    print('we ost current value', value)

                    if value <= 0:
                        da_busts += 1
                        break
                currentWager += 1

            if value > funds:
                da_profits += 1
dAlembert(startingFunds, wagerSize, wagerCount)

def doubler_bettor(funds, initial_wager, wager_count):

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
                if value < 0:
                    currentWager += 10000000000000000
        elif previousWager == 'loss':
            if rollDice():
                wager = previousWagerAmount * 2
                value += wager
                wager = initial_wager
                previousWager = 'win'
                wX.append(currentWager)
                vY.append(value)
            else:
                wager = previousWagerAmount * 2
                value -= wager
                previousWager = 'loss'
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value < 0:
                    currentWager += 10000000000000000

        currentWager += 1
    # this guy goes cyan #
    plt.plot(wX,vY,'c')


def simple_bettor(funds,initial_wager,wager_count,color):
    global broke_count


    value = funds
    wager = initial_wager
    wX = []
    vY = []
    currentWager = 1
    while currentWager <= wager_count:
        if rollDice():
            value += wager
            wX.append(currentWager)
            vY.append(value)
        else:
            value -= wager
            wX.append(currentWager)
            vY.append(value)

            ###add me
            if value < 0:
                currentWager += 10000000000000000
        currentWager += 1

        if value < 0:
            value = 'broke'
            broke_count += 1
    plt.plot(wX,vY,color)


x = 0
broke_count = 0

while x < sampleSize:
    simple_bettor(startingFunds,wagerSize,wagerCount,'k')
    simple_bettor(startingFunds,wagerSize*2,wagerCount,'c')
    #doubler_bettor(startingFunds,wagerSize,wagerCount)
    x+=1

plt.axhline(0, color = 'r')
plt.ylabel('Account Value')
plt.xlabel('Wager Count')
plt.show()