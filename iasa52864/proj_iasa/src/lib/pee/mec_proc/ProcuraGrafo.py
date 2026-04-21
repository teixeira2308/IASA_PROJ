from lib.pee.mec_proc.MecanismoProcura import MecanismoProcura

"""
    Esta classe representa o ProcuraGrafo, que é uma classe 
    para implementar algoritmos de procura em grafos.
    Ela herda da classe MecanismoProcura e implementa os métodos necessários
    para a busca em grafos. 
    Grafos são estruturas de dados que consistem em um conjunto de nós e um 
    conjunto de arestas que conectam esses nós.
    A busca em grafos é uma técnica utilizada para encontrar um caminho entre um nó inicial e um nó objetivo,
    explorando os nós e as arestas do grafo.
"""

class ProcuraGrafo(MecanismoProcura):
    def _iniciar_memoria(self):
        """
            Inicia a memória do mecanismo de procura. Ele cria um dicionário 
            para armazenar os estados explorados, onde a chave é o estado e o valor é 
            o nó correspondente. Isso permite que o mecanismo de procura evite explorar
            estados ja explorados. 
        """
        self._explorados = {}
        pass

    def _memorizar(self, no):
        """
            Memoriza um nó na memória do mecanismo de procura. Ele chama 
            o método inserir da classe pai para adicionar o nó à fronteira
            e também adiciona o estado do nó ao dicionário de explorados, associando-o ao nó.
        """
        super()._memorizar(no) #chama o método inserir da classe pai para adicionar o nó à fronteira
        self._explorados[no.estado] = no #adiciona o estado do nó ao dicionário de explorados, associando-o ao nó
        pass

    def _manter(self, no):
        return no.estado not in self._explorados #verifica se o estado do nó não está no dicionário de explorados, 
                                                #retornando True se o nó deve ser mantido na fronteira para exploração futura,
                                                # ou False se o nó já foi explorado e deve ser descartado.