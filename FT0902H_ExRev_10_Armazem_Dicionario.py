import os
queroSair = False
produtos = {}
contador_produtos = 0

while not queroSair:
    os.system('cls' if os.name == 'nt' else 'clear')
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

    resposta = input(" -> Escolha uma opção (1-7): ")
    print()
    escolha = resposta[0] if resposta else '0'
    
#Opção 1 listar
    if escolha == '1':
        if not produtos:
            print("Sem Produtos!")
        else:
            print("Produtos inseridos:")
            for identificador, produto in produtos.items():
                print("Produto ID:", {identificador}," Nome:", {produto['Nome']}," Preço:", {produto['Preço']}," Quantidade:", {produto['Quantidade']})
        input("Prima qq tecla para continuar ...")       
        print()
 
#opção 2 inserir nome produto       
    elif escolha == '2':
        contador_produtos += 1
        nome = input("Insira o nome do produto: ")
        preco = float(input("Insira o preço do produto: "))
        quantidade = int(input("Insira a quantidade de produtos: "))
        produtos[contador_produtos] = {'Nome': nome, 'Preço': preco, 'Quantidade': quantidade}
        print("Produto inserido com sucesso!")

#Opção 3 alterar preço
    elif escolha == '3':
        id_produto = int(input("Qual é o ID do produto que deseja alterar o preço?: "))
        if id_produto in produtos:
            novo_preco = float(input("Digite o novo preço: "))
            produtos[id_produto]['Preço'] = novo_preco
            print("Preço atualizado com sucesso!")
        else:
            print("Produto não encontrado.")
        input("Prima qq tecla para continuar ...")
        print()

#opção 4 registar venda 
    elif escolha == '4':
        id_produto = int(input("Quer registar a venda de qual produto? Insira o ID: "))
        if id_produto in produtos:
            venda = int(input("Qual a quantidade de produtos que vendeu? "))
            produtos[id_produto]['Quantidade'] -= venda
            print("Venda registada com sucesso!")
            if produtos[id_produto]['Quantidade'] <= 0:
                produtos[id_produto]['Quantidade'] = "Sem Stock!"
        else:
            print("Produto não encontrado.")
        input("Prima qq tecla para continuar ...")
        print()

#opção 5 reposição
    elif escolha == '5':
        id_produto = int(input("Quer registar a reposição de qual produto? Insira o ID: "))
        if id_produto in produtos:
            nova_reposicao = int(input("Qual a quantidade que vai repor? "))
            if produtos[id_produto]['Quantidade'] == "Sem Stock!":
                produtos[id_produto]['Quantidade'] = nova_reposicao
            else:
                produtos[id_produto]['Quantidade'] += nova_reposicao
            print("Reposição registada com sucesso!")
        else:
            print("Produto não encontrado.")
        input("Prima qq tecla para continuar ...")
        print()

#opção 6 apagar
    elif escolha == '6':
        id_produto = int(input("Qual o ID do produto que deseja apagar? "))
        if id_produto in produtos:
            del produtos[id_produto]
            print("O produto foi apagado com sucesso!")
        else:
            print("Produto não encontrado.")
        input("Prima qq tecla para continuar ...")
        print()

#opção 7 sair
    elif escolha == '7':
        resposta = input("Tem a certeza (S/N)? ")
        if resposta and (resposta[0] == 's' or resposta[0] == 'S'):
            queroSair = True
        elif resposta and (resposta[0] == 'n' or resposta[0] == 'N'):
            print()
            continue
        else:
            print("Opção Inválida.")
        input("Prima qq tecla para continuar ...")
        print()
            
#opção else
    else:
        print("Opção inválida!")
        input("Prima qq tecla para continuar ...")
        print()

print("Obrigado por ter usado o nosso programa!")
print()
