from lib.ecr import Reacao
from lib.agente_prosp.controlo_react.reacoes.evitar.EstimuloObst import EstimuloObst
from lib.agente_prosp.controlo_react.respostas.RespostaEvitar import RespostaEvitar

class EvitarObst(Reacao):
    def __init__(self):
        estimulo = EstimuloObst()
        resposta = RespostaEvitar()