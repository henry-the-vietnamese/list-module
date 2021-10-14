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

    Parameters
    ----------
    my_list : list
        List whose elements are to be counted.

    Returns
    -------
    int
        The number of elements contained in the list.
    """
    LEN = 0         # Initialise a variable to keep track of each element encountered in the list.
    for _ in my_list:
        LEN += 1
    return LEN



def to_string(my_list, sep=', '):
    """ Function to_string()

    Parameters
    ----------
    my_list : list
        List to be converted.
    sep : **kwargs
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
    # Function count_item()





