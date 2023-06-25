import matplotlib.pyplot as plt

# Dados de exemplo
dias = list(range(1, 31))
temperaturas = [22, 24, 23, 25, 24, 23, 22, 24, 25, 26, 25, 24, 23, 22, 23, 24, 25, 26, 25, 24, 23, 22, 24, 25, 24,
23, 24, 25, 24, 23]

# Criar um gráfico de linha
plt.plot(dias, temperaturas, color='blue', label='Temperatura')
plt.title('Variação da Temperatura ao Longo do Mês')
plt.xlabel('Dia')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.show()

# Criar um gráfico de barras
temperatura_maxima = max(temperaturas)
temperatura_minima = min(temperaturas)
plt.bar(['Máxima', 'Mínima'], [temperatura_maxima, temperatura_minima], color=['red', 'blue'])
plt.title('Temperatura Máxima e Mínima do Mês')
plt.ylabel('Temperatura (°C)')
plt.show()