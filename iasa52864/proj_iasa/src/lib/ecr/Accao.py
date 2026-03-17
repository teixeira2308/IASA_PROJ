from lib.agente.Accao import Accao

class Accao(Accao):
    def __init__(self, prioridade):
        self._prioridade = prioridade
        pass

    @property
    def _prioridade(self):
        return self._prioridade