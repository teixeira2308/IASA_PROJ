"""
    Estado do agente.

    Representa um estado do agente no ambiente. Cada estado é identificado
    pela posição ocupada e por um valor único associado a essa posição.
"""

class EstadoAgente:
    def __init__(self, posicao):
        """
            Inicializa um estado do agente.

            Parâmetros:
                posicao -> posição do agente no ambiente.
        """
        self.__posicao = posicao
        self.__id_valor = hash(self.__posicao) #identificador unico do estado baseado na posição
        pass
    
    @property
    def id_valor(self):
        """
            Devolve o identificador único do estado.

            O valor é calculado a partir da posição.
        """
        return self.__id_valor