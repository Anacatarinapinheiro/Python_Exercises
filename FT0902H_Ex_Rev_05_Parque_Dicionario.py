import os
NUMLUGARES = 7
LIVRE = 0
OCUPADO = 1
queroSair = False
numLugaresOcupados = 0
parqueCheio = False


lugares = {numLugar: {'estado': LIVRE, 'matricula': ''} for numLugar in range(1, NUMLUGARES + 1)}


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
    print()
    if resposta:
        escolha = resposta[0]
    else:
        escolha = '0'

#opção 1 escolher lugar
    if escolha == '1':
        print("Listagem de Lugares:")
        for numLugar, info in lugares.items():
            estado = "livre" if info['estado'] == LIVRE else "ocupado"
            if info['estado'] == LIVRE:
                print(" -> Lugar:", {numLugar}, {estado})
            else:
                print(" -> Lugar:", {numLugar}, {estado}, "por", {info['matricula']})
        input("Prima qq tecla para continuar ...")       
        print()

#opção 2 ocupar lugar
    elif escolha == '2':
        if not parqueCheio:
            print("Qual é o lugar a ocupar (1-",{NUMLUGARES},")? ", end="")
            numLugar = input()
            if numLugar.isdigit():
                numLugar = int(numLugar)
                if numLugar < 1 or numLugar > NUMLUGARES:
                    print("Lugar inválido! Lugares vão de 1 a", {NUMLUGARES})
                elif lugares[numLugar]['estado'] == OCUPADO:
                    print("Lugar já está ocupado!")
                else:
                    lugares[numLugar]['estado'] = OCUPADO
                    print("Insira a sua matrícula:", end="")
                    lugares[numLugar]['matricula'] = input()
                    numLugaresOcupados += 1
                    if numLugaresOcupados == len(lugares):
                        parqueCheio = True
                    print("Lugar ocupado com sucesso!")
            else:
                print("Opção Inválida!")
        else:
            print("Não pode ocupar mais lugares!!")
        input("Prima qq tecla para continuar ...")  
        print()

#opção 3 libertar lugar   
    elif escolha == '3':
        print("Qual é o lugar a libertar (1-", {NUMLUGARES},")? ", end="")
        numLugar = int(input())
        if numLugar < 1 or numLugar > NUMLUGARES:
            print("Lugar inválido! Lugares vão de 1 a", {NUMLUGARES})
        elif lugares[numLugar]['estado'] == LIVRE:
            print("Lugar já está livre!")
        else:
            lugares[numLugar]['estado'] = LIVRE
            numLugaresOcupados -= 1
            if numLugaresOcupados < len(lugares):
                parqueCheio = False
            print("Lugar libertado com sucesso!")
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


