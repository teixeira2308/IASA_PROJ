from lib.agente.Accao import Accao

"""
    Esta classe guarda um ComandoJogo, servindo de ponte entre a decisão lógica 
    do agente e a execução física no simulador. 
    O comando a ser executado no simulador é armazenado como um atributo privado,
    e pode ser acedido através de um método getter.
"""

class AccaoJogo(Accao):
    def __init__(self, comando):
        self.__comando = comando # O comando a ser executado no simulador, armazenado como atributo privado.

    @property
    def comando(self):
        return self.__comando # Permite aceder ao comando da ação. Getter.