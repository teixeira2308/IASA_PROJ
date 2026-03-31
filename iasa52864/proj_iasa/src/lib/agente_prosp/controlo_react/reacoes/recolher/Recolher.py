from lib.agente_prosp.controlo_react.reacoes.evitar import EvitarObst
from lib.agente_prosp.controlo_react.reacoes.explorar.Explorar import Explorar
from lib.ecr.Hierarquia import Hierarquia
from lib.agente_prosp.controlo_react.reacoes.aproximar.AproximarAlvo import AproximarAlvo

class Recolher(Hierarquia):
    def __init__(self):
        super().__init__([
            AproximarAlvo(),
            EvitarObst(),
            Explorar()
        ])
        