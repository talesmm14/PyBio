import pynbiobsp as pnbio
from typing import Union
from fastapi import FastAPI

app = FastAPI()
pnbio.init()


@app.get("/get_biometry")
def read_root():
    return {"biometry": pnbio.capture(10000)}

def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("my_package.main:app", host="0.0.0.0", port=8000, reload=True)


