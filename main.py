from fastapi import FastAPI, Query

app = FastAPI(title="Mock CxFirst Public APIs")

@app.get("/")
def root():
    return {"message": "Mock API is live. Try /order_status?phone_number=9800000000"}

@app.get("/order_status")
def get_order_status(phone_number: str = Query(..., description="Customer phone number")):
    # Always return dummy response
    return {
        "requested_phone": phone_number,
        "customer_name": "John Doe",
        "order_status": "In transit",
        "expected_delivery": "2025-09-28",
        "items": [
            {"item_id": "ITEM123", "name": "Blue T-Shirt", "qty": 1},
            {"item_id": "ITEM456", "name": "Running Shoes", "qty": 1}
        ]
    }
