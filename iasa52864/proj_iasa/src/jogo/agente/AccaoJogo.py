from lib.agente.Accao import Accao

"""
    Esta classe guarda um ComandoJogo, servindo de ponte entre a decisão lógica 
    do agente e a execução física no simulador.
"""

class AccaoJogo(Accao):
    def __init__(self, comando):
        self.__comando = comando

    @property
    def comando(self):
        return self.__comando