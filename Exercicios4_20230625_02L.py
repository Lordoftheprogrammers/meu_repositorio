# Exercício dado para trabalho adicional na aula de 19/06/2023

# importar a biblioteca pandas
import pandas as pd

# Carregar dados do Excel
data = pd.read_excel('P_Data_Extract_From_World_Development_Indicators.xlsx', sheet_name='Data')
# Para simplificar, coloquei o ficheiro excel na mesma pasta que o código

# Selecionar as colunas de interesse (País, Ano e Consumo de Energia)
data = data[['Country Name', '1990 [YR1990]', '2000 [YR2000]']]
# Aqui fui buscar as 3 únicas colunas que me interessavam para o exercício

# Filtrar os dados para Portugal (para o Brasil não temos dados)
data_portugal = data[data['Country Name'] == 'Portugal']
# O enunciado falava em Brasil e Portugal, verifiquei que só lá estava Portugal

# Calcular a variação percentual
def calcular_variacao_percentual(consumo_inicial, consumo_final):
    return (consumo_final - consumo_inicial) / consumo_inicial * 100
# Esta função calcula qualquer variação percentual, seja qual for a fonte de dados. Não é exclusiva para este exercício.

# Extrair os valores para o Brasil
consumo_1990 = data_portugal['1990 [YR1990]'].values[0]
consumo_2000 = data_portugal['2000 [YR2000]'].values[0]
# Vamos buscar os primeiros (e neste caso únicos) valores das colunas '1990 [YR1990]' e '2000 [YR2000]'

# Calcular e imprimir a variação percentual
variacao_percentual = calcular_variacao_percentual(consumo_1990, consumo_2000)
# Chamámos a função

# Aqui coloco uma ideia adicional, para que haja um comentário dependente do valor que for calculado

if variacao_percentual > 25:
    comentario = "Um aumento muito significativo."
else:
    comentario = "Um aumento expectável, dada a evolução típica de consumo de um país desenvolvido nessa década."

# Finalmente, imprimimos o resultado e comentamos.

print("A variação de consumo de energia per capita (kWh), em Portugal, entre 1990 e 2000, foi de " + str(round(variacao_percentual,2))+"%. " + comentario)