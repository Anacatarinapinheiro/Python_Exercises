###############################################
# 0. Bibliotecas
###############################################
import sys   # Biblioteca entradas/saídas do sistema
import os    # Biblioteca das funções/comandos do sistema operativo
# import only system from os
from os import system, name
# import sleep to show output for some time period
from time import sleep
# pip3 install numpy
import numpy as np

# Funçoes

def inicializaParque(lugares, LIVRE):
    for cLugar in range(0,len(lugares),1):
        lugares[cLugar] = LIVRE
    return lugares


#     Função "inicializaMenu()"
def inicializaMenu(menu):
    menu = [
        "*      1. Listar lugares.         *",
        "*      2. Marcar lugar.           *",
        "*      3. Libertar lugar.         *",
        "*      4. Sair do programa.       *"
    ]
    return menu



#     Função "mostraMenu()"
def mostraMenu(menu):
    print("")
    print("***********************************")
    print("*                                 *")
    print("*         Parque Pinheiro         *")
    print("*                                 *")
    for cOpcao in range(0,len(menu),1):
        print(menu[cOpcao])
    print("*                                 *")
    print("***********************************")
    print()
    return

#     Função "mostraParqueCheio()"
def mostraParqueCheio(parqueCheio):
    if (parqueCheio):
       print("***********************************")
       print("*                                 *")
       print("*          Parque Cheio!          *")
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

#     Função "obtemEscolha()"
def processaEscolha(
        escolha, lugares, LIVRE, OCUPADO, queroSair):
    match (escolha):
        case '1':
            listarLugares(lugares, LIVRE)
        case '2':
            marcarLugar(lugares,LIVRE,OCUPADO)
        case '3':
            libertarLugar(lugares,LIVRE)
        case '4':
            queroSair = sairDoProgram(queroSair)
        case _:
            opcaoInvalida()
    return queroSair

#     Função "isParqueCheio()"
def isParqueCheio(lugares, LIVRE):
    parqueCheio = True
    for cLugar in range(0,len(lugares),1):
        if (lugares[cLugar] == LIVRE):
            parqueCheio = False
    return parqueCheio

#     Função "obtemNumLugaresOcupados()"
def obtemNumLugaresOcupados(lugares,OCUPADO):
    numLugaresOcupados = 0
    for cLugar in range(0,len(lugares),1):
        if (lugares[cLugar] == OCUPADO):
            numLugaresOcupados +=1
    return numLugaresOcupados

#opçao mostrar lugares 1
def listarLugares(lugares, LIVRE):
    print("Listagem de Lugares:")
    for cLugar in range(0, len(lugares), 1):
        print(" -> Lugar: ", (cLugar + 1), ": ",
              end="")
        if (lugares[cLugar] == LIVRE):
            print(" Livre.")
        else:
            print(" Ocupado.")
    input("Prima qq tecla para continuar ...")
    return

#  opçao ocupar lugar 2
def marcarLugar(lugares,LIVRE,OCUPADO):
    if (not isParqueCheio(lugares, LIVRE)):
        print("Qual é o lugar a ocupar ( 1 -",
              len(lugares), ")? ", end="")
        numLugar = int(input())
        if (numLugar < 1 or numLugar > len(lugares)):
            print("Lugar inválido!")
            print("Lugares vão de 1 a ", len(lugares), "!")
        elif (lugares[numLugar - 1] == OCUPADO):
            print("Lugar já está ocupado!")
        else:
            lugares[numLugar - 1] = OCUPADO
            print("Lugar ocupado com sucesso!")
    else:
        print("Não pode ocupar mais lugares!!")
        input("Prima qq tecla para continuar ...")
    return

# opçao libertar lugar 3
def libertarLugar(lugares,LIVRE):
    print("Qual é o lugar a libertar ( 1 -",
          len(lugares), ")? ", end="")
    numLugar = int(input())
    if (numLugar < 1 or numLugar > len(lugares)):
        print("Lugar inválido!")
        print("Lugares vão de 1 a ", len(lugares), "!")
    elif (lugares[numLugar - 1] == LIVRE):
        print("Lugar já está livre!")
    else:
        lugares[numLugar - 1] = LIVRE
        print("Lugar libertado com sucesso!")
    input("Prima qq tecla para continuar ...")
    return

# opção sair 4
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

def opcaoInvalida():
    print("Opção inválida!")
    input("Prima qq tecla para continuar ...")
    return

def despedida():
    print("Obrigado por ter usado o nosso programa!")
    input("Prima qq tecla para continuar ...")
    print()
    return

#Fim Funçoes

NUMLUGARES = 7
NUMOPCOES = 4
LIVRE = 0
OCUPADO = 1
queroSair = False
escolha='\0'
menu = ["" for cOpcao in range(NUMOPCOES)]
lugares = np.zeros(NUMLUGARES)

lugares = inicializaParque(lugares, LIVRE)
menu = inicializaMenu(menu)

while (not queroSair):
    mostraMenu(menu)
    mostraParqueCheio(isParqueCheio(lugares, LIVRE))
    escolha = obtemEscolha(escolha, NUMOPCOES)
    queroSair = processaEscolha(
                escolha, lugares, LIVRE,OCUPADO, queroSair)

despedida()