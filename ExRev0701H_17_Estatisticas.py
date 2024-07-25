numValores = 0
nota = []     
media = 0; maximo = 0; minimo = 0;    
      
print("Quantas notas quer inserir? ", end="")
numValores = int(input())
print()
              
for estatisticas in range (1,int(numValores)+1,1):
    print("Insira a", estatisticas,"º nota-> ", end="")
    nota_atual = float(input())
    nota.append(nota_atual)

print()  
media = sum (nota)/ numValores
print("-> A média das notas  é: ", round(media,1))
maximo = max(nota)
print("-> A nota máxima foi: ", maximo)
minimo = min(nota) 
print("-> A nota mínima foi: ", minimo)


print()
print("Fim do programa.")   