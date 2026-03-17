"""
    Define as regras do mundo e gere os eventos, sem ambiente não há eventos a processar.

"""

from jogo.ambiente.EventoJogo import EventoJogo

class AmbienteJogo:
    def __init__(self):
        self.__evento = None
        self.__eventos = {evento.value: evento for evento in EventoJogo}

    def observar(self):
        """Fornece ao agente os dados sensoriais. Na teoria, é
        onde o agente lê o estado do mundo"""
        return self.__evento

    def __gerar_evento(self): 
        """Ambiente discreto. Os eventos são selecionados
        a partir de um conjunto fixo."""
        texto = input("\nDigite um evento (s, r, a, f, o, t): ")
        return self.__eventos.get(texto)
        
    def evoluir(self):
        """Representa a passagem do tempo e a mudança de estado
        do agente"""
        self.__evento = self.__gerar_evento()
        if self.__evento is not None:
            self.__evento.mostrar()
        
    def executar(self, comando):
        """É aqui que a ação que é definida executa no mundo. 
        O ambiente recebe a intenção do agente."""
        comando.mostrar()
        pass    

    def observar(self):
        return self.__evento