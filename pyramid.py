#x=1
n=int(input('Enter the no. : '))
for i in range(1,n+1,1):
    for space in range(1,n-i+1):
        print(" ",end="")
    for j in range(1,i+1,1):
        print("* ",end="")
        #print(x,end=" ")
        #x=x+1
    print("")
