#For loop
name="Yogita"
for w in name:
    print(w)

#2nd example
list=["red","blue","orange","green","white","black"]
for k in list:
    print(k)
    for i in k:
        print(i)

#3rd example
for v in range(5):
    print(v)

#4th example
for j in range(5,11):
    print(j)

#5th example
for o in range(1,17,3):
    print(o)

#while Loop
num=int(input("enter the number"))
while(num>5):
    print(num)
    num=num-1

#while-else loop
num=-5
while(num<0):
    print(num)
    num=num+1
else:
    print("the number is not less than zero")
