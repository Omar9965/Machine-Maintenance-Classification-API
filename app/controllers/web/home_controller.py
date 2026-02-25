from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(tags=["Web"])

templates = Jinja2Templates(directory="app/views/templates")


@router.get("/")
async def home(request: Request):
    """Render the landing page."""
    settings = request.app.state.settings
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "app_name": settings.APP_NAME,
            "version": settings.VERSION,
        },
    )
