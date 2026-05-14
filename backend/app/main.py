from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import stats, alerts, devices, threats

app = FastAPI(title="NetSecure XDR")

# allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(stats.router)
app.include_router(alerts.router)
app.include_router(devices.router)
app.include_router(threats.router)