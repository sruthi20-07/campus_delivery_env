from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/reset")
def reset():
    return {"status": "ok"}

@app.post("/step")
def step(action: dict):
    return {"result": "ok"}

@app.get("/state")
def state():
    return {"state": "ok"}