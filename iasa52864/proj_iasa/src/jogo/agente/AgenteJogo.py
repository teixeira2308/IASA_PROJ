from abc import ABC, abstractmethod

"""
    Atua como o controlador do topo do sistema. É a classe responsável por instanciar o AmbienteJogo e o Agente.
    Garante que o ciclo de vida do programa seja mantido.
"""

from lib.agente.Agente import Agente

class AgenteJogo(Agente):
    def __init__(self, ambiente, controlo):
        self.__ambiente = ambiente
        super().__init__(controlo)

    def percecionar(self):
        """ Obter as perceções do ambiente. """
        return self.__ambiente.percecionar(self)

    def actuar(self):
        """ Executar passo de pensamento """
