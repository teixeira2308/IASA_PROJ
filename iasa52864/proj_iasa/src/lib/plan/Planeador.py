from abc import ABC, abstractmethod

class Planeador(ABC):
    """
        Interface abstrata que define o contrato para os componentes de planeamento.
        Esta classe permite a implementação que diferentes tipos de planeadores
        que podem ser usados de forma diferente pelo controlo deliberativo.
    """
    @abstractmethod
    def planear(self, modelo_plan, objetivos):
        """
            Gera uma sequência de ações (Plano) para atingir um ou mais objetivos.
            
            Parâmetros:
                modelo_plan: O modelo de planeamento que fornece o estado
                             atual e os operadores disponíveis
                objetivos:   Uma lista de objetivos que o agente pretende alcançar.             
        """
        pass