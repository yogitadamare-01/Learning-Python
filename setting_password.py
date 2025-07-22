password=input(print("enter your password "))

if(password.isalpha()):
    print("this is weak password")
elif(password.isalnum()):
    print("this is moderatepassword")
else:
    print("thos is the strong password")


