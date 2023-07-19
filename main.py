from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sandbox import run


class Code(BaseModel):
    code_string: str


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/run")
async def sandbox_run(code: Code):
    code = jsonable_encoder(code)
    code_string = code.get("code_string")
    return run(code_string)
