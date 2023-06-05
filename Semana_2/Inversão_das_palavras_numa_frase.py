#Pede uma frase e guarda na variável frase
frase = input("Dê uma frase: ")
#Parte a frase em palavras
frase_partida=frase.split()
#print(frase_partida)
#Guarda o tamanho da frase
dimensao_da_frase =len(frase_partida)

#Inicializa a frase com palavras invertidas
frase_partida_palavras_invertidas =""

#Ciclo de 0 até ao número de palavras
for p in range(dimensao_da_frase):
    #print(frase_partida_palavras_invertidas)
    #Inverte palavra a palavra
    palavra_add_invertida =frase_partida[p][::-1]
    #Adiciona cumulativamente (+=) à frase cada uma das palavras invertidas e um espaço
    frase_partida_palavras_invertidas+=palavra_add_invertida+" "
#Imprime a frase final com as palavras todas invertidas    
print(frase_partida_palavras_invertidas)
