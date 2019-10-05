#1
print("#1 ===============================================\n")
for i in range(1,10):
    for j in range(1,10):
        s=  i*j
        print ('%d * %d = %d ' %(i, j , s))

#2
print("#2 ===============================================\n")

for i in range(1,10):
    for j in range(1,10):
        s=  i*j
        print ('%d * %d = %d   ' %(i, j , s), end="")

    print('\n')

#3
print("#3 ===============================================\n")    
k=[1,2,3,4,5,6,7,8,9]

for i in k :
    for j in k:
        s=  i*j
        print ('%d * %d = %d   ' %(i, j , s), end="")

    print('\n')    
#4
print("#4 ===============================================\n")
i=1;
while i < 10:
    j=1
    while j < 10:
        s=  i*j
        print ('%d * %d = %d ' %(i, j , s))
        j += 1

    i += 1
    print('\n')
