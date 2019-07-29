#Rock Paper Scissors
#https://www.george.tw/2019/07/29/python-rock-paper-scissors/

import random
gameList=("Rock","Paper","Scissors")
#gameChoice=gameList[random.randint(0,2)]
gameChoice=random.choice(gameList)
validChoice = 1

while (validChoice):
      userChoice=input("Please enter one of following: Rock ,Paper, Scissors")
      if (userChoice in gameList):
            validChoice= 0
      else:
            print("You must enter a valid choice")             
print("I choice:" + gameChoice + ", You choice:" + userChoice      )
if (gameChoice==userChoice):
      print("Tie")
elif ((gameChoice=="Rock" and userChoice=="Paper") or
      (gameChoice=="Paper" and userChoice=="Scissors") or
      (gameChoice=="Scissors" and userChoice=="Rock")):
      print("You win!")
else:
      print("You Lose")

