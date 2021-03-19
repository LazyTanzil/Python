# File-Name: 04_dictionary_sets
# Topic: Practicing some dictionary and sets related problem
# Author: Tanzil Islam
# Website: http://tislam.xyz
# Github : https://github.com/LazyTanzil
# Created-Date: 3/18/2021
# Created-Time: 7:01 AM

# 1. write a python program to create a  dictionary. there will be english words meaning. also make sure there is a option user to decide the word
dictionary = {
    "name": "a word or set of words by which a person or thing is known, addressed, or referred to.",
    "python": "a high-level general-purpose programming language.",
    "programmer": "a person who writes computer programs."
}
user_word = input("choice a word between (name, python, programmer) to see their word meaning: ")
print(dictionary.get(user_word), "\n")

# 2. write a python program to input 8 numbers and display their unique numbers
numberList = input("please enter 8 number (separated by comma)")
uniqueNumbers = {numberList.strip().replace(",", '''","''')}
print("the unique numbers are:", uniqueNumbers, "\n")

# 3. can we have a sets of 18 integer and 18 number as there value?
str_int_set = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    # {1: "one",
    # {2: "two"},
    # {3: "three"},
    # {4: "four"},
    # {5: "five"},
    # {6: "six"},
    # {7: "seven"},
    # {8: "eight"},
    # {9: "nine"},
    # {10: "ten"},
    # {11: "eleven"},
    # {12: "twelve"},
    # {13: "thirteen"},
    # {14: "fourteen"},
    # {15: "fifteen"},
    # {16: "sixteen"},
    # {17: "seventeen"}
    # {18: "eighteen"}
}
user_Number = int(input('Enter a number between 1 to 18'))
print(str_int_set.get(user_Number), "\n")

'''
# 4. what will be length of these following set 
length_set = set()
length_set.add(20)
length_set.add(20.0)
length_set.add(20)
'''
length_set = set()
length_set.add(20)
length_set.add(20.0)
length_set.add(20)
print(len(length_set), "\n")

# 5. what is the type of s = {}

print("the type of 's = {}' is:", type({}))

# 6. create an empty dictionary. allow four friends to add their favorite language as value on it and use name as their keys assume that the names are unique


def myFriends(Message):
    print(Message)
    friend_dict = {}
    per_item = input("Enter a name and give a programming language name (separated by comma) like: john, c \n").split(',')
    friend_dict.update({per_item[0]: per_item[1]})
    per_item = input("Enter a name and give a programming language name (separated by comma) like: john, c \n").split(',')
    friend_dict.update({per_item[0]: per_item[1]})
    per_item = input("Enter a name and give a programming language name (separated by comma) like: john, c \n").split(',')
    friend_dict.update({per_item[0]: per_item[1]})
    per_item = input("Enter a name and give a programming language name (separated by comma) like: john, c \n").split(',')
    friend_dict.update({per_item[0]: per_item[1]})
    print(friend_dict, "'\n")


myFriends("we will be make a dictionary. do following")

# 7. is two friends name are same. then what will be the output? (program 6)
myFriends("we will be testing what will happens if two of your friends name are same (previous program)")

# 8. what will happens if two of friends  programming language are same (program 6)
myFriends("we will be testing what will happens if two of your friends favorite language are same (previous program)")

# 9. can you change the value which is inside on a sets --> mySet = { 8, 7, 12, "Tanzil", [1,2]}
mySet = {8, 7, 12, "Tanzil", [1, 2]}
# mySet[0] = 0 --> failed
print(mySet)
