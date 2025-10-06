# This program is a simulation of BINGO.
# GIFFORD, CHARLES
# 11/12/2024

import random

print("Welcome to BINGO!")

def createCard(rows, columns):
    bingoCard = []
    numberList = []
    for row in range(0, rows):
        bingoCard.append([])
        for column in range(0, columns):
            boundA = column * 15 + 1
            boundB = (column + 1) * 15
            while True:
                randomNum = random.randint(boundA, boundB)
                if randomNum not in numberList and randomNum not in bingoCard[row]:
                    numberList.append(randomNum)
                    bingoCard[row].append(randomNum)
                    break
    bingoCard[2][2] = 0
    print("SELECTION LIST: "+ str(numberList))
    return bingoCard

def bingoGame(card):
    callList = []
    bingoFlag = False
    while bingoFlag == False:
        randomNum = random.randint(1, 75)
        if randomNum not in callList:
            callList.append(randomNum)
            for row in range(len(card)):
                for column in range(len(card[row])):
                    if card[row][column] == randomNum:
                        card[row][column] = 0
                    if isItBingo(card) == True:
                        bingoFlag = True
                        break
                if bingoFlag == True:
                    break
    print("\n")
    print("CALL LIST: " + str(callList) + "\n")
    print("The 0's represent chosen numbers!")
    if bingoFlag == True:
        print("\n")
        print("BINGO")
        return True

def isItBingo(card):
    for row in card:
        if sum(row) == 0:
            return True
    for column in card:
        if sum(column) == 0:
            return True
    diagSumOne = 0
    diagSumTwo = 0
    for i in range(len(card)):
        diagSumOne += card[i][i]
        diagSumTwo += card[i][len(card) - 1 - i]
    if diagSumOne == 0 or diagSumTwo == 0:
        return True
    return False

def printHelper(card):
    print("\n")
    print("         B       I       N       G       O")
    for row in range(len(card)):
        print ()
        for col in range (len(card[row])):
            print ("\t",card[row][col],end = " ")

bingoCardOne = createCard(5, 5)
print("BINGO CARD: " + str(bingoCardOne))
printHelper(bingoCardOne)
if bingoGame(bingoCardOne) == True:
    printHelper(bingoCardOne)


    
    
    


