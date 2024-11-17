from arrayFactroy import ArrayFactory
from objectArray import ObjectArray
from stringArray import StringArray

"""
The CreateArray class implements the ArrayFactory abstract class. 
Creates the ObjectArray and StringArray objects in the given methods. 
This is the specific factory that follows the Factory Method pattern.

"""


class CreateArray(ArrayFactory):
    #Factory implementation
    def create_objarray(self) -> ObjectArray:
        return ObjectArray()
    
    def create_stringarray(self) -> StringArray:
        return StringArray()
    
    