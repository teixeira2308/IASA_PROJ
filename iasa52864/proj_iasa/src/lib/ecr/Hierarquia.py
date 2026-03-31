from lib.ecr.ComportComp import ComportComp

class Hierarquia(ComportComp):
    def selecionar_acao(self, acoes):
        return acoes[0]