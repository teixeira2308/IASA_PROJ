import enum

"""O EstadoPersonagem representa o raciocinio e estad
do agente.
PROCURA -> Estado de exploração
INSPECAO -> O agente está em Alerta
OBSERVACAO -> Está em Foco
REGISTO -> Estado final, faz o registo"""


class EstadoPersonagem(enum.Enum):
    PROCURA = 'p'
    INSPECAO = 'i'
    OBSERVACAO = 'o'
    REGISTO = 'r'

    def mostrar(self):
        return self.name