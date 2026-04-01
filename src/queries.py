import pandas as pd

def run():

    # ler os dados tratados com seguranca
    try:
        df = pd.read_csv("data/dados_tratados.csv", sep=",", decimal=".")
    except FileNotFoundError:
        raise Exception("Arquivo dados_tratados.csv não encontrado")

    # converter para data
    df["data"] = pd.to_datetime(df["data"])

    # criando coluna ano
    df["ano"] = df["data"].dt.year

    # criando coluna mes
    df["mes"] = df["data"].dt.month

    # criando coluna de trimeste
    def trimestre(x):
        if x in [1, 2, 3]:
            return 'Q1'
        elif x in [4, 5, 6]:
            return 'Q2'
        elif x in [7, 8, 9]:
            return 'Q3'
        else:
            return 'Q4'

    df["trimestre"] = df["mes"].apply(trimestre)

    # convertendo para float
    df["valor"] = df["valor"].astype(float)

    # criando coluna de variação em relação ao mês anterior
    df = df.sort_values("data").reset_index(drop=True)
    df["variacao_mensal_absoluta"] = df["valor"].diff().round(2)

    # criando coluna de media movel de 3 meses
    df["media_movel_3"] = df["valor"].rolling(3).mean().round(2)

    # criando coluna de inflação acumulada por ano
    df["inflacao_acumulada_ano"] = df.groupby("ano")["valor"].transform(lambda x: ((1 + x/100).cumprod() - 1) * 100).round(2)

    # conferindo formatacão das colunas
    print(df.dtypes)

    # resetando index
    df = df.reset_index(drop=True)

    # salvar novo df
    df.to_csv("data/df_final.csv", sep=",", decimal=".", index=False)
    df.to_csv(r"G:\My Drive\analise-inflacao-brasil\automacao_mensal\df_final.csv", sep=",", decimal=".", index=False)

    print("Queries finalizado")

if __name__=="__main__":
    run()