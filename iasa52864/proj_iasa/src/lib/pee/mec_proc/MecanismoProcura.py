from lib.pee.mec_proc.Solucao import Solucao
from pee.mec_proc.No import No

"""
    O Mecanismo de Procura é o componente responsável por encontrar uma solução
    para um problema. Ele utiliza uma estrutura de dados chamada fronteira para armazenar os nós
    que foram gerados mas ainda não foram explorados. 
    Esta classe é uma implementação do mecanismo de procura, 
    onde a estratégia de procura é definida pela estrutura de dados
    utilizada na fronteira.
"""

class MecanismoProcura:
    def __init__(self, fronteira):
        """
            O mecanismo é injetado por uma fronteira, o que define
            a estratégia de procura.
        """
        self._fronteira = fronteira

    def _iniciar_memoria(self):
        self._fronteira.iniciar()

    def _memorizar(self, no):
        self._fronteira.inserir(no)

    def procurar(self, problema):
        """
            Inicia a memória, cria o nó inicial com o estado inicial do problema,
            enquanto houver nós na fronteira, remove o próximo nó,
            ser for um nó objetivo, retorna a solução, caso contrário, 
            expande o nó e memoriza os nós sucessores.
        """
        self._iniciar_memoria()
        no = No(problema.estado_inicial)
        self._memorizar(no)
        while not self._fronteira.vazia:
            no = self._fronteira.remover()
            if problema.objetivo(no.estado):
                return Solucao(no)
            for no_suc in self._expandir(problema, no):
                self._memorizar(no_suc)

    def _expandir(self, problema, no):
        """
            Gera os nós sucessores a partir de um nó.
            Para cada operador definido no problema, tenta aplicar ao estado
            atual, se resultar num novo estado, calcula o novo custo,
            cria um novo nó sucessor e o adiciona à lista de sucessores.
        """
        sucessores = []
        estado = no.estado
        for operador in problema.operadores:
            estado_suc = operador.aplica(estado)
            if estado_suc is not None:
                custo = no.custo + operador.custo(estado, estado_suc)
                no_suc = No(estado_suc, operador, no, custo)
                sucessores.append(no_suc)
        return sucessores        