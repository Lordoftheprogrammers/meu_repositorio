import pandas as pd

# Carregar dados do Excel
data = pd.read_excel('P_Data_Extract_From_World_Development_Indicators.xlsx', sheet_name='Data')

# Selecionar as colunas de interesse (País, Ano e Consumo de Energia)
data = data[['Country Name', '1990 [YR1990]', '2000 [YR2000]']]

# Filtrar os dados para Portugal (para o Brasil não temos dados)
data_portugal = data[data['Country Name'] == 'Portugal']

# Calcular a variação percentual
def calcular_variacao_percentual(consumo_inicial, consumo_final):
    return (consumo_final - consumo_inicial) / consumo_inicial * 100

# Extrair os valores para o Brasil
consumo_1990 = data_portugal['1990 [YR1990]'].values[0]
consumo_2000 = data_portugal['2000 [YR2000]'].values[0]

# Calcular e imprimir a variação percentual
variacao_percentual = calcular_variacao_percentual(consumo_1990, consumo_2000)
print("A variação de consumo de energia per capita (kWh), em Portugal, entre 1990 e 2000, foi de " + str(round(variacao_percentual,2))+"%. Um aumento muito significativo.")