from unknownArray import UnknownArray
from numpy import array, empty

"""
The static array method creates a NumPy array that stores items of type object. 
 - size1, size2: the dimensions of the array. 
 - dtype='object': allows the array to store any type of object.

"""


class ObjectArray(UnknownArray):
    #Array of Objects
    @staticmethod
    def array(size1, size2) -> array:
        return empty(shape=(size1, size2), dtype='object')
    
    