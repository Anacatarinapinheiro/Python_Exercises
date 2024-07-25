import os

LIVRE = 0
RESERVADO = 1
OCUPADO = 2
NUMANDARES = 3
NUMQUARTOSPORANDAR = 5
queroSair = False

quartos = {}
for andar in range(1, NUMANDARES + 1):
    quartos[andar] = {quarto: {'estado': LIVRE, 'hospede': None} for quarto in range(1, NUMQUARTOSPORANDAR + 1)}

while not queroSair:
    os.system('cls' if os.name == 'nt' else 'clear')
    print()
    print("***********************************")
    print("*                                 *")
    print("*       Pensão Pinheiro           *")
    print("*                                 *")
    print("*      1. Listar quartos.         *")
    print("*      2. Reservar quarto.        *")
    print("*      3. Ocupar quarto.          *")
    print("*      4. Libertar quarto.        *")
    print("*      5. Sair do programa.       *")
    print("*                                 *")
    print("***********************************")
    print()

    resposta = input(" -> Escolha uma opção (1-5): ")
    if resposta:
        escolha = resposta[0]
    else:
        escolha = '0'
        
#opção 1  Listagem de quartos
    if escolha == '1':  
        print("Listagem de quartos:")
        for andar, quartos_andar in quartos.items():
            print("Andar", andar, ":")
            for num_quarto, info_quarto in quartos_andar.items():
                estado = info_quarto['estado']
                if estado == LIVRE:
                    print(" -> Quarto", {num_quarto},": Livre")
                elif estado == RESERVADO:
                    print(" -> Quarto", {num_quarto},": Reservado para", {info_quarto['hospede']})
                else:
                    print(" -> Quarto", {num_quarto},": Ocupado por", {info_quarto['hospede']})
        input("Prima qq tecla para continuar ...")
        print()
            
# opção 2 Reservar Quarto
    elif escolha == '2':  
        print("Qual é o andar a selecionar (1 -", NUMANDARES, ")? ", end="")
        numAndar = input()
        if numAndar.isdigit():
            numAndar = int(numAndar)
            print("Nesse andar, qual é o quarto a reservar 1 -", {NUMQUARTOSPORANDAR},"?", end="")
            numQuarto = input()
            if numQuarto.isdigit():
                numQuarto= int(numQuarto)
                if 1 <= numAndar <= NUMANDARES and 1 <= numQuarto <= NUMQUARTOSPORANDAR:
                    if quartos[numAndar][numQuarto]['estado'] == LIVRE:
                        nome_hospede = input("Digite o nome do hóspede: ")
                        quartos[numAndar][numQuarto] = {'estado': RESERVADO, 'hospede': nome_hospede}
                        print("Quarto reservado com sucesso!")
                    else:
                        print("Quarto não pode ser reservado!")
                else:
                    print("Número de andar ou de quarto inválido!")
            else:
                print("Número de andar ou de quarto inválido!")
        else:
            print("Número de andar ou de quarto inválido!")
        input("Prima qq tecla para continuar ...")
        print()
        
#opção 3 Ocupar quarto
    elif escolha == '3':  
        print("Qual é o andar a selecionar (1 -", NUMANDARES, ")? ", end="")
        numAndar = input()
        if numAndar.isdigit():
            numAndar = int(numAndar)
            print("Nesse andar, qual é o quarto a ocupar 1 -", {NUMQUARTOSPORANDAR} ,"? ", end="")
            numQuarto = input()
            if numQuarto.isdigit():
                numQuarto = int(numQuarto)
                if 1 <= numAndar <= NUMANDARES and 1 <= numQuarto <= NUMQUARTOSPORANDAR:
                    if quartos[numAndar][numQuarto]['estado'] != OCUPADO:
                        nome_hospede = input("Digite o nome do hóspede: ")
                        quartos[numAndar][numQuarto] = {'estado': OCUPADO, 'hospede': nome_hospede}
                        print("Quarto ocupado com sucesso!")
                    else:
                        print("Quarto não pode ser ocupado!")
                else:
                    print("Opção Inválida!")
            else:
                print("Número de andar ou de quarto inválido!")
        else:
            print("Número de andar ou de quarto inválido!")
        input("Prima qq tecla para continuar ...")   
        print()     

#opção 4 - Check out
    elif escolha == '4':  
        print("Qual é o andar a selecionar (1 -", NUMANDARES, ")? ", end="")
        numAndar = input()
        if numAndar.isdigit():
            numAndar = int(numAndar)
            print("Nesse andar, qual é o quarto a libertar 1 -", {NUMQUARTOSPORANDAR} , "? ", end="")
            numQuarto = input()
            if numQuarto.isdigit():
                numQuarto = int(numQuarto)
                if 1 <= numAndar <= NUMANDARES and 1 <= numQuarto <= NUMQUARTOSPORANDAR:
                    if quartos[numAndar][numQuarto]['estado'] != LIVRE:
                        quartos[numAndar][numQuarto] = {'estado': LIVRE, 'hospede': None}
                        print("Quarto liberado com sucesso!")
                    else:
                        print("Quarto já está livre!")
                else:
                    print("Número de andar ou de quarto inválido!")
            else:
                print("Número de andar ou de quarto inválido!")
        else:
            print("Número de andar ou de quarto inválido!")
        input("Prima qq tecla para continuar ...")
        print()

#opção 5 - Saida
    elif escolha == '5':
        resposta = input("Tem a certeza (S/N)? ")
        if resposta and (resposta[0] == 's' or resposta[0] == 'S'):
            queroSair = True
        elif resposta and (resposta[0] == 'n' or resposta[0] == 'N'):
            print()
            continue
#opção else
    else:
        print("Opção inválida!")
        input("Prima qq tecla para continuar ...")
        print()

# Despedida
print("Obrigado por ter usado o nosso programa!")
print()
