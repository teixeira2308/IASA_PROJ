"""
    Define as regras do mundo e gere os eventos, sem ambiente não há eventos a processar.
"""

from jogo.ambiente.EventoJogo import EventoJogo

class AmbienteJogo:
    def __init__(self):
        self.__evento = None
        self.__eventos = {evento.value: evento for evento in EventoJogo}

    def observar(self):
        return self.__evento

    def __gerar_evento(self): 
        texto = input("\nDigite um evento (s, r, a, f, o, t): ")
        return self.__eventos.get(texto)
        
    def evoluir(self):
        self.__evento = self.__gerar_evento()
        if self.__evento is not None:
            self.__evento.mostrar()
        
    def executar(self, comando):
        comando.mostrar()
        pass    

    def observar(self):
        return self.__evento