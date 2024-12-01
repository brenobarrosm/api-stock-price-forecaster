from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.controllers import app_routers

origins = ['*']

api = FastAPI(title='Stock Price Forecaster', openapi_version='3.0.2',
              version='0.0.1',
              openapi_url='/api/docs/openapi.json',
              docs_url='/api/docs',
              redoc_url='/api/redoc')


def create_app() -> FastAPI:
    api.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )
    app_routers.start_router(api)
    return api


app = create_app()
