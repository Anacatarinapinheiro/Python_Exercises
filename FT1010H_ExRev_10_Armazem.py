
import numpy as np
import array

#FUNÇÕES

def defineTitulo(titulo):
    titulo = "*       Armazem Pinheiro          *"
    return titulo

def inicializaMenu(menu):
    menu = [
        "*      1. Listar produtos         *",
        "*      2. Inserir produto         *",
        "*      3. Alterar preço           *",
        "*      4. Registar Venda          *",
        "*      5. Registar Reposição      *",
        "*      6. Apagar produtos         *",
        "*      7. Sair do programa.       *"
    ]
    return menu

# 1.03  Função do ciclo principal
def cicloPrincipal(produtos, titulo, menu):
    queroSair = False
    escolha = '\0'
    while (not queroSair):
        mostraMenu(titulo, menu)
        escolha = obtemEscolha(escolha, len(menu))
        queroSair = processaEscolha(escolha, produtos, queroSair)
    return

#     Função "mostraMenu()"
def mostraMenu(titulo, menu):
    print("")
    print("***********************************")
    print("*                                 *")
    print(titulo)
    print("*                                 *")
    for cOpcao in range(0,len(menu),1):
        print(menu[cOpcao])
    print("*                                 *")
    print("***********************************")
    print()
    return

#     Função "obtemEscolha()"
def obtemEscolha(escolha, numOpcoes):
    print(" -> Escolha uma opção (1-",end="")
    print(numOpcoes,end="")
    print("): ",end="")
    resposta = input()
    if (len(resposta) > 0):   
       escolha = resposta[0]
    else:
       escolha = 0
    return escolha


#     Função "processaEscolha()"
def processaEscolha(
        escolha, produtos, queroSair):

    match (escolha):
        case '1':
            listarProdutos(produtos)
        case '2':
            inserirProduto(produtos, preco, quantidade, nome)
        case '3':
            alterarPreco(produtos)
        case '4':
            registarVenda(produtos)
        case '5':
            registarReposicao(produtos)
        case '6':
            apagarProdutos(produtos)
        case '7':
            queroSair = sairDoProgram(queroSair)
        case _:
            opcaoInvalida()
    return queroSair

#escolha 1 - Listar produtos
def listarProdutos(produtos):
    if not produtos:
        print("Sem Produtos!")
    else:
        print("Produtos inseridos:")
        produto_numero = 1
        for produto in produtos:
            print("-> Produto", produto_numero,": Nome ->", produto[0], "| Preço ->", produto[1], "| Quantidade ->", produto[2])
            produto_numero += 1
    return

#escolha 2 - Inserir Produto
def inserirProduto(produtos, nome, preco, quantidade):
    while True:
        print("Quantos produtos deseja inserir? ", end="")
        produto_numero = input()
        print()
        if not produto_numero.isdigit() or int(produto_numero) <= 0:
            print("Por favor, insira um número inteiro positivo.")
            print()
        else:
            produto_numero = int(produto_numero)
            for armazem in range(1, produto_numero + 1):
                nome = input("Insira o nome do produto: ")
                while True:
                    preco_input = input("Insira o preço do produto: ")
                    quantidade_input = input("Insira a quantidade de produtos: ")
                    if not (preco_input.replace('.', '',
                                                1).isdigit() or preco_input.isdigit()) or not quantidade_input.isdigit():
                        print("Por favor, insira valores numéricos para preço e quantidade.")
                        print()
                        continue
                    preco = float(preco_input)
                    quantidade = int(quantidade_input)
                    break
                produtos.append([nome, preco, quantidade])
                print()
            break
    return

#escolha 3 - Alterar Preco
def alterarPreco (produtos):
    print()
    if not produtos:
        print("Não existem produtos no armazém!")
    else:
        print("Qual é o número do produto que deseja alterar o preço?: ", end="")
        resposta = int(input()) - 1
        if 0 <= resposta < len(produtos):
            novo_preco = float(input("Digite o novo preço: "))
            produtos[resposta][1] = novo_preco
            print("Preço atualizado com sucesso!")
        else:
            print("Produto não encontrado.")
    return

#escolha 4 - Registar Venda

def registarVenda (produtos):
    if not produtos:
        print("Não existem produtos no armazém!")
    else:
        print("Quer registar a venda de que produto? ", end="")
        resposta = int(input()) - 1
        if 0 <= resposta < len(produtos):
            venda = int(input("Qual a quantidade de produtos que vendeu? "))
            produtos[resposta][2] -= venda
            print("Venda registada com sucesso!")
            if produtos[resposta][2] <= 0:
                produtos[resposta][2] = "Sem Stock!"
        else:
            print("Produto não encontrado.")
    return

#escolha 5 - registar reposicao
def registarReposicao(produtos):
    if not produtos:
        print("Não existem produtos no armazém!")
    else:
        print("Quer registar a reposição de que produto? ", end="")
        resposta = int(input()) - 1
        if 0 <= resposta < len(produtos):
            nova_reposicao = int(input("Qual a quantidade que vai repor? "))
            if produtos[resposta][2] == "Sem Stock!":
                produtos[resposta][2] = nova_reposicao
            else:
                produtos[resposta][2] += nova_reposicao
                print("Reposição registada com sucesso!")
        else:
            print("Produto não encontrado.")
    return

#escolha 6 - apagar produtos
def apagarProdutos(produtos):
    if not produtos:
        print("Não existem produtos no armazém!")
    else:
        print("Qual o produto que deseja apagar? ", end="")
        resposta = int(input()) - 1
        certeza = input("Tem a certeza que deseja apagar as produtos (S/N)? ")
        if (certeza[0] == 's' or certeza[0] == 'S'):
            del produtos[resposta]
            print("O seu produto foi apagado com sucesso!")
        else:
            return
    return resposta

#escolha 7 - sair do programa
def sairDoProgram(queroSair):
    resposta = input("Tem a certeza (S/N)? ")
    if (len(resposta) > 0):
        if (resposta[0] == 's' or resposta[0] == 'S'):
            queroSair = True
        elif (resposta[0] == 'n' or resposta[0] == 'N'):
            return
        else:
            print("Opção Inválida.")
            return
    return queroSair


# escolha "else"
def opcaoInvalida():
    print("Opção inválida!")
    input("Prima qq tecla para continuar ...")
    return


#despedida para sair
def despedida():
    print("Obrigado por ter usado o nosso programa!")
    input("Prima qq tecla para continuar ...")
    print()
    return

#FIM DE FUNÇOES


produto_numero = 0
produtos = []
NUMOPCOES = 7
produto = 0
escolha = 0
nome = '\0'
quantidade = 0
resposta = 0
venda = []
preco = 0
titulo =""
menu = ["" for cOpcao in range(0,NUMOPCOES,1)]
queroSair = False

titulo = defineTitulo(titulo)
menu = inicializaMenu(menu)
cicloPrincipal(produtos,titulo,menu)
despedida()



