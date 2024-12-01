from fastapi import FastAPI

from app.controllers import stocks_controller


class AppRouters:
    def __init__(self):
        self.app = None
        self.api_prefix = '/api/v1'

    def start_router(self, app: FastAPI):
        self.app = app
        self.__include_routes()

    def __include_routes(self):
        self.app.include_router(router=stocks_controller.router, prefix=self.api_prefix, tags=['ProductMatching'])


app_routers = AppRouters()
