from Agenda import Agenda
from Tarefas import Tarefas


#exibe opções
#1-Criar agenda   
#2-Abrir agenda salva passando nome da agenda (abrir arquivo com mesmo nome)

## exibe opções sobre a agenda
# adiciona tarefa na agenda
# altera status da tarefa
# altera categoria da tarefa
# remove tarefa da agenda
# visualiza tarefas do dia
# visualiza todas as tarefas
# apaga todas as tarefas da agenda e mantém a agenda
# apaga agenda inclusive seu arquivo
# fechar


opcao = ''

while opcao != '0':   
    
    
    opcao = input('''
Digite:
- 1 para criar agenda
- 2 abrir agenda
- 3 para inserir tarefa
- 4 para excluir tarefa
- 5 buscar tarefas de uma data específica
- 6 buscar tarefas de uma categoria específica
- 7 imprimir uma agenda inteira
- 8 apaga todas as tarefas da agenda e mantém a agenda

ou qualquer outra coisa para finalizar: ''')
    
    if opcao == '1':
        
        nomeAgenda = input('Digite o nome da agenda: ')
        agenda = Agenda(nomeAgenda)

    elif opcao == '2':
        entrada = {}
        
        tituloTarefa   = input('Digite o nome da tarefa: ')
        prazo          = input('Digite a data limite: ')
        categoria      = input('Digite a categoria: ')       
        concluida      = 0
                
        tarefa = Tarefas(tituloTarefa, prazo, categoria)
        agenda.adicionarTarefa(tarefa)
        
        print('''
        
******** Tarefa '''+ tituloTarefa + ''' cadastrado com sucesso ********        
                
        ''')
        
        
    elif opcao == '3':
        tituloTarefa = input('Digite o nome da tarefa a ser excluda: ')
        agenda.removerTarefa(tituloTarefa)
    
    elif opcao == '4':  
        try:
            print(agenda.tarefasAgendadas)
        except:
            print('Nenhuma agenda aberta')
    
    elif opcao == '5':  
        nomeAgenda = input('Digite o nome da agenda a ser aberta: ')
        agenda = Agenda()
        agenda.abrirAgenda(nomeAgenda)

            
        

    elif opcao == '5':
        prazo = input('Digite a data final da tarefa para consulta: ')
        
        resConsulta = agenda.visualizarTarefa(prazo)
        
        if len(resConsulta) > 0:
            print(f'''
+++++++++ Tarefas do dia {prazo}: {resConsulta}''')
        else:
            print('''
-------- Não há tarefas para esse dia --------
            ''')
    
    elif opcao == '6':
        categoria = input('Digite a categoria para consulta: ')
        
        resConsulta = agenda.visualizarTarefa(categoria)
        
        if len(resConsulta) > 0:
            print(f'''
+++++++++ Tarefas da categoria {categoria}: {resConsulta}''')
        else:
            print('''
-------- Não há tarefas para dessa categoria --------
            ''')
    
    elif opcao == '7':
        agenda.limpar()

        print('''
        
******** Agenda foi esvaziada com sucesso ********        
                
        ''')

    else:        
        break