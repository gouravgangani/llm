from fastapi import FastAPI, Query

app = FastAPI(title="CxFirst Mock APIs")

# -------------------------
# Order Status (already done)
# -------------------------
@app.get("/order_status")
def get_order_status(phone_number: str = Query(..., description="Customer phone number")):
    return {
        "intent": "order_status",
        "requested_phone": phone_number,
        "customer_profile": {
            "customer_id": "CUST123",
            "name": "John Doe"
        },
        "order_details": {
            "order_id": "ORD12345",
            "status": "Shipped",
            "expected_delivery": "2025-09-30"
        }
    }

# -------------------------
# Delivery Delay
# -------------------------
@app.get("/delivery_delay")
def delivery_delay(phone_number: str = Query(...)):
    return {
        "intent": "delivery_delay",
        "customer_profile": {"customer_id": "CUST123", "name": "John Doe"},
        "delivery_details": {"order_id": "ORD98765", "current_status": "Delayed"},
        "delay_reason": "Bad weather conditions"
    }

# -------------------------
# Order Cancellation
# -------------------------
@app.get("/order_cancellation")
def order_cancellation(phone_number: str = Query(...)):
    return {
        "intent": "order_cancellation",
        "customer_profile": {"customer_id": "CUST456", "name": "Jane Smith"},
        "open_orders": [
            {"order_id": "ORD111", "items": ["Shoes", "T-Shirt"]},
            {"order_id": "ORD222", "items": ["Laptop Bag"]}
        ]
    }

@app.post("/cancel_order")
def cancel_order(customer_id: str, order_id: str, items: list[str]):
    return {
        "intent": "order_cancellation",
        "action": "cancel_order",
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
        "intent": "failed_payment_refund",
        "transaction_check": {"txn_id": "TXN123", "status": "Failed"},
        "refund_status": {"refund_id": "R123", "status": "Pending"}
    }

@app.post("/escalate_refund")
def escalate_refund(order_id: str, customer_id: str):
    return {
        "intent": "failed_payment_refund",
        "action": "escalate_refund",
        "order_id": order_id,
        "customer_id": customer_id,
        "escalation_status": "raised"
    }

# -------------------------
# Refund TAT
# -------------------------
@app.get("/refund_tat")
def refund_tat(phone_number: str = Query(...)):
    return {
        "intent": "refund_tat",
        "order_details": {"order_id": "ORD555", "status": "Refund Initiated"},
        "refund_policy_tat": "7 business days"
    }

# -------------------------
# Outside Flipcon Use Case
# -------------------------
@app.get("/outside_flipcon_usecase")
def outside_flipcon_usecase():
    return {
        "intent": "outside_flipcon_usecase",
        "message": "No APIs configured for this intent."
    }
