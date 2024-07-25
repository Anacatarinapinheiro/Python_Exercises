import numpy as np
import array

produto_numero = 0
produtos = []
produto = 0
cProduto = 0
escolha = 0
resposta = 0
venda = []
preco = 0
queroSair = False

while (not queroSair):

    print("")
    print("***********************************")
    print("*                                 *")
    print("*         Café Pinheiro           *")
    print("*                                 *")
    print("*      1. Listar produtos         *")
    print("*      2. Inserir produto         *")
    print("*      3. Apagar produtos         *")
    print("*      4. Inserir preços          *")
    print("*      5. Sair do programa        *")
    print("***********************************")
    print()

# aqui vou perguntar qual é opção
    resposta = input(" -> Escolha uma opção (1-5): ")
    print()
    if len(resposta) > 0:
        escolha = resposta[0]
    else:
        escolha = 0

# aqui mostra os produtos
    if escolha == '1':
        if not produtos:
            print("Sem Produtos!")
        else:
            print("Produtos inseridos:")
            produto_numero = 1
            for produto in produtos:
                print("-> Produto", produto_numero, ": Nome ->", produto[0], "| Preço ->", produto[1])
                produto_numero += 1

# aqui insere os produtos
    elif escolha == '2':
        while True:
            print("Quantos produtos deseja inserir? ", end="")
            produto_numero = input()
            print()
            if not produto_numero.isdigit() or int(produto_numero) <= 0:
                print("Por favor, insira um número inteiro positivo.")
                print()
            elif cProduto >= 9:
                print("Já inseriu o número máximo de produtos.")
                break
            elif int(produto_numero) > 9:
                print("O máximo de produtos é 9!")
            else:
                cProduto += int(produto_numero)
                if cProduto > 9:
                    print("O máximo de produtos é 9!")
                    cProduto = cProduto-int(produto_numero)
                else:
                    produto_numero = int(produto_numero)
                    for armazem in range(1, produto_numero + 1):
                        nome = input("Insira o nome do produto: ")
                        preco = float(0.0)
                        produtos.append([nome, preco])
                        print()

                break

# aqui apaga produtos
    elif escolha == '3':
        if not produtos:
            print("Não existem produtos no armazém!")
        else:
            print("Qual o produto que deseja apagar (1 a,", cProduto, "? ", end="")
            resposta = int(input()) - 1
            if 0 <= resposta < len(produtos):
                certeza = input("Tem a certeza que deseja apagar as produtos (S/N)? ")
                if (certeza[0] == 's' or certeza[0] == 'S'):
                    del produtos[resposta]
                    print("O seu produto foi apagado com sucesso!")
                    cProduto -= 1
            else:
                 print("Não foi encontrado esse produto.")
# aqui insere preço
    elif escolha == '4':
        print()
        if not produtos:
            print("Não existem produtos no armazém!")
        else:
            print("Qual é o número do produto que adicionar/alterar?: ", end="")
            resposta = int(input()) - 1
            if 0 <= resposta < len(produtos):
                while True:
                    novo_preco = input("Insira o preço do produto: ")
                    if not (novo_preco.replace('.', '',
                                                1).isdigit() or novo_preco.isdigit()):
                        print("Por favor, insira valores numéricos para preço.")
                        break
                    novo_preco = float(novo_preco)
                    produtos[resposta][1] = novo_preco
                    print("Preço atualizado com sucesso!")
                    break
            else:
                print("Produto não encontrado.")


# aqui sai do programa
    elif escolha == '5':
        resposta = input("Tem a certeza (S/N)? ")
        if (resposta[0] == 's' or resposta[0] == 'S'):
            queroSair = True

# caso não escolha uma opção de 1 a 6
    else:
        print("Opção inválida!")
        input("Prima qq tecla para continuar ...")

# 2.5 Despedida
print("Obrigado por ter usado o nosso programa!")
print()