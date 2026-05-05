from lib.ecr.Resposta import Resposta
from lib.agente_prosp.accoes.Rodar import Rodar

'''

    A classe RespostaEvitar representa a resposta de evitar um obstáculo.

    Esta resposta é ativada quando o agente deteta a presença de um obstáculo,
    e a sua ação é rodar para uma direção segura.
'''

class RespostaEvitar(Resposta):
    def _obter_acao(self, percecao):
        dir_agente = percecao.direcao
        dir_resposta = dir_agente.rodar()
        return Rodar(dir_resposta)