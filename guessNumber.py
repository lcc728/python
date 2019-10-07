#Guess Number use While
#https://www.george.tw/2019/10/07/python-guess-the-number/
import random
number=random.randint(1,100)
guessFlag=False
while guessFlag==False:
      guess=int(input("Enter a number:"))
      if guess==number:
            print("God job")
            guessFlag=True
      elif guess > number :
            print ("Too high")
      elif guess < number:
            print ("Too low")
            
        
