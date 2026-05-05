from lib.ecr.Accao import Accao
from lib.sae import Movimento
class Avancar(Movimento, Accao):
    def __init__(self):
        super().__init__()