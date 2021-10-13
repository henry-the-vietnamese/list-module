#!/usr/bin/env python3

#
# File:         list_function_test.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         13/10/2021
# Description:  Test file for list_function.py to see check if each predefined function works properly.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.
#


import list_function


def assertEqual(result, expected, worth):
    try:
        global marks, max_marks
        print("Expected:", expected)
        print(f"{'Got':>8s}: {result}")
        if expected == result:
            marks += worth
            marks = int(marks) if float(marks).is_integer() else marks
            print(f"\tPASSED {marks}/{max_marks} (+{worth})")
            return True
        else:
            print("\tFAILED")
            return False
    except Exception as e:
        print("\tFAILED")
        print(e)
    return False


def has_sequence(string, letters):
    try:
        print('Testing', string, 'contains', letters)
        index = -1
        for letter in letters:
            new_index = string.find(letter, index+1)
            if new_index > index:
                index = new_index
            else:
                return False
        return True
    except Exception as e:
        print(e)
    return False


# --- Start Test Code --- #
print("START TESTING")

marks = 0.0
max_marks = 26

print("\nSIZE")
str_list = ['r', 'i', 'n', 'g', 'i', 'n', 'g']
assertEqual(list_function.size(str_list), 7, 1)
empty = []
assertEqual(list_function.size(empty), 0, 1)
num_list = [1, 7, 2, 3, 7, 7]
assertEqual(list_function.size(num_list), 6, 1)

print("\nTO_STRING")
str_list = ['r', 'i', 'n', 'g', 'i', 'n', 'g']
if not assertEqual(list_function.to_string(str_list), 'r, i, n, g, i, n, g', 1.5):
    if not assertEqual(list_function.to_string(str_list), 'r, i, n, g, i, n, g, ', 0.5):
        assertEqual(list_function.to_string(str_list), 'r, i, n, g, i, n, g,', 0.5)
if not assertEqual(list_function.to_string(str_list, sep='-'), 'r-i-n-g-i-n-g', 1.5):
    assertEqual(list_function.to_string(str_list, sep='-'), 'r-i-n-g-i-n-g-', 0.5)
num_list = [1, 7, 2, 3, 7, 7]
assertEqual(list_function.to_string(num_list), '1, 7, 2, 3, 7, 7', 0.5)
assertEqual(list_function.to_string(num_list, sep=' - '), '1 - 7 - 2 - 3 - 7 - 7', 0.5)

print("\nCOUNT_ITEM")
str_list = ['r', 'i', 'n', 'g', 'i', 'n', 'g']
assertEqual(list_function.count_item('i', str_list), 2, 1)
empty = []
assertEqual(list_function.count_item('z', empty), 0, 1)
num_list = [1, 7, 2, 3, 7, 7]
assertEqual(list_function.count_item(7, num_list), 3, 1)

print("\nSEARCH")
str_list = ['r', 'i', 'n', 'g', 'i', 'n', 'g']
assertEqual(list_function.search('g', str_list), 3, 1)
assertEqual(list_function.search('z', str_list), None, 1)
num_list = [1, 7, 2, 3, 7, 7]
assertEqual(list_function.search(7, num_list), 1, 1)

print("\nINSERT_ITEM")
str_list = ['one','three','four', 'five', 'six']
new_list = list_function.insert_item('two', 1, str_list)
assertEqual(new_list, ['one', 'two', 'three','four', 'five', 'six'], 1)
str_list = ['i', 't']
new_list = list_function.insert_item('s', 7, str_list)
assertEqual(new_list, ['i', 't', 's'], 1)
new_list = list_function.insert_item('s', -1, str_list)
assertEqual(new_list, ['s', 'i', 't'], 1)
new_list = list_function.insert_item('p', 0, str_list)
assertEqual(new_list, ['p','i', 't'], 1)
num_list = [1, 3, 4, 5, 6]
new_list = list_function.insert_item(2, 1, num_list)
assertEqual(new_list, [1, 2, 3, 4, 5, 6], 1)

print("\nREMOVE_INDEX")
str_list = ['r','i','n','g']
new_list = list_function.remove_index(2, str_list)
assertEqual(new_list, ['r', 'i', 'g'], 1)
new_list = list_function.remove_index(-1, str_list)
assertEqual(new_list, ['i', 'n', 'g'], 1)
new_list = list_function.remove_index(10, str_list)
assertEqual(new_list, ['r','i', 'n'], 1)
empty = []
new_list = list_function.remove_index(0, empty)
assertEqual(new_list, [], 1)
num_list = [1, 3, 4, 5, 6]
num_list = list_function.remove_index(1, num_list)
assertEqual(num_list, [1, 4, 5, 6], 1)

print("\nGET_UNIQUE")
str_list = ['a', 'a', 'b', 'b', 'a', 'c', 'd', 'b', 'c']
new_list = list_function.get_unique(str_list)
assertEqual(new_list, ['a', 'b', 'c', 'd'], 2)

num_list = [1, 1, 3, 2, 2, 3, 4, 1]
new_list = list_function.get_unique(num_list)
assertEqual(new_list, [1, 3, 2, 4], 1)

print("\nEND TESTING\n")
marks = int(marks) if float(marks).is_integer() else marks
print(f"Final Result: {marks}/{max_marks}\n\n")

if marks == max_marks:
    print("Well done programmer!")
    print("Time to get started on part 2!")
elif marks > max_marks / 2:
    print("Good work, keep it up!")
else:
    print("You can use this test driver to check your progress.")
    print("Compare the expected result to the actual result.")
    print("This should help guide you.")
