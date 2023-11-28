# write a code that prints the number of words entered by user

word = input("enter word or text?\n")
words = word.split()
print("your text has {} ".format(len(words)))

