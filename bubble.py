# 氣泡排序 Bubble Sort
# https://www.george.tw

list= [16,62,93,94,65,96]

for i in range (len(list) -1):
    for j in range(len(list)-1):
        if list[j] < list[j+1]:
            list[j],list[j+1] =list[j+1],list[j]
print (list)     

