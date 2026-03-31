'''
    A classe MaquinaEstados representa uma máquina de estados,
    que é um modelo de comportamento reativo do agente.
'''

class MaquinaEstados:
    def __init__(self, estado_inicial, transicoes = None):
        self.__estado = estado_inicial #estado atual da máquina de estados
        self.__tte = {} #tabela de transições de estados, onde a chave é uma tupla (estado_atual, evento) e o valor é o estado_sucessor
        self.__tae = {} #tabela de ações, onde a chave é uma tupla (estado_atual, evento) e o valor é a ação a executar para essa transição
        if transicoes:
            for transicao in transicoes:
                estado_ant, evento, estado_suc, accao = transicao \
                if len(transicao) == 4 else transicao + (None,) #se a transição não tiver uma ação associada, atribui None
                self.definir_transicao(estado_ant, evento, estado_suc, accao) #definir a transição na máquina de estados

    def definir_transicao(self, estado_ant, evento, estado_suc, accao=None):
        self.__tte[(estado_ant, evento)] = estado_suc #definir a transição na tabela de transições de estados
        if accao is not None:
            self.__tae[(estado_ant, evento)] = accao #definir a ação associada à transição na tabela de ações

    def processar(self, evento):
        accao = self.__tae.get((self.__estado, evento)) #obter a ação associada à transição
        novo_estado = self.__tte.get((self.__estado, evento)) #obter o estado sucessor da transição
        if novo_estado is not None:
            self.__estado = novo_estado #atualizar o estado atual da máquina de estados
        return accao    
    

    @property
    def estado(self):
        return self.__estado


        
