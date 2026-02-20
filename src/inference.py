import joblib
import pandas as pd


def load_model(model_path="models/model_v1.pkl"):
    return joblib.load(model_path)


def predict(model, input_df):
    features = ["lag_1", "rolling_mean_7", "temperature", "humidity"]
    return model.predict(input_df[features])


if __name__ == "__main__":
    model = load_model()

    example_data = pd.DataFrame({
        "lag_1": [120],
        "rolling_mean_7": [118],
        "temperature": [25],
        "humidity": [60]
    })

    prediction = predict(model, example_data)
    print("Predicted consumption:", prediction)

