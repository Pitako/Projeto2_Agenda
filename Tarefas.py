from atualizarCSV import atualizarCSV
class Tarefas:

    def __init__(self, titulo, prazo, categoria=0, status='Pendente'):
        self.titulo = titulo
        self.prazo = prazo
        self.categoria = categoria
        self.status = status

    def __repr__(self) -> str:
        return f'{self.titulo};{self.prazo};{self.categoria};{self.status}'
