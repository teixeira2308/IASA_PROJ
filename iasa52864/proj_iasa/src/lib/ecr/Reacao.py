class Reacao:
    def __init__(self, estimulo, resposta):
        self.__estimulo = estimulo
        self.__resposta = resposta

    def ativar(self, percepcao):
        self.__intensidade = self.__estimulo.detetar(percepcao)
        if self.__intensidade > 0:
            acao = self.__resposta.ativar(percepcao, self.__intensidade)
            return acao
        pass