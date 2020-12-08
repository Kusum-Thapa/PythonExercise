# hello world
msg = "hello world"
msg.capitalize()
print(msg)

sentence = "what's going on?"
sentence = 'what\'s going on?'
greeting = ("Hello"
            "My name is"
            " Kusum")  # concatenation
print(sentence)
print(greeting)

docstring = """
Hello
this
is 
a 
docstring
"""
print(docstring)  # take a new line

word = "Python"
for letter in word:
    print(letter)

# int
x = 5
print(x)
print(x + 9)

y = 100_000_000_000  # for large numbers use _
print(type(y))
print(int(y))

# float
myfloat = 6.0
print(type(myfloat))
print(float(myfloat))

# boolean
the_world_is_flat = True
if the_world_is_flat:
    print("be careful not to fall off!")

# string
hello = "hello"
world = "world"
hello_world: str = hello + " " + world
print(hello_world)

# Sequences
List = ['Milk', 'Bread', 'Eggs', 'Eggs', False, True, {}]  # this can be modified , any types of data type - mutable
Tuples = ('Milk', 'Bread', 'Eggs')  # this cannot be modified , immutable
Sets = {'Milk', 'Bread', 'Eggs', 'Milk', 'Bread'}
String = "Python for Everybody"

List.append('Chocolate')
print(List)
List.reverse()
print(List)
List.remove("Milk")
print(List)
ingredient = List.pop()
print(ingredient)
print(List)

len(Tuples)
print(Tuples)
String.upper()
print(String.upper())
String.isalpha()

for item in List:
    print("List")
    print(item)

for item in Sets:  # only gets the unique ones
    print("Sets")
    print(item)

# Dictionaries or Objects
Dict = {
    'Milk': 'Goats Milk',
    'Eggs': 'Chicken Eggs'
}

person = {
    'name': 'Kusum',
    'sons': 2,
    'family_members': ['Mother', 'Father', 'Husband']
}


# exercise 1
mystring = "hello"
myint = 20
myfloat = 10.0

if mystring == "hello":
    print(f"String: {mystring}")
if isinstance(myfloat, float) and myfloat == 10.0:
    print(f"float: {myfloat:f}")
if isinstance(myint, int) and myint == 20:
    print(f"int: {myint:d}")

# List
myList = [1, 2, 3]

for x in myList:
    if x > 0:
        print(x)

list_item = myList[-1]
print(list_item)  # backwards print

# more List
numbers = [1, 2, 3]
strings = []
names = ["John", "Kayam", "Paanas"]

second_name = names[1]

print(numbers)
print(strings)
print(f"The second name on the names list is : {second_name}")

# python function
course = "Python for Everybody"


def name():
    welcome = "Hello World !"

    def thing():
        print("I am inside the function")


# Function vs Methods
print("Stuff is here", "More stuff in here")  # function - can give parameter

name = "Kusum"
name.upper()  # Method - attached to object

# Property
len(name)  # name is a property

# User Input
# your_name = input("What is your name?")
# print(type(your_name))
# print(your_name)

# age = input("what is your age?")
# print(type(age))

# print
course = "Python for Everybody"
print(f"the course you are in is {course} {course.swapcase()}")

# list matrices
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)
