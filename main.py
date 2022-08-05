import pynbiobsp as pnbio
from typing import Union
from fastapi import FastAPI

app = FastAPI()
pnbio.init()


@app.get("/get_biometry")
def read_root():
    return {"biometry": pnbio.capture(10000)}


