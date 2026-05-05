from lib.pee.melhor_prim.ProcuraMelhorPrim import ProcuraMelhorPrim

"""
    Esta classe representa a ProcuraInformada, que é uma classe para implementar o mecanismo de procura informada.
    O ProcuraInformada é uma implementação do algoritmo de busca informada, que utiliza uma função de avaliação para atribuir
    uma prioridade a cada nó, guiando a busca em direção ao objetivo. Ele é uma variação do algoritmo de procura do melhor primeiro,
    onde a avaliação dos nós é feita com base em uma heurística que estima o custo para chegar ao objetivo a partir de cada nó.
"""

class ProcuraInformada(ProcuraMelhorPrim):
    def procurar(self, problema, heuristica):
        self._avaliador = heuristica
        self._avaliador.heuristica = heuristica #atribui a heurística ao avaliador para que ele possa utilizá-la na função de avaliação dos nós
        return super().procurar(problema) #chama o método procurar da classe pai (ProcuraMelhorPrim) para realizar a busca, passando o problema
        #como argumento. O método procurar da classe pai irá utilizar o avaliador configurado para guiar a busca em direção ao objetivo.