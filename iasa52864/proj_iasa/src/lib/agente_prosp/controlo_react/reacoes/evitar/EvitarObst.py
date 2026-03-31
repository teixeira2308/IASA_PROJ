from lib.ecr.Reacao import Reacao
from lib.agente_prosp.controlo_react.reacoes.evitar.EstimuloObst import EstimuloObst
from lib.agente_prosp.controlo_react.respostas.RespostaEvitar import RespostaEvitar

'''
    A classe EvitarObst representa a reação de evitar um obstáculo.
    Esta reação é ativada quando o agente deteta a presença de um obstáculo,
    e a sua resposta é evitar o obstáculo na direção detetada (determinada
    na variável direcao).
'''

class EvitarObst(Reacao):
    def __init__(self, direcao):
        super().__init__(EstimuloObst(direcao), RespostaEvitar(direcao))  