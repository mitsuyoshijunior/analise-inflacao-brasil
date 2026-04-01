import pandas as pd

def run():

    # ler os dados brutos com segurança
    try:
        df = pd.read_csv("data/dados_brutos.csv", sep=",", decimal=".")
    except FileNotFoundError:
        raise Exception("Arquivo dados_brutos.csv não encontrado")

    # Imprimindo quantidade de nulos e duplicatas
    nulos = df.isnull().sum().sum()
    duplicatas = df.duplicated().sum()

    print(f"Removendo {nulos} valores nulos e {duplicatas} duplicatas")

    # verificando se há valroes nulos e tratando-os
    def valores_nulos(df):
        if df.isnull().values.any():
            df = df.dropna()

        return df

    df = valores_nulos(df)

    # verificando se há duplicatas e tratando-as
    def remover_duplicatas(df):
        if df.duplicated().any():
            df = df.drop_duplicates()

        return df

    df = remover_duplicatas(df)

    # converter coluna de data
    df["data"] = pd.to_datetime(df["data"], format="%d/%m/%Y")

    # converter coluna de valor para float
    df["valor"] = df["valor"].astype(float)

    # ordenando valor por data
    df = df.sort_values("data")

    # resetando o indice
    df = df.reset_index(drop=True)

    # salvar dados tratados
    df.to_csv("data/dados_tratados.csv", sep=",", decimal=".", index=False)

    print("Transform finalizado")

if __name__ == "__main__":
    run()