import requests
import pandas as pd

def run():
    # url da api
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json"

    # requisitando os dados e guardando numa variavel
    response = requests.get(url)
    # valida se a requisição deu certo
    if response.status_code != 200:
        raise Exception(f"Erro na API: {response.status_code}")

    data = response.json()

    # transformando em um df
    df = pd.DataFrame(data)

    # salvando dados brutos
    df.to_csv("data/dados_brutos.csv", sep=",", decimal=".", index=False)

    print("Extract Finalizado")

if __name__ == "__main__":
    run()