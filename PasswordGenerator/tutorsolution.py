import string, random

print("welcome to password generator")
length = int(input("Enter the length of password"))


lower = string.ascii_uppercase
upper = string.ascii_lowercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols
sample = random.sample(all, length)
password = "".join(sample)
print(password)
