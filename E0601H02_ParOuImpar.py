num1 = 0
resto = '\0'

print("Digite um número: ", end="")
num1 = float(input())
resto = round(num1 % 2)

match (resto):
    case 0:
        print("Este número:", num1, "é par.")
    case 1:
        print("Este número:", num1, "é impar.")
    case _:
        print("Inseriu um valor inválido!")

print()
print("Programa Terminado")