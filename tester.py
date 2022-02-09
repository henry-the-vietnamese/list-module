#!/usr/bin/python3

#
# File:         tester.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         13-Oct-2021
# Description:  Test file for function_defined.py to check if each of its
#               pre-defined function works properly.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.
#


# ------------------------------- Module Import -------------------------------
import function_defined


# ---------------------------- Function Definitions ---------------------------
def assertEqual(result, expected, worth):
    try:
        global marks, MAX_MARK
        print("Expected:", expected)
        print(f"{'Got':>8s}: {result}")
        if expected == result:
            marks += worth
            marks = int(marks) if float(marks).is_integer() else marks
            print(f"\tPASSED {marks}/{MAX_MARK} (+{worth})")
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


# ------------------------------- Main Function -------------------------------
if __name__ == '__main__':
    # --- Start Testing Code --- #
    print("-----------------",
          "| START TESTING |",
          "-----------------",
          sep='\n')

    marks = 0.0
    MAX_MARK = 26

    print("\nSIZE")
    str_list = ['r', 'i', 'n', 'g', 'i', 'n', 'g']
    assertEqual(function_defined.size(str_list), 7, 1)
    empty = []
    assertEqual(function_defined.size(empty), 0, 1)
    num_list = [1, 7, 2, 3, 7, 7]
    assertEqual(function_defined.size(num_list), 6, 1)

    print("\nTO_STRING")
    str_list = ['r', 'i', 'n', 'g', 'i', 'n', 'g']
    if not assertEqual(function_defined.to_string(str_list),
                       'r, i, n, g, i, n, g', 1.5):
        if not assertEqual(function_defined.to_string(str_list),
                           'r, i, n, g, i, n, g, ', 0.5):
            assertEqual(function_defined.to_string(str_list),
                        'r, i, n, g, i, n, g,', 0.5)
    if not assertEqual(function_defined.to_string(str_list, sep='-'),
                       'r-i-n-g-i-n-g', 1.5):
        assertEqual(function_defined.to_string(str_list, sep='-'),
                    'r-i-n-g-i-n-g-', 0.5)
    num_list = [1, 7, 2, 3, 7, 7]
    assertEqual(function_defined.to_string(num_list), '1, 7, 2, 3, 7, 7', 0.5)
    assertEqual(function_defined.to_string(num_list, sep=' - '),
                '1 - 7 - 2 - 3 - 7 - 7', 0.5)

    print("\nCOUNT_ITEM")
    str_list = ['r', 'i', 'n', 'g', 'i', 'n', 'g']
    assertEqual(function_defined.count_item('i', str_list), 2, 1)
    empty = []
    assertEqual(function_defined.count_item('z', empty), 0, 1)
    num_list = [1, 7, 2, 3, 7, 7]
    assertEqual(function_defined.count_item(7, num_list), 3, 1)

    print("\nSEARCH")
    str_list = ['r', 'i', 'n', 'g', 'i', 'n', 'g']
    assertEqual(function_defined.search('g', str_list), 3, 1)
    assertEqual(function_defined.search('z', str_list), None, 1)
    num_list = [1, 7, 2, 3, 7, 7]
    assertEqual(function_defined.search(7, num_list), 1, 1)

    print("\nINSERT_ITEM")
    str_list = ['one','three','four', 'five', 'six']
    new_list = function_defined.insert_item('two', 1, str_list)
    assertEqual(new_list, ['one', 'two', 'three','four', 'five', 'six'], 1)
    str_list = ['i', 't']
    new_list = function_defined.insert_item('s', 7, str_list)
    assertEqual(new_list, ['i', 't', 's'], 1)
    new_list = function_defined.insert_item('s', -1, str_list)
    assertEqual(new_list, ['s', 'i', 't'], 1)
    new_list = function_defined.insert_item('p', 0, str_list)
    assertEqual(new_list, ['p','i', 't'], 1)
    num_list = [1, 3, 4, 5, 6]
    new_list = function_defined.insert_item(2, 1, num_list)
    assertEqual(new_list, [1, 2, 3, 4, 5, 6], 1)

    print("\nREMOVE_INDEX")
    str_list = ['r','i','n','g']
    new_list = function_defined.remove_index(2, str_list)
    assertEqual(new_list, ['r', 'i', 'g'], 1)
    new_list = function_defined.remove_index(-1, str_list)
    assertEqual(new_list, ['i', 'n', 'g'], 1)
    new_list = function_defined.remove_index(10, str_list)
    assertEqual(new_list, ['r','i', 'n'], 1)
    empty = []
    new_list = function_defined.remove_index(0, empty)
    assertEqual(new_list, [], 1)
    num_list = [1, 3, 4, 5, 6]
    num_list = function_defined.remove_index(1, num_list)
    assertEqual(num_list, [1, 4, 5, 6], 1)

    print("\nGET_UNIQUE")
    str_list = ['a', 'a', 'b', 'b', 'a', 'c', 'd', 'b', 'c']
    new_list = function_defined.get_unique(str_list)
    assertEqual(new_list, ['a', 'b', 'c', 'd'], 2)

    num_list = [1, 1, 3, 2, 2, 3, 4, 1]
    new_list = function_defined.get_unique(num_list)
    assertEqual(new_list, [1, 3, 2, 4], 1)

    print("\n---------------",
          "| END TESTING |",
          "---------------\n",
          sep='\n')
    marks = int(marks) if float(marks).is_integer() else marks
    print(f"Final Result: [{marks}/{MAX_MARK}] \n")

    if marks == MAX_MARK:
        print("Well done 'list' master!")
    elif marks > MAX_MARK / 2:
        print("Good work, keep it up!")
    else:
        print("Use this test driver to check your progress.",
              "Compare the expected result to the actual result.",
              "This should help guide you.",
              sep='\n')
