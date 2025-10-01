# This is the file for lab eight.
# Gifford, Charles
# 11/20/2024

import random

sideNum = int(input("Enter the size of the square you want: "))


listOfNums = [[0 for num in range(sideNum)] for numTwo in range(sideNum)]
for num in range(sideNum):
    for numTwo in range(sideNum):
        listOfNums[num][numTwo] = random.randint(1, 5)

def printHelper(L):
    for row in range(len(L)):
        print ()
        for col in range (len(L[row])):
            print ("\t",L[row][col],end = " ")

downDiagnol = sum(listOfNums[i][i] for i in range(sideNum))
upDiagnol = sum(listOfNums[i][sideNum - i - 1] for i in range(sideNum))

printHelper(listOfNums)

print("\n")
print(downDiagnol)
print(upDiagnol)





