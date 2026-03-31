from lib.ecr.Estimulo import Estimulo
from lib.sae import Elemento

class EstimuloAlvo(Estimulo):
    def __init__(self, direccao, gama=0.9):
        super().__init__()
        self.__direccao = direccao
        self.__gama = gama
    
    def detetar(self, percecao):
        elemento, distancia, _ = percecao[self.__direccao]
        if elemento == Elemento.ALVO:
            self.intensidade = self.__gama ** distancia
        else:
            self.intensidade = 0
        return self.intensidade
    
    

    