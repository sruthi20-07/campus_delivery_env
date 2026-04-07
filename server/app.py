from fastapi import FastAPI
from env.environment import DeliveryEnv
from env.models import Action

# ✅ IMPORTANT: root_path fix for HF routing
app = FastAPI(root_path="")

env = DeliveryEnv()

@app.get("/")
def home():
    return {"message": "Campus Delivery Env Running"}

@app.post("/reset")
def reset():
    obs = env.reset()
    return {
        "observation": obs.model_dump()
    }

@app.post("/step")
def step(action: dict):
    act = Action(**action)
    obs, reward, done, info = env.step(act)
    return {
        "observation": obs.model_dump(),
        "reward": reward.model_dump(),
        "done": done,
        "info": info
    }

@app.get("/state")
def state():
    return env.state()