# 1. Dados
resposta = '';
 
# 2. Algoritmo
# 2.1 Obter entradas
print("Como classifica a seguinte frase: \n"); 
print("Algoritmia é a ciência que cria, aperfeçoa e optimiza algoritmo.\n");
print("Esta afirmção é verdadeira (v) ou falsa (f): ");
resposta = input()

if (resposta == 'V' or resposta == 'v'):
    print ("A sua resposta está correta.")
    
elif (resposta == 'F' or resposta == 'f'):
    print ("A sua resposta está errada.")
    
else:
    print ("A sua resposta é inválida, escolha v ou f.")