from src.agente_prosp.ControloDeLib.modelo.OperadorMover import OperadorMover
from src.agente_prosp.ControloDeLib.modelo.EstadoAgente import EstadoAgente
from sae import Direccao
import math
from sae import Elemento

"""
    Modelo do mundo.

    Esta classe representa o conhecimento interno que o agente mantém sobre o ambiente.
    É atualizada a partir das perceções recebidas e serve de base
    para a deliberação e para o planeamento das ações.
"""

class ModeloMundo:
    def __init__(self):
        """
            Inicializa o modelo do mundo.

            São criadas as estruturas internas necessárias para guardar
            os elementos observados no ambiente, os estados conhecidos
            e os operadores de ação disponíveis.
        """
        self.__estado = None
        self.__estados = []
        self.__elementos = {} 
        #Operadores de movimento possíveis no ambiente
        self.__operadores = [OperadorMover(self, direcao) for direcao in Direccao]
        self.__alterado = False
        pass

    def __contains__(self, estado):
        """
            Verifica se um estado pertence ao conjunto de estados conhecidos.

            Parâmetros:
                estado -> estado a verificar.
        """
        return estado in self.__estados

    def obter_estado(self):
        """
            Devolve o estado atual do agente.
        """
        return self.__estado

    def obter_estados(self):
        """
            Devolve o conjunto de estados conhecidos pelo agente.
        """
        return self.__estados

    def obter_operadores(self):
        """
            Devolve os operadores de ação disponíveis.
        """
        return self.__operadores

    def obter_elemento(self, estado):
        """
            Obtém o elemento existente numa determinada posição.

            Parâmetros:
                estado -> estado cuja posição será consultada.
        """
        return self.__elementos.get(estado.posicao)

    def distancia(self, estado):
        """
            Calcula a distância entre um estado e o estado atual do agente.

            Parâmetros:
                estado -> estado de referência.
        """
        return math.dist(estado.posicao, self.__estado.posicao)

    def atualizar(self, percecao):
        """
            Atualiza o modelo interno com base numa nova perceção.

            A posição atual do agente é atualizada. Caso a perceção
            introduza alterações no ambiente, o conjunto de elementos
            e de estados conhecidos são reconstruídos.

            Parâmetros:
                percecao: informação observada no ambiente
        """
        self.__estado = EstadoAgente(percecao.posicao)
        self.__alterado = self.__elementos != percecao.elementos
        if self.__alterado:
            self.__elementos = percecao.elementos
            self.__estados = [EstadoAgente(posicao) for posicao in percecao.posicoes]

    def mostrar(self, vista):
        """
            Apresenta visualmente o modelo do mundo.

            São mostrados os elementos relevantes do ambiente e a 
            posição atual do agente.

            Parâmetros:
                vista -> componente responsável pela visualização.
        """
        for posicao, elemento in self.__elementos.items():
            if elemento in [Elemento.ALVO, Elemento.OBSTACULO]:
                vista.mostrar_elemento(posicao, elemento)
        vista.marcar_posicao(self.__estado.posicao)     

    @property
    def alterado(self):
        return self.__alterado       