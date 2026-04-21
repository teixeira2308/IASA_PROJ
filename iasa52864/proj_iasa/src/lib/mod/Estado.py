from abc import ABC, abstractmethod

"""
    Um estado representa uma configuração de um sistema.
    É uma classe abstrata, logo cada estado possui uma identificação unica.
    Esta identificação é dada pelo método id_valor.

"""

class Estado(ABC):

    def __hash__(self):
        """
            Retorna o valor do hash do estado baseando-se no seu id_valor.
            Permite que o estado seja usado em estruturas como conjuntos ou chaves
            em dicionários.
        """
        return self.id_valor()
    
    def __eq__ (self, objeto):
        """
            Define a igualdade entre dois estados.
            Dois estados são considerados iguais se os seus hashes (id_valor) forem iguais.
        """

        return self.__hash__() == objeto.__hash__()

    @abstractmethod
    def id_valor(self):
        """
            Método abstrato que deve ser implementado pelas subclasses.
            Deve retornar um valor que represente a configuração específica do problema.
        """
        pass