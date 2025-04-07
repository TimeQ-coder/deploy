from fastapi import FastAPI
from test01 import output

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
