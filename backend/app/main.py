from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api import (
    dashboard,
    packets,
    alerts,
    devices,
    vulnerabilities,
    threatintel
)

app = FastAPI(title="NetSecure XDR Ultimate")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(dashboard.router)
app.include_router(packets.router)
#app.include_router(alerts.router)
#app.include_router(devices.router)
#app.include_router(vulnerabilities.router)
#app.include_router(threatintel.router)