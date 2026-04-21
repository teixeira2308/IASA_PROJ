from lib.pee.prof.ProcuraProfundidade import ProcuraProfundidade

"""
    Esta classe representa a ProcuraProfLim, que é uma classe para
    implementar a procura em profundidade com limite. Ela herda
    da classe ProcuraProfundidade e o limite é utilizado para evitar
    que a busca se aprofunde demais.
"""

class ProcuraProfLim(ProcuraProfundidade):
    def procurar(self, problema, prof_max=10):
        """
            Este método é responsável por iniciar a procura em profundidade com limite.
            Ele recebe um problema e um limite de profundidade (prof_max) como parâmetros.
            O limite de profundidade é utilizado para evitar que a busca se aprofunde demais.
        """
        self.__prof_max = prof_max

    def _expandir(self, problema, no):
        """
            Este método é responsável por expandir um nó.
            Ele recebe um problema e um nó como parâmetros.
            O nó é expandido apenas se a sua profundidade for menor que o limite de profundidade (prof_max).
        """
        return super()._expandir(problema, no) if no.profundidade < self.__prof_max else [] 
