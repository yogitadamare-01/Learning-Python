#if-else
a=int(input("enter the year:"))
if(a%4==0):
    print("the",a,"is a leap year")
else:
    print("the",a,"is not a leap year")

#elif statement
num=int(input("enter the number"))
if(num>0):
    print(num,"is positive")
elif(num==0):
    print(num,"is equal to zero")
else:
    print(num,"is negative")
    
#nested if
b=int(input("enter the number"))
if(b>0):
    print("the number is positive")
    if(b%2==0):
        print("the",b,"is a even number")
    else:
        print("the",b,"is a odd number")
