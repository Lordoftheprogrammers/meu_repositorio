# Importar bibliotecas

# Ele é que sugere a bilbioteca
import random

num_aleatorio = int(random.random()*100)
num_aleatorio2=random.randint(0,100)
lista_numeros=random.sample(range(2,40),5)
print(num_aleatorio)
print(num_aleatorio2)
print(lista_numeros)

lista_numeros_euromilhoes=random.sample(range(1,50),5)
lista_estrelas_euromilhoes=random.sample(range(1,13),2)
print("Os números do euromilhões seleccionados são: ", lista_numeros_euromilhoes)
print("As estrelas do euromilhões seleccionados são: ", lista_estrelas_euromilhoes)

jogo= ["pedra","papel","tesoura"]
print(random.choice(jogo))
