print("Tha working of a calculator")
a =float(input("Enter the first number"))
b =float(input("Enter the second number"))
operator= input("enter the operator according to performing operation")

match operator:
    case '+':
        print("the addition of two numbers is = ",a+b)
    case '-':
        print("the substraction of two numbers is=",a-b)
    case '*':
        print("the multiplication of two numbers is=",a*b)
    case '/':
        if (b==0):
            print("the invalid number")
        print("the division of two numbers is=",a/b)
        
    case'//':
        if (b==0):
            print("the invalid number")
        print("the float division of two numbers is=",a//b)
    case '**':
        print("the exponential of two numbers is=",a**b)
