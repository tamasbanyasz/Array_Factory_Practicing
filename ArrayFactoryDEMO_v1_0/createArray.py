from arrayFactroy import ArrayFactory
from objectArray import ObjectArray
from stringArray import StringArray


class CreateArray(ArrayFactory):
    def create_objarray(self) -> ObjectArray:
        return ObjectArray()
    
    def create_stringarray(self) -> StringArray:
        return StringArray()
    
    