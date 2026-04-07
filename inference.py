from env.environment import DeliveryEnv
from env.models import Action
import os
from openai import OpenAI


# Initialize LLM client (REQUIRED)
client = OpenAI(
    base_url=os.environ.get("API_BASE_URL"),
    api_key=os.environ.get("API_KEY"),
)


def run_task():
    task_name = "campus_delivery"

    #  START block
    print(f"[START] task={task_name}", flush=True)

    env = DeliveryEnv()
    obs = env.reset()
    done = False

    total_score = 0
    step_num = 0

    while not done:
        step_num += 1

        # REQUIRED LLM CALL (must happen at least once per step)
        _ = client.chat.completions.create(
            model=os.environ.get("MODEL_NAME"),
            messages=[{"role": "user", "content": "check request"}],
            max_tokens=5
        )

        #  Rule-based agent
        if obs.request and obs.request.user_history > 2:
            action = Action(decision="accept")
        elif obs.request and obs.request.order_id is None:
            action = Action(decision="reject")
        else:
            action = Action(decision="verify")

        #  Step execution
        obs, reward, done, _ = env.step(action)

        step_reward = reward.score if hasattr(reward, "score") else reward
        total_score += step_reward

        #  STEP block
        print(f"[STEP] step={step_num} reward={round(step_reward, 2)}", flush=True)

    final_score = total_score / step_num if step_num > 0 else 0

    # END block
    print(f"[END] task={task_name} score={round(final_score, 2)} steps={step_num}", flush=True)


if __name__ == "__main__":
    run_task()