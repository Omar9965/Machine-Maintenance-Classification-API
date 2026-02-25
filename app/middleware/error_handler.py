from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.core.logging import get_logger

logger = get_logger(__name__)


async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    """Handle HTTP exceptions with consistent JSON responses."""
    logger.warning(
        "HTTP %d on %s: %s", exc.status_code, request.url.path, exc.detail
    )
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": str(exc.detail), "status_code": exc.status_code},
    )


async def validation_exception_handler(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    """Handle Pydantic validation errors with detailed error info."""
    logger.warning("Validation error on %s: %s", request.url.path, exc.errors())
    return JSONResponse(
        status_code=422,
        content={
            "detail": "Validation error",
            "status_code": 422,
            "errors": exc.errors(),
        },
    )


async def generic_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """Catch-all handler for unhandled exceptions."""
    logger.error(
        "Unhandled exception on %s: %s", request.url.path, str(exc), exc_info=True
    )
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error", "status_code": 500},
    )
