resposta = 0
fatura = 0
soma = []
somaSIVA =[]
despesas = 0
despesasSIVA = 0
iva = 0

print("Quantas despesas quer inserir: ", end= "")
resposta = int(input())
print()

while resposta > 0:
    print("Introduza o valor da sua despesa: ", end="")
    fatura = float(input())
    print("Introduza o valor do IVA (6%, 13%, 23%): ", end="")
    iva = float(input())
    soma.append((fatura*iva*0.01)+fatura)
    somaSIVA.append((fatura))
    resposta -=1

despesas = round(sum(soma),2)
despesasSIVA = round(sum(somaSIVA),2)


print()
print("-> O valor das suas despesas com IVA foi de: ", despesas, "€ e sem IVA:", despesasSIVA, "€.")
print()
