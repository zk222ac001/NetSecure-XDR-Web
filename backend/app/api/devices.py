from fastapi import APIRouter

router = APIRouter()

@router.get("/devices")
def get_devices():
    return [
        {"id": 1, "ip": "192.168.1.10", "status": "SAFE"},
        {"id": 2, "ip": "192.168.1.20", "status": "WARNING"},
        {"id": 3, "ip": "192.168.1.30", "status": "SAFE"},
    ]