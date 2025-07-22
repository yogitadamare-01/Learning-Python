#list methods

#sort()
l=[1,9,2,8,5,6]
l.sort()
print(l)
l.sort(reverse=True)
print(l)
 
#reverse()
l1=[3,7,9,10,4,3,2,5]
l1.reverse()
print(l1)

#index()
l2=[1,2,3,4,5]
print(l2.index(3))

#count()
l3=[1,2,3,4,2,6,2,5,2,8]
print(l3.count(2))

#copy()
l4=[1,9,7,6,5]
m=l4.copy()
print("m=",m)

#append()
l5=[10,20,30,40,50]
l5.append(60)
print("l5=",l5)

#insert
l6=[1,2,4,5,6]
print("l6",l6)
l6.insert(2,3)
print(l6)

#extend()
l7=[100,200,300,400]
m=[1,2,3,4,5]
l7.extend(m)
print(l7)

#concatenattion of two strings

l8=[90,80,70,60]
m2=[10,20,30,40,50]
k=m2+l8
print("the concatenation of list l8 and list m2 is=",k)
