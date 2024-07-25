num = 0
tabuada = 0

print("Qual a tabuada que quer descobrir? ", end="")
num = int(input())
print()

for tabuada in range (1,11,1):
    print("->", num, "x", tabuada , "= ", num * tabuada)

print()
print("Fim do Programa")