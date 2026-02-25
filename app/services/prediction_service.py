import pandas as pd
from app.models.schemas import MachineData, PredictionResponse
from app.models.ml_models import ModelManager
from app.services.feature_engineering import add_engineered_features
from app.core.logging import get_logger

logger = get_logger(__name__)


class PredictionService:
    """
    Orchestrates the full prediction pipeline.

    Decoupled from HTTP — can be used from API controllers,
    web controllers, CLI tools, or scheduled jobs.
    """

    def __init__(self, model_manager: ModelManager):
        self._model_manager = model_manager

    def predict(self, data: MachineData) -> PredictionResponse:
        """
        Run a prediction for the given machine data.

        Pipeline: schema → DataFrame → feature engineering →
                  preprocessing → model inference → threshold → response
        """
        logger.info("Starting prediction for input: Type=%s", data.type)

        # 1. Convert Pydantic model to DataFrame (using aliases for column names)
        df = pd.DataFrame([data.model_dump(by_alias=True)])

        # 2. Add engineered features
        df = add_engineered_features(df)

        # 3. Apply preprocessing pipeline
        X_processed = self._model_manager.preprocessor.transform(df)

        # 4. Get failure probability
        y_prob = self._model_manager.model.predict_proba(X_processed)[:, 1]
        failure_probability = float(y_prob[0])

        # 5. Apply tuned threshold
        failure_prediction = failure_probability >= self._model_manager.threshold

        logger.info(
            "Prediction complete: probability=%.4f, prediction=%s",
            failure_probability,
            failure_prediction,
        )

        return PredictionResponse(
            Failure_prediction=bool(failure_prediction),
            Failure_probability=failure_probability,
        )
