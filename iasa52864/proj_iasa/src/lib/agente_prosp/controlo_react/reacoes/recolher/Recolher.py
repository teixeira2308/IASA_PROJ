from lib.agente_prosp.controlo_react.reacoes.evitar.EvitarObst import EvitarObst
from lib.agente_prosp.controlo_react.reacoes.explorar.Explorar import Explorar
from lib.ecr.Hierarquia import Hierarquia
from lib.agente_prosp.controlo_react.reacoes.aproximar.AproximarAlvo import AproximarAlvo

'''
    Esta classe representa o comportamento reativo de recolher o alvo.
    O comportamento é organizado hierarquicamente, onde a reação de aproximar o alvo tem a
    maior prioridade, seguida pela reação de evitar obstáculos, e por fim a reação de explorar.
'''

class Recolher(Hierarquia):
    def __init__(self):
        super().__init__([
            AproximarAlvo(),
            EvitarObst(),
            Explorar()
        ])
        