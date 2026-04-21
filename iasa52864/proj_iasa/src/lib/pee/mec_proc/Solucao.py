from lib.pee.mec_proc.PassoSolucao import PassoSolucao

"""
    A solução é a sequencia de ações e estados que levam do estado inicial a um estado objetivo.
    Durante a procura, o mecanismo de procura constrói um nó para cada estado gerado,
    quando o objetivo é atingido, o mecanismo possui um nó final. Como cada nó
    guarda uma referência para o seu antecessor, a solução é construída "andando para trás" 
    do objetivo até ao estado inicial. 
"""

class Solucao:

    def __init__(self, no_final):
        """
            O contrutor reconstroi o caminho completo a partir do nó objetivo.
        """
        self.__dimensao = no_final.profundidade # nº de passos
        self.__custo = no_final.custo #custo total
        self.__passos = [] #lista de objetos PassoSolucao
        no = no_final
        while no.antecessor: #ciclo que percorre a árvore de baixo para cima
            #cria um passo com o estado onde estava e a ação que tomou
            passo = PassoSolucao(no.antecessor.estado, no.operador)
            #insere no inicio da lista para que a solução fique na ordem cronológica correta
            self.__passos.inserir(0, passo)
            no = no.antecessor

    def __iter__ (self):
        """
            Permite iterar/percorrer a solução num ciclo: for passo in solucao:
        """
        iter(self.__passos)

    def __getitem__ (self, index):
        """
            Permite aceder a um passo específico por indexação: solucao[0] para o primeiro passo.
        """
        return self.__passos[index]    

    def dimensao(self):
        """
            Retorna a dimensão da solução, ou seja, o número de passos. Getter.
        """
        pass

    def custo(self):
        """
            Retorna o custo total da solução. Getter.
        """
        pass
