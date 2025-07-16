from pydantic import BaseModel, Field
from typing import Literal

class MachineData(BaseModel):
    """
    Represents the data structure for machine data used in predictive maintenance classification.
    """
    type: Literal["M", "L", "H"] = Field(
        alias="Type",
        description="Product type: L, M, or H"
    )
    AirTemperature: float = Field(
        alias='Air temperature [K]',
        description="Generated using a random walk process normalized to a standard deviation of 2 K around 300 K",
        ge=295.3,
        le=305.4
    )
    ProcessTemperature: float = Field(
        alias='Process temperature [K]',
        description="Generated using a random walk process normalized to a standard deviation of 1 K, added to air temperature plus 10 K.",
        ge=305.7,
        le=313.8
    )
    RotationalSpeed: float = Field(
        alias='Rotational speed [rpm]',
        description="Calculated from a power of 2860 W, overlaid with a normally distributed noise",
        ge=1168.0,
        le=2886.0
    )
    Torque: float = Field(
        alias='Torque [Nm]',
        description="Torque values are normally distributed around 40 Nm with a SD = 10 Nm and no negative values",
        ge=3.8,
        le=76.6
    )
    ToolWear: float = Field(
        alias='Tool wear [min]',
        description="The quality variants H/M/L add 5/3/2 minutes of tool wear to the used tool in the process",
        ge=0.0,
        le=253.0
    )

    class Config:
        allow_population_by_alias = True
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "Type": "M",
                "Air temperature [K]": 300.0,
                "Process temperature [K]": 310.0,
                "Rotational speed [rpm]": 1500.0,
                "Torque [Nm]": 40.0,
                "Tool wear [min]": 10.0
            }
        }