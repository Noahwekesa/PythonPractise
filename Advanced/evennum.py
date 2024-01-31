def sum_even(n):
    sum = 0
    for i in range(0, n+1):
        if i % 2 == 0:
            print(i)
            sum+=i
    return sum

lst = []
num = int(input("enter number of elements"))
for i in range(0, num):
    ele = int(input())
    lst.append(num)
print(f"sum of all even numbers is {sum_even(num)}")
