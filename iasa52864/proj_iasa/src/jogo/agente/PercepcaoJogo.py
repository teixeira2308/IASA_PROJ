from abc import ABC, abstractmethod

from lib.agente.Percecao import Percecao

class PercepcaoJogo(Percecao):
    def __init__ (self, agenteJogo, evento):
        self._agenteJogo = agenteJogo
        self.evento = evento

    @property    
    def evento(self):
        return self.__evento    
    