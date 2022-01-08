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
        self.tarefasAgendadas[tarefa.titulo] = {'prazo':tarefa.prazo, 'categoria':tarefa.categoria , 'concluida':tarefa.concluida}
        atualizarCSV.inserirLinha(self.nome, str(tarefa))


    def removerTarefa(self,tarefa):
        pass
    
    def visualizarTarefa(self,dia=None):
        if dia == None:
            print(self.tarefasAgendadas)

    def limpar():
        pass

    
