from pydantic import BaseModel, Field
from typing import Literal


class MachineData(BaseModel):
    """
    Input schema for machine sensor data used in predictive maintenance.
    Field aliases match the original dataset column names for API compatibility.
    """

    type: Literal["M", "L", "H"] = Field(
        alias="Type",
        description="Product quality type: L (Low), M (Medium), or H (High)",
    )
    air_temperature: float = Field(
        alias="Air temperature [K]",
        description="Air temperature in Kelvin, normalized around 300 K",
        ge=295.3,
        le=305.4,
    )
    process_temperature: float = Field(
        alias="Process temperature [K]",
        description="Process temperature in Kelvin, air temp + ~10 K",
        ge=305.7,
        le=313.8,
    )
    rotational_speed: float = Field(
        alias="Rotational speed [rpm]",
        description="Rotational speed in RPM, derived from 2860 W power",
        ge=1168.0,
        le=2886.0,
    )
    torque: float = Field(
        alias="Torque [Nm]",
        description="Torque in Nm, normally distributed around 40 Nm",
        ge=3.8,
        le=76.6,
    )
    tool_wear: float = Field(
        alias="Tool wear [min]",
        description="Tool wear in minutes, varies by quality type",
        ge=0.0,
        le=253.0,
    )

    model_config = {
        "populate_by_name": True,
        "json_schema_extra": {
            "example": {
                "Type": "M",
                "Air temperature [K]": 300.0,
                "Process temperature [K]": 310.0,
                "Rotational speed [rpm]": 1500.0,
                "Torque [Nm]": 40.0,
                "Tool wear [min]": 10.0,
            }
        },
    }


class PredictionResponse(BaseModel):
    """Response schema for prediction results."""

    Failure_prediction: bool = Field(
        description="Whether the model predicts a machine failure"
    )
    Failure_probability: float = Field(
        description="Probability of machine failure (0.0 to 1.0)"
    )


class HealthResponse(BaseModel):
    """Response schema for health check endpoint."""

    message: str
    version: str


class ErrorResponse(BaseModel):
    """Standard error response schema."""

    detail: str
    status_code: int
