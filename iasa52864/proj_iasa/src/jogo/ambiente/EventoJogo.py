from enum import Enum

class EventoJogo(Enum):
    SILENCIO = 's'
    RUIDO = 'r'
    ANIMAL = 'a'
    FUGA = 'f'
    FOTOGRAFIA = 'o'
    TERMINAR = 't'

    def mostrar(self):
        print(f"\nEvento: {self.name}")