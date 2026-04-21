from abc import ABC, abstractmethod

class Problema(ABC):
    def __init__ (self, estado_inicial, operadores):
        """
            Este método deve retornar True se o estado for o estado final
            desejado, e False caso contrario.

        """
        self.estado_inicial = estado_inicial
        self.operadores = operadores

    @abstractmethod
    def objetivo(self, estado):
        pass