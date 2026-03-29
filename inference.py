from env.environment import DeliveryEnv
from env.models import Action

env = DeliveryEnv()

obs = env.reset()
done = False
total_score = 0

while not done:
    # simple rule-based agent
    if obs.request and obs.request.user_history > 2:
        action = Action(decision="accept")
    elif obs.request and obs.request.order_id is None:
        action = Action(decision="reject")
    else:
        action = Action(decision="verify")

    obs, reward, done, _ = env.step(action)
    total_score += reward.score

print("Total Score:", total_score)