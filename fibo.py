#費氏函數

fibos=[1,1]
for i in range (2 , 10 ): 
   fibos.append(fibos[-1] + fibos[-2])
print (fibos)
