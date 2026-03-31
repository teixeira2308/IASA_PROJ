from lib.ecr.ComportComp import ComportComp

'''

    A classe Hierarquia representa uma hierarquia de comportamentos composto do agente.
    Esta classe é responsável por gerir um conjunto de comportamentos reativos em uma estrutura hierárquica,
    e selecionar a ação a executar com base nas perceções do ambiente.


'''

class Hierarquia(ComportComp):
    def __init__(self, comportamentos):
        super().__init__(comportamentos)

    def selecionar_acao(self, acoes):
        return acoes[0]