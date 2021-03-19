# File-Name: 02_variable_data-type.py
# Topic: practice set-2
# Author: Tanzil Islam
# Website: http://tislam.xyz
# Github : https://github.com/LazyTanzil
# Created-Date: 17 Mar, 2021
# Created-Time: 15:42:16


# write a  python program to add two number
firstNumber = 25
secondNumber = 30
print("The sum of firstNumber (25) and secondNumber (30) is: ", firstNumber + secondNumber)


# white a python program to find reminder of a number which dived by 2
number = 25  # int(input("Please enter a number: "))
print("the reminder of given number (25) is", number % 2)


# check the type of a variable that has given using type() function

print("15  => ", type(15))
print("this is string  => ", type("this is string"))
print("13.15  => ", type(13.15))
print("True  => ", type(True))
print("None  => ", type(None))

# use comparison operator to find out:  'a' is greater than 'b' or not, take a = 34, b = 80
a = 34
b = 80
print("is A (34) greater than B (80)? : ", a > b)

# write a python program to find average of two number (given by user)
number1 = int(input('Please enter Number One (for average): '))
number2 = int(input('Please enter Number Two (for average): '))
print('the average of two given number is:', number1 + number2 / 2)


# write a python program to show square of a number that has been entered by user
sqrNumber = int(input("Enter a number(for Square) : "))
print("square of that number is: ", sqrNumber * sqrNumber)
