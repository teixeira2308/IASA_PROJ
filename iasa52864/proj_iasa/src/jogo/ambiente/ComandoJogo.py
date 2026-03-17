from enum import Enum

"""Espaço de Ações, as ações são os comportamentos do agente."""

class ComandoJogo(Enum):
    PROCURAR = 'p'
    APROXIMAR = 'a'
    OBSERVAR = 'o'
    FOTOGRAFAR = 'f'

    def mostrar(self):
        print(f"\nComando: {self.name}")
