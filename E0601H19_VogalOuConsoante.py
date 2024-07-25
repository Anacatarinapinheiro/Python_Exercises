digito = '\0'

print("Insira uma letra: ", end="")
digito = input()
print()

match digito[0].lower():
    case 'a' | 'e' | 'i' | 'o' | 'u':
        print("A letra", digito, "é uma vogal.")
    case 'b' | 'c' | 'd' | 'f' | 'g' | 'h' | 'j' | 'k' | 'l' | 'm' | 'n' | 'p' | 'q' | 'r' | 's' | 't' | 'v' | 'x' | 'z':
        print("A letra", digito, "é uma consoante.")
    case _:
        print("Erro: Você inseriu um dígito inválido.")

print()
print("Fim do Programa.")