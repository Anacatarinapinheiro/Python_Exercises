num1 = 0
resto = '\0'

print("Digite um número entre 5 e 27:", end="")
num1 = float(input())

while num1 > 27 or num1 < 5:
    print("Dígito inválido. Digite um número entre 5 e 27.")
    break
else:
    resto = round(num1 % 2)
    print ()

    match (resto):
        case 0:
            print("Este número,", num1, ", é par.")
        case 1:
            print("Este número,", num1, ", é impar.")
        case _:
            print("Inseriu um valor inválido!")

print()
print("Programa Terminado")