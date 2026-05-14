from fastapi import APIRouter

router = APIRouter()

@router.get("/alerts")
def get_alerts():
    return [
        {"id": 1, "msg": "Malware detected", "severity": "HIGH"},
        {"id": 2, "msg": "Port scan detected", "severity": "MEDIUM"},
        {"id": 3, "msg": "Suspicious login", "severity": "LOW"},
    ]