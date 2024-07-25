# 1. Dados
num1 = 0;
num2 = 0;
resposta = '';
operacao = 0;
 
# 2. Algoritmo
# 2.1 Obter entradas

print("Insira dois números para realizar operações matemáticas. \n")
print("Insira um número: ", end="");
num1 = float(input())
print("Insira o segundo número: ", end="");
num2 = float(input())

print("Qual a operação que quer realizar (+), (-), (*) ou (/): ", end="");
resposta = input()

if (resposta == '+'):
    operacao = round((num1 + num2), 2)
    print("Escolheu somar, o seu resultado é:", operacao)
elif (resposta == '-'):
    operacao = round((num1 - num2), 2)
    print("Escolheu subtrair, o seu resultado é:", operacao)
elif (resposta == '*'):
    operacao = round((num1 * num2), 2)
    print("Escolheu multiplicar, o seu resultado é:", operacao)
elif (resposta == '/'):
    operacao = round((num1 / num2), 2)
    print("Escolheu dividir, o seu resultado é:", operacao)
else:
    print("Escolheu uma opção inválida, escolha (+), (-), (*) ou (/)")