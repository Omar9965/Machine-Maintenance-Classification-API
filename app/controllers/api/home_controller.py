from fastapi import APIRouter, Request
from app.models.schemas import HealthResponse

router = APIRouter(tags=["General"])


@router.get("/", response_model=HealthResponse)
async def health_check(request: Request) -> HealthResponse:
    """Health check endpoint — confirms the API is live."""
    settings = request.app.state.settings
    return HealthResponse(
        message=f"Welcome to {settings.APP_NAME}",
        version=settings.VERSION,
    )
