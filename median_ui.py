import median

str_number_operations = input("Enter number of operations: ")
if str_number_operations.isnumeric():
    list_numbers = list()
    number_operations = int(str_number_operations)
    for operation in range(0,number_operations):
        command, value = median.handle_operation()
        if command is not None and value is not None:
            if command == 'a':
                median.add_to_median(list_numbers, value)
            if command == 'r':
                median.remove_to_median(list_numbers,value)
else:
    print("Invalid number of operations.")