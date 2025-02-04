import os
from fastapi import FastAPI
import uvicorn
import yaml
from app.api.main import router as api_router
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

# from app.core.db import init_db
from app.core.config import settings

# from init import init
import logging

app = FastAPI()

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(
        "__main__:app",
        host="localhost",
        port=settings.SERVER_PORT,
        reload=(settings.ENVIRONMENT == "local"),
        workers=4,
    )

logger = logging.getLogger("uvicorn.error")


class ExceptionHandlingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        try:
            # Call the next middleware or endpoint
            response = await call_next(request)
            return response
        except Exception as e:
            # Log the error
            logger.error(f"Exception: {str(e)}")
            # Return a 500 response
            return JSONResponse(
                status_code=500, content={"detail": "Internal Server Error"}
            )


# Add the custom middleware
app.add_middleware(ExceptionHandlingMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8080",
        "http://localhost:8081",
        "http://127.0.0.1:8081",
        "*",
    ],  # Allows CORS from this origin
    allow_credentials=True,  # Allows cookies and credentials
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all HTTP headers
)

# TODO: выбрать какое то другое место для этого, но пока пусть тут полежит
# мб создать файл для эксепшн хедлеров
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"status": "error", "detail": exc.errors()},
    )


# @app.on_event("startup")
# async def on_startup():
#     await init()
