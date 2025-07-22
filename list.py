#list
list1=[1,2,3,4,"Harry",True,87]
print(list1)
print(list1[4])
print(list1[:])

#Check wheather the particular item is present in list or not
marks=[23,45,98,67,45,43]
if 98 in marks:
    print("It is present in list")
else:
    print("it is not present in list")

#Range of index
list2=[7,5,3,9,"harry","won","shaw",2,67]
print(len(list2))
print(list2[:])
print(list2[1:8])
print(list2[4:])
print(list2[:9])
print(list2[1:7])
print(list2[1:7:2])

#List comprehension
list3=[i*i for i in range(10)]
print(list3)
list4=[i for i in range(10)if i%2==0]
print(list4)
