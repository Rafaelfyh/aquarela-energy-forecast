import duckdb
import pandas as pd
import numpy as np
import joblib
import json
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error


def train_model(db_path="aquarela.db"):

    con = duckdb.connect(database=db_path, read_only=False)
    df = con.execute("SELECT * FROM consumo_features").fetchdf()
    con.close()

    df = df.dropna()
    df["date"] = pd.to_datetime(df["date"])

    features = ["lag_1", "rolling_mean_7", "temperature", "humidity"]
    target = "consumption_kwh"

    cutoff_date = "2023-06-01"
    train = df[df["date"] < cutoff_date]
    test = df[df["date"] >= cutoff_date]

    X_train = train[features]
    y_train = train[target]

    X_test = test[features]
    y_test = test[target]

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))

    metrics = {
        "MAE": float(mae),
        "RMSE": float(rmse)
    }

    joblib.dump(model, "models/model_v1.pkl")

    with open("models/metrics_v1.json", "w") as f:
        json.dump(metrics, f)

    return metrics


if __name__ == "__main__":
    metrics = train_model()
    print(metrics)

