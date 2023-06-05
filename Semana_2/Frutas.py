# Este programa foi a atividade da 2ª semana, 2ª aula
fruta = input("Escolha uma fruta: ") # Esta linha pede uma fruta (texto)
quantidade = input("Escolha uma quantidade: ") # Esta linha pede uma quantidade, mas fica em texto
qtd=int(quantidade) #Esta linha converte a quantidade em um número inteiro
print("O valor a pagar por "+quantidade+" "+ fruta +" é de "+str(qtd*2)"€") # Esta linha compõe a frase e converte a conta em texto para poder concatená-la

# Exemplo de If's
"""if texto=="bananas":
    print ("Voce escreveu bananas")
elif texto =="laranjas":
    print("Voce escreveu laranjas")
else:
    print("Voce não escreveu nem um, nem outro, voce escreveu "+texto)"""