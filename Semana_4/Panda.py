# Trabalhar com a biblioteca Panda

import pandas as pd

# Criação de Séries

lista1 =[1,2,3,4,5]
s1 = pd.Series(lista1)

lista2 =[1,2,3,4,5]
s2= pd.Series(lista2)

# Cálculo com séries

print(s1*s2)

# Criando e Manipulando DataFrames (lista de listas)

dados = {
 'Nome': ['João', 'Maria', 'Ana'],
 'Idade': [25, 32, 18],
 'Cidade': ['Lisboa', 'Porto', 'Coimbra']
}

df = pd.DataFrame(dados)
print(df)

# Aceder coluna por nome
nomes = df['Nome']
print(nomes)

# Aceder linhas por índice (loc)
linha = df.loc[0]
print(linha)

# Filtrar por idade maior que 20
adultos = df[df['Idade'] > 20]
print(adultos)

# Renomear colunas
#df = df.rename(columns={'Nome': 'Nome Completo'})
df = df['Nome Completo']
print(df)

# Preencher valores nulos
df = df.fillna(0)

# Agrupar dados
agrupado_contagem = df.groupby('Cidade').count()
agrupado_soma = df.groupby('Cidade').sum('Idade')
print(agrupado_contagem)
print(agrupado_soma)