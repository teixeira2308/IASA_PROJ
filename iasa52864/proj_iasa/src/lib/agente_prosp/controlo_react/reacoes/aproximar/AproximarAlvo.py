from lib.agente_prosp.controlo_react.reacoes.aproximar import AproximarDir
from lib.ecr.Prioridade import Prioridade
from lib.sae.ambiente.direccao import Direccao

class AproximarAlvo(Prioridade):
    def __init__(self):
        super().__init__([AproximarDir(direcao) for direcao in Direccao])