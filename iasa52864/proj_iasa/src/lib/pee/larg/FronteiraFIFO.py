from lib.pee.mec_proc.Fronteira import Fronteira

"""
    Esta classe representa a FronteiraFIFO, (First In First Out)
    que é uma estrutura de dados utilizada para armazenar os nós
    a serem explorados. A FronteiraFIFO é utilizada na busca em largura,
    onde o primeiro nó inserido é o próximo a ser explorado. Ela herda
    da classe Fronteira e implementa o metodo inserir de forma a adicionar
    os nós no final da lista, garantindo que o primeiro nó inserido seja 
    o primeiro a ser removido.
"""

class FronteiraFIFO(Fronteira):
    def inserir(self, no):
        self.__lista.append(no) #adiciona o nó no final da lista,
                                #garantindo que o primeiro nó inserido seja
                                # o primeiro a ser removido.
        pass