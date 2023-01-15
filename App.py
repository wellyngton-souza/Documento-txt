import pandas as pd

def arquivoTxt(diretorio):
    diretorio = diretorio + ".txt"
    return diretorio

def arquivoCsv(diretoriocsv):
    diretoriocsv = diretoriocsv + ".csv"
    return diretoriocsv

def ler():
    dir = input("Digite o diretorio do arquivo:\n")
    diretorio = arquivoTxt(dir)
    try:
        arquivo = open(diretorio, "r") #Abre o arquivo para leitura
        print(arquivo.read())
        arquivo.close()
    except:
        print("Arquivo não encontrado")

def escrever():
    dir = input("Digite o diretorio do arquivo:\n")
    diretorio = arquivoTxt(dir)
    arquivo = open(diretorio, "a") #Abre o arquivo para escrita e acrecenta um texto com o antigo
    texto = input("Digite o texto a ser acrescentado ao arquivo\n")
    arquivo.write(texto)
    arquivo.close()
    print("Texto Digitado com sucesso")

def verificar():
    resposta = input("Digite 1- Abrir\nDigite 2- Escrever\n")

    match resposta:
        case "1":
            ler()
        
        case "2":
            escrever()

        case _:
            print("Digite um valor valido")

def csv():
    respostacsv = input("Deseja Ler ou Editar um arquivo csv:\n")
    respostacsv = respostacsv.lower()
    match respostacsv:
        case "ler":
            try:
                arquivoCSV = input("Digite o nome do arquivo csv\n")
                arquivoCSV = arquivoCSV + ".csv"
                df = pd.read_csv(arquivoCSV)
                df.head()
            except:
                print("Digite um valor valido")
                csv()
        
        case "editar":
            try:
                dir = input("Digite o diretorio do arquivo: (Caso o arquivo não exista, sera criado um do zero)\n")
                diretorio = arquivoCsv(dir)
                arquivo = open(diretorio, "a") #Abre o arquivo para escrita e acrecenta um texto com o antigo
                texto = input("Digite o texto a ser acrescentado ao arquivo\n")
                arquivo.write("\n" + texto)
                arquivo.close()
                print("Texto Digitado com sucesso")
            except:
                print("Não foi possivel editar o arquivo")

def txtoucsv(R):
    match R:
        case "txt":
            verificar()
        
        case "csv":
            csv()
        
        case _:
            print("Digite um valor valido")

modeloarquivo = txtoucsv(input("Trabalhar com arquivo txt ou csv?\n"))