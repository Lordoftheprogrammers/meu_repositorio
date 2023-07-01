entrada = input("Por favor, insira uma lista de números inteiros separados por espaços: ")
lista_desordenada = [int(numero) for numero in entrada.split()]
#print(lista_desordenada)
lista_ordenada = sorted(lista_desordenada)
print(lista_ordenada)

# Bubble Sort
n = len(lista_desordenada)

for i in range(n):
    print(i)
    for j in range(0, n-i-1):
        print(i, j, lista_desordenada)
        if lista_desordenada[j] > lista_desordenada[j+1]:
            lista_desordenada[j],lista_desordenada[j+1]=lista_desordenada[j+1],lista_desordenada[j]

print(lista_desordenada)

# trocar índice j com j+1 """