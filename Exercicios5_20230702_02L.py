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

# importar a biblioteca pandas
import pandas as pd
import math

# Carregar dados do Excel
data = pd.read_excel('P_Data_Extract_From_World_Development_Indicators.xlsx', sheet_name='Data')
# Para simplificar, coloquei o ficheiro excel na mesma pasta que o código

# Seleccionar colunas e limpar dados

data = data[['Country Name', '1990 [YR1990]', '2000 [YR2000]']]
data = data[(data['Country Name'].notnull())&(data['1990 [YR1990]']!='..')&(data['2000 [YR2000]']!='..')]
data = data.reset_index(drop=True)

# 2. Ordenar dados (1 vez pelo default do Python, outra pelo Bubble Sort)

# Ordenar pelo deafult do Python
data_ordenada_1990_1=data.sort_values('1990 [YR1990]')

# Ordenar pelo Bubble sort

data_ordenada_1990_2=data.copy()

for linha in range(len(data_ordenada_1990_2)):
    for linha_2 in range(len(data_ordenada_1990_2)-linha-1):
        if data_ordenada_1990_2.iloc[linha_2]['1990 [YR1990]'] > data_ordenada_1990_2.iloc[linha_2+1]['1990 [YR1990]']:
            _ = data_ordenada_1990_2.iloc[linha_2].copy()
            data_ordenada_1990_2.iloc[linha_2] = data_ordenada_1990_2.loc[linha_2+1]
            data_ordenada_1990_2.loc[linha_2+1] = _

# Gráfico de Barras

categorias = data
valores = [4, 7, 2]

plt.bar(categorias, valores)
plt.xlabel("Categorias")
plt.ylabel("Valores")
plt.title("Gráfico de Barras")
plt.show()

