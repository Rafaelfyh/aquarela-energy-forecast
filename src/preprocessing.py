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
