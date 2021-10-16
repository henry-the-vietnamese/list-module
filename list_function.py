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
    """Docstring for the function size().

    Process a list and return its length.

    Parameters
    ----------
    my_list : list
        List whose elements are to be counted.

    Returns
    -------
    int
        The number of elements the list has.
    """
    LEN = 0         # Initialise a variable to keep track of each element encountered in the list.
    for _ in my_list:
        LEN += 1
    return LEN


def to_string(my_list, sep=', '):
    """Docstring for the function to_string().

    Process a list and return a string.

    Parameters
    ----------
    my_list : list
        List to be converted.
    sep : str, default=', '
        Separate each element when converted.

    Returns
    ------
    str
        Result of the conversion of the list.
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


def count_item(value, my_list):
    """Docstring for the function count_item().

    Take one of a list's elements and return how many times that element occurs in the list.

    Parameters
    ----------
    value : str
        The element to be counted.
    my_list : list
        The list whose elements are to be counted.

    Returns
    -------
    int
        The occurrences of the specified value.
    """




