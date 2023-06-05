import random
lista_de_eventos = ["tive um encontro com alienígenas","houve muitas falhas de equipamentos", "fizemos algumas descobertas científicas"]
lista_de_separadores = ["mas ", "porém ", "ainda "]
historia = ""
escolhidas=[]
for i in range(3):
    historia = historia + lista_de_eventos[random.randint(0,2)]
print(historia)
