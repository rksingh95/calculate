from fastapi import APIRouter
from starlette import status

from app.calculate import Calculator
from app.models import CalcResponse
from app.validate import validate_input

router = APIRouter()


@router.get(
    path="/calculates/",
    name="Get calculations",
    description="Get the calculation from the base64 encoded string",
    tags=["calculator"],
    operation_id="get-base64-encoded-string",
    status_code=status.HTTP_200_OK,
    response_model=CalcResponse,
)
async def get_calculations(query: str):
    try:
        validated_params = validate_input(query)
        result = Calculator(validated_params)
    except (ValueError, IndexError, TypeError) as e:
        content = {"error": str(e)}
        return CalcResponse(result=0.0, error=True, message=content.get("error"))
    else:
        return CalcResponse(
            result=result.result, error=False, message="Result Calculated"
        )
