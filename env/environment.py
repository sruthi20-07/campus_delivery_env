import json
from .models import *

class DeliveryEnv:
    def __init__(self):
        with open("data/requests.json") as f:
            self.data = json.load(f)
        self.index = 0

    def reset(self):
        self.index = 0
        return self._get_obs()

    def _get_obs(self):
        if self.index < len(self.data):
            req = Request(**self.data[self.index])
            return Observation(request=req)
        return Observation(request=None)

    def step(self, action: Action):
        current = Request(**self.data[self.index])
        reward = self._reward(current, action)

        self.index += 1
        done = self.index >= len(self.data)

        return self._get_obs(), reward, done, {}

    def state(self):
        return {"index": self.index}

    def _reward(self, req, action):
        score = 0.0

        # 🟢 EASY: detect fake vs real
        if req.is_real and action.decision == "accept":
            score += 0.4
        elif not req.is_real and action.decision == "reject":
            score += 0.4

        # 🟡 MEDIUM: safer decisions
        if action.decision == "verify":
            score += 0.2

        # 🔴 HARD: fraud signals

        if not req.order_exists and action.decision == "reject":
            score += 0.3

        if not req.screenshot_uploaded and action.decision == "verify":
            score += 0.2

        if req.active_orders > 2 and action.decision == "reject":
            score += 0.2

        if req.cancel_after_pickup and action.decision == "reject":
            score += 0.3

        if req.device_trust_score > 0.8 and action.decision == "accept":
            score += 0.2

        if score == 0:
            score = -1.0

        return Reward(score=score, reason="advanced fraud detection reward")