# Pedir o input de 
Frase=input("Frase: ")

# Inicialização das variáveis
vogais=["a","e","i","o","u"]
mensagem=""
contador=0

# Ciclo letra a letra da frase introduzida (For)
# Todas as strings são listas de caracteres

for letra in Frase.lower():
    # Verifica se uma 
    if letra in vogais:
        contador = contador + 1
        mensagem=mensagem+letra
print(mensagem)
print(contador)  