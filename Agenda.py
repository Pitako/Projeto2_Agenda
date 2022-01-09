import os
from Tarefas import Tarefas

from atualizarCSV import atualizarCSV

class Agenda:

    
    def __init__(self, nome=None):        

        if nome != None:
            try:
                atualizarCSV.criarArquivo(nome)               
                    
            except Exception as e:
                print('Não foi possível criar a agenda. ')
                print(e)       

        self.nome = nome
        self.tarefasAgendadas = {}


    def abrirAgenda(self,nome):
        self.nome = nome

        # ler arquivo e carregar tarefas na agenda
        linhas = atualizarCSV.carregarLinhasArquivo(self.nome)
        for registro in linhas:
            tarefa = registro.split(';')
            self.adicionarTarefa(Tarefas(tarefa[0],tarefa[1],tarefa[2],tarefa[3]))

        

    def adicionarTarefa(self,tarefa):
        self.tarefasAgendadas[tarefa.titulo] = {'prazo':tarefa.prazo, 'categoria':tarefa.categoria , 'status':tarefa.status}
        atualizarCSV.inserirLinha(self.nome, str(tarefa))

    def update_status(self, nome):
        if self.tarefasAgendadas[nome]['status'] == 'Pendente':
            self.tarefasAgendadas[nome]['status'] = 'Concluída'
        else:
            self.tarefasAgendadas[nome]['status'] = 'Pendente'

    def alterarCategoria(self, nome, categoria):
        self.tarefasAgendadas[nome]['categoria'] = categoria

    def removerTarefa(self,tarefa):
        resExcluir = self.tarefasAgendadas.pop(tarefa, False)
        
        if resExcluir:
            print(f'''
+++++++++ Tarefa {tarefa} excluída: {resExcluir}''')
        else:
            print('''
-------- Tarefa não encontrada --------
            ''')
    
    def visualizarTarefa(self,consulta=None):
        resultado_consulta = []
        for i in self.tarefasAgendadas.keys():
            if consulta in self.tarefasAgendadas[i].values():
                print(f'{i} : {self.tarefasAgendadas[i]}')
                resultado_consulta.append(i)
        return resultado_consulta
            
    
    def limpar(self):
        self.tarefasAgendadas.clear()

    def __repr__(self) -> str:
        return f'{self.nome}'

    
