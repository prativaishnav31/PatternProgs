#This is for Loop pttern program which print numeric pyramid
 
r= int(input("enter the raw: "))

for i in range(r,0,-1):
    for j in range(1,i):
        print(j,end=" ")
    print()

#this is 2nd For Loop program
 
r= int(input("enter the raw: "))

for i in range(r,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()


exit()
