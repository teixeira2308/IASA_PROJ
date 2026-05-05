from lib.agente.Agente import Agente
import sae

"""
    Especialização do Agente para a prospeção.

    Esta classe utiliza o transdutor para mediar a comunicação entre o sistema de 
    controlo interno e o ambiente externo (SAE).
"""

class AgenteProsp(Agente):
    def _percecionar(self):
        """Percecionar com base no transdutor da plataforma SAE."""
        return sae.transdutor.percepcionar()

    def _actuar(self, acao):
        """Actuar com base no transdutor da plataforma SAE."""
        return sae.transdutor.actuar(acao)