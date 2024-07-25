# 1. Dados
num1 = 0
num2 = 0
resposta = '\0'
operacao = 0


print("Insira um número: ", end="")
num1 = int(input())
print("Insira o segundo número: ", end="")
num2 = int(input())

while (num1 < 5 or num1 > 30 ) or (num2 < 5 or num2 > 30):
    print("Dígito inválido. Os dígitos têm de ser entre 5 e 30!")
    print()
    print("Insira um número: ", end="")
    num1 = int(input())
    print("Insira o segundo número: ", end="")
    num2 = int(input())
else:
    print ()
    print ("Vamos passar para as operações!")
    print()
    if num1 < 11 and num2 < 11:
        operacao = num1 * num2
        print("Vai ocorrer uma multiplicação. O seu resultado foi:", operacao)
    elif num1 > 20 and num2 > 20:
        operacao = round(num1 / num2)
        print("Vai ocorrer uma divisão. O seu resultado foi:", operacao)
    else:
        operacao = num1 + num2
        print("Vai ocorrer uma soma. O seu resultado foi:", operacao)
print()
print("Programa Terminado")