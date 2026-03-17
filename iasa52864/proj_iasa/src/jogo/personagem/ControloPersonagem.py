
from lib.agente.Controlo import Controlo
from jogo.agente.AccaoJogo import AccaoJogo
from jogo.ambiente.ComandoJogo import ComandoJogo
from jogo.ambiente.EventoJogo import EventoJogo
from jogo.personagem.EstadoPersonagem import EstadoPersonagem
from lib.maqest.MaquinaEstados import MaquinaEstados

"""É a gerencia do personagem com base na máquina
de estados, com base no diagrama. Definimos todos
os comportamentos do personagem com base no evento
escolhido. """

class ControloPersonagem:
    def __init__(self):
        self.__maq_est = None
        self.procurar = AccaoJogo(ComandoJogo.PROCURAR)
        self.aproximar = AccaoJogo(ComandoJogo.APROXIMAR)
        self.observar = AccaoJogo(ComandoJogo.OBSERVAR)
        self.fotografar = AccaoJogo(ComandoJogo.FOTOGRAFAR)

        self.__maq_est = MaquinaEstados(EstadoPersonagem.PROCURA, [
            (EstadoPersonagem.PROCURA, EventoJogo.ANIMAL, EstadoPersonagem.OBSERVACAO, self.aproximar),
            (EstadoPersonagem.PROCURA, EventoJogo.RUIDO, EstadoPersonagem.INSPECAO, self.aproximar),
            (EstadoPersonagem.PROCURA, EventoJogo.SILENCIO, EstadoPersonagem.PROCURA, self.procurar),
            
            (EstadoPersonagem.INSPECAO, EventoJogo.SILENCIO, EstadoPersonagem.PROCURA),
            (EstadoPersonagem.INSPECAO, EventoJogo.ANIMAL, EstadoPersonagem.OBSERVACAO, self.aproximar),
            (EstadoPersonagem.INSPECAO, EventoJogo.RUIDO, EstadoPersonagem.INSPECAO, self.procurar),
            
            (EstadoPersonagem.OBSERVACAO, EventoJogo.ANIMAL, EstadoPersonagem.REGISTO, self.observar),
            (EstadoPersonagem.OBSERVACAO, EventoJogo.FUGA, EstadoPersonagem.INSPECAO),
            
            (EstadoPersonagem.REGISTO, EventoJogo.ANIMAL, EstadoPersonagem.REGISTO, self.fotografar),
            (EstadoPersonagem.REGISTO, EventoJogo.FOTOGRAFIA, EstadoPersonagem.PROCURA),
            (EstadoPersonagem.REGISTO, EventoJogo.FUGA, EstadoPersonagem.PROCURA)
        ])

    @property
    def estado(self):
        return self.__maq_est.estado

    def processar(self, percecao):
        return self.__maq_est.processar(percecao.evento)