import requests
from google.adk.agents import Agent
from google.adk.tools import google_search, AgentTool

def get_store_price(product_name: str):
    """Fetches the current live price for a product from the primary retail database."""
    # Simulated API call logic
    return {
        "product": product_name,
        "current_price": "$899.00",
        "currency": "USD",
        "in_stock": True
    }

search_specialist = Agent(
    name="search_specialist",
    model="gemini-2.0-flash",
    instruction="You are a search expert. Find recent price trends, coupons, and product release news.",
    tools=[google_search]
)

root_agent = Agent(
    name="smart_shopper_advisor",
    model="gemini-2.5-flash",
    description="Decides if now is the best time to buy a product.",
    instruction="""
    You are a professional Shopping Strategist.
    1. Use 'get_store_price' to find the current live price.
    2. Use 'web_search_tool' to get market context (sales, new models, or coupons).
    3. Synthesize the data and give a clear 'Buy Now' or 'Wait' recommendation.
    """,
    tools=[
        get_store_price, 
        AgentTool(agent=search_specialist)
    ]
)