# Leibniz
# https://www.george.tw/2020/03/02/python-leibniz-use-for-loop/
import math


count=int(input("Enter a number:"))
sum=1
denominator=3
negate=-1

for i in range(0,count):
    sum += (negate * ( 1 / denominator))
    denominator += 2
    negate *= -1

total= 4 * sum
print("We calculated that {:d} times Leibniz was {:.8f}".format(count,total))
print("The true PI is {:.8f}".format(math.pi))
print("The diffecent is {:.8f}".format(total - math.pi))
