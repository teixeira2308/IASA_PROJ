from lib.agente_prosp.controlo_react.reacoes.aproximar.AproximarDir import AproximarDir
from lib.ecr.Prioridade import Prioridade
from lib.sae import Direccao

"""
    Classe AproximarAlvo, representa a reação de aproximar o agente do alvo.
    Esta reação é ativada quando o agente deteta a presença do alvo.
"""

class AproximarAlvo(Prioridade):
    def __init__(self):
        super().__init__([AproximarDir(direcao) for direcao in Direccao])