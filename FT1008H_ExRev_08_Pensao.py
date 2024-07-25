import sys   # Biblioteca entradas/saídas do sistema
import os    # Biblioteca das funções/comandos do sistema operativo
# import only system from os
from os import system, name
# import sleep to show output for some time period
from time import sleep
#pip3 install numpy
import numpy as np
from array import *

# Funções

def defineTitulo(titulo):
    titulo = "*        Pensão Pinheiro          *"
    return titulo

#     Função "inicializaMenu()"
def inicializaMenu(menu):
    menu = [
        "*      1. Listar quartos.         *",
        "*      2. Reservar quarto.        *",
        "*      3. Check-in.               *",
        "*      4. Check-out.              *",
        "*      5. Sair do programa.       *"
    ]
    return menu

# 1.03  Função do ciclo principal
def cicloPrincipal(quartos, LIVRE, RESERVADO,
                   OCUPADO, titulo, menu):
    queroSair = False
    escolha = '\0'
    while (not queroSair):
        mostraMenu(titulo, menu)
        escolha = obtemEscolha(escolha, len(menu))
        queroSair = processaEscolha(
            escolha, quartos, LIVRE, RESERVADO,
                   OCUPADO, queroSair)
    return

#     Função "mostraMenu()"
def mostraMenu(titulo, menu):
    print("")
    print("***********************************")
    print("*                                 *")
    print(titulo)
    print("*                                 *")
    for cOpcao in range(0,len(menu),1):
        print(menu[cOpcao])
    print("*                                 *")
    print("***********************************")
    print()
    return

#     Função "obtemEscolha()"
def obtemEscolha(escolha, numOpcoes):
    print(" -> Escolha uma opção (1-",end="")
    print(numOpcoes,end="")
    print("): ",end="")
    resposta = input()
    if (len(resposta) > 0):  
       escolha = resposta[0]
    else:
       escolha = 0
    return escolha

#     Função "processaEscolha()"
def processaEscolha(
        escolha, quartos, LIVRE, RESERVADO,
                   OCUPADO, queroSair):
    match (escolha):
        case '1':
            listarQuartos(quartos, LIVRE, RESERVADO)
        case '2':
            reservarQuarto(quartos,LIVRE, RESERVADO)
        case '3':
            checkIN(quartos,OCUPADO)
        case '4':
            checkOUT(quartos,LIVRE)
        case '5':
            queroSair = sairDoProgram(queroSair)
        case _:
            opcaoInvalida()
    return queroSair

# opção 1 "listarQuartos()"
def listarQuartos(quartos, LIVRE, RESERVADO):
    print("Listagem de quartos:")
    for cAndar in range(0, len(quartos), 1):
        print("Andar ", (cAndar + 1), ": ", end="\n")
        for cQuarto in range(0, len(quartos[0]), 1):
            print(" -> Quarto ", (cQuarto + 1), ": ", end="")
            if (quartos[cAndar][cQuarto] == LIVRE):
                print(" livre.")
            elif (quartos[cAndar][cQuarto] == RESERVADO):
                print(" reservado.")
            else:
                print(" ocupado.")
        input("Prima qq tecla para continuar ...")
    return

# opção 2  "reservarQuarto()"
def reservarQuarto(quartos,LIVRE, RESERVADO):
    print("Qual é o andar a selecionar ( 1 -",
          len(quartos), ")? ", end="")
    numAndar = int(input())
    print("Nesse andar, qual é o quarto a reservar ( 1 -",
          len(quartos[0]), ")? ", end="")
    numQuarto = int(input())
    if (numAndar >= 1
            and numAndar <= len(quartos)
            and numQuarto >= 1
            and numQuarto <= len(quartos[0])):
        if (quartos[numAndar - 1][numQuarto - 1] == LIVRE):
            quartos[numAndar - 1][numQuarto - 1] = RESERVADO
            print("Quarto reservado com sucesso!")
        else:
            print("Quarto não pode ser reservado!")
    else:
        print("Número de andar ou de quarto inválido!")
    input("Prima qq tecla para continuar ...")
    return


# opção 3 "checkIN()"
def checkIN(quartos,OCUPADO):
    print("Qual é o andar a selecionar ( 1 -",
          len(quartos), ")? ", end="")
    numAndar = int(input())
    print("Nesse andar, qual é o quarto a ocupar ( 1 -",
          len(quartos[0]), ")? ", end="")
    numQuarto = int(input())
    if (numAndar >= 1
            and numAndar <= len(quartos)
            and numQuarto >= 1
            and numQuarto <= len(quartos[0])):
        if (quartos[numAndar - 1][numQuarto - 1] != OCUPADO):
            quartos[numAndar - 1][numQuarto - 1] = OCUPADO
            print("Quarto ocupado com sucesso!")
        else:
            print("Quarto já está ocupado!")
    else:
        print("Número de andar ou de quarto inválido!")
    input("Prima qq tecla para continuar ...")
    return

# opção 4 "checkOUT()"
def checkOUT(quartos,LIVRE):
    print("Qual é o andar a selecionar ( 1 -",
          len(quartos), ")? ", end="")
    numAndar = int(input())
    print("Nesse andar, qual é o quarto a libertar ( 1 -",
          len(quartos[0]), ")? ", end="")
    numQuarto = int(input())
    if (numAndar >= 1
            and numAndar <= len(quartos)
            and numQuarto >= 1
            and numQuarto <= len(quartos[0])):
        if (quartos[numAndar - 1][numQuarto - 1] != LIVRE):
            quartos[numAndar - 1][numQuarto - 1] = LIVRE
            print("Quarto libertado com sucesso!")
        else:
            print("Quarto já está livre!")
    else:
        print("Número de andar ou de quarto inválido!")
    input("Prima qq tecla para continuar ...")
    return

#  opção 5 sair
def sairDoProgram(queroSair):
    resposta = input("Tem a certeza (S/N)? ")
    if (len(resposta) > 0):
        if (resposta[0] == 's' or resposta[0] == 'S'):
            queroSair = True
        elif (resposta[0] == 'n' or resposta[0] == 'N'):
            return
        else:
            print("Opção Inválida.")
            return            
    return queroSair

#     Função "opcaoInvalida()"
def opcaoInvalida():
    print("Opção inválida!")
    input("Prima qq tecla para continuar ...")
    return

#     Função "despedida()"
def despedida():
    print("Obrigado por ter usado o nosso programa!")
    input("Prima qq tecla para continuar ...")
    print()
    return

NUMANDARES = 3; NUMQUARTOSPORANDAR = 5
NUMOPCOES = 5
LIVRE = 0; RESERVADO = 1; OCUPADO = 2
titulo =""
menu = ["" for cOpcao in range(0,NUMOPCOES,1)]
quartos = [
  [LIVRE for cQuarto in range(NUMQUARTOSPORANDAR)]
         for cAndar in range(NUMANDARES)
  ]

titulo = defineTitulo(titulo)
menu   = inicializaMenu(menu)
cicloPrincipal(quartos, LIVRE,RESERVADO,OCUPADO, titulo,menu)
despedida()