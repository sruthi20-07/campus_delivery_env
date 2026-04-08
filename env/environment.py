import json
from .models import *

class DeliveryEnv:
    def __init__(self):
        # ✅ FIXED: properly load data
        with open("data/requests.json") as f:
            self.data = json.load(f)

        self.index = 0
        self.task = "easy_detect_fake"   # ✅ match YAML

    # ✅ Accept task name
    def reset(self, task="easy_detect_fake"):
        self.index = 0
        self.task = task
        return self._get_obs()

    def _get_obs(self):
        if self.index < len(self.data):
            req = Request(**self.data[self.index])
            return Observation(request=req)
        return Observation(request=None)

    def step(self, action: Action):
        current = Request(**self.data[self.index])

        # ✅ Task-based reward
        reward = self._reward(current, action)

        self.index += 1
        done = self.index >= len(self.data)

        return self._get_obs(), reward, done, {}

    def state(self):
        return {"index": self.index, "task": self.task}

    # ✅ MAIN FIX: 3 TASK GRADERS
    def _reward(self, req, action):

        # 🟢 EASY TASK
        if self.task == "easy_detect_fake":
            if req.is_real and action.decision == "accept":
                score = 1.0
            elif not req.is_real and action.decision == "reject":
                score = 1.0
            else:
                score = 0.0

            return Reward(score=score, reason="easy grading")

        # 🟡 MEDIUM TASK
        elif self.task == "medium_choose_action":
            score = 0.0

            if req.is_real and action.decision == "accept":
                score += 0.5
            elif not req.is_real and action.decision == "reject":
                score += 0.5

            if action.decision == "verify":
                score += 0.5

            score = min(score, 1.0)

            return Reward(score=score, reason="medium grading")

        # 🔴 HARD TASK
        elif self.task == "hard_edge_cases":
            score = 0.0

            if req.is_real and action.decision == "accept":
                score += 0.4
            elif not req.is_real and action.decision == "reject":
                score += 0.4

            if action.decision == "verify":
                score += 0.2

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

            # ✅ Normalize
            score = max(0.0, min(score, 1.0))

            return Reward(score=score, reason="hard grading")

        # ✅ Fallback (VERY IMPORTANT)
        return Reward(score=0.0, reason="unknown task")