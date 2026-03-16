from jogo.agente.AgenteJogo import AgenteJogo
from jogo.personagem.ControloPersonagem import ControloPersonagem
"""
    A classe personagem é a classe base para os personagens do jogo, que são agentes que atuam no ambiente do jogo.
    O personagem é a representação do agente dentro do ambiente do jogo. Enquanto o agente é o "cérebro", a personagem é o "corpo" que ocupa o espaço do jogo
"""

class Personagem(AgenteJogo):
    def __init__(self, ambiente):
        super().__init__(ambiente, ControloPersonagem())

    def mostrar(self):
        """ Mostrar o estado do personagem. """
