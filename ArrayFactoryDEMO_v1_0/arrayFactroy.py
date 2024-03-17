from abc import ABC, abstractmethod
from objectArray import ObjectArray
from stringArray import StringArray


class ArrayFactory(ABC):
    @abstractmethod
    def create_objarray(self) -> ObjectArray:
        pass
    
    @abstractmethod
    def create_stringarray(self) -> StringArray:
        pass

    