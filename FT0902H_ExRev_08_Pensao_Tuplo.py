import os

LIVRE = 0
RESERVADO = 1
OCUPADO = 2
NUMANDARES = 3
NUMQUARTOSPORANDAR = 5
queroSair = False
escolha = '\0'
quartos = []
quarto_tuplo = tuple(range(NUMQUARTOSPORANDAR))

for numAndar in range(1, NUMANDARES+1, 1):
    quartos_andar = []
    for numQuarto in range (1, NUMQUARTOSPORANDAR+1, 1):
        quartos_andar.append (quarto_tuplo)
    quartos.append(quartos_andar)


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
        for numAndar in range (0, NUMANDARES):
            print("Andar", numAndar + 1, ":")
            for numQuarto in range(0, NUMQUARTOSPORANDAR):
                if numAndar < len(quartos) and numQuarto < len(quartos[numAndar]):
                    print("Quarto ", numQuarto + 1, ":", end="")
                    if quartos[numAndar][numQuarto][0]  == LIVRE:
                        print("Livre")
                    elif quartos[numAndar][numQuarto][0] == RESERVADO:
                        print("Reservado para", quartos[numAndar][numQuarto][1])
                    else:
                        print("Ocupado por", quartos[numAndar][numQuarto][1])
                else:
                    print("Índice inválido - andar ou quarto fora do intervalo válido.")
        input("Prima qq tecla para continuar ...")
        print()
            
# opção 2 Reservar Quarto
    elif escolha == '2':  
        print("Qual é o andar a selecionar (1 -", NUMANDARES, ")? ", end="")
        numAndar = input()
        if numAndar.isdigit():
            numAndar = int(numAndar)
            print("Nesse andar, qual é o quarto a reservar 1 -", NUMQUARTOSPORANDAR,"?", end="")
            numQuarto = input()
            if numQuarto.isdigit():
                numQuarto = int(numQuarto)
                if 1 <= numAndar <= NUMANDARES and 1 <= numQuarto <= NUMQUARTOSPORANDAR:
                    if quartos[numAndar-1][numQuarto-1][0] == LIVRE:
                        quarto_lista = list(quartos[numAndar-1][numQuarto-1])
                        quarto_lista[0]= RESERVADO
                        print("Em que nome fica a reserva?:", end="")
                        quarto_lista[1] = input()
                        quarto_tuplo = tuple(quarto_lista)
                        quartos[numAndar-1][numQuarto - 1] = quarto_tuplo 
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
            print("Nesse andar, qual é o quarto a ocupar 1 -", NUMQUARTOSPORANDAR,"?", end="")
            numQuarto = input()
            if numQuarto.isdigit():
                numQuarto = int(numQuarto)
                if 1 <= numAndar <= NUMANDARES and 1 <= numQuarto <= NUMQUARTOSPORANDAR:
                    if quartos[numAndar-1][numQuarto-1][0] != OCUPADO:
                        quarto_lista = list(quartos[numAndar-1][numQuarto-1])
                        quarto_lista[0]= OCUPADO
                        print("Em que nome fica o quarto?:", end="")
                        quarto_lista[1] = input()
                        quarto_tuplo = tuple(quarto_lista)
                        quartos[numAndar-1][numQuarto - 1] = quarto_tuplo  
                        print("Quarto ocupado com sucesso!")
                    else:
                        print("Quarto não pode ser ocupado!")
                else:
                    print("Número de andar ou de quarto inválido!")
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
            print("Nesse andar, qual é o quarto a libertar 1 -", NUMQUARTOSPORANDAR , "? ", end="")
            numQuarto = input()
            if numQuarto.isdigit():
                numQuarto = int(numQuarto)
                if 1 <= numAndar <= NUMANDARES and 1 <= numQuarto <= NUMQUARTOSPORANDAR:
                    estado_quarto = quartos[numAndar - 1][numQuarto - 1][0]
                    if estado_quarto == RESERVADO or estado_quarto == OCUPADO:
                        quarto_lista = list(quartos[numAndar - 1][numQuarto - 1])
                        quarto_lista[0] = LIVRE
                        quartos[numAndar - 1][numQuarto - 1] = tuple(quarto_lista) 
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
