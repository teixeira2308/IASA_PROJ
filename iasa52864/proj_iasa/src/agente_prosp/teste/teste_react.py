from lib.agente_prosp.controlo_react.reacoes.explorar.Explorar import Explorar
from lib.agente_prosp.controlo_react.ControloReact import ControloReact
from lib.agente_prosp.AgenteProsp import AgenteProsp
from lib.sae import Simulador
from lib.agente_prosp.controlo_react.reacoes.recolher.Recolher import Recolher

"""
    Este módulo é um teste para o agente prospectivo com controlo reativo.
    O agente prospectivo é um agente que utiliza um modelo do ambiente para tomar decisões.
    O controlo reativo é um tipo de controlo que reage a estímulos do ambiente
    de forma imediata, sem a necessidade de planeamento.
    Neste teste, o agente prospectivo com controlo reativo é colocado em um ambiente
    simulado, onde ele deve recolher um recurso. O comportamento do agente é definido
    pela reação de recolher, que é responsável por recolher o recurso quando ele está presente no ambiente.
"""

if __name__ == "__main__": # Teste para o agente prospectivo com controlo reativo
    comportamento = Recolher() # Comportamento do agente, neste caso, a reação de recolher, que é responsável
                            #por recolher o recurso quando ele está presente no ambiente.
    controlo = ControloReact(comportamento) # O controlo reativo é responsável por gerir as reações do agente,
                                            #neste caso, a reação de recolher. Ele recebe o comportamento do agente
                                            # como parâmetro e é responsável por executar a reação quando o estímulo 
                                            #do ambiente é detectado.
    agente = AgenteProsp(controlo) # O agente prospectivo é responsável por tomar decisões com base no modelo do ambiente e no controlo reativo.
                                    # Ele recebe o controlo reativo como parâmetro e é responsável por executar as ações definidas pelo controlo
                                    # reativo quando os estímulos do ambiente são detectados.
    simulador = Simulador(1, agente) # O simulador é responsável por simular o ambiente e as interações do agente com o ambiente.
                                    #Ele recebe o agente como parâmetro e é responsável por executar a simulação,
                                    # permitindo que o agente reaja aos estímulos do ambiente de acordo com o seu comportamento
                                    # definido pelo controlo reativo.
    simulador.executar()     #Executa a simulação, permitindo que o agente reaja aos estímulos do ambiente de acordo com o seu comportamento