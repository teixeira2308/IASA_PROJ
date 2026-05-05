from agente_prosp.accoes.Avancar import Avancar

class ExplorarMem():
    '''
        Esta classe é a implementação de uma reação da package explorar, que
        tem como objetivo explorar a memória do agente.
        O agente tem uma memória limitada, e esta reação tem como objetivo explorar
        a memória do agente, avançando para uma posição que ainda não foi visitada.
    '''
    def __init__(self, dim_max_mem = 100):
        self.__dim_max_mem = dim_max_mem
        self.__memoria = []
        self.__acao = Avancar()
        pass


    def ativar(self, percecao):
        situacao = (percecao.posicao, percecao.direcao)
        if situacao not in self.__memoria:
            self.__memoria.append(situacao)
            #Se a memória fica cheia, remove o elemento mais antigo
            if len(self.__memoria) > self.__dim_max_mem:
                self.__memoria.pop(0) #remove o primeiro elemento da lista (o mais antigo)
            return self.__acao    
    