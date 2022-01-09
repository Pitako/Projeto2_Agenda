from Agenda import Agenda
from Tarefas import Tarefas
from atualizarCSV import atualizarCSV


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
- 1  para criar agenda
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
        agenda = Agenda(nomeAgenda)

    elif opcao == '2':  
        nomeAgenda = input('Digite o nome da agenda a ser aberta: ')
        agenda = Agenda()
        agenda.abrirAgenda(nomeAgenda)

    elif opcao == '3':
        print(f'********* Agenda {agenda} *********')
        entrada = {}
        
        tituloTarefa   = input('Digite o nome da tarefa: ')
        prazo          = input('Digite a data limite: ')
        categoria      = input('Digite a categoria: ')       
        status         = 'Pendente'
                
        tarefa = Tarefas(tituloTarefa, prazo, categoria, status)
        agenda.adicionarTarefa(tarefa)
        
        print('''
        
******** Tarefa '''+ tituloTarefa + ''' cadastrado com sucesso ********        
                
        ''')
        atualizarCSV.inserirLinha(agenda, tarefa)

    elif opcao == '4':
        print(f'********* Agenda {agenda} *********')
        prazo = input('Digite a data final da tarefa para consulta: ')
        
        resConsulta = agenda.visualizarTarefa(prazo)
        
        if len(resConsulta) > 0:
            print(f'''
+++++++++ Tarefas do dia {prazo}: {resConsulta}''')
        else:
            print('''
-------- Não há tarefas para esse dia --------
            ''')
    
    elif opcao == '5':
        print(f'********* Agenda {agenda} *********')
        categoria = input('Digite a categoria para consulta: ')
        
        resConsulta = agenda.visualizarTarefa(categoria)
        
        if len(resConsulta) > 0:
            print(f'''
+++++++++ Tarefas da categoria {categoria}: {resConsulta}''')
        else:
            print('''
-------- Não há tarefas para dessa categoria --------
            ''')

    elif opcao == '6':  
        print(f'********* Agenda {agenda} *********')
        try:
            nome = input('Qual tarefa você deseja alterar o status?')   
            agenda.update_status(nome)
        except:
            print('''
-------- Não há tarefas para com esse nome --------
            ''')
        
        #atualizarCSV.carregarLinhasArquivo(agenda)

    elif opcao == '7':  
        print(f'********* Agenda {agenda} *********')
        nome = input('Qual tarefa você deseja alterar a categoria?')  
        categoria = input('Qual será a nova categoria? ')     
        try: 
            agenda.alterarCategoria(nome, categoria)
        except:
            print('''
-------- Não há tarefas para com esse nome --------
            ''')

    elif opcao == '8':  
        try:
            print(f'********* Agenda {agenda} *********')
            print(agenda.tarefasAgendadas)
        except:
            print('Nenhuma agenda aberta')
        
    elif opcao == '9':
        print(f'********* Agenda {agenda} *********')
        tituloTarefa = input('Digite o nome da tarefa a ser excluda: ')
        agenda.removerTarefa(tituloTarefa)
        atualizarCSV
    
    
    elif opcao == '10':
        print(f'********* Agenda {agenda} *********')
        agenda.limpar()
        atualizarCSV

        print(f'''
        
******** Agenda {agenda} foi esvaziada com sucesso ********        
                
        ''')

    elif opcao == '11':
        print(f'********* Agenda {agenda} *********')
        del agenda
        atualizarCSV

        print('''
        
******** Agenda foi apagada com sucesso ********        
                
        ''')

    else:        
        break