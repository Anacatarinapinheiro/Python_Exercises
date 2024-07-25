import numpy as np

# 1. Dados
EstadoSala = np.zeros((10, 2))  
Projetores = [205,206,208,204] 
LIVRE = 0
OCUPADO = 1
queroSair = False
escolha = '\0'

while not queroSair:

    print("")
    print("***********************************")
    print("*                                 *")
    print("*         Videoprojetores         *")
    print("*                                 *")
    print("*      1. Lista de Salas          *")
    print("*      2. Levantar Projetor       *")
    print("*      3. Devolver Projetor       *")
    print("*      4. Sair do programa        *")
    print("*                                 *")
    print("***********************************")
    print()

#aqui vou escolher 1 a 4
    resposta = input(" -> Escolha uma opção (1-4): ")
    if len(resposta) > 0: 
        escolha = resposta[0]
    else:
        escolha = 0

#aqui escolho ver as salas e se tem projetor
    if escolha == '1':
        for sala in range(1, 11):
            if EstadoSala[sala - 1][0] == LIVRE:
                estado = 'Vazia'
                id_projetor = 'Nenhum'
                print("-> Sala", sala, "Estado:", estado)
            else:
                estado = 'com projetor'
                id_projetor = EstadoSala[sala - 1][1]
                print("-> Sala", sala, "Estado:", estado, "ID do Projetor:", id_projetor)

#aqui vou levantar um projetor para uma sala
    elif escolha == '2':
        sala_levantar = int(input(" -> Digite o número da sala para levantar o projetor: "))
        if EstadoSala[sala_levantar - 1][0] == LIVRE:
            if Projetores:  
                projetor_id = Projetores.pop(0)  
                EstadoSala[sala_levantar - 1][0] = OCUPADO
                EstadoSala[sala_levantar - 1][1] = projetor_id
                print("Projetor com ID", projetor_id, "levantado com sucesso para a sala", sala_levantar)
            else:
                print("Não existem projetores disponíveis.")
        else:
            print("Esta sala já tem um projetor.")
 
#aqui devolvo o projetor de uma sala           
    elif escolha == '3':
        sala_devolver = int(input(" -> Digite o número da sala para devolver o projetor: "))
        if EstadoSala[sala_devolver - 1][0] == OCUPADO:
            projetor_id = EstadoSala[sala_devolver - 1][1]
            EstadoSala[sala_devolver - 1][0] = LIVRE
            Projetores.append(projetor_id)  
            print("Projetor da sala", sala_devolver, "devolvido com sucesso!")
        else:
            print("Não existe um projetor nesta sala.")

#aqui saio do programa       
    elif escolha == '4':
        resposta = input("Tem a certeza (S/N)? ")
        if resposta[0] == 's' or resposta[0] == 'S':
            queroSair = True

#se meter um valor inválido        
    else:
        print("Escolha inválida! Por favor, escolha uma opção de 1 a 4.")

#Despedida
print("Obrigado por ter usado o nosso programa!")
