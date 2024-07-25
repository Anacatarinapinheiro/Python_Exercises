# 1. Dados
num1 = 0
num2 = 0
resposta = '\0'
operacao = 0


print("Qual o perimetro que quer descobrir: quadrado(q), retângulo (r), círculo (c) ou triângulo (t): ", end="")
resposta = input()

match(resposta):
    case 'Q'|'q':
        print("Insira a largura: ", end="")
        num1 = float(input())
        operacao = num1 * 4
        print("Escolheu saber o perímetro do quadrado, o seu resultado é:", operacao)
        
    case 'C'|'c':
        print("Insira o raio: ", end="")
        num1 = float(input())
        operacao = round((num1*3.14159*2),1)
        print("Escolheu saber o perímetro do círculo, o seu resultado é:", operacao)

    case 'R'|'r':
        print("Insira a largura: ", end="")
        num1 = float(input())
        print("Insira o comprimento: ", end="")
        num2 = float(input())
        operacao = num1*2 + num2*2
        print("Escolheu saber o perímetro do retângulo, o seu resultado é:", operacao)

    case 'T'|'t':
        print("Insira o comprimento do primeiro lado: ", end="")
        num1 = float(input())
        print("Insira o comprimento do segundo lado: ", end="")
        num2 = float(input())
        print("Insira o comprimento do terceiro lado: ", end="")
        num3 = float(input())
        operacao = num1 + num2 + num3
        print("Escolheu saber o perímetro do triângulo, o seu resultado é:", operacao)

    case _:
        print("Escolheu uma opção inválida, quadrado(q), retângulo (r), círculo (c) ou triângulo (t).")
        
print()
print("Programa Terminado")