import os

class atualizarCSV:

    def __init__(self) -> None:
        pass


    @staticmethod
    def criarArquivo(nome):
        
        arquivo = open(nome+'.csv', mode='a')

        if os.stat(arquivo.name).st_size == 0:            
            arquivo.write('titulo;prazo;categoria;concluida\n')
            
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
    def apagarLinha(titulo):
        pass

    @staticmethod
    def inserirLinha(nome, texto):
        arquivo = open(nome+'.csv', mode='a' )
        arquivo.write(texto+'\n')


