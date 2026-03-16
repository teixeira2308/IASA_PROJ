"""Classe responsável para executar o jogo, que é o ambiente onde os personagens atuam.
Classe main"""

from jogo.ambiente.AmbienteJogo import AmbienteJogo
from jogo.personagem.Personagem import Personagem
from jogo.ambiente.EventoJogo import EventoJogo


class jogo:
    def __init__ (self):
        self.__ambiente = AmbienteJogo(EventoJogo)
        self.__personagem = Personagem(self.__ambiente)

    def Jogo(self):
        return 0
    
    def executar(self):
        while True:
            self.__ambiente.evoluir()
            self.__personagem.executar()
            self.__personagem.mostrar()
            if self.observar() == True:
                self.__personagem.mostrar()
        pass        


if __name__ == "__main__":
    jogo().executar()    