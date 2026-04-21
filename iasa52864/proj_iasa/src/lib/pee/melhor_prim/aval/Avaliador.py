from abc import ABC, abstractmethod

"""
    O Avaliador é o componente responsável por atribuir uma prioridade
    a cada nó.
"""

class Avaliador(ABC):
    @abstractmethod
    def prioridade(self, no):
        """
            Este método deve retornar um valor numérico que representa a prioridade do nó.
        """
        pass