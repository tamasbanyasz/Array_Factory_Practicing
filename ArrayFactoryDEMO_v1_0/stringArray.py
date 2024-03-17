from unknownArray import UnknownArray
from numpy import array, empty


class StringArray(UnknownArray):
    @staticmethod
    def array(size1, size2) -> array:
        return empty(shape=(size1, size2), dtype="<U8")
    
    