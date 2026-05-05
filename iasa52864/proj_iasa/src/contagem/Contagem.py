from lib.pee.prof.ProcuraProfundidade import ProcuraProfundidade
from lib.pee.larg.ProcuraLargura import ProcuraLargura
from lib.pee.prof.ProcuraProfLim import ProcuraProfLim
from lib.pee.prof.ProcuraProfIter import ProcuraProfIter
from lib.pee.melhor_prim.ProcuraCustoUnif import ProcuraCustoUnif
from lib.pee.melhor_prim.ProcuraSofrega import ProcuraSofrega
from lib.pee.melhor_prim.ProcuraAA import ProcuraAA
from contagem.mod_prob.ProblemaContagem import ProblemaContagem
from contagem.mod_prob.HeuristicaContagem import HeuristicaContagem
from lib.pee.melhor_prim.ProcuraInformada import ProcuraInformada

"""
    Este módulo é responsável por implementar a contagem utilizando diferentes mecanismos de procura.
    Ele define os mecanismos de procura a serem utilizados, os valores de contagem inicial e final
    e os incrementos disponíveis. Ele também define a função de teste que executa os mecanismos de procura
    no problema de contagem e imprime os resultados. 
"""

MECANISMOS_PROCURA = [
    ProcuraProfundidade(),
    ProcuraLargura(),
    ProcuraProfLim(),
    ProcuraProfIter(),
    ProcuraCustoUnif(),
    ProcuraSofrega(),
    ProcuraAA(),
]

"""
    A lista MECANISMOS_PROCURA contém as instâncias dos mecanismos de procura a serem testados no problema de contagem.
    Ela inclui os seguintes mecanismos de procura:
    - ProcuraProfundidade: busca em profundidade, que explora o caminho mais profundo primeiro.
    - ProcuraLargura: busca em largura, que explora todos os nós em um nível antes de passar para o próximo nível.
    - ProcuraProfLim: busca em profundidade limitada, que explora o caminho mais profundo primeiro, mas com um limite de profundidade.
    - ProcuraProfIter: busca em profundidade iterativa, que explora o caminho mais profundo primeiro, mas com um limite de profundidade que é aumentado iterativamente.
    - ProcuraCustoUnif: busca de custo uniforme, que explora o nó com o menor custo acumulado primeiro.
    - ProcuraSofrega: busca que explora o nó com a menor heurística primeiro, sem considerar o custo acumulado.
    - ProcuraAA: busca A*, que explora o nó com a menor soma do custo acumulado e da heurística primeiro.
"""

VALOR_INICIAL = 0 # Valor de contagem inicial, que é o estado inicial do problema.
VALOR_FINAL = 8 # Valor de contagem final, que é o estado objetivo do problema.
INCREMENTOS = [1, 2, 3] # Lista de incrementos disponíveis, que são os operadores de incremento que podem ser aplicados para alcançar o estado objetivo.

def teste_contagem(valor_inicial, valor_final, incrementos, mecanismos_procura):
    print() 
    print("Valor Inicial: ", valor_inicial) 
    
    problema = ProblemaContagem(valor_inicial, valor_final, incrementos) 

    for mec_proc in mecanismos_procura: 
        if isinstance(mec_proc, ProcuraInformada): # Verifica se o mecanismo de procura é uma instância da classe ProcuraInformada, que é a classe base para os mecanismos de procura informada (ProcuraSofrega, ProcuraAA e ProcuraA*).
            heuristica = HeuristicaContagem(valor_final) # Cria uma instância da heurística de contagem, que é utilizada pelos mecanismos de procura informada para estimar o custo de chegar ao estado objetivo a partir do estado atual.
            solucao = mec_proc.procurar(problema, heuristica) 
        else:
            solucao = mec_proc.procurar(problema) 
        print() 
        print(mec_proc.__class__.__name__) # Imprime o nome da classe do mecanismo de procura utilizado, para identificar qual mecanismo de procura foi testado.
        print("Solução: ", [passo.operador.incremento for passo in solucao]) # Imprime a solução encontrada, que é uma lista dos incrementos aplicados para alcançar o estado objetivo, extraídos dos operadores dos passos da solução.
        print("Dimensao: ", solucao.dimensao) # Imprime a dimensão da solução, que é o número de passos necessários para alcançar o estado objetivo a partir do estado inicial.
        print("Custo: ", solucao.custo) # Imprime o custo da solução, que é a soma dos custos dos operadores aplicados para alcançar o estado objetivo a partir do estado inicial. No caso do problema de contagem, o custo de cada operador é igual ao valor do incremento aplicado.

###
# 
if __name__ == "__main__":
    teste_contagem(VALOR_INICIAL, VALOR_FINAL, INCREMENTOS, MECANISMOS_PROCURA) # Chama a função de teste teste_contagem, passando os valores de contagem inicial, final, os incrementos disponíveis e a lista de mecanismos de procura a serem testados. Esta função executa os mecanismos de procura no problema de contagem e imprime os resultados.         