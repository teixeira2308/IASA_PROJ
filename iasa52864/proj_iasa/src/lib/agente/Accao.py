from abc import ABC, abstractmethod

"""
    A ação é a "saída" do sistema de controlo, representado uma intenção de alterar o estado do ambiente.

    Esta classe é uma classe abstrata que define a interface para as ações, que são responsáveis por representar
    a intenção do agente de alterar o estado do ambiente.
 """

class Accao(ABC):
    """ Interface que representa uma ação """

    def __init__(self, agente, comando):
        pass

