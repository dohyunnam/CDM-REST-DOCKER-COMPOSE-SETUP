from fastapi import FastAPI, HTTPException, Request
import os
import httpx

app = FastAPI()

@app.post("/get-token")
async def get_token(request: Request):
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")

    if not client_id or not client_secret:
        raise HTTPException(status_code=400, detail="Environment variables not set")

    token_url = "https://auth.octopia-io.net/auth/realms/maas/protocol/openid-connect/token"
    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials"
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(token_url, data=data)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())

    return response.json()