resposta = input("Digite 1- Abrir\nDigite 2- Escrever\n")

def arquivoTxt(diretorio):
    diretorio = diretorio + ".txt"
    return diretorio

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

def verificar(R):
    if R == "1":
        ler()

    elif R == "2":
        escrever()

    else:
        print("Digite um valor valido")

resposta = verificar(resposta)