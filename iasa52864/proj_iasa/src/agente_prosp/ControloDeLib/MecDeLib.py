from sae import Elemento
"""
    Mecanismo de deliberação.

    Este componente é responsável por analisar o modelo do mundo e decidir 
    quais os objetivos que o agente deverá perseguir. A deliberação permite
    escolher, entre várias possibilidades, aquelas que são mais adequadas
    ao estado atual do ambiente.
"""

class MecDeLib:
    def __init__(self, modelo_mundo):
        """
            Inicializa o mecanismo de deliberação.

            Parâmetros:
                modelo_mundo -> modelo interno do ambiente usado para
                                identificar objetivos possíveis.
        """
        self.__modelo_mundo = modelo_mundo
        pass

    def deliberar(self):
        """
            Executa o processo de deliberação.
            Gera objetivos possíveis com base no modelo do mundo e 
            depois seleciona os mais adequados segundo um critério.
        """
        objetivos = self.__gerar_objetivos()
        if objetivos:
            return self.__selecionar_objetivos(objetivos)
        return None

    def __gerar_objetivos(self):
        """
            Gera uma lista de objetivos possíveis.

            Neste caso, os objetivos correspondem a estados onde existe
            um elemento do tipo ALVO no ambiente.
        """
        return [estado for estado in self.__modelo_mundo.obter_estados()
                 if self.__modelo_mundo.obter_elemento(estado) == Elemento.ALVO]

    def __selecionar_objetivos(self, objetivos):
        """
            Seleciona os objetivos mais relevantes.

            Critério utilizado é a menor distância ao estado atual do agente.

            Apenas o conjunto de objetivos mais próximo é selecionado.
        """
        objetivos.sort(key=self.__modelo_mundo.distancia)
        return objetivos[:1]