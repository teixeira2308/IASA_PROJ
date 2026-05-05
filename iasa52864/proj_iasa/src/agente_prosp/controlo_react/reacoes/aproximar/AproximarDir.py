from lib.agente_prosp.controlo_react.reacoes.aproximar.EstimuloAlvo import EstimuloAlvo
from lib.agente_prosp.controlo_react.respostas.RespostaMover import RespostaMover
from lib.ecr.Reacao import Reacao

'''
    A classe AproximarDir representa a reação de aproximar o agente do alvo numa direção específica.
    Esta reação ocorre quando deteta a presença do alvo numa direção específica.
'''

class AproximarDir(Reacao):
    def __init__(self, direcao):
        super().__init__(EstimuloAlvo(direcao), RespostaMover(direcao))