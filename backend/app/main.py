from fastapi import FastAPI

app = FastAPI(
    title="GKAI-OS API",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "GKAI-OS Backend Running"
    }