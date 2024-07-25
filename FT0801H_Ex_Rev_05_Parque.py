import sys   # Biblioteca entradas/saídas do sistema
import os    # Biblioteca das funções/comandos do sistema operativo
# import only system from os
from os import system, name
# import sleep to show output for some time period
from time import sleep
#pip3 install numpy
import numpy as np

# 1. Dados
NUMLUGARES = 7
LIVRE = 0
OCUPADO = 1
queroSair = False
escolha='\0'
numLugaresOcupados = 0
parqueCheio = False
lugares =[LIVRE for cLugar in range(NUMLUGARES)]

while (not queroSair):
# 2. Algoritmo
    # 2.1 Apresentar o menu
    #os.system('cls' if os.name == 'nt' else 'clear') # Limpa o ecrã
    print("")
    print("***********************************")
    print("*                                 *")
    print("*             Parque Gest         *")
    print("*                                 *")
    print("*      1. Listar lugares.         *")
    print("*      2. Marcar lugar.           *")
    print("*      3. Libertar lugar.         *")
    print("*      4. Sair do programa.       *")
    print("*                                 *")
    print("***********************************")
    print()
    if (parqueCheio):
       print("***********************************")
       print("*                                 *")
       print("*         Parque Completo!        *")
       print("*                                 *")
       print("***********************************")
    print()


    # 2.2 Pedir uma opção de escolha ao utilizador
    resposta = input(" -> Escolha uma opção (1-4): ")
    if (len(resposta) > 0):   # Evita "out of index error"
       escolha = resposta[0]
    else:
       escolha = 0

    # 2.3 Processa escolha
    if (escolha == '1'):
        print("Listagem de Lugares:")
        for cLugar in range(0,NUMLUGARES,1):
            print(" -> Lugar: ",(cLugar+1),": ", end =" ")
            if (lugares[cLugar] == LIVRE):
                print(" livre.")
            else:
                print(" ocupado.")
        input("Prima qq tecla para continuar ...")
    elif (escolha == '2'):
        if (not parqueCheio):
           print("Qual é o lugar a ocupar ( 1 -",NUMLUGARES,")? ",end =" ")
           numLugar = int(input())
           if (numLugar < 1  or numLugar > NUMLUGARES):
              print("Lugar inválido!")
              print("Lugares vão de 1 a ",NUMLUGARES,"!")
           elif (lugares[numLugar-1]==OCUPADO):
              print("Lugar já está ocupado!")
           else:
              lugares[numLugar-1]=OCUPADO
              numLugaresOcupados +=1
              if (numLugaresOcupados == len(lugares)):
                  parqueCheio = True
              elif (numLugaresOcupados < len(lugares)):
                  parqueCheio = False
              print("Lugar ocupado com sucesso!")
        else:
           print("Não pode ocupar mais lugares!!")
        input("Prima qq tecla para continuar ...")
    elif (escolha == '3'):
        print("Qual é o lugar a libertar ( 1 -",NUMLUGARES,")? ",end =" ")
        numLugar = int(input())
        if (numLugar < 1  or numLugar > NUMLUGARES):
            print("Lugar inválido!")
            print("Lugares vão de 1 a ",NUMLUGARES,"!")
        elif (lugares[numLugar-1] == LIVRE):
            print("Lugar já está livre!")
        else:
            lugares[numLugar-1]=LIVRE
            numLugaresOcupados -=1
            if (numLugaresOcupados < len(lugares)):
                parqueCheio = False
            print("Lugar libertado com sucesso!")
        input("Prima qq tecla para continuar ...")
    elif (escolha == '4'):
        resposta = input("Tem a certeza (S/N)? ")
        if (resposta[0] =='s' or resposta[0] =='S'):
            queroSair = True
    else:
        print("Opção inválida!")
        input("Prima qq tecla para continuar ...")

# 2.5 Despedida
print("Obrigado por ter usado o nosso programa!")
input("Prima qq tecla para continuar ...")
print()