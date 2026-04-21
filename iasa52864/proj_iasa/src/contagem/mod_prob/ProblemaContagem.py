from contagem.mod_prob.OperadorIncremento import OperadorIncremento
from contagem.mod_prob.EstadoContagem import EstadoContagem
from lib.mod.Problema import Problema

"""
    Módulo que define a classe ProblemaContagem, que representa o problema de contagem.
    O problema de contagem é um problema de busca em que o objetivo é alcançar um estado
    de contagem final a partir de um estado de contagem inicial, utilizando um conjunto de
    operadores de incremento.
"""

class ProblemaContagem(Problema):
    def __init__ (self, contagem_inicial, contagem_final, incrementos):
        super().__init__(EstadoContagem(contagem_inicial),
                         [OperadorIncremento(incremento) for incremento in incrementos])
        ## O estado inicial é criado a partir do valor de contagem inicial, e os operadores
        ## de incremento são criados a partir dos valores de incremento recebidos como parâmetro.
        self.__contagem_final = contagem_final # O valor de contagem final é armazenado como atributo privado.