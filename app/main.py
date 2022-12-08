from fastapi import APIRouter, FastAPI
from starlette.responses import RedirectResponse

from app.api.v1.routes import get_calculations

app = FastAPI(
    title="Calculator APP",
    version="0.0.1",
    docs_url="/",
)

router = APIRouter()
router.include_router(get_calculations.router)


@app.get("/docs", name="Openapi UI", tags=["utils"])
async def docs_url():
    return RedirectResponse("/")


app.include_router(router, prefix="/v1")
