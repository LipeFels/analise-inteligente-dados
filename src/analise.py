import pandas as pd

dados = pd.read_csv("data/transacoes.csv")

print(dados)

print("\n--- RESUMO DAS TRANSACOES ---")

quantidade = len(dados)
media = dados["valor"].mean()
maior_valor = dados["valor"].max()
menor_valor = dados["valor"].min()

print("Quantidade de transacoes:", quantidade)
print("Valor medio:", media)
print("Maior valor:", maior_valor)
print("Menor valor:", menor_valor)

# Calcula o desvio padrao
desvio = dados["valor"].std()

# Define o limite para identificar anomalias
limite = media + (2 * desvio)

# Filtra as transacoes acima do limite
anomalias = dados[dados["valor"] > limite]

print("\n--- DETECCAO DE ANOMALIAS ---")
print("Desvio padrao:", desvio)
print("Limite calculado:", limite)
print("\nTransacoes fora do padrao:")
print(anomalias)

# Calcula os quartis
q1 = dados["valor"].quantile(0.25)
q3 = dados["valor"].quantile(0.75)

# Calcula o IQR
iqr = q3 - q1

# Define o limite superior usando IQR
limite_iqr = q3 + (1.5 * iqr)

# Filtra as transacoes acima do limite
anomalias_iqr = dados[dados["valor"] > limite_iqr]

print("Limite IQR:", limite_iqr)
print("\nTransacoes fora do padrao pelo IQR:")
print(anomalias_iqr)

print("\n--- ANALISE COM IQR ---")
print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)
