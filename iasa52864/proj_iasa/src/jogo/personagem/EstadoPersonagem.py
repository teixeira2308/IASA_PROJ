import enum


class EstadoPersonagem(enum.Enum):
    PROCURA = 'p'
    INSPECAO = 'i'
    OBSERVACAO = 'o'
    REGISTO = 'r'

    def mostrar(self):
        return self.name