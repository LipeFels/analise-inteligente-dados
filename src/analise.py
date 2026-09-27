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
