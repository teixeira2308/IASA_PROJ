from abc import ABC, abstractmethod

class Plano(ABC):
    """
        Interface abstrata para a representação de um Plano de ação.
        Define a estrutura necessária para que o agente possa consultar a próxima
        ação a executar e visualizar o caminho planeado no ambiente.
    """
    @abstractmethod
    def obter_acao(self, estado):
        """
            Retorna a ação (operador) planeada para um determinado estado.

            Parâmetros:
                estado: O estado atual onde o agente se encontra.
        """
        pass

    @abstractmethod
    def mostrar(self, vista):
        """
            Representação visual do plano.

            Parâmetros:
                vista: O componente da interface gráfica (sae.vista) utilizado para
                        desenhar os elementos do plano no simulador.
        """
        pass