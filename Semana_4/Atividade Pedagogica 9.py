# Importar Excel ou CSV

import pandas as pd

def ler_dados_excel(caminho_ficheiro):
 # Ler dados do ficheiro Excel e carregar num DataFrame
 return pd.read_excel(caminho_ficheiro)

def calcular_media_notas(dataframe, coluna_notas):
 # Calcular a média das notas de cada aluno
 return dataframe[coluna_notas].mean()

def encontrar_aluno_nota_mais_alta(dataframe, coluna_prova):
 # Encontrar o aluno com a nota mais alta em uma prova específica
 return dataframe.loc[dataframe[coluna_prova].idxmax()]

def calcular_media_por_prova(dataframe, colunas_provas):
 # Calcular a média de notas para cada prova
 return dataframe[colunas_provas].mean()

# Exemplo de uso das funções
dados = ler_dados_excel('C:/Users/andre/OneDrive/Desktop/Formação/Python/Repo/meu_repositorio/Semana_4/AtividadePedagogica4_10793_02.xlsx')
print(dados)
media_notas = calcular_media_notas(dados, ["Prova 1", "Prova 2","Prova 3"])
aluno_nota_mais_alta = encontrar_aluno_nota_mais_alta(dados, "Prova 1")
media_por_prova = calcular_media_por_prova(dados, ["Prova 1", "Prova 2", "Prova 3"])

print(media_notas)
print(aluno_nota_mais_alta)
print(media_por_prova)