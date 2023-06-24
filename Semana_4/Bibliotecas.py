import matplotlib
import scipy
import pandas as pd
import numpy as np

print("Matplotlib version:", matplotlib.__version__)
print("SciPy version:", scipy.__version__)
print("Pandas version:", pd.__version__)
print("NumPy version:", np.__version__)

import matplotlib.pyplot as plt

# Dados para o gráfico
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
 
# Criar e exibir o gráfico
plt.plot(x, y)
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.title("Exemplo de Gráfico com Matplotlib")
plt.show()

