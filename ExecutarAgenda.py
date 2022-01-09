from Agenda import Agenda
from Tarefas import Tarefas
from atualizarCSV import atualizarCSV
import os

def pressioneEnter():
    input(''' 
    Pressione enter para continuar....''')


def erroAgenda():
    print('''
        
******** Abra ou crie uma agenda antes de executar essa função ********        
                
        ''')
    pressioneEnter()   

def infoAgenda():
    print(f'''
********* Agenda {agenda} *********
''')


opcao = ''

while opcao != '0':   
    os.system('cls')
    
    opcao = input('''
Digite:
- 1  criar agenda
- 2  abrir agenda
- 3  para inserir tarefa
- 4  buscar tarefas de uma data específica
- 5  buscar tarefas de uma categoria específica
- 6  alterar status de uma tarefa
- 7  alterar categoria de uma tarefa
- 8  imprimir uma agenda inteira 
- 9  para excluir tarefa
- 10 apaga todas as tarefas da agenda e mantém a agenda
- 11 apaga a agenda

ou qualquer outra coisa para finalizar: ''')
    
    if opcao == '1':
        
        nomeAgenda = input('Digite o nome da agenda: ')
        try:
            agenda = Agenda(nomeAgenda)
            print('''
            
    ******** Agenda '''+ nomeAgenda + ''' criada com sucesso ********        
                    
            ''')
            pressioneEnter()
        except:
            print('Falha ao criar agenda')
            pressioneEnter()

    elif opcao == '2':  
        nomeAgenda = input('Digite o nome da agenda a ser aberta: ')        
        agenda = Agenda()
        try:
            agenda.abrirAgenda(nomeAgenda)
            print('''
            
    ******** Agenda '''+ nomeAgenda + ''' carregada com sucesso ********        
                    
            ''')
            pressioneEnter()
        except:
            print('Agenda não encontrada!!!')
            pressioneEnter()

    elif opcao == '3':
        infoAgenda()
        entrada = {}
        
        tituloTarefa   = input('Digite o nome da tarefa: ')
        prazo          = input('Digite a data limite: ')
        categoria      = input('Digite a categoria: ')       
        status         = 'Pendente'
                
        tarefa = Tarefas(tituloTarefa, prazo, categoria)
        try:
            agenda.adicionarTarefa(tarefa)
            print('''
        
******** Tarefa '''+ tituloTarefa + ''' cadastrado com sucesso ********        
                
        ''')
            pressioneEnter()
        except:
            erroAgenda()
            
        

    elif opcao == '4':
        infoAgenda()
        prazo = input('Digite a data final da tarefa para consulta: ')
        
        try:
            resConsulta = agenda.visualizarTarefa(prazo)
            
            if len(resConsulta) > 0:
                print(f'''
    +++++++++ Tarefas do dia {prazo}: {resConsulta}''')
                pressioneEnter()
            else:
                print('''
    -------- Não há tarefas para esse dia --------
                ''')
                pressioneEnter()
        except:
            erroAgenda()
    
    elif opcao == '5':
        infoAgenda()
        categoria = input('Digite a categoria para consulta: ')
        try:

            resConsulta = agenda.visualizarTarefa(categoria)
            
            if len(resConsulta) > 0:
                print(f'''
    +++++++++ Tarefas da categoria {categoria}: {resConsulta}''')
                pressioneEnter()
            else:
                print('''
    -------- Não há tarefas dessa categoria --------
                ''')
                pressioneEnter()
        except:
            erroAgenda()
    
    elif opcao == '6':  
        infoAgenda()
        try:
            nome = input('Qual tarefa você deseja alterar o status?')               
            agenda.update_status(nome)
            print('''
        
******** Tarefa '''+ nome + ''' alterada com sucesso ********        
                
        ''')
            pressioneEnter()
        except:
            print('''
-------- Não há tarefas com esse nome --------
            ''')
            pressioneEnter()
        
        #atualizarCSV.carregarLinhasArquivo(agenda)

    elif opcao == '7':  
        infoAgenda()
        nome = input('Qual tarefa você deseja alterar a categoria?')  
        categoria = input('Qual será a nova categoria? ')     
        try: 
            agenda.alterarCategoria(nome, categoria)
            print('''
        
******** Tarefa '''+ nome + ''' alterada com sucesso ********        
                
        ''')
            pressioneEnter()
        except:
            print('''
-------- Não há tarefas para com esse nome --------
            ''')
            pressioneEnter()

    elif opcao == '8':  
        try:
            infoAgenda()
            print(agenda.tarefasAgendadas)
            pressioneEnter()
        except:
            erroAgenda()        
    
    elif opcao == '9':
        infoAgenda()
        tituloTarefa = input('Digite o nome da tarefa a ser excluída: ')
        try:
            agenda.removerTarefa(tituloTarefa)
            print('''
        
******** Tarefa '''+ tituloTarefa + ''' excluída com sucesso ********        
                
        ''')
            pressioneEnter()
            
        except:
            print('''
        
******** A tarefa não existe ********        
                
        ''')
            pressioneEnter()  
    
    
    elif opcao == '10':
        infoAgenda()
        try:
            agenda.limparTarefasAgenda()           
            

            print('''
            
******** Agenda foi esvaziada com sucesso ********        
                    
            ''')
            pressioneEnter()
        except:
            erroAgenda() 

    elif opcao == '11':
        infoAgenda()
        try:
            agenda.excluirAgenda()        
            agenda = ''

            print('''
        
******** Agenda foi apagada com sucesso ********        
                
        ''')
            pressioneEnter()
        except:
            erroAgenda()   
        


    else:        
        break