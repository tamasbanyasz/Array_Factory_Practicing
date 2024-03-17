from unknownArray import UnknownArray
from numpy import array, empty


class ObjectArray(UnknownArray):
    @staticmethod
    def array(size1, size2) -> array:
        return empty(shape=(size1, size2), dtype='object')
    
    