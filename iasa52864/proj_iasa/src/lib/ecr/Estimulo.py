from abc import ABC, abstractmethod

'''

    A classe Estimulo representa um estimulo no ambiente.

    Esta classe é uma classe abstrata que define a interface para os estimulos,
    que são responsáveis por detetar eventos no ambiente.

'''
class Estimulo(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def detetar(self, percepcao):
        pass