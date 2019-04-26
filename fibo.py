#費氏函數
#https://www.george.tw/2019/04/25/%E8%B2%BB%E6%B0%8F%E6%95%B8%E5%88%97-fibonacci-sequence/
fibos=[1,1]
for i in range (2 , 10 ): 
   fibos.append(fibos[-1] + fibos[-2])
print (fibos)
