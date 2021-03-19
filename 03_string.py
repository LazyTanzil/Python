# File-Name: 03_string 
# Topic: Practicing some problem about string
# Author: Tanzil Islam 
# Website: http://tislam.xyz 
# Github : https://github.com/LazyTanzil 
# Created-Date: 3/17/2021 
# Created-Time: 6:59 PM

import datetime  # used in letter template (problem 2)

# 1.write a python program display user name followed by "Good afternoon," using input()
user_name = input('Please enter your Name: ')
greeting = "Good afternoon, " + user_name
print(greeting)


print()  # for extra spaces


'''
 2. write a program to fill this template  
 dear <Name>,
        your are selected
        <Date>
'''
template_letter = ''' 
dear {},
        we age glad to inform you that your last competition  performance was awesome. you did pretty well 
        So, your are selected for your dream job :>
        for more information check out your email 
        {}'''.format(user_name, datetime.datetime.today())
print(template_letter)


print()  # for extra spaces


# 3.write a program which can detect double space in string
string = "Hello  there this is a program which  can detect double  space on this line"
string_count = string.count("  ")
string_firstFind = string.find("  ")
print(string)
print("in this line total double space: {} \nand first double space founded at: {}".format(string_count, string_firstFind))


print()  # for extra spaces


# 4. replace all double space to single space (from problem 3)
print("now I'm Replacing all double space to single space")
print(string.replace("  ", " "))


print()  # for extra spaces


# 5.format the following letter using special sequence character  -> letter = "Hey Harry, this python course was nice. thanks!"
letter = "Hey Harry,\n\tthis python course was nice.\n\t thanks!"
print(letter)
