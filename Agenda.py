import os
import Tarefas

class Agenda:

    
    def __init__(self, nome):
        
        arqAgenda = open(nome+'.csv', mode='+a')

        if os.stat(arqAgenda.name).st_size == 0:            
            arqAgenda.write('titulo;dataRealizacao;categoria;concluida')
        else:
            raise FileExistsError('Já existe agenda com esse nome')
        
        self.nome = nome
        self.tarefasAgendadas = {}
        self.arquivo = arqAgenda

    
    def abrirAgenda(self,nome):
        # ler arquivo e carregar tarefas na agenda
        pass        	

    def adicionarTarefa(self,tarefa):
        self.tarefasAgendadas[tarefa.titulo] = {'dataRealizacao':tarefa.dataRealizacao, 'categoria':tarefa.categoria , 'concluida':tarefa.concluida}

    def removerTarefa(self,tarefa):
        pass
    
    def visualizarTarefa(self,dia=None):
        if dia == None:
            print(self.tarefasAgendadas)

    def limpar():
        pass

    
