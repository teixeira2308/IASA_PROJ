from abc import ABC, abstractmethod

"""
    É o conjunto de todos os nós (estados) que foram gerados, mas 
    que ainda não foram explorados.
    Esta classe é uma implementação da fronteira,
    onde a estratégia de exploração é definida pelo método de inserção dos nós.
"""

class Fronteira(ABC):
    
    def __init__ (self):
        """
            Inicializa a fronteira chamando o método iniciar.
        """
        self.iniciar()
        
    def iniciar(self):
        """
            Cria a estrutura de dados para armazenar os nós.
        """
        self._nos = []

    @abstractmethod    
    def inserir(self, no):
        """
            Método abstrato. Cada tipo de procura implementa este método
            de forma diferente.

        """
        self._nos.append(no)

    def remover(self):
        """
            Remove o próximo nó a ser explorado.
            Nesta implementação base, remove sempre o primeiro elemento (índice 0).
        """
        self._nos.pop(0)

    @property
    def vazia(self):
        """
            Propriedade que indica se já não há mais nós para explorar.
        """
        return len(self._nos) == 0