import os

NUMLUGARES = 7
LIVRE = 0
OCUPADO = 1
queroSair = False
lugar_tuplo =  tuple(range(NUMLUGARES))
parqueCheio = False
lugares = []
lugares_ocupados = 0

for numLugar in range(0,NUMLUGARES,1):
    lugar = (LIVRE, "") 
    lugares.append(lugar_tuplo)


while not queroSair:
    os.system('cls' if os.name == 'nt' else 'clear')
    print()
    print("***********************************")
    print("*                                 *")
    print("*        Parque Pinheiro          *")
    print("*                                 *")
    print("*      1. Listar lugares.         *")
    print("*      2. Marcar lugar.           *")
    print("*      3. Libertar lugar.         *")
    print("*      4. Sair do programa.       *")
    print("*                                 *")
    print("***********************************")
    print()

    if parqueCheio:
        print("***********************************")
        print("*                                 *")
        print("*         Parque Completo!        *")
        print("*                                 *")
        print("***********************************")
        print()

    resposta = input(" -> Escolha uma opção (1-5): ")
    if resposta:
        escolha = resposta[0]
    else:
        escolha = '0'

#   Opcao 1  listagem dos lugares
    if escolha == '1':
        print("Listagem de Lugares:")
        for numLugar in range(0,NUMLUGARES,1):
            print(" ->Lugar", (numLugar+1), ":", end="")
            if lugares[numLugar][0] == LIVRE:
                print(" Livre.")
            else:
                print(" Ocupado por ", lugares[numLugar][1], ".")
        input("Prima qq tecla para continuar ...")
        print()

#opção 2  - marcar um lugar
    elif escolha == '2':
        if not parqueCheio:
            print("Qual é o lugar a ocupar (1-", NUMLUGARES,")? ", end="")
            numLugar = input()
            if numLugar.isdigit():
                numLugar = int(numLugar)
                if 1 <= numLugar <= NUMLUGARES:
                    if lugares[numLugar-1][0] == OCUPADO:
                        print("Lugar já está ocupado!")
                    else:
                        lugares_lista = list(lugares[numLugar-1])
                        lugares_lista[0] = OCUPADO
                        print("Insira a sua matrícula:", end="")
                        lugares_lista[1] = input()
                        lugar_tuplo = tuple(lugares_lista)
                        lugares[numLugar-1] = lugar_tuplo
                        print("Lugar ocupado com sucesso!")
                        lugares_ocupados += 1
                        if lugares_ocupados == 7:
                            parqueCheio  = True

            else:
                print("Lugar inválido! Lugares vão de 1 a", NUMLUGARES)
        input("Prima qq tecla para continuar ...")
        print()

#opção 3  - Liberar um lugar
    elif escolha == '3':
        print("Qual é o lugar a libertar (1-", NUMLUGARES,")? ", end="")
        numLugar = input()
        if  numLugar.isdigit():
            numLugar = int(numLugar)
            if numLugar >= 1 and numLugar <= NUMLUGARES:
                if  lugares[numLugar-1][0] == OCUPADO:
                    lugares_lista = list(lugares [numLugar-1])
                    lugares_lista [0] = LIVRE
                    lugares_lista[1] = ""
                    lugar_tuplo= tuple (lugares_lista)
                    lugares[numLugar -1]= lugar_tuplo
                    print("Lugar libertado com sucesso!")
                    parqueCheio = False
                else:
                    print("Lugar já está livre!")
            else:
                print("Lugar inválido! Lugares vão de 1 a", NUMLUGARES)
        else:
            print("Lugar inválido! Lugares vão de 1 a", NUMLUGARES)
        input("Prima qq tecla para continuar ...")
        print()
        
#opção 4 sair
    elif escolha == '4':
        resposta = input("Tem a certeza (S/N)? ")
        if resposta and (resposta[0] == 's' or resposta[0] == 'S'):
            queroSair = True
            print("Obrigado por ter usado o nosso programa!")
        elif resposta and (resposta[0] == 'n' or resposta[0] == 'N'):
            print()
            continue
        else:
            print("Opção Inválida.")
            print()
        input("Prima qq tecla para continuar ...")
        print()
        
#opção else
    else:
        print("Opção inválida!")
        input("Prima qq tecla para continuar ...")
        print()





