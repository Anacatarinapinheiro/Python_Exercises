
import numpy as np
import array

produto_numero = 0
produtos = []
produto = 0
escolha = 0
resposta = 0
venda = []
preco = 0
queroSair = False


while (not queroSair):
    
    print("")
    print("***********************************")
    print("*                                 *")
    print("*       Armazém Pinheiro          *")
    print("*                                 *")
    print("*      1. Listar produtos         *")
    print("*      2. Inserir produto         *")
    print("*      3. Alterar preço           *")
    print("*      4. Registar Venda          *")
    print("*      5. Registar Reposição      *")
    print("*      6. Apagar produtos         *")
    print("*      7. Sair do programa.       *")
    print("*                                 *")
    print("***********************************")
    print()
    
#aqui vou perguntar qual é opção
    resposta = input(" -> Escolha uma opção (1-7): ")
    print()
    if len (resposta) > 0:  
        escolha = resposta[0]
    else:
        escolha = 0
    
#aqui mostra os produtos
    if escolha == '1':
        if not produtos:
            print("Sem Produtos!")
        else:
            print("Produtos inseridos:")
            produto_numero = 1
            for produto in produtos:
                print("-> Produto", produto_numero,": Nome ->", produto[0], "| Preço ->", produto[1], "| Quantidade ->", produto[2])
                produto_numero += 1

#aqui insere os produtos
    elif escolha == '2':
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
                        if not (preco_input.replace('.', '', 1).isdigit() or preco_input.isdigit()) or not quantidade_input.isdigit():
                            print("Por favor, insira valores numéricos para preço e quantidade.")
                            print()
                            continue
                        preco = float(preco_input)
                        quantidade = int(quantidade_input)
                        break
                    produtos.append([nome, preco, quantidade])
                    print()
                break

#aqui altera o preço
    elif (escolha == '3'):
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

#aqui regista vendas
    elif (escolha == '4'):
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

#aqui adiciona stock
    elif escolha == '5':
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

#aqui apaga produtos
    elif (escolha == '6'):
        if not produtos:
            print("Não existem produtos no armazém!")
        else:
            print("Qual o produto que deseja apagar? ", end="")
            resposta = int(input()) - 1        
            certeza = input("Tem a certeza que deseja apagar as produtos (S/N)? ")
            if (certeza[0] == 's' or certeza[0] == 'S'):
                del produtos[resposta]
                print("O seu produto foi apagado com sucesso!")

#aqui sai do programa
    elif (escolha == '7'):
        resposta = input("Tem a certeza (S/N)? ")
        if (resposta[0] == 's' or resposta[0] == 'S'):
            queroSair = True

#caso não escolha uma opção de 1 a 7     
    else:
        print("Opção inválida!")
        input("Prima qq tecla para continuar ...")

# 2.5 Despedida
print("Obrigado por ter usado o nosso programa!")
print()