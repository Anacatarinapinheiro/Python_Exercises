# 1. Dados
lado1 = 0;
lado2 = 0;
lado3 = 0;
lado4 = 0;
perimetro = 0;
 
# 2. Algoritmo
# 2.1 Obter entradas

print("Insira a medida do lado 1 (cm): ",end="")
lado1 = float(input())
print("Insira a medida do lado 2 (cm): ",end="")
lado2 = float(input())
print("Insira a medida do lado 3(cm): ",end="")
lado3 = float(input())
print("Insira a medida do lado 4(cm): ",end="")
lado4 = float(input())

# 2.2 Processar as entradas

perimetro = lado1 + lado2 + lado3 + lado4

# 2.3 Apresentar a saída
print("O perímetro do trapézio é: ", perimetro,"cm.")