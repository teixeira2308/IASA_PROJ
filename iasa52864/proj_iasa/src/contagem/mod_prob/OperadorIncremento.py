from contagem.mod_prob.EstadoContagem import EstadoContagem

"""
    Módulo que define a classe OperadorIncremento, que representa um operador
    de incremento para o problema de contagem.
    O operador de incremento é responsável por aplicar um incremento
    a um estado de contagem, gerando um novo estado de contagem.
    O operador de incremento também é responsável por calcular o custo
    da aplicação do operador, que é definido como o quadrado do incremento.
"""

class OperadorIncremento:
    def __init__(self, incremento):
        self.__incremento = incremento # Incremento a ser aplicado ao estado de contagem

    def aplica(self, estado):
        return EstadoContagem(estado.contagem + self.__incremento)
    """
        Este método é responsável por aplicar o operador de incremento a um estado
        de contagem e retornar um novo estado de contagem. 
        Ele recebe um estado de contagem como parâmetro e retorna um novo estado
        de contagem com o incremento aplicado.
    """
    
    def custo(self, estado, estado_suc):
        """
            Este método é responsável por calcular o custo da aplicação do
            operador de incremento. O custo é definido como o quadrado do incremento.
            Porque o custo de aplicar um incremento maior é 
            maior do que o custo de aplicar um incremento menor, e o quadrado é uma foram de
            representar isso de forma mais acentuada.
        """
        return self.__incremento**2

    @property
    def incremento(self):
        """
            Permite aceder ao valor do incremento do operador. Getter.
        """
        return self.__incremento