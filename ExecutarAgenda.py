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
# apaga todas as tarefas da agenda e mantém a agend
# apaga agenda inclusive seu arquivo
# fechar



opcao = ''

while opcao != '0':   
    
    
    opcao = input('''
Digite:
- 1 para criar agenda
- 2 para inserir tarefa
- 3 para excluir 
- 4 imprimir a lista inteira

ou qualquer outra coisa para finalizar: ''')
    
    if opcao == '1':
        
        nomeAgenda = input('Digite o nome da agenda: ')
        agenda = Agenda(nomeAgenda)

    elif opcao == '2':
        entrada = {}
        
        tituloTarefa   = input('Digite o nome da tarefa: ')
        dataRealizacao = input('Digite a data limite: ')
        categoria      = input('Digite a categoria: ')       
        concluida      = 0
                
        tarefa = Tarefas(tituloTarefa, dataRealizacao, categoria)
        agenda.adicionarTarefa(tarefa)
        
               
        print('''
        
******** Tarefa '''+ tituloTarefa + ''' cadastrado com sucesso ********        
                
        ''')
        
        
    elif opcao == 'implementar':
        codBusca = int(input('Digite o código para consulta: '))
        
        resConsulta = agenda.get(codBusca, False)
        
        if resConsulta:
            print(f'''
+++++++++ Fornecedor encontrado: {resConsulta}''')
        else:
            print('''
-------- Código não encontrado --------
            ''')
        
    elif opcao == 'implementar':
        codBusca = int(input('Digite o código para excluir: '))
        
        resExcluir = agenda.pop(codBusca, False)
        
        if resExcluir:
            print(f'''
+++++++++ Fornecedor excluído: {resExcluir}''')
        else:
            print('''
-------- Código não encontrado --------
            ''')
    
    elif opcao == '4':  
        try:
            print(agenda.tarefasAgendadas)
        except:
            
            print('Nenhuma agenda aberta')
            
        
    else:        
        break