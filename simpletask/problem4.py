age = int(input("enter your age? "))

if age >= 18:
    print("You're eligible to vote")
elif age < 18:
    rem_age = 18 - age
    print("you will be able to participate after {}".format(rem_age))
