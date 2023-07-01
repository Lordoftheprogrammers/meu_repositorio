import matplotlib.pyplot as plt
import random

# Dados aleatórios para as barras
dados = [random.randint(1, 250) for _ in range(250)]

# Plotagem das barras aleatórias
plt.bar(range(len(dados)), dados)
plt.title("Gráfico de Barras Aleatório")
plt.xlabel("Índice")
plt.ylabel("Valor")
plt.show()

# Ordenação das barras com o pré-definido Timsort
dados_ordenados = sorted(dados)

# Plotagem das barras ordenadas
plt.bar(range(len(dados_ordenados)), dados_ordenados)
plt.title("Gráfico de Barras Ordenado")
plt.xlabel("Índice")
plt.ylabel("Valor")
plt.show()