from pydantic import BaseModel


class PlannerDecision(BaseModel):
    tool: str
    input: str