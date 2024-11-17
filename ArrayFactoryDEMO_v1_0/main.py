from createArray import CreateArray
from math import sqrt
import numpy as np

"""
Data preparation: 
    - Two lists are created: one with numbers (list_of_int) and one with text versions (list_of_str_nums). 

Determination of dividers: 
    - Calculates list length divisors to use to format arrays later. 

To create empty arrays: 
    - Empty, appropriately sized NumPy arrays are created for objects (ObjectArray) and text (StringArray). 

To upload arrays: 
    - Fills empty arrays with items from lists. 

Purification: 
    - Removes blank values (None and ''). 

Reformatting: 
    - It converts arrays filled with data into two-dimensional ones based on divisors. 

Target: 
    - The code dynamically creates arrays, populates them with data, and formats them to optimal sizes.
"""


def divisor(n):
    for i in range(1, n):
        if n % i == 0:
            yield i


list_of_ints = [i for i in range(1, 2_001_110+1)]

list_of_str_nums = [str(i) for i in range(1, 1_211_110+1)]

# find the divisors of the list of the values
divisors_of_ints = list(divisor(len(list_of_ints)))
print(divisors_of_ints)
divisors_of_str_numbs = list(divisor(len(list_of_str_nums)))
print(divisors_of_str_numbs)


create_arr_class = CreateArray()
obj_arr = create_arr_class.create_objarray()
string_arr = create_arr_class.create_stringarray()

# create empty arrays with using the "math sqrt" method to adjust the shape size what we will filling below
empty_obj_arr = obj_arr.array(int(sqrt(len(list_of_ints))) + 2, int(sqrt(len(list_of_ints))))
empty_string_arr= string_arr.array(int(sqrt(len(list_of_str_nums))) + 2, int(sqrt(len(list_of_str_nums))))

# reshape the arrays to fill they with values in easy way
reshaped_empty_obj_arr = empty_obj_arr.reshape(-1)
reshaped_empty_str_arr = empty_string_arr.reshape(-1)

# filling the empty reshaped arrays with the values 
for index, value in enumerate(list_of_ints):
    reshaped_empty_obj_arr[index] = value

for index, _ in enumerate(list_of_str_nums):
    reshaped_empty_str_arr[index] = list_of_str_nums[index]
   
# clear the arrays from the "None" and " '' " 
cleared_obj_arr = reshaped_empty_obj_arr[np.where(reshaped_empty_obj_arr != None)]
cleared_str_arr= reshaped_empty_str_arr[np.where(reshaped_empty_str_arr != '')]

# reshape the new array by the value of largest divisors. We can choose the athor values to reshape.
for divisor in divisors_of_ints:
    rows = divisor
    try:
        cols = len(cleared_obj_arr) // rows  # Automatikusan kiszámítja az oszlopok számát
        new_obj_arr = cleared_obj_arr.reshape(rows, cols)
        print(f"Object array reshaped to ({rows}, {cols}):")
        print(new_obj_arr)
    except ValueError:
        print(f"Cannot reshape object array to ({rows}, {cols}).")

for divisor in divisors_of_str_numbs:
    rows = divisor
    try:
        cols = len(cleared_str_arr) // rows
        new_str_arr = cleared_str_arr.reshape(rows, cols)
        print(f"String array reshaped to ({rows}, {cols}):")
        print(new_str_arr)
    except ValueError:
        print(f"Cannot reshape string array to ({rows}, {cols}).")    
        