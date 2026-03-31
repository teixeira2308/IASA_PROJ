from lib.agente.Percecao import Percecao

"""
    Representa o estado sensorial do agente num determinado instante.

    Esta classe encapsula os eventos do AmbienteJogo, permitindo que o sistema 
    de controlo tome decisões baseadas em observações.
"""

class PercepcaoJogo(Percecao):
    def __init__ (self, evento):
        self.__evento = evento

    @property    
    def evento(self):
        return self.__evento    
    