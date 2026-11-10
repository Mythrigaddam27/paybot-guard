from fastapi import FastAPI
from .paypal_client import get_access_token

app = FastAPI(title="PayBot Guard")

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/paypal/test")
async def paypal_test():
    token = await get_access_token()
    return {"ok": True, "token_preview": token[:8] + "..."}