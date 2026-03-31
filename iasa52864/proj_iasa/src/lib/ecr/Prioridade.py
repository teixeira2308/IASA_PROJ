from lib.ecr.ComportComp import ComportComp

class Prioridade(ComportComp):
    def selecionar_acao(self, acoes):
        return max(acoes, key=lambda acao: acao.prioridade)
    
