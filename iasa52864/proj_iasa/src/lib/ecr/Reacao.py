'''
    A classe Reacao representa a reação do agente a um estímulo específico.
    Esta classe é composta por um estímulo, que é responsável por detetar eventos
    no ambiente, e uma resposta, que é responsável por gerar uma ação com base na
    perceção do estímulo.
'''

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