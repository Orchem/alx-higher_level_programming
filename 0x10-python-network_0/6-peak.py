#!/usr/bin/python3
"""module containing peak funnction"""


def find_peak(list_of_integers):
    """find the peak integer in a sequence"""
    if (len(list_of_integers) == 0):
        return None
    elif (len(list_of_integers) == 1):
        return list_of_integers[0]
    elif (len(list_of_integers) == 2):
        if list_of_integers[0] > list_of_integers[1]:
            return list_of_integer[0]
        else:
            return list_of_integers[1]
    elif (len(list_of_integers) == 3):
        if list_of_integers[0] > list_of_integers[1]:
            return list_of_integers[0]
        elif list_of_integers[2] > list_of_integers[1]:
            return list_of_integers[2]
        else:
            return list_of_integers[1]
    else:
        mid_index = len(list_of_integers) // 2

        if list_of_integers[mid_index] > list_of_integers[mid_index - 1] and\
                list_of_integers[mid_index] > list_of_integers[mid_index + 1]:
            return list_of_integers[mid_index]
        else:
            first_half = list_of_integers[:mid_index]
            second_half = list_of_integers[mid_index:]
            if first_half[0] > first_half[1]:
                return first_half[0]
            count = 1
            while count < (len(first_half) - 1):
                if first_half[count] > first_half[count - 1] and\
                        first_half[count] > first_half[count + 1]:
                    return first_half[count]
                count = count + 1
            count = 1
            while count < (len(second_half) - 1):
                if second_half[count] > second_half[count - 1] and\
                        second_half[count] > second_half[count + 1]:
                    return second_half[count]
                count = count + 1
            if second_half[count] > second_half[count - 1]:
                return second_half[count]
