from lib.agente.Accao import Accao

class AccaoJogo(Accao):
    def __init__(self, agenteJogo, comando):
        self._agenteJogo = agenteJogo
        self.comando = comando

    @property
    def comando(self):
        return self.__comando