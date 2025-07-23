#Bubble Sorting
list1=[9,7,4,6,8,3,4,5,1,2]
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]> list1[j]:
            temp=list1[i]
            list1[i]=list1[j]
            list1[j]=temp

print("the sorted list is",list1)
