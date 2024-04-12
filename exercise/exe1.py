# Write a python program that takes a name and returns a greeting in the form of a string.


name = input("enter your name: ")


def hello_there(name):
    return "Hello {}".format(name)


print(hello_there(name))
