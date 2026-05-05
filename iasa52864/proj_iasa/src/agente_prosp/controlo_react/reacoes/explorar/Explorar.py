import random
from lib.agente_prosp.accoes.Avancar import Avancar
from lib.agente_prosp.accoes.Rodar import Rodar
from lib.ecr.Comportamento import Comportamento
from lib.sae import Direccao

"""
    Comportamento reativo simples para exploração aleatória do ambiente.

    Esta classe representa um comportamento de exploração aleatória,
    onde o agente tem uma tendência a avançar na mesma direção, mas ocasionalmente
    decide rodar para uma direção aleatória. A probabilidade de rodar é controlada
    pelo parâmetro prob_rotacao, que pode ser ajustado para aumentar ou diminuir a 
    tendência do agente para mudar de direção. Este comportamento é útil para permitir
    que o agente explore o ambiente de uma forma mais inteligente e menos previsível.
"""

class Explorar(Comportamento):
    def __init__(self, prob_rotacao=0.7):
        """
            Define a tendencia do agente para mudar de direção
        """
        self.__prob_rotacao = prob_rotacao

    def ativar(self, percecao):
        """
            Decide a próxima ação com base numa distribuição probabilistica.
        """
        if random.uniform(0, 1) >= self.__prob_rotacao:
            return Avancar()
        else:
            return Rodar(random.choice(list(Direccao)))
    