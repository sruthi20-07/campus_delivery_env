from env.environment import DeliveryEnv
from env.models import Action
import sys

def run_task():
    task_name = "campus_delivery"

    print(f"[START] task={task_name}", flush=True)

    env = DeliveryEnv()
    obs = env.reset()
    done = False

    total_score = 0
    step_num = 0

    while not done:
        step_num += 1

        # your rule-based agent (UNCHANGED)
        if obs.request and obs.request.user_history > 2:
            action = Action(decision="accept")
        elif obs.request and obs.request.order_id is None:
            action = Action(decision="reject")
        else:
            action = Action(decision="verify")

        obs, reward, done, _ = env.step(action)

        step_reward = reward.score if hasattr(reward, "score") else reward
        total_score += step_reward

        print(f"[STEP] step={step_num} reward={step_reward}", flush=True)

    final_score = total_score / step_num if step_num > 0 else 0

    print(f"[END] task={task_name} score={final_score} steps={step_num}", flush=True)


if __name__ == "__main__":
    run_task()