import numpy
import array

numValores = 6
nota = []
media = 0
maximo = 0
minimo = 0
escolha = 0
apagar = 0
queroSair = False

while (not queroSair):

    print("")
    print("***********************************")
    print("*                                 *")
    print("*       Escola Pinheiro           *")
    print("*                                 *")
    print("*      1. Inserir Notas           *")
    print("*      2. Listar Notas            *")
    print("*      3. Apresentar Média        *")
    print("*      4. Apresentar Máximo       *")
    print("*      5. Apresentar Mínimo       *")
    print("*      6. Apagar Notas            *")
    print("*      7. Sair do programa.       *")
    print("*                                 *")
    print("***********************************")
    print()


    resposta = input(" -> Escolha uma opção (1-7): ")
    if len (resposta) > 0:  
        escolha = resposta[0]
    else:
        escolha = 0

    if escolha == '1':
        estatisticas = 1
        print("Vai inserir 6 notas.")
        while estatisticas <= int(numValores):
            print("Insira a", estatisticas, "ª nota -> ", end="")
            nota_atual = input()

            if nota_atual.replace('.', '', 1).isdigit() or (nota_atual.count('.') == 1 and nota_atual.replace('.', '', 1).isdigit()):
                nota_atual = float(nota_atual)
                if nota_atual < 0 or nota_atual > 20:
                    print("Opção inválida! As notas devem estar entre 0 e 20.")
                else:
                    nota.append(nota_atual)
                    estatisticas += 1
            else:
                print("Por favor, insira um valor numérico válido para a nota.")


    elif (escolha == '2'):
        if not nota:
            print("Não existem notas no sistema!")  
        else:
            for aluno in range(len(nota)):      
                print(nota[aluno])

    elif (escolha == '3'):
        print()
        media = sum(nota) / numValores
        print("-> A média das notas  é: ", round(media, 1))

    elif (escolha == '4'):
        print()
        maximo = max(nota)
        print("-> A nota máxima foi: ", maximo)

    elif (escolha== '5'):
        print()
        minimo = min(nota)
        print("-> A nota mínima foi: ", minimo)

    elif (escolha == '6'):
        resposta = input("Tem a certeza que deseja apagar as notas (S/N)? ")
        if (resposta[0] == 's' or resposta[0] == 'S'):
            nota.clear()

        else:
            input("Prima qq tecla para continuar ...")

    elif (escolha == '7'):
        resposta = input("Tem a certeza (S/N)? ")
        if (resposta[0] == 's' or resposta[0] == 'S'):
            queroSair = True
            
    else:
        print("Opção inválida!")
        input("Prima qq tecla para continuar ...")

# 2.5 Despedida
print("Obrigado por ter usado o nosso programa!")
print()