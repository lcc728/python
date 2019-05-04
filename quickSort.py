#快速排序
#https://www.george.tw

unsort = [77, 88, 44, 33, 22, 99, 66, 55, 11]

def quicksort(unsort, left, right): 
    if left >= right :            
        return

    i = left                      
    j = right                     
    key = unsort[left]                 

    while i != j:                  
        while unsort[j] > key and i < j:   
            
            j -= 1
            
        while unsort[i] <= key and i < j:  
            
            i += 1

        if i < j:                        
            unsort[i], unsort[j] = unsort[j], unsort[i]
    
         

    
    unsort[left],unsort[i] = unsort[i],unsort[left]
    quicksort(unsort, left, i-1)   
    quicksort(unsort, j+1, right)
    
print(unsort)
quicksort(unsort, 0, len(unsort)-1)
print(unsort)
