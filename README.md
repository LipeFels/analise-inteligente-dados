#  Análise Inteligente de Dados

Projeto desenvolvido em Python para análise de uma base fictícia de transações, com foco em organização de dados, análise estatística e identificação de valores fora do padrão.

##  Objetivo

O objetivo do projeto é demonstrar como Python pode ser utilizado para automatizar etapas de análise de dados e identificar possíveis anomalias em uma base de transações.

> As transações utilizadas são fictícias e uma anomalia estatística não significa necessariamente fraude.

##  Tecnologias

- Python
- Pandas
- Git e GitHub

## 📂 Estrutura

```text
analise-inteligente-dados/
├── data/
│   └── transacoes.csv
├── src/
│   └── analise.py
├── requirements.txt
└── README.md
```

##  Análises realizadas

O programa:

- lê os dados de um arquivo CSV;
- calcula quantidade de transações;
- calcula média, maior e menor valor;
- calcula o desvio padrão;
- identifica valores fora do padrão usando média e desvio padrão;
- utiliza IQR (Intervalo Interquartil) como uma segunda abordagem para detecção de anomalias.

##  Comparação dos métodos

No conjunto de dados utilizado, o método baseado em média e desvio padrão gerou um limite de aproximadamente **R$ 8.222,93**, identificando apenas a transação de **R$ 9.500**.

Ao testar o IQR, o limite calculado foi **R$ 305,625**, permitindo identificar as transações de **R$ 7.800** e **R$ 9.500** como valores fora do padrão.

Esse teste demonstra como valores extremos podem influenciar a média e o desvio padrão e por que diferentes métodos estatísticos devem ser avaliados.

##  Como executar

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

Execute o projeto a partir da raiz:

```bash
python src/analise.py
```

##  Aprendizados

O projeto permitiu praticar:

- manipulação de dados com Pandas;
- leitura de arquivos CSV;
- filtros em DataFrames;
- média e desvio padrão;
- quartis e IQR;
- comparação entre diferentes métodos de identificação de anomalias;
- interpretação dos resultados, além da implementação do código.
