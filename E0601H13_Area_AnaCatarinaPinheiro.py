# 1. Dados
num1 = 0;
num2 = 0;
resposta = '';
operacao = 0;
 
# 2. Algoritmo
# 2.1 Obter entradqas

print("Qual a área que quer descobrir: quadrado(q), retângulo (r), círculo (c) ou triângulo (t): ", end="");
resposta = input()

if (resposta == 'Q' or resposta == 'q'):
    print("Insira a largura (cm): ", end="");
    num1 = float(input())
    print("Insira o comprimento (cm): ", end="");
    num2 = float(input())
    operacao = num1 * num2
    print("Escolheu saber a área do quadrado, o seu resultado é:",operacao, "cm2")
    
elif (resposta == 'C' or resposta == 'c'):
    print("Insira o raio (cm): ", end="");
    num1 = float(input())
    operacao = round((num1 * num1 * 3.14159), 2)
    print("Escolheu saber a área do círculo, o seu resultado é:", operacao, "cm2")
    
elif (resposta == 'R' or resposta == 'r'):
    print("Insira a largura (cm): ", end="");
    num1 = float(input())
    print("Insira o comprimento (cm): ", end="");
    num2 = float(input())
    operacao = num1 * num2
    print("Escolheu saber a área do retângulo, o seu resultado é:",operacao, "cm2")
    
elif (resposta == 'T' or resposta == 't'):
    print("Insira a altura (cm): ", end="");
    num1 = float(input())
    print("Insira o comprimento da base (cm): ", end="");
    num2 = float(input())
    operacao = (num1 * num2) / 2
    print("Escolheu saber a área do triângulo, o seu resultado é:",operacao, "cm2")

else:
    print("Escolheu uma opção inválida! Escolha: quadrado(q), retângulo (r), círculo (c) ou triângulo (t).")