# File-Name: 08_function_recursive
# Topic:  Problem solving on Function and recursive (codeWithHarry)
# Author: Tanzil Islam
# Website: http://tislam.xyz
# Github : https://github.com/LazyTanzil
# Created-Date: 3/19/2021
# Created-Time: 2:42 PM

"""
# 1. write a python program which find the greatest of number using function
def findGreatest(number1, number2, number3):
    greatestNumber = number1
    greatestNumber = number2 if greatestNumber < number2 else greatestNumber
    greatestNumber = number3 if greatestNumber < number3 else greatestNumber
    return greatestNumber


userNumbers = input("Enter three numbers (separated by space) to find the greatest one: \n").split(" ")
print(
    f"the greatest number between {userNumbers} is {findGreatest(int(userNumbers[0]), int(userNumbers[1]), int(userNumbers[2]))}",
    "\n")

# 2. make a python program to convert celsius fahrenheit
celsius = int(input("Enter the celsius to convert in fahrenheit: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius}°C = {fahrenheit}°F", "\n")


# 3. how you prevent python print() function to print a new line at the end
# print("print something", end="")

# def pint(data):  # custom function
#     print(data, end="")
#
#
# pint("hello ")
# pint("world ")




# 4. write a recursive function to calculate the sum of first n natural numbers
# :argument -> n = 5
# :return ->
# 5 + functionName(4)
# 4 + functionName(3)
# 3 + functionName(2)
# 2 + functionName(1) # (if) condition will be true so here recursive will be stop
# ->
# :stack -> 5 + 4 + 3 + 2 + 1


def sumOfN(number):
    if number <= 0 or number == 1:
        return 1
    return number + sumOfN(number - 1)


N_numbers = int(input("Please enter a number to calculate sum of first N natural numbers: \n"))
print(sumOfN(N_numbers), "\n")


# 5. write a python function to print first n number of following pattern
#  ***
#  **  # for n = 3
#  *


def pattern(n=3):
    if n <= 0 or n == 1:
        return print("*" * 1)
    print("*" * n)
    pattern(n - 1)


pattern()


# 6. write a python program to convert inch to centimeter
def inchToCenti(number):
    return number * 2.54


inch = int(input("Enter any inch to convert in centimeter: "))
print(f"{inch} inch = {inchToCenti(inch)} centimeter")



# 7. write a python program to remove a given word from a list and strip it at same time


def remove(word_list, blocked_word):
    updated_list = []

    for word in word_list:
        if word.strip() != blocked_word:
            updated_list.append(word.strip())
    return updated_list


nameList = ["adib", "tanzil", "sadman", "masrafi", "samir", "sourove", "sadman", "redwan"]
word_to_remove = "sadman"

print(remove(nameList, word_to_remove))
"""

# 8. write a python function to print multiplication table of a given number


def multiplication_table(n):
    for i in range(1, 10 + 1):
        print(f"{n} X {i} : {n * i}")


number = 5  # input("Enter a Number to see multiplication table of it")
multiplication_table(number)
