from fastapi import FastAPI
from sandbox import run

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/run")
async def sandbox_run(code_string: str):
    return run(code_string)
