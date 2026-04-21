"""
Módulo que define a classe EstadoContagem, que representa um 
estado do problema de contagem.
O estado é definido por um valor de contagem, que representa
a configuração atual do problema.
"""

class EstadoContagem:
    def __init__(self, contagem):
        """
            Construtor da classe EstadoContagem.
            Recebe um valor de contagem e armazena como atributo privado.
        """
        self.__contagem = contagem

    def id_valor(self):
        """
            ???
        """
        return self.__contagem

    @property
    def contagem(self):
        """
            Permite aceder ao valor de contagem do estado. Getter.
        """
        return self.__contagem