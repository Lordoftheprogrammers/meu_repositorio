# Criar uma história tão inesperada quanto possível.
import random
lista_de_eventos = ["tive um encontro com alienígenas","houve muitas falhas de equipamentos", "fizemos algumas descobertas científicas"]
lista_de_separadores = ["mas", "porém", "ainda"]
historia = ""
escolhidas=[]
for i in range(3):
    if i==1:
        historia = historia+", "
    historia = historia + lista_de_separadores[random.randint(0,2)] +" "+ lista_de_eventos[random.randint(0,2)]
historia = historia+"."
# Ainda não estou muito satisfeito com o resultado porque a história ainda é repetitiva.
print(historia)
