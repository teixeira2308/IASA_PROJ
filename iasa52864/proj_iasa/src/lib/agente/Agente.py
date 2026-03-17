""" 
A classe agente é a classe base para os agentes, que lêm o ambiente através de perceções.
O agente atua de forma autónoma num ambiente, ele tem de efetuar o "ciclo" perceção - decisão - ação.
"""

from abc import ABC, abstractmethod


class Agente(ABC): 
    """ Construtor da classe Agente (__init__)  que recebe uma instância da classe Controlo."""
    def __init__ (self, controlo):
        self._controlo = controlo

    """ Abstract method percecionar() que deve ser implementado pelas subclasses,
    para obter as perceções do ambiente. É um método abstrato, ou seja,
    não tem implementação na classe base e deve ser implementado pelas subclasses.
    """

    @abstractmethod
    def _percecionar(self):
        """ Obter as perceções do ambiente. """

    def _actuar(self, accao):
        pass

    """ Método executar() que serve para executar o pensamento do agente."""

    def executar(self):

        """ Executar passo de pensamento """

        percecao = self._percecionar()
        accao = self._controlo.processar(percecao)
        if accao is None:
            self._actuar(accao)


