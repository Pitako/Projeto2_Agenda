class Tarefas:

    def __init__(self, titulo, prazo, categoria=0, concluida=0):
        self.titulo = titulo
        self.prazo = prazo
        self.categoria = categoria
        self.concluida = concluida

    def update_status(self, status=None):
        if status != None:
            self.status = status

    def alterarCategoria(self,idCategoria):
        self.categoria = idCategoria

    def __repr__(self) -> str:
        return f'{self.titulo};{self.prazo};{self.categoria};{self.concluida}'
