"""Classe responsável para executar o jogo, que é o ambiente onde os personagens atuam.
Classe main"""

from jogo.ambiente.AmbienteJogo import AmbienteJogo
from jogo.personagem.Personagem import Personagem
from jogo.ambiente.EventoJogo import EventoJogo


class Jogo:
    def __init__ (self):
        self.__ambiente = AmbienteJogo()
        self.__personagem = Personagem(self.__ambiente)
        self.__personagem.mostrar()
    
    def executar(self):
        while True:
            self.__ambiente.evoluir()
            self.__personagem.executar()
            self.__personagem.mostrar()
            
            percepcao = self.__personagem._percecionar()

            if percepcao.evento == EventoJogo.TERMINAR:
                break

            if percepcao.evento is None:
                continue

            accao = self.__personagem.processar(percepcao)
            if accao:
                self.__personagem._actuar(accao)


if __name__ == "__main__":
    Jogo().executar()    