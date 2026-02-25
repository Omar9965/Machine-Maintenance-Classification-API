from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from app.models.schemas import MachineData

router = APIRouter(tags=["Web"])

templates = Jinja2Templates(directory="app/views/templates")


@router.get("/predict")
async def predict_form(request: Request):
    """Render the prediction input form."""
    settings = request.app.state.settings
    return templates.TemplateResponse(
        "predict.html",
        {
            "request": request,
            "app_name": settings.APP_NAME,
        },
    )


@router.post("/predict")
async def predict_submit(
    request: Request,
    Type: str = Form(...),
    air_temperature: float = Form(..., alias="Air temperature [K]"),
    process_temperature: float = Form(..., alias="Process temperature [K]"),
    rotational_speed: float = Form(..., alias="Rotational speed [rpm]"),
    torque: float = Form(..., alias="Torque [Nm]"),
    tool_wear: float = Form(..., alias="Tool wear [min]"),
):
    """Process the prediction form and render the result."""
    settings = request.app.state.settings
    prediction_service = request.app.state.prediction_service

    try:
        data = MachineData(
            **{
                "Type": Type,
                "Air temperature [K]": air_temperature,
                "Process temperature [K]": process_temperature,
                "Rotational speed [rpm]": rotational_speed,
                "Torque [Nm]": torque,
                "Tool wear [min]": tool_wear,
            }
        )

        result = prediction_service.predict(data)

        return templates.TemplateResponse(
            "result.html",
            {
                "request": request,
                "app_name": settings.APP_NAME,
                "prediction": result.Failure_prediction,
                "probability": result.Failure_probability,
                "input_data": {
                    "Type": Type,
                    "Air Temperature": f"{air_temperature} K",
                    "Process Temperature": f"{process_temperature} K",
                    "Rotational Speed": f"{rotational_speed} rpm",
                    "Torque": f"{torque} Nm",
                    "Tool Wear": f"{tool_wear} min",
                },
            },
        )
    except Exception as e:
        return templates.TemplateResponse(
            "predict.html",
            {
                "request": request,
                "app_name": settings.APP_NAME,
                "error": str(e),
            },
        )
