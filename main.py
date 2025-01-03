import json
import sys
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from decouple import config

from web import car
from web import user
from model.check_db import test_database_connection

logging.basicConfig(level="DEBUG") # TODO test with log_level="debug"


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://ui.cryptids.com",], # TODO test
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(car.router)
app.include_router(user.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    test_database_connection()
    url_list = json.dumps([{"name": route.name,
                            "url": f"http://127.0.0.1:8000{route.path}"}
                           for route in app.routes], indent=4)
    print("LIST OF DEFINED URL PATHS: ", url_list)

    import uvicorn
    uvicorn.run("main:app", reload=True, log_level='debug', access_log=True)
