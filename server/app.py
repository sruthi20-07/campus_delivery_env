from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(root_path="")

# Dummy state
state_data = {"step": 0}

class Action(BaseModel):
    decision: str

@app.get("/")
def home():
    return {"status": "ok"}

@app.post("/reset")
def reset():
    global state_data
    state_data = {"step": 0}
    return {"step": 0}   # SIMPLE JSON

@app.post("/step")
def step(action: Action):
    global state_data
    state_data["step"] += 1
    return {
        "observation": state_data,
        "reward": {"score": 0.5},
        "done": state_data["step"] > 5,
        "info": {}
    }

@app.get("/state")
def state():
    return state_data