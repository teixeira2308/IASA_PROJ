"""
    O nó de procura é um elemento da árvore de procura.
    Ele contém o estado atual (configuração que o nó representa),
    o antecessor (nó anterior),
    o operador (ação que foi aplicada ao antecessor para gerar o nó atual),
    a profundidade (quantos passos foram dados desde o nó inicial),
    o custo (custo acumulado para chegar ao nó atual).
"""

class No:
    def __init__(self, estado, operador=None, antecessor=None, custo=None):
        """
            Construtor do nó.
        """
        self.__custo = custo if custo is not None else 0 #custo acumulado para chegar ao nó atual, se não for fornecido, assume-se 0
        self.__prioridade = 0 

        if antecessor:
            self.__profundidade = antecessor.profundidade + 1 #se tiver um antecessor, a profundidade é a profundidade do antecessor + 1
        else:
            self.__profundidade = 0 #se não tiver antecessor, é o nó inicial, então a profundidade é 0

    def __lt__ (self, no):
        """
            'Less Than' (menor que). Permite que objetos 'No' sejam
            comparados diretamente. Essencial para a fronteira ordenar os nós.
        """
        return self.__prioridade < no.prioridade

    @property
    def prioridade(self):
        return self.__prioridade

    def set_prioridade(self, prioridade):
        """
            Define a prioridade do nó. Setter.
        """
        self.__prioridade = prioridade

    @property
    def custo(self):
        """
            Retorna o custo acumulado para chegar ao nó atual. Getter.
        """
        return self.__custo

    @property
    def profundidade(self):
        """
            Retorna a profundidade do nó na árvore de procura. Getter.
        """
        return self.__profundidade            