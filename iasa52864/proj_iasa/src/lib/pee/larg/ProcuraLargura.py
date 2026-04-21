from lib.pee.mec_proc.ProcuraGrafo import ProcuraGrafo

"""
    Esta classe representa a ProcuraLargura, que é uma classe para implementar
    algoritmos de procura em largura. Ela herda da classe ProcuraGrafo
    e utiliza uma FronteiraFIFO (First In First Out) para armazenar os nós a serem explorados.
    A busca em largura é uma estratégia de procura que explora todos os nós
    em um nível antes de passar para o próximo nível, garantindo que o caminho mais curto
    seja encontrado, caso exista um caminho entre o nó inicial e o nó objetivo.
"""

class ProcuraLargura(ProcuraGrafo):
    def __init__(self):
        """
            Construtor da classe ProcuraLargura. Ele chama o construtor da classe pai
            passando uma instância da FronteiraFIFO (First In First Out), que é a estrutura de dados utilizada
            para armazenar os nós a serem explorados.
        """
        super()._iniciar_memoria()