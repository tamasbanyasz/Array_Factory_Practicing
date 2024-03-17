from createArray import CreateArray
from math import sqrt
import numpy as np


def divisor(n):
    for i in range(1, n):
        if n % i == 0:
            yield i


list_of_int = [i for i in range(1, 2_001_110+1)]

list_of_str_nums = [str(i) for i in range(1, 1_211_110+1)]

# find the divisors of the list of the values
div_int = list(divisor(len(list_of_int)))
print(div_int)
div_str = list(divisor(len(list_of_str_nums)))
print(div_str)


arr_class = CreateArray()
obj_arr = arr_class.create_objarray()
string_arr = arr_class.create_stringarray()

# create empty arrays with using the "math sqrt" method to adjust the shape size what we will filling below
empty_obj_arr = obj_arr.array(int(sqrt(len(list_of_int))) + 2, int(sqrt(len(list_of_int))))
empty_string_arr= string_arr.array(int(sqrt(len(list_of_str_nums))) + 2, int(sqrt(len(list_of_str_nums))))

# reshape the arrays to fill they with values in easy way
reshaped_empty_obj_arr = empty_obj_arr.reshape(-1)
reshaped_empty_str_arr = empty_string_arr.reshape(-1)

# filling the empty reshaped arrays with the values 
for index, value in enumerate(list_of_int):
    reshaped_empty_obj_arr[index] = value

for index, _ in enumerate(list_of_str_nums):
    reshaped_empty_str_arr[index] = list_of_str_nums[index]
   
# clear the arrays from the "None" and " '' " 
cleared_obj_arr = reshaped_empty_obj_arr[np.where(reshaped_empty_obj_arr != None)]
cleared_str_arr= reshaped_empty_str_arr[np.where(reshaped_empty_str_arr != '')]

# reshape the new array by the value of largest divisors. We can choose the athor values to reshape.
new_obj_arr= cleared_obj_arr.reshape(div_int[-1], -1)
print(new_obj_arr)
new_str_arr = cleared_str_arr.reshape(div_str[-1], -1)
print(new_str_arr)
    
        