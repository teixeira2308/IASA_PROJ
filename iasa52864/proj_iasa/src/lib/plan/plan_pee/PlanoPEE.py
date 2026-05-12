from lib.plan.Plano import Plano

class PlanoPEE(Plano):
    """
        Representa um plano de ação gerado através de Procura em Espaço de Estados.
        Armazena a sequência de passos (nós) que levam do estado inicial ao objetivo.
    """
    def __init__(self, solucao):
        """
            Construtor do Plano.

            Parâmetros:
                solução -> Objeto Solucao retornado pelo MecanismoProcura, 
                que contém a trajetória encontrada.
        """
        self.__solucao = solucao
        #Converte a solução (iterável) numa lista de passos para execução sequencial
        self.__passos = [passo for passo in solucao]

    def obter_acao(self, estado):
        """
            Retorna a próxima ação (operador) a executar, verificando se o agente
            se encontra no estado esperado pelo plano.
        """
        if self.__passos:
            # Retira o primeiro passo da lista
            passo = self.__passos.pop(0)
            # Validação: O agente só executa a ação se estiver onde o plano previu
            if passo.estado == estado:
                return passo.operador
            return None

    def mostrar(self, vista):
        """
            Visualização gráfica do plano no simulador.
            Desenha vetores que indicam o caminho e a direção de cada movimento planeado.
        """
        if self.__passos:
            for passo in self.__passos:
                # Desenha um vetor na posição do estado com o ângulo do operador aplicado
                vista.mostrar_vector(passo.estado.posicao, passo.operador.ang)