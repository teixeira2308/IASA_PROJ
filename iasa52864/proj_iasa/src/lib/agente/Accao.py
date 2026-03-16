from abc import ABC, abstractmethod

"""
    A ação é a "saída" do sistema de controlo, representado uma intenção de alterar o estado do ambiente.
 """

class Accao(ABC):
    """ Interface que representa uma ação """

    def __init__(self, agente, comando):
        pass

