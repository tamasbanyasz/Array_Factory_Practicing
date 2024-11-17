from abc import ABC, abstractmethod
from objectArray import ObjectArray
from stringArray import StringArray

""" 
ArrayFactory is an abstract class (interface) and it determines that all descendants must implement 
'create_objarray' and 'create_stringarray' methods. These methods are responsible for creating 
arrays of different types (ObjectArray and StringArray).

"""


class ArrayFactory(ABC):
    #Abstract factory class
    @abstractmethod
    def create_objarray(self) -> ObjectArray:
        pass
    
    @abstractmethod
    def create_stringarray(self) -> StringArray:
        pass

    