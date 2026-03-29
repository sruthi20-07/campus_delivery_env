from pydantic import BaseModel
from typing import Optional

class Request(BaseModel):
    user_id: int
    order_id: Optional[int]
    is_real: bool
    user_history: int

    payment_status: str
    location_match: bool
    device_trust_score: float

    active_orders: int
    screenshot_uploaded: bool
    order_exists: bool
    order_age: int
    cancel_after_pickup: bool

class Observation(BaseModel):
    request: Optional[Request]

class Action(BaseModel):
    decision: str  # accept / reject / verify

class Reward(BaseModel):
    score: float
    reason: str