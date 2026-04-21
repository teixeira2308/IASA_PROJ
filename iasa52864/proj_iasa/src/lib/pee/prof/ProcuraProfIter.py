from lib.pee.prof.ProcuraProfLim import ProcuraProfLim

"""
    Esta classe representa a ProcuraProfIter, que é uma classe para
    implementar a procura em profundidade iterativa. Ela herda
    da classe ProcuraProfLim e utiliza um limite de profundidade iterativo.
    A busca em profundidade iterativa é uma estratégia de procura que
    explora o mais profundo possível antes de retroceder,
    mas com um limite de profundidade que é incrementado a cada iteração.
"""

class ProcuraProfIter(ProcuraProfLim):
    def procurar(self, problema, inc_prof=1, limite_prof= 100): 
        for prof_max in range(0, limite_prof+1, inc_prof): 
            solucao = super().procurar(problema, prof_max) # Chama o método procurar da classe pai,
                                                            #passando o limite de profundidade atual (prof_max) como parâmetro.
            if solucao: # Se uma solução for encontrada, ela é retornada.
                        # Caso contrário, a busca continua com o próximo
                        #  limite de profundidade.
                return solucao
