# 1. Dados
num1 = 0;
num2 = 0;
 
# 2. Algoritmo
# 2.1 Obter entradas
print("Insira o primeiro número: ", end="");
num1 = float(input())
print("Insira o segundo número: ", end="");
num2 = float(input())

if (num1 > num2 ):
    print(num2,"<", num1)
elif(num2 > num1):
    print(num1,"<", num2)
else:
    print("Escolheu dois números iguais.")