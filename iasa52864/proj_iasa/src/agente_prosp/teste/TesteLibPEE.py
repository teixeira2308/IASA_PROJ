from lib.plan.plan_pee.PlaneadorPEE import PlaneadorPEE
from agente_prosp.ControloDeLib.ControloDeLib import ControloDeLib
from agente_prosp.AgenteProsp import AgenteProsp
from sae import Simulador

if __name__ == "__main__":
    # Instanciar o motor de planeamento baseado em PEE (Procura em Espaço de Estados)
    planeador = PlaneadorPEE()
    # Criação da camada deliberativa, e usa o planeador como motor de decisão
    controlo = ControloDeLib(planeador)
    # Instanciação do agente prospetor, que utiliza o controlo deliberativo para agir
    agente = AgenteProsp(controlo)

    # Configuração e execução do simulador SAE
    # Parâmetros:
    #   - 1: Número do ambiente
    #   - agente: O agente a executar
    #   - vista_modelo: Ativa a visualização gráfica do modelo interno do agente

    simulador = Simulador(1, agente, vista_modelo=True)
    simulador.executar()