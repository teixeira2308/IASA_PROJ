from lib.ecr.Estimulo import Estimulo
from lib.sae import Elemento

'''

    Classe EstimuloAlvo, representa o estimulo de deteção do alvo.

    Um estimulo é uma representação da perceção do agente sobre o ambiente,
    que pode ser utilizada para tomar decisões. No caso do EstimuloAlvo,
    ele representa a deteção do alvo numa direção específica,
    e a sua intensidade é calculada com base na distância ao alvo,
    utilizando um fator de decaimento gama, de modo a que quanto mais longe
    o alvo estiver, menor será a intensidade do estimulo.
'''

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
    
    

    