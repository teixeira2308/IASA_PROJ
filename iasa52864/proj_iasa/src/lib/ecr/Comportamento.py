from abc import ABC, abstractmethod

class Comportamento(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def ativar(self, percepcao):
        pass