from abc import ABC, abstractmethod
from numpy import array


class UnknownArray(ABC):
    @abstractmethod
    def array(self) -> array:
        pass

