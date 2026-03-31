from lib.agente_prosp.controlo_react.reacoes.aproximar.EstimuloAlvo import EstimuloAlvo
from lib.agente_prosp.controlo_react.respostas.RespostaMover import RespostaMover
from lib.ecr.Reacao import Reacao

class AproximarDir(Reacao):
    def __init__(self, direcao):
        super().__init__(EstimuloAlvo(direcao), RespostaMover(direcao))