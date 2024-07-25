contador = 10
vogais = 0
caracteres = []
print("Vai inserir 10 caracteres.")

while contador > 0:
    print("->Insira um caractere: ", end="")
    resposta = input()
    caracteres.append(resposta)
    if resposta.lower() in 'aeiou':
        vogais += 1
    contador -= 1
print()
print("Inseriu", vogais, "vogais.")
print()
print("Fim do Programa.")