from src.agente_prosp.ControloDeLib.modelo.ModeloMundo import ModeloMundo
from src.agente_prosp.ControloDeLib.MecDeLib import MecDeLib


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

        pass

    def __assimilar(self, percecao):
        """
            Integra a nova perceção no modelo do mundo.
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
        pass

    def __planear(self):
        pass
    
    def __executar(self):
        pass

    def __mostrar(self):
        pass