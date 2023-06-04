# array, list
# co

lista =[1,2,3]
print(lista[2])
print("\n")

texto ="circulo"
#Vai buscar a primeira letra desta variável
print(texto[0])

lista_palavras=['circulo','triangulo']
#vai buscar a primeira (0) letra do segundo (1) elemento
print(lista_palavras[1][0])
#vai buscar as primeiras 4 letras do segundo (1) elemento
print(lista_palavras[1][0:3])

#Inverter uma lista
print(texto[::-1])

#Dar o n-último elemento da lista
print(texto[-1])
print(texto[-2])
print(texto[-3:-1])

#Dar o último do invertido = primeiro do normal
print(texto[::-1][-1])

#Separar um texto em segmentos, por defeito onde há espaços, mas também onde houver outros caracteres
frase="Esta é a frase que eu quero partir".split()
print(frase)
varias_frases="Eu estou aqui. Vou estar ali. Já estive noutros lados.".split(".")
print(varias_frases)

#Juntar elementos a uma lista
lista.append(5)
print(lista)
lista.insert(3,4)
print(lista)