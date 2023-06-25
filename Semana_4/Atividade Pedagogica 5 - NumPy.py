import numpy as np

# Exemplo de criação de um array
temperaturas = [22, 24, 23, 25, 24, 23, 22, 24, 25, 26, 25, 24, 23, 22, 23, 24, 25, 26, 25, 24, 23, 22, 24, 25, 24,
23, 24, 25, 24, 23]
temperaturas_array = np.array(temperaturas)

# Calcular a média das temperaturas
media = np.mean(temperaturas_array)
print(f"Média das temperaturas: {media} graus Celsius")

# Encontrar a temperatura mais alta e a mais baixa
temperatura_maxima = np.max(temperaturas_array)
temperatura_minima = np.min(temperaturas_array)
print(f"Temperatura máxima: {temperatura_maxima} graus Celsius")
print(f"Temperatura mínima: {temperatura_minima} graus Celsius")

# Calcular o desvio padrão das temperaturas
desvio_padrao = np.std(temperaturas_array)
print(f"Desvio padrão das temperaturas: {desvio_padrao}")