from fastapi import FastAPI, Query

app = FastAPI(title="CxFirst Mock APIs")

@app.get("/")
def root():
    return {"message": "API is live. Use /order_status?phone_number=9876543210"}

@app.get("/order_status")
def get_order_status(phone_number: str = Query(...)):
    return {
        "requested_phone": phone_number,
        "customer_name": "John Doe",
        "order_status": "In transit",
        "expected_delivery": "2025-09-28"
    }
