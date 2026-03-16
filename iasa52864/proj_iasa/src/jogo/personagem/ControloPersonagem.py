
from lib.agente.Controlo import Controlo
from jogo.agente import AccaoJogo
from jogo.ambiente.ComandoJogo import ComandoJogo
from jogo.ambiente.EventoJogo import EventoJogo
from jogo.personagem.EstadoPersonagem import EstadoPersonagem
from lib.maqest.MaquinaEstados import MaquinaEstados

class ControloPersonagem(Controlo):
    def __init__(self):
        self.procurar = AccaoJogo(ComandoJogo.PROCURAR)
        self.aproximar = AccaoJogo(ComandoJogo.APROXIMAR)
        self.observar = AccaoJogo(ComandoJogo.OBSERVAR)
        self.fotografar = AccaoJogo(ComandoJogo.FOTOGRAFAR)

    def processar(self, percepcao):
        self.__maq_est = MaquinaEstados(EstadoPersonagem.PROCURA, [
            (EstadoPersonagem.PROCURA, EventoJogo.ANIMAL, 
            EstadoPersonagem.OBSERVACAO, self.aproximar),
            (EstadoPersonagem.INSPECAO, EventoJogo.SILENCIO,
            EstadoPersonagem.PROCURA),
            (EstadoPersonagem.REGISTO, EventoJogo.FOTOGRAFIA, EstadoPersonagem.PROCURA),
            (EstadoPersonagem.REGISTO, EventoJogo.FUGA, EstadoPersonagem.PROCURA),
            (EstadoPersonagem.PROCURA, EventoJogo.SILENCIO, EstadoPersonagem.PROCURA, self.procurar)], 
            EstadoPersonagem.INSPECAO, [
                (EstadoPersonagem.INSPECAO, EventoJogo.ANIMAL, EstadoPersonagem.OBSERVACAO, self.aproximar),
                (EstadoPersonagem.OBSERVACAO, EventoJogo.FUGA, EstadoPersonagem.INSPECAO),
                (EstadoPersonagem.INSPECAO, EventoJogo.RUIDO, EstadoPersonagem.INSPECAO, self.procurar),
                (EstadoPersonagem.PROCURA, EventoJogo.RUIDO, EstadoPersonagem.INSPECAO, self.aproximar),
                (EstadoPersonagem.INSPECAO, EventoJogo.SILENCIO, EstadoPersonagem.PROCURA)
            ], 
            EstadoPersonagem.REGISTO, [
                (EstadoPersonagem.REGISTO, EventoJogo.FUGA, EstadoPersonagem.PROCURA),
                (EstadoPersonagem.REGISTO, EventoJogo.FOTOGRAFIA, EstadoPersonagem.PROCURA),
                (EstadoPersonagem.OBSERVACAO, EventoJogo.ANIMAL, EstadoPersonagem.REGISTO, self.observar),
                (EstadoPersonagem.REGISTO, EventoJogo.ANIMAL, EstadoPersonagem.REGISTO, self.fotografar),
                
            ],
            EstadoPersonagem.OBSERVACAO, [
                (EstadoPersonagem.OBSERVACAO, EventoJogo.FUGA, EstadoPersonagem.INSPECAO),
                (EstadoPersonagem.OBSERVACAO, EventoJogo.ANIMAL, EstadoPersonagem.REGISTO, self.observar),
                (EstadoPersonagem.INSPECAO, EventoJogo.ANIMAL, EstadoPersonagem.OBSERVACAO, self.aproximar),
                (EstadoPersonagem.PROCURA, EventoJogo.ANIMAL, EstadoPersonagem.OBSERVACAO, self.aproximar)
            ]
        )
