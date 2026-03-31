from enum import Enum

"""Espaço de Ações, as ações são os comportamentos do agente.
    Esta classe é uma enumeração que define as ações possíveis no ambiente do jogo,
    que são definidos em baixo (linha 9).
"""

class ComandoJogo(Enum):
    PROCURAR = 'p'
    APROXIMAR = 'a'
    OBSERVAR = 'o'
    FOTOGRAFAR = 'f'

    def mostrar(self):
        print(f"\nComando: {self.name}")
