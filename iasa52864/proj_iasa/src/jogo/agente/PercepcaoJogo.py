from lib.agente.Percecao import Percecao

class PercepcaoJogo(Percecao):
    def __init__ (self, evento):
        self.__evento = evento

    @property    
    def evento(self):
        return self.__evento    
    