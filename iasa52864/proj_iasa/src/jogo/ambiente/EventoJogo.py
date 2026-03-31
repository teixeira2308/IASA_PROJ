from enum import Enum

"""Os eventos representam o que os sensores do agente captam.
    Esta classe é uma enumeração que define os eventos possíveis no ambiente do jogo,
    que são definidos em baixo (linha 9).
"""

class EventoJogo(Enum):
    SILENCIO = 's'
    RUIDO = 'r'
    ANIMAL = 'a'
    FUGA = 'f'
    FOTOGRAFIA = 'o'
    TERMINAR = 't'

    def mostrar(self):
        print(f"\nEvento: {self.name}")