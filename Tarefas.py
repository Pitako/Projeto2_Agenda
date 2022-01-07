class Tarefas:

    def __init__(self, titulo, dataRealizacao, categoria=0):
        self.titulo = titulo
        self.dataRealizacao = dataRealizacao
        self.categoria = categoria
        self.concluida = 0

    def alterarStatus(self):
        pass

    def alterarCategoria(self,idCategoria):
        self.categoria = idCategoria

    def __repr__(self) -> str:
        return f'{self.titulo};{self.dataRealizacao};{self.categoria};{self.concluida}'
