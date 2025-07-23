#Linear Search
customerid=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1100]
flag=0
key=int(input("Enter the Customer Id"))
for i in customerid:
    if(key==i):
        flag=1
        break
    else:
        flag=0
if(flag==1):
    print("Customer Id ",key,"is present")
else:
    print("Customer Id",key," is not present")
