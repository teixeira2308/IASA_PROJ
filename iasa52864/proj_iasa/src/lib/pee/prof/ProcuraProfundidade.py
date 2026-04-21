from lib.pee.mec_proc.MecanismoProcura import MecanismoProcura
from pee.prof.FronteiraLIFO import FronteiraLIFO

"""
Procura em Profundidade é uma classe que implementa o algoritmo de procura
em profundidade. Ela herda da classe MecanismoProcura e utiliza uma FronteiraLIFO
para armazenar os nós a serem explorados. A busca em profundidade é uma estratégia de
procura que explora o mais profundo possível antes de retroceder.
"""

class ProcuraProfundidade(MecanismoProcura):
    def __init__(self):
        """
            Construtor da classe ProcuraProfundidade. Ele chama o construtor da classe pai
            passando uma instância de FronteiraLIFO, que é a estrutura de dados utilizada
            para armazenar os nós a serem explorados.
        """
        super().__init__(FronteiraLIFO())