""" 4. Exercício de Funções
        • Escreva uma função chamada calcula_area_retangulo que recebe dois parâmetros: comprimento e largura.
        • Dentro da função, calcule a área do retângulo multiplicando o comprimento pela largura.
        • Retorne o valor da área.
        • Teste a função chamando-a com diferentes valores de comprimento e largura.
        • Exiba o resultado na consola """

# Função chamada calcula_area_retangulo que recebe dois parâmetros: comprimento e largura.
# Dentro da função, calcule a área do retângulo multiplicando o comprimento pela largura.
# Retorne o valor da área.
def calcula_area_retangulo(comprimento, largura):
    return (comprimento)*(largura)

# Teste a função chamando-a com diferentes valores de comprimento e largura.
for c in range(1,11):
    for l in range(1,11):
        #Exiba o resultado na consola
        print("Comprimento " + str(c) + " e "+ "Largura " + str(l)+" dá uma área de: "+str(calcula_area_retangulo(c,l)))