from lib.ecr.Resposta import Resposta
from lib.agente_prosp.accoes.Mover import Mover

'''

    A classe RespostaMover representa a resposta de mover o agente numa direção específica.

    Esta resposta é ativada quando o agente deteta a presença do alvo numa direção específica,
    e a sua ação é mover-se para essa direção (determinada na variável direcao).
'''
class RespostaMover(Resposta):
    def __init__(self, direcao):
        super().__init__(Mover(direcao))