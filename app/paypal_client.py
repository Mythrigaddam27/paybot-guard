import httpx
from .config import PAYPAL_BASE, PAYPAL_CLIENT_ID, PAYPAL_CLIENT_SECRET

async def get_access_token() -> str:
    async with httpx.AsyncClient() as client:
        r = await client.post(
            f"{PAYPAL_BASE}/v1/oauth2/token",
            auth=(PAYPAL_CLIENT_ID, PAYPAL_CLIENT_SECRET),
            data={"grant_type": "client_credentials"},
        )
        r.raise_for_status()
        return r.json()["access_token"]