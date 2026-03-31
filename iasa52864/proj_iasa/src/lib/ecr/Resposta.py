'''

    A classe Resposta representa a resposta do agente a uma percepção específica.
    Esta classe é responsável por gerar uma ação com base na percepção recebida.
'''

class Resposta:
    def __init__(self, acao=None):
        self.__acao = acao

    def ativar(self, percepcao, intensidade):
        """incompleto"""
        return self.__acao
        pass

    def _obter_acao(self, percepcao):
        pass