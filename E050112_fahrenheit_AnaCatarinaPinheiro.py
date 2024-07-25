# 1. Dados
fahrenheit = 0;
conversao = 0;
 
# 2. Algoritmo
# 2.1 Obter entradas

print("Insira a temperatura em Fahrenheit (ºF): ",end="")
fahrenheit = float(input())

# 2.2 Processar as entradas
conversao = round(((fahrenheit - 32) * 5 / 9), 2)
# 2.3 Apresentar a saída
print("A temperatura em graus celsius é: ", conversao,"ºC.")
