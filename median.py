import pytest
import math


def calculate_median(number_list):
    number_list.sort()
    length = len(number_list)
    median_calculated = None
    if length == 1:
        median_calculated = number_list[0]
    elif length % 2 == 0:
        second_index = int(length/2)
        first_index = second_index - 1
        median_calculated = (number_list[first_index] + number_list[second_index])/2
        median_calculated = median_to_int( median_calculated)
    elif length % 2 != 0:
        median_index = math.floor(length/2)
        median_calculated = number_list[median_index]

    return median_calculated


def median_to_int( original_median):
    if original_median.is_integer():
        return int(original_median)
    else:
        return original_median


def print_median (median_value):
    print("This is the median of the list of numbers: " + str(median_value))


def print_error():
    print("Wrong!")


def add_to_median_list(number_list, new_value):
    list_numbers.append(new_value)
    median_value = calculate_median(number_list)
    print_median(median_value)


def remove_to_median(number_list, new_value):
    if new_value in number_list:
        number_list.remove(new_value)
        if not list_numbers:
            print_error()
        else:
            median = calculate_median(number_list)
            print_median(median)
    elif new_value not in number_list:
        print_error()
    elif len(number_list) == 0:
        print_error()


str_number_operations= input("Enter number of operations: ")
list_numbers = list()
number_operations = int(str_number_operations)
for operation in range(0,number_operations):
    input_operation = input("Enter operation:")
    tokens_operation = input_operation.split(' ')
    command = tokens_operation[0]
    value = int(tokens_operation[1])
    if command == 'a':
        add_to_median_list(list_numbers, value)
    if command == 'r':
        remove_to_median(list_numbers,value)



