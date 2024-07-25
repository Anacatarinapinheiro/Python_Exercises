
NUMEROS = 8
nota = []
media = 0
maximo = 0
minimo = 0
resposta = 0
escolha = 0
queroSair = False

print()
print("Vai inserir 8 notas(0 a 20).")
print()

for estatisticas in range(1, NUMEROS + 1):
    while True:
        print("Insira a", estatisticas, "ª nota -> ", end="")
        nota_atual = input()
        if nota_atual.replace('.', '', 1).isdigit():
            nota_atual = float(nota_atual)
            if 0 <= nota_atual <= 20:
                nota.append(nota_atual)
                break
            else:
                print("Opção inválida! As notas devem estar entre 0 e 20.")
        else:
            print("Por favor, insira um valor numérico válido para a nota.")

while (not queroSair):
    print()
    print("Qual a operação que deseja realizar: média (1), máximo (2), mínimo (3). Para sair escolha (4).")
    resposta = input(" -> Escolha uma opção (1-4): ")
    if len(resposta) > 0:
        escolha = resposta[0]
    else:
        escolha = 0

    match (escolha):
        case '1':
            print()
            media = sum(nota) / NUMEROS
            print("-> A média das notas  é: ", round(media, 1))

        case '2':
            print()
            maximo = max(nota)
            print("-> A nota máxima foi: ", maximo)

        case '3':
            print()
            minimo = min(nota)
            print("-> A nota mínima foi: ", minimo)

        case '4':
            resposta = input("Tem a certeza (S/N)? ")
            if (resposta[0] == 's' or resposta[0] == 'S'):
                queroSair = True
            print("Obrigado por utilizar o programa! Volte sempre!")

        case _:
            print("Opção inválida!")
            input("Prima qq tecla para continuar ...")

print()
print("Fim do programa.")