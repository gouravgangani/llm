from fastapi import FastAPI, Query
from typing import List

app = FastAPI(title="CxFirst Mock APIs")

# -------------------------
# Root
# -------------------------
@app.get("/")
def root():
    return {"message": "API is live. Use /order_status?phone_number=9876543210"}

# -------------------------
# Order Status
# -------------------------
@app.get("/order_status")
def get_order_status(phone_number: str = Query(...)):
    return {
        "requested_phone": phone_number,
        "customer_name": "John Doe",
        "order_status": "In transit",
        "expected_delivery": "2025-09-28"
    }

# -------------------------
# Delivery Delay
# -------------------------
@app.get("/delivery_delay")
def delivery_delay(phone_number: str = Query(...)):
    return {
        "requested_phone": phone_number,
        "customer_name": "John Doe",
        "order_id": "ORD98765",
        "current_status": "Delayed",
        "delay_reason": "Bad weather conditions",
        "expected_delivery": "2025-10-02"
    }

# -------------------------
# Order Cancellation
# -------------------------
@app.get("/order_cancellation")
def order_cancellation(phone_number: str = Query(...)):
    return {
        "requested_phone": phone_number,
        "customer_name": "Jane Smith",
        "open_orders": [
            {"order_id": "ORD111", "items": ["Shoes", "T-Shirt"]},
            {"order_id": "ORD222", "items": ["Laptop Bag"]}
        ]
    }

@app.post("/cancel_order")
def cancel_order(customer_id: str, order_id: str, items: List[str]):
    return {
        "customer_id": customer_id,
        "order_id": order_id,
        "items_cancelled": items,
        "status": "success"
    }

# -------------------------
# Failed Payment Refund
# -------------------------
@app.get("/failed_payment_refund")
def failed_payment_refund(phone_number: str = Query(...)):
    return {
        "requested_phone": phone_number,
        "transaction_status": "Failed",
        "refund_status": "Pending"
    }

@app.post("/escalate_refund")
def escalate_refund(customer_id: str, order_id: str):
    return {
        "customer_id": customer_id,
        "order_id": order_id,
        "escalation_status": "raised"
    }

# -------------------------
# Refund TAT
# -------------------------
@app.get("/refund_tat")
def refund_tat(phone_number: str = Query(...)):
    return {
        "requested_phone": phone_number,
        "order_id": "ORD555",
        "refund_status": "Refund Initiated",
        "refund_policy_tat": "7 business days"
    }

# -------------------------
# Outside Flipcon Usecase
# -------------------------
@app.get("/outside_flipcon_usecase")
def outside_flipcon_usecase():
    return {
        "message": "No APIs configured for this intent."
    }
