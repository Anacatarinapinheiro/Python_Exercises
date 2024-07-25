import sys   # Biblioteca entradas/saídas do sistema
import os    # Biblioteca das funções/comandos do sistema operativo
# import only system from os
from os import system, name
# import sleep to show output for some time period
from time import sleep
#pip3 install numpy
import numpy as np
from array import *

# 1. Dados
NUMANDARES = 3; NUMQUARTOSPORANDAR = 5
LIVRE = 0; RESERVADO = 1; OCUPADO = 2
queroSair = False
escolha='\0'


quartos = [
  [LIVRE for cQuarto in range(NUMQUARTOSPORANDAR)]
         for cAndar in range(NUMANDARES)
  ]


while (not queroSair):
# 2. Algoritmo
    # 2.1 Apresentar o menu
    #os.system('cls' if os.name == 'nt' else 'clear') # Limpa o ecrã
    print("")
    print("***********************************")
    print("*                                 *")
    print("*       Pensão Meireles           *")
    print("*                                 *")
    print("*      1. Listar quartos.         *")
    print("*      2. Reservar quarto.        *")
    print("*      3. Ocupar quarto.          *")
    print("*      4. Libertar quarto.        *")
    print("*      5. Sair do programa.       *")
    print("*                                 *")
    print("***********************************")
    print()

    # 2.2 Pedir uma opção de escolha ao utilizador
    resposta = input(" -> Escolha uma opção (1-5): ");
    if (len(resposta) > 0):   # Evita "out of index error"
       escolha = resposta[0]
    else:
       escolha = 0

    # 2.3 Processa escolha
    if (escolha == '1'):
        print("Listagem de quartos:")
        for cAndar in range(0,NUMANDARES,1):
            print("Andar ",(cAndar+1),": ", end ="\n")
            for cQuarto in range(0,NUMQUARTOSPORANDAR,1):
                print(" -> Quarto ",(cQuarto+1),": ", end ="")
                if (quartos[cAndar][cQuarto] == LIVRE):
                    print(" livre.")
                elif (quartos[cAndar][cQuarto] == RESERVADO):
                    print(" reservado.")
                else:
                    print(" ocupado.")
            input("Prima qq tecla para continuar ...")
    elif (escolha == '2'): # Reserva de Quarto
        print("Qual é o andar a selecionar ( 1 -",
               NUMANDARES,")? ",end ="")
        numAndar = int(input())
        print("Nesse andar, qual é o quarto a reservar ( 1 -",
               NUMQUARTOSPORANDAR,")? ",end ="")
        numQuarto = int(input())
        if (numAndar >= 1
        and numAndar <= NUMANDARES
        and numQuarto >=1
        and numQuarto <= NUMQUARTOSPORANDAR):
            if (quartos[numAndar-1][numQuarto-1] == LIVRE):
                quartos[numAndar-1][numQuarto-1]=RESERVADO
                print("Quarto reservado com sucesso!")
            else:
                print("Quarto não pode ser reservado!")
        else:
            print("Número de andar ou de quarto inválido!")
        input("Prima qq tecla para continuar ...")
    elif (escolha == '3'):  # Check-in
        print("Qual é o andar a selecionar ( 1 -",
               NUMANDARES,")? ",end ="")
        numAndar = int(input())
        print("Nesse andar, qual é o quarto a ocupar ( 1 -",
               NUMQUARTOSPORANDAR,")? ",end ="")
        numQuarto = int(input())
        if (numAndar >= 1
        and numAndar <= NUMANDARES
        and numQuarto >= 1
        and numQuarto <= NUMQUARTOSPORANDAR):
            if (quartos[numAndar - 1][numQuarto - 1]!=OCUPADO):
                quartos[numAndar - 1][numQuarto - 1]=OCUPADO
                print("Quarto ocupado com sucesso!")
            else:
                print("Quarto não pode ser ocupado!")
        else:
            print("Número de andar ou de quarto inválido!")
        input("Prima qq tecla para continuar ...")
    elif (escolha == '4'):  # Check-out
        print("Qual é o andar a selecionar ( 1 -",
               NUMANDARES,")? ",end ="")
        numAndar = int(input())
        print("Nesse andar, qual é o quarto a libertar ( 1 -",
               NUMQUARTOSPORANDAR,")? ",end ="")
        numQuarto = int(input())
        if (numAndar >= 1
        and numAndar <= NUMANDARES
        and numQuarto >= 1
        and numQuarto <= NUMQUARTOSPORANDAR):
            if (quartos[numAndar - 1][numQuarto - 1] != LIVRE):
                quartos[numAndar - 1][numQuarto - 1] = LIVRE
                print("Quarto libertado com sucesso!")
            else:
                print("Quarto já está livre!")
        else:
            print("Número de andar ou de quarto inválido!")
        input("Prima qq tecla para continuar ...")
    elif (escolha == '5'):
        resposta = input("Tem a certeza (S/N)? ")
        if (resposta[0] =='s' or resposta[0] =='S'):
            queroSair = True
    else:
        print("Opção inválida!")
        input("Prima qq tecla para continuar ...")

# 2.5 Despedida
print("Obrigado por ter usado o nosso programa!")
print()