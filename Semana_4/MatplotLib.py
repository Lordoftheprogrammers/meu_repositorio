import matplotlib.pyplot as plt
import numpy as np

# Gráfico de Linhas

x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.title("Gráfico de Linha")
plt.show()

# Gráfico de Dispersão (Scatter Plot)

x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y)
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.title("Gráfico de Dispersão")
plt.show()

# Gráfico de Barras

categorias = ['A', 'B', 'C']
valores = [4, 7, 2]

plt.bar(categorias, valores)
plt.xlabel("Categorias")
plt.ylabel("Valores")
plt.title("Gráfico de Barras")
plt.show()

# Histogramas

dados = np.random.randn(1000)

plt.hist(dados, bins=20)
plt.xlabel("Dados")
plt.ylabel("Frequência")
plt.title("Histograma")
plt.show()

# Gráficos de Pizza (Pie Charts)

labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Gráfico de Pizza")
plt.show()

# Subplots

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
plt.subplot(2, 1, 1)
plt.plot(x, y1)
plt.title("Seno")
plt.subplot(2, 1, 2)
plt.plot(x, y2)
plt.title("Cosseno")
plt.tight_layout()
plt.show()

# Personalização de Gráficos

x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y, color='red', linestyle='dashed', linewidth=2, label='Seno de x')
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.title("Gráfico Personalizado")
plt.legend()
plt.show()

## Guardar os Gráficos em imagens

x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.title("Gráfico de Linha")
plt.savefig("grafico.png")