from abc import ABC, abstractmethod

"""
    É o conjunto de todos os nós (estados) que foram gerados, mas 
    que ainda não foram explorados. 
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
        self.nos = []

    @abstractmethod    
    def inserir(self, no):
        """
            Método abstrato. Cada tipo de procura implementa este método
            de forma diferente.

        """
        self.nos.append(no)

    def remover(self):
        """
            Remove o próximo nó a ser explorado.
            Nesta implementação base, remove sempre o primeiro elemento (índice 0).
        """
        self.nos.pop(0)

    @property
    def vazia(self):
        """
            Propriedade que indica se já não há mais nós para explorar.
        """
        return len(self.nos) == 0