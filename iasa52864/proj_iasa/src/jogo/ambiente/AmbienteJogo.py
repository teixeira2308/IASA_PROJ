"""
    Define as regras do mundo e gere os eventos, sem ambiente não há eventos a processar.
"""

class AmbienteJogo:
    def __init__(self, EventoJogo):
        self.__evento = None
        self.__eventos = {evento.value: evento for evento in EventoJogo}

    def observar(self):
        return self.__eventos

    def _gerar_evento(self): 
        texto = input("\nDigite um evento (s, r, a, f, o, t): ")
        if texto in self.__eventos:
            return self.__eventos.get(texto)
        else:
            print("Evento inválido. Tente novamente.")
            return self._gerar_evento()
        
    def evoluir(self):
        texto = input("\nDigite um comando (p, a, o, f): ")
        self.__evento = self._gerar_evento()
        if self.__evento is not None:
            return self.__evento.get(texto)
        
    def executar(self, comando):
        comando.mostrar()
        pass    