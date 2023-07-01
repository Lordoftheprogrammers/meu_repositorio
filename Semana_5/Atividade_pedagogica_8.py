palavra = input("Insira uma string: ")

nova_palavra = ""

for caracter in palavra:
    nova_palavra = caracter + nova_palavra

print("String invertida:", nova_palavra)

numero = input("Dê lá um número: ")

numero_em_string = str(int(numero))

novo_numero = ""

for digito in numero_em_string:
    novo_numero = digito + novo_numero

print("Numero invertido: ", novo_numero)

primeira_palavra = input("Palavrinha: ")
segunda_palavra = primeira_palavra[::-1]
print(segunda_palavra)

primeiro_numero = input("Número: ")
segundo_numero = int(str(primeiro_numero)[::-1])
print(segundo_numero)

# Bubble sort