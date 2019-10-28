# 氣泡排序 Bubble Sort
# https://www.george.tw

my_list= [16,62,93,94,65,96]

for i in range (len(my_list) -1):
    for j in range(len(my_list)-1):
        if my_list[j] < my_list[j+1]:
            my_list[j],my_list[j+1] =my_list[j+1],my_list[j]
print (my_list)

