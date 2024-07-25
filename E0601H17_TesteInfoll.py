resposta = 0
tentativas = 2

print()
print("O que é que a sigla pip representa no contexto de Python?")
print()
print("Opção 1 -> Python Invoques Patience")
print("Opção 2 -> Python Integrated Package")
print("Opção 3 -> Pip Installs Problems")
print("Opção 4 -> Python Package Install")

while tentativas > 0:
    print("Escolhe a resposta (1), (2), (3) ou (4)")
    print()
    print("Insira a sua resposta: ", end=" ")
    resposta = float(input())

    match (resposta):
        case 1 | 3 | 4:
            print("Errou!")
            print()
            tentativas -= 1
            print("Tem mais", tentativas, "tentativa.")
        case 2:
            print("Acertou!")
            break
        case _:
            print("Resposta inválida.")
            print()

print()
print("Programa Terminado")