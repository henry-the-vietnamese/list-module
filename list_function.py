#!/usr/bin/python3

#
# File:         list_function.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         13-Oct-2021
# Description:  Define some of the major list functions.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.
#


# ---------------------------- Function Definitions ---------------------------
def size(my_list):
    """Process a list and return its length.

    Parameters
    ----------
    list
        List whose elements are to be counted.

    Returns
    -------
    int
        The number of elements the list has.
    """
    # Initialise a variable to keep track of each element
    # encountered in the list.
    length = 0

    for _ in my_list:
        length += 1

    return length


def to_string(my_list, sep=', '):
    """Process a list and return the string version of it.

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
    # Initialise an empty string to be appended later.
    string = ''

    # Begin the conversion.
    # If the list contains no element (an empty list), returns an empty string.
    if size(my_list) == 0:
        return ''

    else:
        # Initialise a variable to keep track of the location of the current
        # element being iterated.
        count = 1
        for i in my_list:
            if size(my_list) != count:
                string += (str(i) + sep)
            else:
                string += (str(i))
            count += 1
        return string


def count_item(value, my_list):
    """Receive a value and return the occurrences of that value
       in the given list.

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
    # Initialise an accumulator to 0 that counts the occurrences of the value.
    count = 0

    for i in my_list:
        if i == value:
            count += 1

    return count


def search(value, my_list):
    """Receive a value and return the location of that value in the given list.

    Parameters
    ----------
    value : str
        The element to be located.
    my_list : list
        The list to be looped through to locate the specified value.

    Returns
    -------
    int or None
        The location of the value in the list,
        or None if the value is not in the list.
    """
    # Initialise a variable to specify looping form the start.
    index = 0

    # Initialise a placeholder for the index of the value.
    # If the value is not in the list, that is the value returned.
    value_index = None

    # Start the loop of counting.
    for i in my_list:
        if i == value and not value_index:
            value_index = index
        index += 1

    return value_index


def insert_item(value, insert_position, my_list):
    """Receive a list and return a copy with a value inserted into the list
       at the specified index.

    Parameters
    ----------
    value
        The value to be inserted into the list (type not specified).
    insert_position : int
        The index which the value to be inserted into.
        1. If the insert_position is greater than the length of the list,
        insert the value at the end of the list.
        2. If the insert_position is less than or equal to zero, insert the
        value at the start of the list.
    my_list : list
        The original list to be processed to create a new one.

    Returns
    -------
    list
        The copy of my_list that has the new value inserted into
        the specified position.
    """
    # Initialise an empty list to be appended later.
    copy = []

    # Three cases of the value of insert_position.
    if insert_position > size(my_list):
        for index, item in enumerate(my_list):
            copy.append(item)
        copy.append(value)
    elif insert_position <= 0:
        copy.append(value)
        for index, item in enumerate(my_list):
            copy.append(item)
    else:
        for index, item in enumerate(my_list):
            if index != insert_position:
                copy.append(item)
            else:
                copy.append(value)
                copy.append(item)
                index -= 1

    return copy


def remove_index(remove_position, my_list):
    """Receive a list and return a copy with the item at the specified index
       removed from the list.

    Parameters
    ----------
    remove_position : int
        The index where the item is to be removed from the list.
        1. If the remove_position is greater than the length of the list,
        remobe the item at the end of the list.
        2. If the remove_position is less than or equal to zero, remove the
        item at the start of the list.
    my_list : list
        The original list to be processed to create a new one.

    Returns
    -------
    list
        The copy of my_list that has an item at the specified position removed.
    """
    # Initialise an empty list to be appended later.
    copy = []

    # Three cases of the value of remove_position.
    if remove_position > size(my_list):
        for item in my_list[:-1]:
            copy.append(item)
    elif remove_position <= 0:
        for item in my_list[1:]:
            copy.append(item)
    else:
        for index, item in enumerate(my_list):
            if index != remove_position:
                copy.append(item)
            else:
                pass

    return copy


def get_unique(my_list):
    """Receive a list and return a copy which contains only the unique items
       from the original list.

    Parameters
    ----------
    list
        The original list to be processed to create a new one.

    Returns
    -------
    list
        The copy of my_list that does not contain any duplicate items.
    """
    # Initialise an empty list to be appended later.
    no_duplicate = []

    # Initialise a temporary list to keep track of values that has been looped.
    temp = []

    for item in my_list:
        if item not in temp:
            no_duplicate.append(item)
            temp.append(item)

    return no_duplicate
