import os

class atualizarCSV:
    __cabecalho = 'titulo;prazo;categoria;concluida\n'

    def __init__(self) -> None:
        
        pass


    @staticmethod
    def criarArquivo(nome):
        
        arquivo = open(nome+'.csv', mode='a')

        if os.stat(arquivo.name).st_size == 0:            
            arquivo.write(atualizarCSV.__cabecalho)
            
        else:
            raise FileExistsError('Já existe arquivo com esse nome')

    @staticmethod
    def carregarLinhasArquivo(nome):
        linhas = []       

        with open(nome+'.csv', 'r') as arq:
            arq.readline() #pulando linha do cabecalho
            for texto in arq:
                linhas.append(texto.replace('\n',''))

        return linhas

    @staticmethod
    def atualizarLinhasArquivo(titulo, tarefas):
        arquivo = open(titulo+'.csv','w')

        arquivo.write(atualizarCSV.__cabecalho)
        for linha in tarefas.keys():
            txt = linha + ';' + tarefas[linha]['prazo'] + ';' + tarefas[linha]['categoria'] + ';' + tarefas[linha]['status'] + '\n'
            arquivo.write(txt)
    
    @staticmethod
    def apagarLinhasArquivo(titulo):
        arquivo = open(titulo+'.csv','w')
        arquivo.write(atualizarCSV.__cabecalho)        

    @staticmethod
    def inserirLinha(nome, texto):
        arquivo = open(nome+'.csv', mode='a' )
        arquivo.write(texto+'\n')

    @staticmethod
    def apagarArquivo(nome):
        os.remove(nome+'.csv')        


