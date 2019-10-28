#費氏函數
#https://www.george.tw/2019/04/25/費氏數列-fibonacci-sequence/
fibos=[1,1]
for i in range (2 , 10 ):
   fibos.append(fibos[-1] + fibos[-2])
print (fibos)
