from Agenda import Agenda
from Tarefas import Tarefas
from atualizarCSV import atualizarCSV


def erroAgenda():
     print('''
        
******** Abra ou crie uma agenda antes de executar essa função ********        
                
        ''')   


opcao = ''


while opcao != '0':   
    
    
    opcao = input('''
Digite:
- 1  criar agenda
- 2  abrir agenda
- 3  para inserir tarefa
- 4  buscar tarefas de uma data específica
- 5  buscar tarefas de uma categoria específica
- 6  imprimir uma agenda inteira
- 7  para excluir tarefa
- 8  apaga todas as tarefas da agenda e mantém a agenda
- 9  apaga a agenda

ou qualquer outra coisa para finalizar: ''')
    
    if opcao == '1':
        
        nomeAgenda = input('Digite o nome da agenda: ')
        agenda = Agenda(nomeAgenda)

    elif opcao == '2':  
        nomeAgenda = input('Digite o nome da agenda a ser aberta: ')
        agenda = Agenda()
        agenda.abrirAgenda(nomeAgenda)

    elif opcao == '3':
        entrada = {}
        
        tituloTarefa   = input('Digite o nome da tarefa: ')
        prazo          = input('Digite a data limite: ')
        categoria      = input('Digite a categoria: ')       
        concluida      = 0
                
        tarefa = Tarefas(tituloTarefa, prazo, categoria)
        try:
            agenda.adicionarTarefa(tarefa)
            print('''
        
******** Tarefa '''+ tituloTarefa + ''' cadastrado com sucesso ********        
                
        ''')
        except:
            erroAgenda()  
        

    elif opcao == '4':
        prazo = input('Digite a data final da tarefa para consulta: ')
        
        try:
            resConsulta = agenda.visualizarTarefa(prazo)
            
            if len(resConsulta) > 0:
                print(f'''
    +++++++++ Tarefas do dia {prazo}: {resConsulta}''')
            else:
                print('''
    -------- Não há tarefas para esse dia --------
                ''')
        except:
            erroAgenda()
    
    elif opcao == '5':
        categoria = input('Digite a categoria para consulta: ')
        try:

            resConsulta = agenda.visualizarTarefa(categoria)
            
            if len(resConsulta) > 0:
                print(f'''
    +++++++++ Tarefas da categoria {categoria}: {resConsulta}''')
            else:
                print('''
    -------- Não há tarefas para dessa categoria --------
                ''')
        except:
            erroAgenda()
    
    elif opcao == '6':  
        try:
            print(agenda.tarefasAgendadas)
        except:
            erroAgenda()
        
    elif opcao == '7':
        tituloTarefa = input('Digite o nome da tarefa a ser excluída: ')
        try:
            agenda.removerTarefa(tituloTarefa)
            
        except:
            erroAgenda()
    
    elif opcao == '8':
        try:
            agenda.limparTarefasAgenda()           
            

            print('''
            
******** Agenda foi esvaziada com sucesso ********        
                    
            ''')
        except:
            erroAgenda()   

    elif opcao == '9':
        try:
            agenda.excluirAgenda()        
            agenda = ''
            
            print('''
        
******** Agenda foi apagada com sucesso ********        
                
        ''')
        except:
            erroAgenda()   
        


    else:        
        break