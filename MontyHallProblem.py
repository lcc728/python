#The Monty Hall Problem
#https://www.george.tw/2020/03/05/python-the-monty-hall-problem/

import random
guessCount=0
rightCount = 0
while True:
    door=random.randrange(3)+1
    firstChoice=int(input("Choose a door from 1-3 , to exit the program, press 4 :"))
    if (firstChoice==4): break
    guessCount =guessCount +1
    doorList=[1,2,3]
    doorList.pop(door-1)
    if (firstChoice != door):
        newList=[firstChoice,door]
    else:
        second=random.randrange(1)+1 
        newList=[doorList[second-1], door]
    newList.sort()
    secondChoice=int(input("Choice another door from {:d},{:d}:".format(newList[0],newList[1])))
    if (secondChoice==door):
        print ("You win, the door is {:d}".format(door))
        rightCount = rightCount+ 1
    else:
        print ("You loss, the door is {:d}".format(door))


print("{:d} guesses in total".format(guessCount))
print("{:d} correct guesses".format(rightCount))
print ("The chance of guessing correctly is {:.3f}".format(rightCount/guessCount))
