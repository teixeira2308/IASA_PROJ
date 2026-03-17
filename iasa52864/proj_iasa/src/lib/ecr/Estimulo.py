from abc import ABC, abstractmethod
class Estimulo(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def detetar(self, percepcao):
        pass