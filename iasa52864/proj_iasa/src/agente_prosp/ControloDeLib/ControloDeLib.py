from src.agente_prosp.ControloDeLib.modelo.ModeloMundo import ModeloMundo
from src.agente_prosp.ControloDeLib.MecDeLib import MecDeLib
import sae

"""
    Controlo deliberativo.

    Esta classe implementa o ciclo de decisão de um agente deliberativo.
    O agente recebe perceções do ambiente, atualiza o seu modelo interno,
    reconsidera objetivos, escolhe uma intenção, constrói um plano de ação
    e executa esse plano.
"""



class ControloDeLib:
    def __init__(self, planeador):
        """
            Inicializa o controlador deliberativo.

            Parâmetros: planeador -> componente responsável por gerar
                                    planos para atingir os objetivos definidos.
        """
        self.__planeador = planeador
        self.__modeloMundo = ModeloMundo()
        self.__mecDelib = MecDeLib(self.__modeloMundo)
        self.__objetivos = None
        self.__plano = None

    def processar(self, percecao):
        """
            Ciclo de execução do agente deliberativo.
            Coordena a atualização de considerações, deliberação, planeamento
            de ações e execução.
        """
        self.__assimilar(percecao)
        #se houve mudança no mundo ou o plano terminou, reconsidera a estratégia
        if self.__reconsiderar():
            self.__deliberar()
            self.__planear()
        return self.__executar()    


    def __assimilar(self, percecao):
        """
            Integra a nova perceção no modelo do mundo com base nas novas perceções.
        """
        self.__modeloMundo.atualizar(percecao)
        pass

    def __reconsiderar(self):
        """
            Determina se deve ocorrer nova deliberação.

            A deliberação é repetida quando o ambiente foi alterado ou 
            quando não existe plano disponível.
        """
        return self.__modeloMundo.alterado or not self.__plano

    def __deliberar(self):
        """
            Executa a fase de deliberação.

            Com base no estado atual do modelo do mundo, determina
            os objetivos que o agente deverá perseguir no ciclo corrente.
        """
        self.__objetivos = self.__mecDelib.deliberar()

    def __planear(self):
        if self.__objetivos:
            #gerar plano
            self.__plano = self.__planeador.planear(self.__modeloMundo, self.__objetivos)
        else:
            #anular plano
            self.__plano = None
    
    def __executar(self):
        """
            Extrai a próxima ação do plano para o estado atual.
            Se o plano não prevê o estado atual, o plano é invalidado.
        """
        if self.__plano:
            estado = self.__modeloMundo.obter_estado()
            # Obtém o operador agendado para o estado atual no plano
            operador = self.__plano.obter_estado(estado)
            if operador:
                return operador.accao
            else:
                # Se o estado atual não está no plano, forçar replaneamento no próximo ciclo.
                self.__plano = None

    def __mostrar(self):
        sae.vista.limpar()
        self.__modeloMundo.mostrar(sae.vista)
        if self.__plano:
            self.__plano.mostrar(sae.vista)
        if self.__objetivos:
            for objetivo in self.__objetivos:
                sae.vista.marcar_posicao(objetivo.posicao)    
        