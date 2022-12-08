from pydantic import BaseModel


class CalcResponse(BaseModel):
    """
    Claculator response model for the get API call
    """

    error: bool
    result: float
    message: str
