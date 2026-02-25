import pandas as pd
from .feature_engineering import add_engineered_features
from app.models import MachineData

def predict_new(data: MachineData, preprocessor, model, best_threshold: float) -> dict:
    """
    Predicts machine failure using a trained model and preprocessor with a custom threshold.
    """

    # Convert Pydantic object to DataFrame
    df = pd.DataFrame([data.model_dump(by_alias=True)])
    # Add engineered features
    df = add_engineered_features(df)

    # Apply preprocessing pipeline
    X_processed = preprocessor.transform(df)

    # Predict probabilities
    y_prob = model.predict_proba(X_processed)[:, 1]
    failure_probability = float(y_prob[0])

    # Apply the tuned threshold
    y_pred = int(failure_probability >= best_threshold)

    return {
        "Failure_prediction": bool(y_pred),
        "Failure_probability": failure_probability
    }
