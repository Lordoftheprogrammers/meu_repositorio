""" Exercício
Para este exercício, utilize os dados do ficheiro CSV da Atividade Pedagógica 4 - parte 2 (CSV 
Ficheiro). Link para o ficheiro: https://moodle.eisnt.com/mod/resource/view.php?id=31890
1. Importar Dados: Escreva um script em Python para importar os dados para o seu 
programa. Isso pode envolver a leitura de um arquivo CSV, Excel, ou qualquer outro 
formato de sua escolha.
2. Aplicar Algoritmos de Ordenação: utilize dois algoritmos de ordenação diferentes 
para ordenar os produtos com base no número de vendas de forma ascendente.
3. Apresentar Resultados: Crie um gráfico de barras com o matplotlib para apresentar 
de forma ascendente os produtos com o seu total número de vendas.
4. PEP 8: Certifique-se de que o seu código adere às convenções de estilo descritas no 
PEP 8. Consulte o PEP 8 para mais detalhes.
5. Documentação e Comentários: Documente o seu código adequadamente e escreva 
comentários claros que expliquem o funcionamento do código.
"""

# 1. Importar dados

# importar a biblioteca pandas e a matplot lib para mais tarde fazer os gráficos
import pandas as pd
import matplotlib.pyplot as plt


# Carregar dados do Excel
data = pd.read_csv('AtividadePedagogica4_10793_02.csv')
# Para simplificar, coloquei o ficheiro excel na mesma pasta que o código

# Limpeza de dados e reindexação da dataframe (caso fosse necessário)

"""
data = data[(data['Coluna_1'].notnull())&(data['Coluna_1']!='..')]
data = data.reset_index(drop=True) 
"""

# 2. Agrupar os valores por categoria

data = data.groupby('produto')['quantidade_vendida'].sum()
data = data.reset_index()

print("Agregada: ",data)

# 3. Ordenar dados (1 vez pelo default do Python, outra pelo Bubble Sort)

# Ordenar pelo deafult do Python
data_ordenada_qtd_1=data.sort_values('quantidade_vendida')
print("Sort pré-definido no Python:", data_ordenada_qtd_1)
# Ordenar pelo Bubble sort

data_ordenada_qtd_2=data.copy()

for linha in range(len(data_ordenada_qtd_2)):
    print("linha: ", linha)
    for linha_2 in range(len(data_ordenada_qtd_2)-linha-1):
        print("linha_2: ", linha_2)
        if data_ordenada_qtd_2.iloc[linha_2]['quantidade_vendida'] > data_ordenada_qtd_2.iloc[linha_2+1]['quantidade_vendida']:
            print(data_ordenada_qtd_2)
            _ = data_ordenada_qtd_2.iloc[linha_2].copy()
            data_ordenada_qtd_2.iloc[linha_2] = data_ordenada_qtd_2.loc[linha_2+1]
            data_ordenada_qtd_2.loc[linha_2+1] = _
print(data_ordenada_qtd_2)

# Gráfico de Barras

categorias = data_ordenada_qtd_2['produto']
valores = data_ordenada_qtd_2['quantidade_vendida']

plt.bar(categorias, valores)
plt.xlabel("Categorias")
plt.ylabel("Valores")
plt.title("Gráfico de Barras")
plt.show()

# Gráfico de Barras

categorias = data_ordenada_qtd_1['produto']
valores = data_ordenada_qtd_1['quantidade_vendida']

plt.bar(categorias, valores)
plt.xlabel("Categorias")
plt.ylabel("Valores")
plt.title("Gráfico de Barras")
plt.show()