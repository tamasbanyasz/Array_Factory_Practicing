from abc import ABC, abstractmethod
from numpy import array

"""
UnknownArray is an abstract class that ensures that all descendants (e.g. ObjectArray, StringArray) must have the array method. 
This is a kind of contract that defines the basic operation.
"""


class UnknownArray(ABC):
    #Basic abstract class
    @abstractmethod
    def array(self) -> array:
        pass

