from abc import ABC, abstractmethod

'''

    A classe Comportamento representa o comportamento reativo do agente.

    Esta classe é uma classe abstrata que define a interface para os comportamentos reativos do agente.
'''

class Comportamento(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def ativar(self, percepcao):
        pass