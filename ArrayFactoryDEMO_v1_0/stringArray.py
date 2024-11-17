from unknownArray import UnknownArray
from numpy import array, empty

"""
Similar to ObjectArray, but here the array stores strings up to 8 characters long. 
    - dtype="<U8"  Unicode string, up to 8 characters long.

"""


class StringArray(UnknownArray):
    #Array of strings
    @staticmethod
    def array(size1, size2) -> array:
        return empty(shape=(size1, size2), dtype="<U8")
    
    