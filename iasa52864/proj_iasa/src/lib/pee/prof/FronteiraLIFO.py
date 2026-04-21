from lib.pee.mec_proc.Fronteira import Fronteira

"""
    Esta classe representa a FronteiraLIFO, (Last In First Out)
    que é uma estrutura de dados utilizada para armazenar os nós
    a serem explorados. A FronteiraLIFO é utilizada na busca em profundidade,
    onde o último nó inserido é o próximo a ser explorado. Ela herda
    da classe Fronteira e implementa o metodo inserir de forma a adicionar
    os nós no final da lista, garantindo que o último nó inserido seja o primeiro a ser removido.
"""

class FronteiraLIFO(Fronteira):
    def inserir(self, no):
        """
            Insere um nó na fronteira. O nó é adicionado no final da lista,
            garantindo que o último nó inserido seja o primeiro a ser removido.
        """
        self.__lista.append(no)
        pass