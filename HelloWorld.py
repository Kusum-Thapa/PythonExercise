# hello world
msg = "hello world"
msg.capitalize()
print(msg)

# int
x = 5
print(x)
print(x + 9)

# float
myfloat = 6.0
print(float(myfloat))

# boolean
the_world_is_flat = True
if the_world_is_flat:
    print("be careful not to fall off!")

#string
hello = "hello"
world = "world"
helloworld : str = hello + " " + world
print(helloworld)

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


