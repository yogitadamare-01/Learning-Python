print("the following pattern is displaying")
for i in range(1,5):
    for j in range(0,i):
        if(j%2!=0):
            print("*",end=" ")
        else:
            print("#", end=" ")

    print("\n")
