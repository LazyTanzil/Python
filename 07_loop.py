# File-Name: 06_loop
# Topic: Problem solving on python loop (given by CodeWithHarry)
# Author: Tanzil Islam
# Website: http://tislam.xyz
# Github : https://github.com/LazyTanzil
# Created-Date: 3/18/2021
# Created-Time: 5:06 PM

# 1. write a program that's show Multiplication table of A given number by user using for loop
tableOf = int(input("Enter a number to see multiplication table of it: "))
for number in range(1, 10 + 1):
    print("{} x {} : {}".format(tableOf, number, (tableOf * number)))

# 2. write a program to greet all the person name stored in a list l1 = ["harry", "subhuman", "sachin", "rahul"] and start with s
greetNameList = ["harry", "subhuman", "sachin", "rahul"]
for name in greetNameList:
    if name.lower().startswith("s"):
        print(name)
else:
    print("these was the name of you list starting with s", "\n")

# 3. attempt problem one using while loop
count = 1
print("attempting problem one using while loop")
while count <= 10:
    print("{} X {} : {} (while loop)".format(tableOf, count, (tableOf * count)))
    count += 1

# 4 . write a program that's find out weather a given number is a prime number or not
primeCheck = int(input("Enter a number to check it's prime number or not: "))
print("prime check", primeCheck)
for num in range(2, primeCheck):
    if primeCheck % num == 0:
        print(f"{primeCheck} is not a prime number. it can be divided by {num}", "\n")
        break
else:
    print(f"{primeCheck} is a Prime Number")

# 5. write a python program that's give you sum of first natural n number (given by user) using while loop
sumOf = int(input("Enter a number to see sum of first natural  numbers: "))
count = 0
total_sum = 0
while count <= sumOf:
    total_sum += count
    count += 1
print("sum of first {} natural number is: {}".format(sumOf, total_sum), "\n")

# 6. write a program to calculate factorial of a given number using for loop
factorial_num = int(input("Enter a number to see sum of first natural  numbers: "))
count = 1
total_sum = 1
while count <= factorial_num:
    total_sum *= count
    count += 1
print("factorial of  {}  number is: {}".format(factorial_num, total_sum), "\n")

# 7. write a python program to print the following start pattern
#        *
#       ***
#      *****
row_Number = 20
for i in range(1, row_Number, 2):  # row of pattern
    for k in range(row_Number - i):  # printing blank spaces before start
        print(" ", end="")
    for j in range(i):
        print("*", end=" ")
    print()

# 8. write a python program to print the following start pattern
#      *
#      **
#      ***
collum_Number = 3
for i in range(1, collum_Number + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
