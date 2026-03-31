from lib.agente_prosp.controlo_react.reacoes.explorar.Explorar import Explorar
from lib.agente_prosp.controlo_react.ControloReact import ControloReact
from lib.agente_prosp.AgenteProsp import AgenteProsp
from lib.sae.simulador import Simulador


if __name__ == "__main__":
    comportamento = Explorar()
    controlo = ControloReact(comportamento)
    agente = AgenteProsp(controlo)
    simulador = Simulador(1, agente)
    simulador.executar()    