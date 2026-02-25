from fastapi import APIRouter, Request, HTTPException
from app.models.schemas import MachineData, PredictionResponse

router = APIRouter(tags=["Predictions"])


@router.post("/predict/xgboost", response_model=PredictionResponse)
async def predict_xgboost(data: MachineData, request: Request) -> PredictionResponse:
    """
    Predict machine failure using the XGBoost model.

    Accepts sensor data, applies feature engineering and preprocessing,
    then returns the failure prediction and probability.
    """
    try:
        prediction_service = request.app.state.prediction_service
        return prediction_service.predict(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
