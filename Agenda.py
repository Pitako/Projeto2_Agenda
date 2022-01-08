import os
from Tarefas import Tarefas

class Agenda:

    def __init__(self, nome):
        
        arqAgenda = open(nome+'.csv', mode='+a')

        if os.stat(arqAgenda.name).st_size == 0:            
            arqAgenda.write('titulo;prazo;categoria;concluida')
        else:
            raise FileExistsError('Já existe agenda com esse nome')
        
        self.nome = nome
        self.tarefasAgendadas = {}
        self.arquivo = arqAgenda

    
    def abrirAgenda(self,nome):
        # ler arquivo e carregar tarefas na agenda
        pass        	

    def adicionarTarefa(self,tarefa):
        self.tarefasAgendadas[tarefa.titulo] = {'prazo':tarefa.prazo, 'categoria':tarefa.categoria , 'concluida':tarefa.concluida}

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

    
