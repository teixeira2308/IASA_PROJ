from enum import Enum

class ComandoJogo(Enum):
    PROCURAR = 'p'
    APROXIMAR = 'a'
    OBSERVAR = 'o'
    FOTOGRAFAR = 'f'

    def mostrar(self):
        print(f"\nComando: {self.name}")
