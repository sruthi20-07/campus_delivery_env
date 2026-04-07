from fastapi import FastAPI
from env.environment import DeliveryEnv
from env.models import Action

app = FastAPI()

env = DeliveryEnv()

@app.get("/")
def home():
    return {"status": "ok"}

@app.post("/reset")
def reset():
    obs = env.reset()
    return obs.model_dump()   # ✅ IMPORTANT FIX

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