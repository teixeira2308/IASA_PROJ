"""
    Uma solução para um problema é composta por uma sequência de passos,
    que levam do estado inicial a um estado objetivo.
    Cada passo precisa registar dois elementos: o estado alcançado,
    e o operador que foi aplicado para chegar a esse estado.
    Após a procura, ele percorre os antecessores e converte em objeto para apresentar
    um plano de ação.
"""

class PassoSolucao:
    def __init__(self, estado, operador):
        """
            Construtor da etapa da solução.
        """
        self.__estado = estado
        self.__operador = operador

    @property
    def estado(self):
        """
            Permite aceder ao estado do passo. Getter.
        """
        return self.__estado

    @property
    def operador(self):
        """
            Permite aceder ao operador do passo. Getter.
        """
        return self.__operador    