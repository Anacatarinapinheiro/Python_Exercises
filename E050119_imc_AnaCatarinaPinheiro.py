# 1. Dados
peso = 0;
altura = 0;
imc = 0;
 
# 2. Algoritmo
# 2.1 Obter entradas

print("Insira o seu peso em kg: ",end="")
peso = float(input())

print("Insira a sua altura em m: ",end="")
altura = float(input())

# 2.2 Processar as entradas
imc = round((peso / (altura * altura)), 2)
# 2.3 Apresentar a saída
print("O seu IMC é:", imc,".")