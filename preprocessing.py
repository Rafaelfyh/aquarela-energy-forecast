import duckdb
import pandas as pd


def create_integrated_table(db_path, consumo_df, clientes_df, clima_df):
    con = duckdb.connect(database=db_path, read_only=False)

    con.register("consumo", consumo_df)
    con.register("clientes", clientes_df)
    con.register("clima", clima_df)

    query = """
    CREATE OR REPLACE TABLE consumo_integrado AS
    SELECT
        c.client_id,
        c.date,
        c.consumption_kwh,
        cli.region,
        cl.temperature,
        cl.humidity
    FROM consumo c
    JOIN clientes cli
        ON c.client_id = cli.client_id
    JOIN clima cl
        ON cli.region = cl.region
       AND c.date = cl.date
    """

    con.execute(query)
    con.close()


def create_feature_table(db_path="aquarela.db"):
    con = duckdb.connect(database=db_path, read_only=False)

    query_features = """
    CREATE OR REPLACE TABLE consumo_features AS
    SELECT *,
           LAG(consumption_kwh, 1) OVER (
               PARTITION BY client_id
               ORDER BY date
           ) AS lag_1,

           AVG(consumption_kwh) OVER (
               PARTITION BY client_id
               ORDER BY date
               ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
           ) AS rolling_mean_7

    FROM consumo_integrado
    """

    con.execute(query_features)
    con.close()


if __name__ == "__main__":
    # Ler CSVs
    consumo = pd.read_csv("data/consumo.csv")
    clientes = pd.read_csv("data/clientes.csv")
    clima = pd.read_csv("data/clima.csv")

    # Criar tabelas
    create_integrated_table(
        db_path="aquarela.db",
        consumo_df=consumo,
        clientes_df=clientes,
        clima_df=clima
    )

    create_feature_table()

    print("Tabelas criadas com sucesso.")
