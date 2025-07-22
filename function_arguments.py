#function argument
#Default argument

def operation(a=4,b=5):
    print("the avrage of a and b is",(a+b)/2)

operation(b=2)

#keyword argument
def cal(c=4,d=3):
      e=c-d
      print(e)
cal(d=2,c=5)


#required argument
def mean(g,h,f=1):
    i=(f+g+h)/3
    print(i)

mean(g=7,h=3)

#variable length argument
def val(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    return sum/len(numbers)
c=val(1,2,3,4,5,54,56,78)
print(c)

    
 
