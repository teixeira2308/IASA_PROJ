from lib.ecr.Comportamento import Comportamento

"""
    Classe que implementa o controlo reativo de um agente.
    Atua como mediador para um comportamento específico
"""

class ControloReact(Comportamento):
    def __init__(self, comportamento):
        """
            Inicializa o controlo com um comportamento. 
        """
        super().__init__()
        self.__comportamento = comportamento

    def ativar(self, percecao):
        """
            Executa a lógica de ativação do comportamento associado.
        """
        return self.__comportamento.ativar(percecao)    

    def processar(self, percecao):
        """
            Método principal chamado pelo ciclo de execução do agente.
            Redireciona a perceção para a lógica de ativação
        """
        return self.__comportamento.ativar(percecao)