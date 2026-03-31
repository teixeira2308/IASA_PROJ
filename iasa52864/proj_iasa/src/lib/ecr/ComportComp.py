from abc import ABC, abstractmethod

'''

    A classe ComportComp representa o comportamento composto do agente.
    Esta classe é responsável por gerir um conjunto de comportamentos reativos, 
    e selecionar a ação a executar com base nas perceções do ambiente.
'''

class ComportComp(ABC):
    def __init__(self, comportamentos):
        self.comportamentos = []

    def ativar(self, percepcao):
        pass

    @abstractmethod
    def selecionar_acao(self, acoes):
        pass