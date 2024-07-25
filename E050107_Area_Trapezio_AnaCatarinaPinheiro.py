# 1. Dados
basemaior = 0;
basemenor = 0;
altura = 0;
area = 0;
 
# 2. Algoritmo
# 2.1 Obter entradas
# "end()" -> qual é o caractere termnador do print
print("Insira a medida da base maior (cm): ",end="")
basemaior = float(input())
print("Insira a medida da base menor (cm): ",end="")
basemenor = float(input())
print("Insira a medida da altura (cm): ",end="")
altura = float(input())
 
# 2.2 Processar as entradas

area = ((basemaior + basemenor)*altura)/2

# 2.3 Apresentar a saída
print("A área do trapézio é: ", area,"cm2.")