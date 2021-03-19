# File-Name: 06_conditional_logic
# Topic: Problem Solving on Conditional logic (code with harry)
# Author: Tanzil Islam
# Website: http://tislam.xyz
# Github : https://github.com/LazyTanzil
# Created-Date: 3/18/2021
# Created-Time: 12:52 PM

import math  # used floor function

# 1. write a python program that find greatest number of four number given by the user
numbers = input("Enter four number (separated by space) to find the greatest number: ")
allNumber = list(numbers.split(" "))
greatestNumber = int(allNumber[0])

if greatestNumber < int(allNumber[1]):
    greatestNumber = int(allNumber[1])
if greatestNumber < int(allNumber[2]):
    greatestNumber = int(allNumber[2])
if greatestNumber < int(allNumber[3]):
    greatestNumber = int(allNumber[3])
print("the greatest number between following number is", allNumber, "is:", greatestNumber, "\n")

# 2. write a program to find weather a student is fail or pass, its require 40% mark and 33% mark each subject to pas. assume there is 3 subject. takes marks from user

studentMarks = input("enter 3 students mark to see his result (separated by space): ").split(" ")
highestMark = 100
markOfSubjectOne = int(studentMarks[0])
markOfSubjectTwo = int(studentMarks[1])
markOfSubjectThree = int(studentMarks[2])
IsAbove33Percent = ((markOfSubjectOne / highestMark) * 100) > 33 and ((markOfSubjectTwo / highestMark) * 100) > 33 and (
            (markOfSubjectThree / highestMark) * 100) > 33

if IsAbove33Percent:
    totalMark = markOfSubjectOne + markOfSubjectTwo + markOfSubjectThree
    totalPretence = (totalMark / 300) * 100
    print(
        f"You got {totalMark} out of {highestMark * 3}. \nthat's is {math.floor(totalPretence)}%. So your are  {'passed. congratulation!' if totalPretence > 40 else 'failed. better luck next time'}",
        "\n")

else:
    print(f"you got less than 33% in a subject :(. good luck for next time", "\n")

# 3. a spam comment is defined as a text is containing keywords
# "make a Lot of money", "buy now", "click now"
# write a program to detect those type of comment

spamKeywords = ["make a Lot of money", "buy now", "click now"]
commentList = ["nice video, you have cleared my all confusion, buy now, you are a alien boss!, click now", "click now"]
if commentList in spamKeywords:
    print("excuse me sir! we got some spam comment on your youtube comment section", "\n")
else:
    print("Hurrah!, your comment list is clear", "\n")

# 4. write a python program which found out weather a username is contains 10 character or not
userName = input("Please enter a userName: ")
print("your userName is too sort" if len(userName) < 10 else "Your username contains 10 character :>", "\n")

# 5. write python program which found out weather a name is present on a list or not
nameList = ["Tanzil", "Maserati", "Adib", "Samir"]
name = "Tanzil"  # input("enter your name: ")
if name in nameList:
    print("{} present in {}".format(name, nameList), "\n")
else:
    print("{} name doesn't present in {}".format(name, nameList), "\n")

# 6. write a python program that's telling you a grade of a student
'''
    90 - 100 --> ex
    80 - 89 --> A
    70 - 79 --> B
    60 - 69 --> C
    50 - 59 --> D
    bellow 50 --> F
'''
studentMark = int(input('Enter a Mark that you got in you last exam'))
if 90 <= studentMark <= 100:
    print("you Got EXCELLENT! xD")
elif 80 <= studentMark <= 89:
    print("you Got A!")
elif 70 <= studentMark <= 79:
    print("you Got B :>")
elif 60 <= studentMark <= 69:
    print("you Got C :|")
elif 50 <= studentMark <= 59:
    print("you Got D :3")
elif 50 <= studentMark <= 59:
    print("you Got Failed :(")


# 7. write a python program that's found out weather a post is talking about Tanzil or not
postCaption = "Hi there!, we went to cinemaplax today. we have Tanzil, Adib and samir "
print("Your name is in the post" if postCaption.find("Tanzil") != -1 else "They didn't mention your name is the post",
      "\n")
