# Is used for single line comment
""" These double quotations is used for 
multi line comments"""
# Simple printing format
print("Hello World")
print("Geek for geek")

#Input /output
"""str1=input("Enter your name: ")
print(str1)
#Input is Always taken as a string
age=int(input("Enter your age: "))
print(age)
print(str1);print(age)"""

#Type() is used to determine the datatype of variable
x = 10         # int
y = 3.14       # float
z = 1 + 2j     # complex

print(type(x))
print(type(y))
print(type(z))

# Boolean
flag = True
print(type(flag))

#Strings
mainstring="This is a message"
print(mainstring)

substring=mainstring[0:7]
print(substring)

newlinestring="This is a message \nIts a new line"
print(newlinestring)

escapecharstring="Using single of double quotations within a string \"like this\""
print(escapecharstring)

print(mainstring[0])
print(mainstring[1])
print(mainstring[2])
print(mainstring[3])

#Lists
list1=[1,2,3,4,5,6,7,8,9,9.1,"string"]
print(list1)

print(list1[0:3])
print(list1[2:6])
print(list1[-9:-1])

#tuples (Immutable)
tuple1=(1,5,6,7)
print(tuple1)
#if else
age=int(input("Enter your age: "))
if age<18:
    print("You are a minor")
elif age>=18 and age<=40:
    print("You are an adult")
elif age>40 and age<=60:
    print("You are slowly getting old")
else:
    print("You are old man")
