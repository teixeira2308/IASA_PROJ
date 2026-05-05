from src.agente_prosp.accoes.Mover import Mover
import math

"""
    Operador de movimento.

    Representa uma ação de deslocação que pode ser aplicada a um estado do modelo do mundo.
    Cada operador define uma direção de movimento e permite calcular o estado sucessor
    e o respetivo custo.
"""

class OperadorMover():
    def __init__(self, modelo_mundo, direcao):
        """
            Inicializa o operador de movimento.

            Parâmetros: modelo_mundo -> modelo do mundo utilizado
                                        para validar transições
                                        entre estados.
                        direcao -> direção associada ao movimento.                
        """
        self.__modelo_mundo = modelo_mundo
        #ângulo assocaido à direção de movimento
        self.__ang = direcao.value
        #Ação concreta de movimento
        self.__acao = Mover(direcao)
        pass

    def aplicar(self, estado):
        pass

    def custo(self, estado, estado_suc):
        """
            Calcula o custo de transição entre dois estados.

            É garantido num custo mínimo de 1 para evitar transições
            com custo nulo.
        """
        return max(math.dist(estado.posicao, estado_suc.posicao), 1)
    
    def __repr__(self):
        """
            Representação textual do operador.
        """
        return "OperadorMover(%s)" % self.__acao
    
    @property
    def ang(self):
        """
            Ângulo associado à direção do movimento.
        """
        return self.__ang
    
    @property
    def acao(self):
        """
            Ação concreta associada ao operador.
        """
        return self.__acao