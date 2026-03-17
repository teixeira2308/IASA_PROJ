from abc import ABC, abstractmethod

class ComportComp(ABC):
    def __init__(self,):
        self.comportamentos = []

    def ativar(self, percepcao):
        
        pass

    @abstractmethod
    def selecionar_acao(self, acoes):
        pass