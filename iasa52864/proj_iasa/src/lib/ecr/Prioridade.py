from lib.ecr.ComportComp import ComportComp

'''

    A classe Prioridade representa um comportamento composto do agente
    que seleciona a ação a executar com base na prioridade dos comportamentos reativos.

    Esta classe é responsável por gerir um conjunto de comportamentos reativos,
    e selecionar a ação a executar com base nas perceções do ambiente,
    dando prioridade aos comportamentos com maior prioridade.

'''

class Prioridade(ComportComp):
    def selecionar_acao(self, acoes):
        return max(acoes, key=lambda acao: acao.prioridade)
    
