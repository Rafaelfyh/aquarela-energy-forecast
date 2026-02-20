import pandas as pd


def load_raw_data(data_path="data"):
    consumo = pd.read_csv(f"{data_path}/consumo.csv")
    clientes = pd.read_csv(f"{data_path}/clientes.csv")
    clima = pd.read_csv(f"{data_path}/clima.csv")

    return consumo, clientes, clima

from ingestion import load_raw_data

if __name__ == "__main__":
    consumo, clientes, clima = load_raw_data()

    create_integrated_table(
        db_path="aquarela.db",
        consumo_df=consumo,
        clientes_df=clientes,
        clima_df=clima
    )

    create_feature_table()

