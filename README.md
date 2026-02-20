# aquarela-energy-forecast
Solução preditiva para estimar consumo energético residencial, desenvolvida com Python, DuckDB e SQL, incluindo engenharia de features, validação temporal e pipeline estruturado seguindo boas práticas de MLOps.

AQUARELA-ENERGY-FORECAST
│
├── data/                  # Dados brutos
│   ├── consumo.csv
│   ├── clima.csv
│   ├── clientes.csv
│
├── models/                # Modelos versionados
│   ├── model_v1.pkl
│   ├── metrics_v1.json
│
├── src/
│   ├── ingestion.py       # <-- Ingestão
│   ├── preprocessing.py
│   ├── train.py
│
├── notebooks/
│   ├── dashboard.ipynb
│
├── aquarela.db
├── requirements.txt
├── README.md
