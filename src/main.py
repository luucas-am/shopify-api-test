from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from src.api.controller import router

app = FastAPI(title="Shopify API Test", description="", version="0.1.0")

cors_origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Home"], status_code=200, response_model=None)
async def redirect_to_docs():
    return RedirectResponse("/docs")


app.include_router(router)
