from fastapi import FastAPI, Query
from typing import List

app = FastAPI(title="CxFirst Mock APIs")

# -------------------------
# Root
# -------------------------
@app.get("/")
def root():
    return {"message": "API is live. Use /order_status?mobile_number=9876543210"}

# -------------------------
# Order Status
# -------------------------
@app.get("/order_status")
def get_order_status(mobile_number: str = Query(...)):
    return {
        "requested_mobile": mobile_number,
        "customer_name": "John Doe",
        "order_status": "In transit",
        "expected_delivery": "2025-09-28"
    }

# -------------------------
# Delivery Delay
# -------------------------
@app.get("/delivery_delay")
def delivery_delay(mobile_number: str = Query(...)):
    return {
        "requested_mobile": mobile_number,
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
def order_cancellation(mobile_number: str = Query(...)):
    return {
        "requested_mobile": mobile_number,
        "customer_name": "Jane Smith",
        "open_orders": [
            {"order_id": "ORD111", "items": ["Shoes", "T-Shirt"]},
            {"order_id": "ORD222", "items": ["Laptop Bag"]}
        ]
    }

@app.post("/cancel_order")
def cancel_order(mobile_number: str, order_id: str, items: List[str]):
    return {
        "mobile_number": mobile_number,
        "order_id": order_id,
        "items_cancelled": items,
        "status": "success"
    }

# -------------------------
# Failed Payment Refund
# -------------------------
@app.get("/failed_payment_refund")
def failed_payment_refund(mobile_number: str = Query(...)):
    return {
        "requested_mobile": mobile_number,
        "transaction_status": "Failed",
        "refund_status": "Pending"
    }

@app.post("/escalate_refund")
def escalate_refund(mobile_number: str, order_id: str):
    return {
        "mobile_number": mobile_number,
        "order_id": order_id,
        "escalation_status": "raised"
    }

# -------------------------
# Refund TAT
# -------------------------
@app.get("/refund_tat")
def refund_tat(mobile_number: str = Query(...)):
    return {
        "requested_mobile": mobile_number,
        "order_id": "ORD555",
        "refund_status": "Refund Initiated",
        "refund_policy_tat": "7 business days"
    }

# -------------------------
# SOP Extension APIs
# -------------------------
@app.post("/create_ticket")
def create_ticket(mobile_number: str, issue_type: str, description: str):
    return {
        "mobile_number": mobile_number,
        "issue_type": issue_type,
        "description": description,
        "ticket_id": "TICK123",
        "status": "created"
    }

@app.post("/update_order_flag")
def update_order_flag(mobile_number: str, order_id: str, flag: str):
    return {
        "mobile_number": mobile_number,
        "order_id": order_id,
        "flag": flag,
        "status": "updated"
    }

@app.post("/create_return_request")
def create_return_request(mobile_number: str, order_id: str, reason: str):
    return {
        "mobile_number": mobile_number,
        "order_id": order_id,
        "reason": reason,
        "return_status": "initiated"
    }

@app.get("/verify_payment_attempt")
def verify_payment_attempt(mobile_number: str = Query(...)):
    return {
        "requested_mobile": mobile_number,
        "payment_attempts": 2,
        "last_attempt_status": "Failed"
    }

@app.get("/check_refund_status")
def check_refund_status(mobile_number: str = Query(...)):
    return {
        "requested_mobile": mobile_number,
        "refund_status": "Processing"
    }

@app.get("/check_refund_initiation_date")
def check_refund_initiation_date(mobile_number: str = Query(...)):
    return {
        "requested_mobile": mobile_number,
        "refund_initiated_on": "2025-09-20"
    }

@app.get("/check_wallet_refund")
def check_wallet_refund(mobile_number: str = Query(...)):
    return {
        "requested_mobile": mobile_number,
        "wallet_balance": 1500,
        "refund_in_wallet": True
    }

@app.post("/wallet_withdraw_process")
def wallet_withdraw_process(mobile_number: str, amount: float):
    return {
        "mobile_number": mobile_number,
        "amount_withdrawn": amount,
        "status": "initiated"
    }

@app.post("/create_damage_ticket")
def create_damage_ticket(mobile_number: str, order_id: str, description: str):
    return {
        "mobile_number": mobile_number,
        "order_id": order_id,
        "description": description,
        "ticket_id": "DMG456",
        "status": "created"
    }

@app.post("/resend_otp")
def resend_otp(mobile_number: str):
    return {
        "mobile_number": mobile_number,
        "otp": "654321",
        "status": "resent"
    }

@app.post("/log_call_no_response")
def log_call_no_response(mobile_number: str):
    return {
        "mobile_number": mobile_number,
        "status": "logged",
        "remark": "No response from customer"
    }

@app.post("/create_system_error_ticket")
def create_system_error_ticket(mobile_number: str, error_details: str):
    return {
        "mobile_number": mobile_number,
        "error_details": error_details,
        "ticket_id": "SYS789",
        "status": "created"
    }

# -------------------------
# Outside Flipcon Use Case
# -------------------------
@app.get("/outside_flipcon_usecase")
def outside_flipcon_usecase():
    return {
        "message": "No APIs configured for this intent."
    }
