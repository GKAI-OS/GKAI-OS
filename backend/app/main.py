from fastapi import FastAPI
from app.api.brands import router as brand_router

app = FastAPI(
    title="GKAI-OS API",
    version="1.0"
)


@app.get("/")
def home():
    return {"message": "GKAI-OS Backend Running"}


app.include_router(brand_router)