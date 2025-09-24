from fastapi import FastAPI, Query
import requests

app = FastAPI(title="CxFirst Public APIs")

@app.get("/order_status")
def get_order_status(phone_number: str = Query(..., description="Customer phone number")):
    """
    Order status flow → Get customer profile + order details
    """
    # Forward request to your backend (or mock it if backend not ready)
    url = f"https://cxfirst.in:8081/public/get_customer_and_tickets_details?phone_number={phone_number}"
    response = requests.get(url)
    return {
        "requested_phone": phone_number,
        "backend_response": response.json() if response.ok else {"error": "backend not reachable"}
    }
