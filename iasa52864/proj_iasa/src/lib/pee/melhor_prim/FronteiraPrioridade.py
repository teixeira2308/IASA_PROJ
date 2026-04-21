from lib.pee.mec_proc.Fronteira import Fronteira
from heapq import heappush, heappop

"""
    O termo heap designa uma fila de prioridade, onde
    cada elemento tem uma prioridade associada.
    A fila de prioridade é uma estrutura de dados onde os elementos
    são removidos com base na prioridade, em vez de na ordem de inserção. 
    A FronteiraPrioridade é uma implementação de uma fila de prioridade,
    onde os nós são armazenados em uma lista e a prioridade é determinada
    por um avaliador.
"""

class FronteiraPrioridade(Fronteira):
    def __init__(self, avaliador):
        """
            Construtor da classe FronteiraPrioridade.
            Ele chama o construtor da classe pai e inicializa o avaliador,
            que é responsável por calcular a prioridade dos nós.
        """
        super().__init__() #chama o construtor da classe pai para inicializar a estrutura de dados
        self.__avaliador = avaliador #inicializa o avaliador, que é responsável por calcular a prioridade dos nós

    def inserir(self, no):
        """
            Insere um nó na fronteira. O nó é adicionado à lista de nós,
            e a prioridade é calculada usando o avaliador.
            A função heappush é utilizada para manter a propriedade de heap,
            garantindo que o nó com a menor prioridade seja removido primeiro.
        """
        no.prioridade = self.__avaliador.prioridade(no) #calcula a prioridade do nó usando o avaliador
        heappush(self._nos, no) #adiciona o nó à lista de nós, mantendo a propriedade de heap

    def remover(self):
        """
            Remove o próximo nó a ser explorado. O nó com a menor prioridade é removido primeiro,
            utilizando a função heappop, que mantém a propriedade de heap.
        """
        return heappop(self._nos) #remove e retorna o nó com a menor prioridade, mantendo a propriedade de heap