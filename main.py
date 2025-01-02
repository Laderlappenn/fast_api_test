import json
import sys

from fastapi import FastAPI
from decouple import config

from web import car


# startup
pythonpath = config('PYTHONPATH')
if pythonpath:
    sys.path.append(pythonpath)  # now import main in tests works


app = FastAPI()
app.include_router(car.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    url_list = json.dumps([{"name": route.name,
                            "url": f"http://127.0.0.1:8000{route.path}"}
                           for route in app.routes], indent=4)
    print("LIST OF DEFINED URL PATHS: ", url_list)

    import uvicorn
    uvicorn.run("main:app", reload=True)
