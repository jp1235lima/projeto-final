cadastro = []

def  leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31#Erro: por favor digite um número válido. \033[n')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[n')
            return 0
        else:
            return n

def linha(tam=42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[32mSua Opção: \033[m')
    return opc

def add_cadastro():
    name = input('\033[31mColoque seu nome: \033[m')
    email = input('\033[31mColoque seu email: \033[m')
    telephone = input('\033[31mColoque seu número de telefone: \033[m')
    cadastro.append([name, email, telephone])

def pesquisa(name):
    n = name.lower()
    for i, t in enumerate(cadastro):
        if t[0].lower() == n:
            return i
    return None

def apaga():
    name = input('\033[31mQual conta gostaria de excluir? \033[m')
    i = pesquisa(name)
    if i is not None:
        del cadastro[i]
    else:
        print('\033[31mNome não encontrado.\033[m')

def altere():
    i = pesquisa(input('\033[31mInsira o nome que deseja alterar: \033[m'))
    if i is not None:
        nome = cadastro[i][0]
        email = cadastro[i][1]
        telefone = cadastro[i][2]
        print('\033[32mEncontrado:\033[m')
        print(nome,email, telefone)
        nome = input('\033[31mColoque seu nome: \033[m')
        email = input('\033[31mColoque seu número de telefone: \033[m')
        telefone = input('\033[31mColoque seu email: \033[m')
        cadastro[i] = [nome, email, telefone]
    else:
        print('\033[31Nome não encontrado.\033[m')


def ordena():
    cadastro.sort()


while True:
    resposta = menu(['Cadastrar nova Pessoa', 'Vizualizar os cadastros', 'Excluir cadastro','Alterar Cadastro','Ordenar cadastros', 'Sair do sitema'])
    if resposta == 1:
        add_cadastro()
    elif resposta == 2:
        print(cadastro)
    elif resposta == 3:
        apaga()
    elif resposta == 4:
        altere()
    elif resposta == 5:
        ordena()
    elif resposta == 6:
        break
    else:
        print('\033[31mErro! Digite uma opção válida!\033[m')