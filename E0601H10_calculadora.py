# 1. Dados
num1 = 0
num2 = 0
resposta = '\0'
operacao = 0


print("Insira um número: ", end="")
num1 = int(input())
print("Insira o segundo número: ", end="")
num2 = int(input())

print("Qual a operação que quer realizar (+), (-), (*) ou (/): ", end="")
resposta = input()

match(resposta[0]):
    case '+':
        operacao = num1 + num2
        print("Escolheu somar, o seu resultado é:", operacao)
    case '-':
        operacao = num1 - num2
        print("Escolheu subtrair, o seu resultado é:", operacao)
    case '*':
        operacao = num1 * num2
        print("Escolheu multiplicar, o seu resultado é:", operacao)
    case '/':
        operacao = round(num1 / num2)
        print("Escolheu dividir, o seu resultado é:", operacao)
    case _:
        print("Escolheu uma opção inválida, escolha (+), (-), (*) ou (/)")

print()
print("Programa Terminado")