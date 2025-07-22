#tuple
tup=(1,2,3,4)
print(tup)
#slicing of the tuple
tup1=(1,22,34,56,"yogi","sam",True)
print(tup1[:])
print(len(tup1))
print(tup1[:6])
print(tup1[:5:2])

#searching the items in the tuple
tup2=(11,22,33,44,55)
if 22 in tup2:
    print("22 is present on the tuple")
else:
    print("22 is not present on the tuple")


# change the tuple into the list and perform the operations on it

countries=("india","england","australia","Italy","Dubai")
temp=list(countries)
temp.append("america")
temp.pop(3)
temp.insert(2,"thailand")
countries=tuple(temp)
print(countries)

#operations on the tuple
#count()
num=(1,2,3,4,2,3,1,2,4,2,5,2)
cou=num.count(2)
print(cou)
print(len(num))
print(num.index(4,4,9))
