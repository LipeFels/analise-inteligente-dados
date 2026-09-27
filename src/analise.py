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
