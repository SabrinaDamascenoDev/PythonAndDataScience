import pandas as pd

print(pd.__version__)
arquivo = 'arquivos/arquivos/salarios.csv'
df = pd.read_csv(arquivo)

print(df.head())

print(df['Position Title'].value_counts())
