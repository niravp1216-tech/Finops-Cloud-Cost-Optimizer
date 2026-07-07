"""
FinOps Cloud Cost Optimizer - Backend Entry Point
Minimal FastAPI scaffold. Wire in real collectors/services as you build them out.
"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="FinOps Cloud Cost Optimizer", version="0.1.0")


class CostSummary(BaseModel):
    provider: str
    total_cost: float
    currency: str = "USD"
    period: str


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/api/v1/costs/summary", response_model=list[CostSummary])
def get_cost_summary():
    """
    Placeholder endpoint. Replace with real aggregation from
    collectors/aws, collectors/azure, collectors/gcp.
    """
    return [
        CostSummary(provider="aws", total_cost=0.0, period="current_month"),
        CostSummary(provider="azure", total_cost=0.0, period="current_month"),
        CostSummary(provider="gcp", total_cost=0.0, period="current_month"),
    ]


@app.get("/api/v1/recommendations")
def get_recommendations():
    """
    Placeholder endpoint. Replace with output from the recommendation engine
    (idle resources, rightsizing, storage cleanup, RI/Savings Plan gaps).
    """
    return {"recommendations": []}
