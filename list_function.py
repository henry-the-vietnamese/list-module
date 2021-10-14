#!/usr/bin/env python3

#
# File:         list_function.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         13/10/2021
# Description:  Define some of the list functions.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.
#



def size(my_list):
    """ Function size()

    :param my_list: List whose elements are to be counted.
    :param type: list
    :returns: The number of elements contained in the list.
    "rtype: int
    """
    LEN = 0         # Initialise a variable to keep track of each element encountered in the list.
    for _ in my_list:
        LEN += 1
    return LEN



def to_string(my_list, sep=', '):
    """ Function to_string()

    :param my_list: List to be converted.
    :type my_list: list
    :returns: Result of the conversion of the list.
    :rtype: str
    """

    if size(my_list) == 0:      # If the list contains no element (an empty list), returns an empty string.
        return ''
    else:
        string = ''         # Initialise an empty string to be appended later.
        COUNT = 1           # Initialise a variable to keep track of the location of the current element being iterated.
        for i in my_list:
            if size(my_list) != COUNT:
                string += (str(i) + sep)
            else:
                string += (str(i))
            COUNT += 1
        return string




