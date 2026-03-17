from lib.agente.Agente import Agente
import sae


class AgenteProsp(Agente):
    def _percecionar(self):
        return sae.transdutor.percepcionar()

    def _actuar(self, acao):
        return sae.transdutor.actuar(acao)