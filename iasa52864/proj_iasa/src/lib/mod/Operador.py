from abc import ABC, abstractmethod

"""
    Um operador representa uma ação ou regra de transição que pode ser aplicada
    a um estado. É o mecanismo que permite "mover-se" dentro do espaço de estados.
"""

class Operador(ABC):
    @abstractmethod
    def aplica(self, estado):
        """
            Recebe um objeto da classe 'Estado' e retorna um novo estado.
            Representa a execução da ação. Se a ação não for aplicável ao estado,
            pode retornar None.
        """
        pass
    @abstractmethod
    def custo(self, estado, estado_suc):
        """
            Calcula o custo de transição entre o estado original e o 
            estado sucessor.
        """
        pass