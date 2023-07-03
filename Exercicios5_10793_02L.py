""" Exercício 5 - 20230702 - 10793_02L

Para este exercício, utilize os dados do ficheiro CSV da Atividade Pedagógica 4 - parte 2 (CSV 
Ficheiro). Link para o ficheiro: https://moodle.eisnt.com/mod/resource/view.php?id=31890

1. Importar Dados: Escreva um script em Python para importar os dados para o seu programa. Isso pode envolver a leitura de um arquivo CSV, Excel, ou qualquer outro formato de sua escolha.
2. Aplicar Algoritmos de Ordenação: utilize dois algoritmos de ordenação diferentes para ordenar os produtos com base no número de vendas de forma ascendente.
3. Apresentar Resultados: Crie um gráfico de barras com o matplotlib para apresentar de forma ascendente os produtos com o seu total número de vendas.
4. PEP 8: Certifique-se de que o seu código adere às convenções de estilo descritas no PEP 8. Consulte o PEP 8 para mais detalhes.
5. Documentação e Comentários: Documente o seu código adequadamente e escreva comentários claros que expliquem o funcionamento do código.

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

# 2. Agrupar os valores por produto, somando a quantidade vendida, reindexando a frame.

data = data.groupby('produto')['quantidade_vendida'].sum()
data = data.reset_index()

# 3. Ordenar dados (1 vez pelo default do Python, outra pelo Bubble Sort)

# Ordenar com o Bubble sort

def bubble_sort(dataframe, coluna):
    
    """# A Função bubble_sort:
       ## 1. Recebe dois parâmetros:
       ### - Uma dataframe: basta por o nome da variável quando invocada
       ### - Uma coluna: deve ser o nome da coluna entre plicas
       ## 2. Compara pares de elementos.
       ## 3. Caso o elemento seguinte seja menor, troca os valores da linha de um pela do outro.
       ## 4. Assim, sucessivamente, até ter colocado os valores em ordem ascendente"""
        
    for linha in range(len(dataframe)):
        for linha_2 in range(len(dataframe)-linha-1):
            if dataframe.iloc[linha_2][coluna] > dataframe.iloc[linha_2+1][coluna]:
                temp = dataframe.iloc[linha_2]
                dataframe.iloc[linha_2] = dataframe.loc[linha_2+1]
                dataframe.loc[linha_2+1] = temp
    return dataframe
            
# Ordenar com o Insertion Sort

def insertion_sort(dataframe, coluna):

    """# A Função insertion_sort:
       ## 1. Recebe dois parâmetros:
       ### - Uma dataframe: basta por o nome da variável quando invocada
       ### - Uma coluna: deve ser o nome da coluna entre plicas
       ## 2. Segmenta a dataframe inicial.
       ## 3. Compara os elementos dentro de cada segmento.
       ## 4. Assim, sucessivamente, até ter colocado os valores em ordem ascendente"""
       
    for i in range(1, len(dataframe)):
        temp = dataframe.iloc[i][coluna]
        j = i - 1
        while j >= 0 and dataframe.iloc[j][coluna] > temp:
            dataframe.iloc[j + 1] = dataframe.iloc[j]
            j -= 1
        dataframe.iloc[j + 1][coluna] = temp
    return dataframe

# Gráfico de Barras para dataframes

def Mostrar_df_em_grafico(titulo, dataframe, categoria, valor):

    """# A Função Mostrar_df_em_grafico:
       ## 1. Recebe quatro parâmetros:
       ### - Um título, para a janela do gráfico
       ### - Uma dataframe: basta por o nome da variável quando invocada
       ### - Uma categoria: o nome da coluna entre plicas, para servir de legenda ao gráfico
       ### - Valores: o nome da coluna entre plicas, para determinar a altura das barras
       ## 2. Esta função funciona como um procedimento, executando uma ação, sem devolver qualquer valor."""

    categorias = dataframe[categoria]
    valores = dataframe[valor]

    plt.bar(categorias, valores)
    plt.xlabel("Categorias")
    plt.ylabel("Valores")
    plt.title(titulo)
    plt.show()

# Ordenar de várias maneiras, mostrando uma mensagem e um gráfico para cada uma

Mostrar_df_em_grafico("Timsort", data.sort_values('quantidade_vendida'),'produto','quantidade_vendida')
Mostrar_df_em_grafico("Bubble sort", bubble_sort(data,'quantidade_vendida'),'produto','quantidade_vendida')
Mostrar_df_em_grafico("Insertion sort", insertion_sort(data,'quantidade_vendida'),'produto','quantidade_vendida')
