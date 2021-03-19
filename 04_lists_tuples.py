# File-Name: 04_lists_tuples 
# Topic: practicing on List and Tuples related problem
# Author: Tanzil Islam 
# Website: http://tislam.xyz 
# Github : https://github.com/LazyTanzil 
# Created-Date: 3/17/2021 
# Created-Time: 7:33 PM 

# 1. write a program to store 7 fruits name in a list entered by user
fruits_names = input("Enter 7 fruits name (separated by comma): \n")  # "apple,banana,mango,pineapple,watermelon,berry, chocolate"
fruit_list = [fruits_names.strip().replace(",", '''","''')]
print(fruit_list, "\n")


# 2. write a program that accept 6 student mark and store it
student_marks = input("Enter 6 Student mark (separated by comma): \n")  # "89, 50, 20,40,90,99"
student_marks_list = [student_marks.strip().replace(",", '''","''')]
print(student_marks_list, "\n")

# 3. check that if a tuple can changed or not?
check_the_tuple = ("hello", "hi", "good morning", "there")
# check_the_tuple[0] = 'there' ==> failed
# check_the_tuple.__add__("can you add me?") ==> failed
# print(check_the_tuple.count("hello"))

# 4. write a program to sum a list of 4 numbers
sum_list = [20, 50, 15, 10]
total_sum = sum(sum_list)  # sum_list[0] + sum_list[1] + sum_list[2] + sum_list[3]
print("sum of following numbers", sum_list, "is:", total_sum, "\n")

# 5. write a program that count zero in following tuple (7, 0, 8, 0, 0, 9)
zero_tuple = (7, 0, 8, 0, 0, 9)
print("Number of Zero in following tuple", zero_tuple, "is:", zero_tuple.count(0))
