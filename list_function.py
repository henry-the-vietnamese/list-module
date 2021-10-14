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
    # Function size()
    LEN = 0
    for _ in my_list:
        LEN += 1
    return LEN



def to_string(my_list, sep=', '):
    # Function to_string()
    if size(my_list) == 0:
        return ''
    else:
        string = ''
        COUNT = 1
        for i in my_list:
            if size(my_list) != COUNT:
                string += (str(i) + sep)
            else:
                string += (str(i))
            COUNT += 1
        return string




