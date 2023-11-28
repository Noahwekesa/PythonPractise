# password generator

import string
import secrets

letters = string.ascii_letters
digits = string.digits
speciaChars = string.punctuation

alphabet = letters + digits + speciaChars

pwd_length = int(input("Enter the length of the password"))

password = ''
for i in range(pwd_length):
    password += secrets.choice(alphabet)

print(password)
