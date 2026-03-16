from abc import ABC, abstractmethod

""" recebe ABC e abstractmethod para criar uma classe abstrata Controlo, que define um método abstrato processar().
    O controlo funciona como "cérebro" do agente, ele controla o comportamento
"""

class Controlo(ABC):
    
    """ 
        Método abstrato processar() implementado pelas subclasses, que recebe uma perceção e gera uma ação. 
        É um método abstrato, ou seja, não tem implementação na classe base e deve ser implementado pelas subclasses.
    """

    @abstractmethod
    def processar(self, percecao):
        """ Processar perceção gerando uma ação """