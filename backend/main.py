from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return "Hello, this is the New Backend Project"

