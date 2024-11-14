import pandas as pd

url = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/refs/heads/master/aula1.2/ratings.csv"

try:
    df = pd.read_csv(url)
    print(df)

except Exception as e:
    print(f"Erro: {e}")
