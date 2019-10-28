#Guess Number use While
#https://www.george.tw/2019/10/07/python-guess-the-number/
import random
num=random.randint(1,100)
guessFlag=False
while guessFlag==False:
      guess=int(input("Enter a number:"))
      if guess==num:
            print("God job")
            guessFlag=True
<<<<<<< HEAD
      elif guess > num:
=======
      elif guess > number:
>>>>>>> c8c2ca924a4fc850ec9f674d63d0a6668b944a5f
            print ("Too high")
      elif guess < num:
            print ("Too low")
