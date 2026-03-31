from lib.agente.Accao import Accao

"""
    Representa uma intenção de atuação com um mecanismo de decisão por prioridade.

    Em arquiteturas de agentes complexas, a prioridade permite ao sistema de controlo
    resolver conflitos entre múltiplos comportamentos concorrentes.
"""

class Accao(Accao):
    def __init__(self, prioridade):
        self._prioridade = prioridade
        pass

    @property
    def _prioridade(self):
        return self._prioridade