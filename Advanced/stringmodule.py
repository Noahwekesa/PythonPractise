# introduction to string modules

import string

#print(string.ascii_letters)
#print(string.digits)
#print(string.punctuation)
 
# methods of string modules

greeting = "hi welcome to my practise files"
print(greeting)

#this will capitalize the fist letter
greeting = greeting.capitalize()
print(greeting)

# join all the list together
my_list = ["tom", "luna", "liz"]
print(my_list)
	
members = ", ".join(my_list)
print(members)

#split method
txt = "welcome to my repo"
x = txt.split()
print(type(x))
