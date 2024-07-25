num1 = 0
num2 = 0
menor ='\0'

print("Digite dois números para ver qual dos dois é menor.")
print("Digite o primeiro número: ", end="")
num1 = float(input())

print("Digite o segundo número: ", end="")
num2 = float(input())

match (menor):
    case _ if num1>num2:
        print("O número menor é:", num2)
    case _ if num1==num2:
        print("Os números são iguais.")
    case _:
        print("O número menor é:", num1)
        
print()
print("Programa Terminado")



