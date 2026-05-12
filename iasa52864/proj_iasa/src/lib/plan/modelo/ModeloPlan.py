from abc import ABC, abstractmethod

class ModeloPlan(ABC):

    """
        Interface para o modelo de planeamento.
        Define os métodos necessários para que um motor de procura possa extrair
        informações sobre o espaço de estados e operadores disponíveis.
    """
    
    @abstractmethod
    def obter_estado():
        """
            Retorna o estado atual do agente no ambiente.
        """
        pass

    @abstractmethod
    def obter_estados():
        """
            Retorna o conjunto de todos os estados possíveis
        """
        pass

    @abstractmethod
    def obter_operadores():
        """
            Retorna a lista de operadores (ações).
        """
        pass