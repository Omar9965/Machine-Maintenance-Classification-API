from fastapi import FastAPI
from app.controllers.api import home_controller as api_home
from app.controllers.api import prediction_controller as api_prediction
from app.controllers.web import home_controller as web_home
from app.controllers.web import prediction_controller as web_prediction


def register_routes(app: FastAPI) -> None:
    """Register all API and web route controllers."""

    # --- API routes (versioned) ---
    app.include_router(api_home.router, prefix="/api/v1")
    app.include_router(api_prediction.router, prefix="/api/v1")

    # --- Web routes ---
    app.include_router(web_home.router)
    app.include_router(web_prediction.router)
