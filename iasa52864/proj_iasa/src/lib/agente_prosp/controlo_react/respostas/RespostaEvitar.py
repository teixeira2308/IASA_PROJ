from lib.ecr.Resposta import Resposta
from lib.agente_prosp.accoes.Rodar import Rodar

class RespostaEvitar(Resposta):
    def _obter_acao(self, percecao):
        dir_agente = percecao.direcao
        dir_resposta = dir_agente.rodar()
        return Rodar(dir_resposta)