# STRING
name="Yogita"
animal="peacock"
self='my name is yogita "i love cricket" '
print(name)
print(self)
#multiline string
multi='''Pune is a major city in Maharashtra, India,
known for its rich history, vibrant culture,
and thriving education and IT sectors.
It's a popular destination for both tourists and students,
offering a blend of historical sites, modern amenities,
and a pleasant climate'''
print(multi)

# to access the character in the string
print(name[2])
print(name[0])

# access the elements by using for loop
for character in self:
    print(character)

#string length
fruit="watermelon"
print(len(fruit))

#slicing of the string
print(fruit[0:5])

print(fruit[-5:-2])
print(fruit[:-7])
print(fruit[:4])
print(fruit[:])
