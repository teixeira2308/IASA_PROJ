import sae
from lib.ecr.Accao import Accao
class Mover(Movimento, Accao):
    def __init__(self, direcao):
        super().__init__(direcao, 1)