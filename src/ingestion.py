import pandas as pd


def load_raw_data(data_path="data"):
    consumo = pd.read_csv(f"{data_path}/consumo.csv")
    clientes = pd.read_csv(f"{data_path}/clientes.csv")
    clima = pd.read_csv(f"{data_path}/clima.csv")

    return consumo, clientes, clima


