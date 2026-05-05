from abc import ABC, abstractmethod

"""
    Esta classe representa a Heurística, que é uma função que estima o custo de chegar ao estado objetivo a partir de um estado dado.
    A heurística é utilizada pelos mecanismos de procura informada para guiar a busca em direção ao objetivo, atribuindo uma
    prioridade a cada nó com base na estimativa do custo para alcançar o objetivo a partir daquele nó.
    A classe Heurística é uma classe abstrata, ou seja, não pode ser instanciada diretamente, e deve ser uma subclasse
    para implementar a função heurística específica para o problema em questão.
    """

class Heuristica(ABC):
    @abstractmethod
    def h(self, estado):
        """
            Método abstrato que deve ser implementado pelas subclasses para calcular a heurística de um estado.
            O método h recebe um estado e retorna a estimativa do custo para chegar ao estado objetivo a partir daquele estado.
        """
        pass

    @property
    def heuristica(self):
        """
            Propriedade para acessar a heurística associada ao avaliador. Getter para retornar a heurística armazenada.
        """
        return self._heuristica
    
    @heuristica.setter
    def heuristica(self, heuristica):
        """
            Setter para definir a heurística associada ao avaliador. Permite atribuir uma instância de heurística ao avaliador.
        """
        self._heuristica = heuristica